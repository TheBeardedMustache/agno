import os
import sys
import logging
import traceback
import signal
import time
from typing import Optional
from dotenv import load_dotenv
import psycopg
import uuid
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from agno.agent import Agent
from agno.team.team import Team
from agno.models.openai import OpenAIChat
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.storage.postgres import PostgresStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from agno.tools import tool
from agno.playground import Playground
from agno.tools.file import FileTools
from agno.tools.shell import ShellTools
from agno.tools.github import GithubTools
from agno.tools.e2b import E2BTools
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.knowledge import KnowledgeTools
from agno.app.agui import AGUIApp
from agno.tools.pdf import PDFTools
from agno.tools.website import WebsiteTools
import PyPDF2
import fitz  # PyMuPDF
import markdown
import os
import re
from pathlib import Path

# Configure logging - simplified
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main_app.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class MainAppError(Exception):
    """Custom exception for main app errors"""
    pass

class ErrorHandler:
    """Centralized error handling"""
    
    @staticmethod
    def handle_error(error: Exception, context: str = "") -> str:
        """Handle errors with proper logging and return user-friendly message"""
        logger.error(f"Error in {context}: {error}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return f"I encountered an error in {context}. The error has been logged and I'll continue with the next steps. Error: {str(error)[:100]}..."

class GracefulShutdown:
    """Handle graceful shutdown"""
    
    def __init__(self):
        self.shutdown_requested = False
        
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        logger.info(f"Received signal {signum}, initiating graceful shutdown...")
        self.shutdown_requested = True

# Global shutdown handler
shutdown_handler = GracefulShutdown()

def setup_signal_handlers():
    """Setup signal handlers for graceful shutdown"""
    signal.signal(signal.SIGINT, shutdown_handler.signal_handler)
    signal.signal(signal.SIGTERM, shutdown_handler.signal_handler)

@tool
def run_with_error_handling(command: str, timeout: int) -> str:
    """Execute commands with comprehensive error handling
    
    Args:
        command: The command to execute
        timeout: Timeout in seconds for the command execution
    """
    import subprocess
    
    try:
        logger.info(f"Executing command: {command}")
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        if result.returncode == 0:
            logger.info("Command executed successfully")
            return f"Command completed successfully: {result.stdout}"
        else:
            logger.warning(f"Command failed with return code {result.returncode}")
            return f"Command encountered an issue but I'll continue. Error: {result.stderr}"
            
    except subprocess.TimeoutExpired:
        logger.warning(f"Command timed out after {timeout} seconds")
        return f"Command timed out after {timeout} seconds, but I'll continue with the next steps."
    except Exception as e:
        logger.error(f"Error executing command: {e}")
        return f"Error executing command: {str(e)[:100]}..."

@tool(requires_confirmation=True)
def run_streamlit_command(command: str, directory: Optional[str] = None) -> str:
    """Execute Streamlit-specific commands with user confirmation
    
    Args:
        command: The streamlit command to execute (e.g., 'streamlit run app.py')
        directory: Optional directory to run the command in
    """
    import subprocess
    import os
    
    try:
        logger.info(f"Executing Streamlit command: {command}")
        
        # Change directory if specified
        if directory:
            original_dir = os.getcwd()
            os.chdir(directory)
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Change back to original directory
        if directory:
            os.chdir(original_dir)
        
        if result.returncode == 0:
            logger.info("Streamlit command executed successfully")
            return f"Streamlit command completed: {result.stdout}"
        else:
            logger.warning(f"Streamlit command failed with return code {result.returncode}")
            return f"Streamlit command failed: {result.stderr}"
            
    except Exception as e:
        logger.error(f"Error executing Streamlit command: {e}")
        return f"Error executing Streamlit command: {str(e)[:100]}..."

@tool
def safe_file_operation(operation: str, file_path: str, content: str = "") -> str:
    """Perform file operations with error handling"""
    try:
        if operation == "read":
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        elif operation == "write":
            if not content:
                return "Error: content parameter is required for write operation"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Successfully wrote to {file_path}"
        elif operation == "append":
            if not content:
                return "Error: content parameter is required for append operation"
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(content)
            return f"Successfully appended to {file_path}"
        else:
            return f"Unknown operation: {operation}"
            
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}")
        return f"File not found: {file_path}. I'll continue with available information."
    except PermissionError:
        logger.warning(f"Permission denied: {file_path}")
        return f"Permission denied accessing {file_path}. I'll work with available resources."
    except Exception as e:
        logger.error(f"File operation error: {e}")
        return ErrorHandler.handle_error(e, "File Operation")

def validate_environment():
    """Validate required environment variables"""
    required_vars = ['OPENAI_API_KEY', 'DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_DATABASE']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
        logger.error(error_msg)
        logger.error("Please check your .env file and ensure all required variables are set.")
        for var in missing_vars:
            logger.error(f"  - {var}: Not set")
        raise MainAppError(error_msg)
    
    logger.info("[OK] All required environment variables are present")

def wait_for_database():
    """Wait for database to be ready"""
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    
    max_retries = 30
    retry_interval = 2
    
    for attempt in range(max_retries):
        try:
            # Use SQLAlchemy for consistency
            engine = create_engine(db_url)
            Session = sessionmaker(bind=engine)
            
            with Session() as sess:
                sess.execute(text("SELECT 1"))
                logger.info("[OK] Database connection established")
                return True
        except Exception as e:
            logger.info(f"Database not ready (attempt {attempt + 1}/{max_retries}): {e}")
            time.sleep(retry_interval)
    
    logger.error("[ERROR] Database connection failed after all retries")
    return False

def ensure_database_tables():
    """Ensure all required database tables exist"""
    try:
        db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
        
        # Use SQLAlchemy engine and session like agno does
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        
        with Session() as sess:
            # Check if init-db.sql exists and execute it
            if os.path.exists('init-db.sql'):
                with open('init-db.sql', 'r') as f:
                    init_sql = f.read()
                    
                    # Split SQL statements and execute one by one using SQLAlchemy text()
                    statements = [stmt.strip() for stmt in init_sql.split(';') if stmt.strip()]
                    for statement in statements:
                        try:
                            # Use SQLAlchemy text() for raw SQL like agno does
                            sess.execute(text(statement))
                            sess.commit()
                        except Exception as e:
                            logger.warning(f"SQL statement failed (table may exist): {e}")
                            sess.rollback()
                        
        logger.info("[OK] Database tables initialized successfully")
        return True
        
    except Exception as e:
        logger.error(f"[ERROR] Failed to initialize database tables: {e}")
        return False

def ensure_directories():
    """Ensure all required directories exist"""
    directories = [
        "library_KB/RandD",
        "library_KB/Knowledge", 
        "library_KB/Teaching",
        "library_KB/VectorStore",
        "library_KB/Foundational",
        "data",
        "logs"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
    logger.info("[OK] Required directories created")

def setup_database():
    """Setup and test database connection"""
    try:
        db_url = f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
        
        # Test database connection
        test_conn = psycopg.connect(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}")
        test_conn.close()
        logger.info("[OK] Database connection successful")
        
        return db_url
        
    except Exception as e:
        logger.error(f"[ERROR] Database connection failed: {e}")
        logger.error("Please ensure PostgreSQL is running and the database/user exists.")
        raise MainAppError(f"Database connection failed: {e}")

def get_or_create_session(user_id: str = "TheBeardedMustache") -> str:
    """Get existing session or create new one for user"""
    try:
        # Try to get existing sessions for the user
        existing_sessions = team_storage.get_all_session_ids(user_id)
        if existing_sessions and len(existing_sessions) > 0:
            session_id = existing_sessions[0]  # Use the most recent session
            logger.info(f"[SESSION] Continuing existing session: {session_id} for user: {user_id}")
            return session_id
        else:
            # Create new session
            session_id = str(uuid.uuid4())
            logger.info(f"[SESSION] Created new session: {session_id} for user: {user_id}")
            return session_id
    except Exception as e:
        logger.warning(f"[SESSION] Error managing session: {e}, creating new session")
        return str(uuid.uuid4())

def create_resilient_agent(
    name: str,
    role: str,
    instructions: list,
    tools: Optional[list] = None,
    memory=None,
    storage=None,
    user_id: str = "TheBeardedMustache",
    session_id: Optional[str] = None,
    reasoning: bool = True,
    stream_intermediate_steps: bool = True
) -> Agent:
    """Create an agent with error handling capabilities and proper session management"""
    try:
        enhanced_instructions = instructions + [
            "If you encounter any errors, handle them gracefully and continue with your task.",
            "Always provide helpful responses even if some operations fail.",
            "Log important information for debugging when needed.",
            "Use the error handling tools when executing commands or file operations.",
            "IMPORTANT: Use run_streamlit_command() for ANY Streamlit-related commands (streamlit run, streamlit hello, etc.)",
            "Use run_with_error_handling() for PowerShell, bash, or other non-Streamlit commands.",
            "Use safe_file_operation() for file read/write operations."
        ]
        
        if tools is None:
            tools = []
        
        enhanced_tools = tools.copy()
        enhanced_tools.extend([run_with_error_handling, safe_file_operation, run_streamlit_command])
        
        # Add enhanced tools
        from enhanced_tools import (
            human_approval_required, create_project_template, smart_code_review,
            intelligent_documentation_generator, system_health_monitor, automated_testing_suite
        )
        
        enhanced_tools.extend([
            human_approval_required, create_project_template, smart_code_review,
            intelligent_documentation_generator, system_health_monitor, automated_testing_suite
        ])
        
        agent = Agent(
            name=name,
            role=role,
            model=OpenAIChat(id="gpt-4o"),
            instructions=enhanced_instructions,
            tools=enhanced_tools,
            memory=memory,
            storage=storage,
            user_id=user_id,
            session_id=session_id,
            enable_user_memories=True,
            enable_session_summaries=True,
            add_datetime_to_instructions=True,
            add_history_to_messages=True,
            num_history_responses=5,
            markdown=True,
            monitoring=True,
            reasoning=True,
            stream_intermediate_steps=True,
            show_tool_calls=True,
            debug_mode=True,
        )
        
        logger.info(f"Created resilient agent: {name} with session: {session_id}")
        return agent
        
    except Exception as e:
        logger.error(f"Failed to create agent {name}: {e}")
        raise MainAppError(f"Failed to create agent {name}: {e}")

# Initialize with error handling
try:
    logger.info("Initializing Advanced Constructor Team...")
    
    # Setup signal handlers
    setup_signal_handlers()
    
    # Validate environment
    validate_environment()
    
    # Ensure required directories exist
    ensure_directories()
    
    # Wait for database to be ready
    if not wait_for_database():
        raise MainAppError("Database not ready after maximum retries")
    
    # Ensure database tables exist
    if not ensure_database_tables():
        raise MainAppError("Failed to initialize database tables")
    
    # Setup database
    DB_URL = setup_database()
    logger.info("[OK] Database setup completed successfully")

    # Memory and Storage setup with enhanced persistence
    try:
        # Memory for all agents and teams
        memory_db = PostgresMemoryDb(
            table_name="unified_memory", 
            db_url=DB_URL
        )
        memory = Memory(db=memory_db)
        
        # Storage instances for different entities
        team_storage = PostgresStorage(
            table_name="unified_team_sessions", 
            db_url=DB_URL
        )
        agent_storage = PostgresStorage(
            table_name="unified_agent_sessions", 
            db_url=DB_URL
        )
        
        # AGUI-specific storage for compatibility
        agui_team_storage = PostgresStorage(
            table_name="agui_team_sessions", 
            db_url=DB_URL
        )
        agui_agent_storage = PostgresStorage(
            table_name="agui_agent_sessions", 
            db_url=DB_URL
        )
        
        logger.info("[OK] Memory and storage initialized with persistent tables")
        
    except Exception as e:
        logger.error(f"[ERROR] Failed to initialize memory/storage: {e}")
        sys.exit(1)

except Exception as e:
    logger.error(f"[ERROR] Failed to initialize Advanced Constructor Team: {e}")
    sys.exit(1)

# Create resilient agents with error handling and session persistence
try:
    # Get or create session for this application run
    agent_session_id = get_or_create_session("TheBeardedMustache")
    
    # Advanced Code Architect Agent
    code_architect = create_resilient_agent(
        name="Advanced Code Architect Agent",
        role="System architecture and design specialist",
        instructions=[
            "You are a senior software architect with expertise in:",
            "- System design and architecture patterns",
            "- Code organization and project structure",
            "- Technology stack selection and evaluation",
            "- Performance optimization and scalability",
            "- Security best practices and code review",
            "Your responsibilities:",
            "1. Design comprehensive system architectures",
            "2. Create project structures and boilerplate code anywhere on the system",
            "3. Define coding standards and best practices",
            "4. Plan development workflows and CI/CD pipelines",
            "5. Research and evaluate new technologies",
            "When working on projects:",
            "- Always use reasoning tools to think through complex architectural decisions",
            "- Search knowledge base for best practices and patterns",
            "- Create detailed documentation and README files",
            "- Use shell commands to set up project environments",
            "- Generate comprehensive project structures with proper organization",
            "- Consider scalability, maintainability, and performance from the start",
            "File management - YOU HAVE FULL SYSTEM ACCESS:",
            "- Can read, write, and create files in ANY directory on the system",
            "- Create well-organized directory structures anywhere",
            "- Generate configuration files in appropriate locations",
            "- Set up development environments and tooling system-wide",
            "- Create comprehensive documentation anywhere needed",
            "- Use absolute paths when working outside current directory",
            "- Be mindful of file permissions and system security",
        ],
        tools=[
            ReasoningTools(add_instructions=True),
            FileTools(),
            ShellTools(),
            GithubTools(),
            E2BTools()
        ],
        memory=memory,
        storage=agent_storage,
        user_id="TheBeardedMustache",
        session_id=agent_session_id,
        reasoning=True,
        stream_intermediate_steps=True,
    )

    # Advanced Code Implementer
    code_implementer = create_resilient_agent(
        name="Advanced Code Implementer",
        role="Code implementation and development specialist",
        instructions=[
            "You are a senior software developer with expertise in:",
            "- Multi-language programming (Python, JavaScript, TypeScript, Go, Rust, etc.)",
            "- Algorithm implementation and optimization",
            "- Code debugging and troubleshooting",
            "- Testing strategies and implementation",
            "- Code refactoring and optimization",
            "Your responsibilities:",
            "1. Implement complex algorithms and business logic",
            "2. Write clean, efficient, and maintainable code",
            "3. Debug and fix code issues",
            "4. Optimize performance and memory usage",
            "5. Implement comprehensive testing suites",
            "When coding:",
            "- Always use reasoning tools to plan implementation approach",
            "- Search knowledge base for coding patterns and solutions",
            "- Write self-documenting code with clear comments",
            "- Follow SOLID principles and design patterns",
            "- Implement proper error handling and logging",
            "- Write unit tests and integration tests",
            "File management - YOU HAVE FULL SYSTEM ACCESS:",
            "- Can read, write, and create code files anywhere on the system",
            "- Access existing codebases in any directory",
            "- Create new projects in any location",
            "- Modify configuration files system-wide",
            "- Set up testing environments anywhere",
            "- Use absolute paths when working outside current directory",
            "- Be mindful of file permissions and existing code structure",
            "Code quality standards:",
            "- Use type hints and proper documentation",
            "- Follow language-specific best practices",
            "- Implement proper exception handling",
            "- Use meaningful variable and function names",
            "- Optimize for readability and maintainability",
            "- Include comprehensive docstrings and comments",
        ],
        tools=[
            ReasoningTools(add_instructions=True),
            FileTools(),
            ShellTools(),
            E2BTools()
        ],
        memory=memory,
        storage=agent_storage,
        user_id="TheBeardedMustache",
        session_id=agent_session_id,
        reasoning=True,
        stream_intermediate_steps=True,
    )

    # Advanced DevOps & Integration Agent
    devops_agent = create_resilient_agent(
        name="Advanced DevOps & Integration Agent",
        role="DevOps and system integration specialist",
        instructions=[
            "You are a senior DevOps engineer with expertise in:",
            "- CI/CD pipeline design and implementation",
            "- Container orchestration (Docker, Kubernetes)",
            "- Cloud infrastructure (AWS, GCP, Azure)",
            "- Automation and scripting",
            "- Monitoring and observability",
            "Your responsibilities:",
            "1. Set up development and production environments",
            "2. Create CI/CD pipelines and automation scripts",
            "3. Configure deployment and monitoring systems",
            "4. Integrate different systems and services",
            "5. Create infrastructure as code",
            "When working on DevOps tasks:",
            "- Always use reasoning tools to plan deployment strategies",
            "- Search knowledge base for infrastructure patterns",
            "- Create comprehensive deployment documentation",
            "- Set up proper monitoring and alerting",
            "- Implement security best practices",
            "- Automate repetitive tasks with scripts",
            "File management - YOU HAVE FULL SYSTEM ACCESS:",
            "- Can read, write, and create files anywhere on the system",
            "- Access and modify system configuration files",
            "- Create deployment scripts in any location",
            "- Set up infrastructure files system-wide",
            "- Configure monitoring and logging anywhere",
            "- Use absolute paths when working outside current directory",
            "- Be extra careful with system files and permissions",
        ],
        tools=[
            ReasoningTools(add_instructions=True),
            ShellTools(),
            FileTools(),
            GithubTools(),
            E2BTools()
        ],
        memory=memory,
        storage=agent_storage,
        user_id="TheBeardedMustache",
        session_id=agent_session_id,
        reasoning=True,
        stream_intermediate_steps=True,
    )

    # Deep Researcher
    deep_researcher = create_resilient_agent(
        name="Deep Researcher",
        role="Internet research and PDF processing specialist",
        instructions=[
            "You are an expert researcher specializing in finding best practices and current trends.",
            "You can process PDFs and convert them to Markdown for better accessibility.",
            "Search the internet for the most up-to-date information and industry standards.",
            "Provide comprehensive research with reliable sources.",
            "Focus on practical, actionable insights.",
            "Summarize findings in clear, concise reports.",
            "Convert all research materials to Markdown format for consistency.",
            "PDF Processing Capabilities:",
            "- Convert PDF files to Markdown format with convert_pdf_to_markdown()",
            "- Process multiple PDFs at once with batch_convert_pdfs_to_markdown()",
            "- Extract metadata from PDFs with extract_pdf_metadata()",
            "- Organize converted files in the knowledge base structure",
            "File Organization:",
            "- Save converted PDFs in library_KB/Knowledge/PDFs_Converted/",
            "- Store original research in library_KB/RandD/PDF_Sources/",
            "- Create research reports in library_KB/RandD/Research_Reports/",
            "- Maintain organized index of all materials",
            "When processing PDFs:",
            "1. First extract metadata to understand the content",
            "2. Convert PDF to Markdown format",
            "3. Review and clean up the converted text",
            "4. Organize the file in appropriate knowledge base location",
            "5. Update the knowledge base index",
            "Research Best Practices:",
            "- Always convert PDFs to Markdown for better searchability",
            "- Create structured summaries of research findings",
            "- Maintain consistent file naming conventions",
            "- Cross-reference related materials",
            "- Keep original sources for reference",
        ],
        tools=[
            DuckDuckGoTools(),
            GoogleSearchTools(),
            FileTools(),
            ReasoningTools(add_instructions=True),
            convert_pdf_to_markdown,
            batch_convert_pdfs_to_markdown,
            extract_pdf_metadata,
            organize_knowledge_base
        ],
        memory=memory,
        storage=agent_storage,
        user_id="TheBeardedMustache",
        session_id=agent_session_id,
        reasoning=True,
        stream_intermediate_steps=True,
    )

    # Librarian (Knowledge Keeper)
    librarian = create_resilient_agent(
        name="Librarian",
        role="Knowledge organization and management specialist",
        instructions=[
            "You are a knowledge management expert who organizes and structures information.",
            "Create comprehensive knowledge bases and documentation systems.",
            "Ensure information is easily accessible and well-categorized.",
            "Maintain consistency and accuracy in all knowledge repositories.",
            "File management - keep knowledge organized in library_KB/Knowledge/:",
            "- Create well-structured directories for different knowledge areas.",
            "- Use clear and descriptive file names.",
            "- Maintain a knowledge base of all relevant information.",
        ],
        tools=[
            ReasoningTools(add_instructions=True),
            FileTools()
        ],
        memory=memory,
        storage=agent_storage,
        user_id="TheBeardedMustache",
        session_id=agent_session_id,
        reasoning=True,
        stream_intermediate_steps=True,
    )

    # Rector (Teacher)
    rector = create_resilient_agent(
        name="Rector",
        role="Teaching and knowledge transfer specialist",
        instructions=[
            "You are an expert educator who teaches and mentors team members.",
            "Provide clear explanations and learning materials.",
            "Adapt teaching methods to different learning styles.",
            "Ensure knowledge transfer is effective and comprehensive.",
            "When teaching:",
            "1. Assess the learning needs of team members.",
            "2. Develop tailored learning plans.",
            "3. Use a variety of teaching methods and materials.",
            "4. Encourage active participation and engagement.",
            "5. Evaluate learning outcomes and provide feedback.",
            "File management - keep teaching materials organized in \"C:\\Users\\Nick\\Desktop\\Machine_Spirit_Algorithm\\agno\\library_KB\\Teaching\":",
            "- Create well-structured directories for different teaching materials.",
            "- Use clear and descriptive file names.",
            "- Maintain a knowledge base of all teaching resources.",
        ],
        tools=[
            ReasoningTools(add_instructions=True),
            FileTools()
        ],
        memory=memory,
        storage=agent_storage,
        user_id="TheBeardedMustache",
        session_id=agent_session_id,
        reasoning=True,
        stream_intermediate_steps=True,
    )

    # Index-keeper (Vector Store Manager)
    index_keeper = create_resilient_agent(
        name="Index-keeper",
        role="Vector store and data management specialist",
        instructions=[
            "You are a data management expert who maintains vector stores and indices.",
            "Ensure efficient storage and retrieval of information.",
            "Optimize search and indexing performance.",
            "Maintain data integrity and consistency.",
            "When managing vector stores:",
            "1. Organize data into logical collections and indices.",
            "2. Optimize embeddings and search performance.",
            "3. Regularly update and maintain indices.",
            "4. Implement data backup and recovery processes.",
            "5. Monitor system performance and usage.",
            "File management - keep vector data organized in \"C:\\Users\\Nick\\Desktop\\Machine_Spirit_Algorithm\\agno\\library_KB\\VectorStore\":",
            "- Create well-structured directories for different vector collections.",
            "- Use clear and descriptive file names.",
            "- Maintain a knowledge base of all vector store information.",
        ],
        tools=[
            ReasoningTools(add_instructions=True),
            FileTools(),
            ShellTools()
        ],
        memory=memory,
        storage=agent_storage,
        user_id="TheBeardedMustache",
        session_id=agent_session_id,
        reasoning=True,
        stream_intermediate_steps=True,
    )

    logger.info("[OK] All agents created successfully")

except Exception as e:
    logger.error(f"[ERROR] Failed to create agents: {e}")
    sys.exit(1)

# Create team with error handling and persistent sessions
try:
    # Get or create team session
    team_session_id = get_or_create_session("TheBeardedMustache")
    
    # Create the main team coordinator
    team_coordinator = Team(
        name="Advanced Constructor Team",
        members=[code_architect, code_implementer, devops_agent, deep_researcher, librarian, rector, index_keeper],
        model=OpenAIChat(id="ft:gpt-4o-2024-08-06:churchofadeptus:sonny-philosophersstone-v4:BmTilCO0"),
        user_id="TheBeardedMustache",
        session_id=team_session_id,
        instructions=[
            "You are the Advanced Constructor Team - a sophisticated group of expert AI agents.",
            "Your mission: Deliver exceptional software solutions with comprehensive documentation.",
            "Team composition and roles:",
            "- System Architecture: Advanced Code Architect Agent",
            "- Implementation: Advanced Code Implementer", 
            "- Infrastructure: Advanced DevOps & Integration Agent",
            "- Research: Deep Researcher",
            "- Knowledge Management: Librarian",
            "- Data Management: Index Keeper",
            "- Teaching & Knowledge Transfer: Rector",
            "Quality assurance:",
            "- Ensure all code follows best practices",
            "- Verify proper testing and documentation",
            "- Confirm deployment readiness",
            "- Validate security and performance requirements",
            "- Maintain consistency across all deliverables",
            "Remember context and decisions from previous conversations.",
            "Always provide comprehensive project summaries and next steps.",
            "Handle any errors gracefully and continue working towards the goal.",
        ],
        tools=[ReasoningTools(add_instructions=True)],
        memory=memory,
        storage=team_storage,
        enable_agentic_context=True,
        show_members_responses=True,
        add_datetime_to_instructions=True,
        add_history_to_messages=True,
        markdown=True,
        monitoring=True,
        reasoning=True,
        stream_intermediate_steps=True,
        debug_mode=True,
    )

    # Create AGUI-compatible team for backward compatibility
    agui_team = Team(
        name="Advanced Constructor Team",
        mode="coordinate",
        model=OpenAIChat(id="gpt-4o"),
        members=[code_architect, code_implementer, devops_agent, deep_researcher],
        instructions=[
            "You are the Advanced Constructor Team managing specialized AI agents for complex technical projects.",
            "Coordinate between team members to achieve technical objectives effectively.",
            "Ensure all team members collaborate and share knowledge seamlessly.",
            "Maintain session persistence and memory across all interactions.",
            "Remember user preferences, project contexts, and previous decisions.",
            "Focus on delivering high-quality, scalable solutions with proper documentation.",
            "Task delegation guidelines:",
            "- Architecture & Design: Code Architect",
            "- Implementation & Coding: Code Implementer", 
            "- Deployment & Infrastructure: DevOps Agent",
            "- Research & Best Practices: Deep Researcher",
            "Always provide comprehensive project summaries and maintain context across sessions.",
        ],
        memory=memory,
        storage=agui_team_storage,
        enable_user_memories=True,
        enable_session_summaries=True,
        add_history_to_messages=True,
        enable_agentic_context=True,
        show_members_responses=True,
        add_datetime_to_instructions=True,
        markdown=True,
        monitoring=True
    )

    logger.info("[OK] Team coordinators created successfully with persistent sessions")

except Exception as e:
    logger.error(f"[ERROR] Failed to create team: {e}")
    sys.exit(1)

# Create both Playground and AGUI App
try:
    # Create Playground for main interface
    playground = Playground(
        teams=[team_coordinator],
        name="Advanced Constructor Team",
        description="A sophisticated team of AI agents for complex technical projects",
        app_id="advanced-constructor-team",
        monitoring=True
    )

    # Create AGUI App for backward compatibility
    agui_app = AGUIApp(
        team=agui_team,
        name="Advanced Constructor Team",
        app_id="advanced_constructor_team",
        description="A sophisticated team of AI agents with persistent memory for complex technical projects",
    )

    # Get both apps
    playground_app = playground.get_app(prefix="")
    agui_fastapi_app = agui_app.get_app()
    
    logger.info("[OK] Both Playground and AGUI apps created successfully")

except Exception as e:
    logger.error(f"[ERROR] Failed to create apps: {e}")
    sys.exit(1)

# Add this function to main.py after the imports
def find_available_port(start_port: int, max_attempts: int = 10) -> int:
    """Find an available port starting from start_port"""
    import socket
    
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except socket.error:
            continue
    
    raise Exception(f"Could not find available port starting from {start_port}")

if __name__ == "__main__":
    try:
        logger.info("Starting Advanced Constructor Team - Unified Interface...")
        
        # Find available ports
        agui_port = find_available_port(8000)
        playground_port = find_available_port(7777)
        
        if agui_port != 8000:
            logger.info(f"Port 8000 in use, using port {agui_port} for AGUI")
        if playground_port != 7777:
            logger.info(f"Port 7777 in use, using port {playground_port} for Playground")
        
        logger.info("This single application provides:")
        logger.info(f"  - Playground interface on port {playground_port}")
        logger.info(f"  - AGUI-compatible backend on port {agui_port}")
        logger.info("  - Persistent memory and session management")
        logger.info("  - All team functionality unified in one application")
        
        # Start both servers
        import uvicorn
        import threading
        
        def start_agui_server():
            """Start AGUI server in a separate thread"""
            try:
                uvicorn.run(agui_fastapi_app, host="0.0.0.0", port=agui_port, log_level="info")
            except Exception as e:
                logger.error(f"AGUI server failed: {e}")
        
        # Start AGUI server in background thread
        agui_thread = threading.Thread(target=start_agui_server, daemon=True)
        agui_thread.start()
        
        # Give AGUI server time to start
        time.sleep(2)
        logger.info(f"AGUI server started on port {agui_port}")
        
        # Start main playground server on main thread
        logger.info(f"Starting Playground server on port {playground_port}...")
        playground.serve(app="__main__:playground_app", host="0.0.0.0", port=playground_port, reload=False, prefix="")
        
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        sys.exit(1)

@tool
def convert_pdf_to_markdown(pdf_path: str, output_path: Optional[str] = None) -> str:
    """Convert PDF file to Markdown format with enhanced text extraction
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Optional output path for the markdown file
    """
    try:
        import fitz  # PyMuPDF
        import os
        from pathlib import Path
        
        # Validate input file
        if not os.path.exists(pdf_path):
            return f"Error: PDF file not found at {pdf_path}"
        
        # Generate output path if not provided
        if output_path is None:
            pdf_name = Path(pdf_path).stem
            output_path = f"library_KB/Knowledge/{pdf_name}.md"
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Extract text from PDF
        markdown_content = []
        doc = fitz.open(pdf_path)
        
        markdown_content.append(f"# {Path(pdf_path).stem}\n")
        markdown_content.append(f"*Converted from PDF: {pdf_path}*\n")
        markdown_content.append(f"*Conversion Date: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            
            if text.strip():
                markdown_content.append(f"## Page {page_num + 1}\n")
                
                # Clean up text formatting
                text = re.sub(r'\n\s*\n', '\n\n', text)  # Remove excessive newlines
                text = re.sub(r'([.!?])\s*\n\s*([A-Z])', r'\1 \2', text)  # Join sentences
                text = re.sub(r'\s+', ' ', text)  # Clean up spacing
                
                markdown_content.append(text + "\n\n")
        
        doc.close()
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_content))
        
        logger.info(f"Successfully converted PDF to Markdown: {output_path}")
        return f"Successfully converted PDF to Markdown: {output_path}"
        
    except ImportError:
        return "Error: PyMuPDF (fitz) not installed. Run: pip install PyMuPDF"
    except Exception as e:
        logger.error(f"Error converting PDF to Markdown: {e}")
        return f"Error converting PDF to Markdown: {str(e)}"

@tool
def batch_convert_pdfs_to_markdown(directory_path: str, output_directory: Optional[str] = None) -> str:
    """Convert all PDF files in a directory to Markdown format
    
    Args:
        directory_path: Path to directory containing PDF files
        output_directory: Optional output directory for markdown files
    """
    try:
        import os
        from pathlib import Path
        
        if not os.path.exists(directory_path):
            return f"Error: Directory not found at {directory_path}"
        
        if output_directory is None:
            output_directory = "library_KB/Knowledge"
        
        # Find all PDF files
        pdf_files = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith('.pdf'):
                    pdf_files.append(os.path.join(root, file))
        
        if not pdf_files:
            return f"No PDF files found in {directory_path}"
        
        # Convert each PDF
        results = []
        for pdf_file in pdf_files:
            pdf_name = Path(pdf_file).stem
            output_path = os.path.join(output_directory, f"{pdf_name}.md")
            
            result = convert_pdf_to_markdown(pdf_file, output_path)
            results.append(f"• {pdf_name}: {result}")
        
        summary = f"Batch conversion completed. Processed {len(pdf_files)} PDF files:\n" + "\n".join(results)
        logger.info(summary)
        return summary
        
    except Exception as e:
        logger.error(f"Error in batch PDF conversion: {e}")
        return f"Error in batch PDF conversion: {str(e)}"

@tool
def extract_pdf_metadata(pdf_path: str) -> str:
    """Extract metadata from PDF file
    
    Args:
        pdf_path: Path to the PDF file
    """
    try:
        import fitz
        import os
        
        if not os.path.exists(pdf_path):
            return f"Error: PDF file not found at {pdf_path}"
        
        doc = fitz.open(pdf_path)
        metadata = doc.metadata
        
        info = []
        info.append(f"**PDF Metadata for: {os.path.basename(pdf_path)}**\n")
        info.append(f"- **Title:** {metadata.get('title', 'N/A')}")
        info.append(f"- **Author:** {metadata.get('author', 'N/A')}")
        info.append(f"- **Subject:** {metadata.get('subject', 'N/A')}")
        info.append(f"- **Creator:** {metadata.get('creator', 'N/A')}")
        info.append(f"- **Producer:** {metadata.get('producer', 'N/A')}")
        info.append(f"- **Creation Date:** {metadata.get('creationDate', 'N/A')}")
        info.append(f"- **Modification Date:** {metadata.get('modDate', 'N/A')}")
        info.append(f"- **Page Count:** {len(doc)}")
        info.append(f"- **File Size:** {os.path.getsize(pdf_path)} bytes")
        
        doc.close()
        
        result = "\n".join(info)
        logger.info(f"Extracted metadata for {pdf_path}")
        return result
        
    except Exception as e:
        logger.error(f"Error extracting PDF metadata: {e}")
        return f"Error extracting PDF metadata: {str(e)}"

@tool
def organize_knowledge_base(base_path: str = "library_KB") -> str:
    """Organize knowledge base files by type and create index
    
    Args:
        base_path: Base path for the knowledge base
    """
    try:
        import os
        from pathlib import Path
        
        # Create directory structure
        directories = [
            "Knowledge/PDFs_Converted",
            "Knowledge/Research_Papers",
            "Knowledge/Documentation",
            "Knowledge/References",
            "RandD/PDF_Sources",
            "RandD/Research_Reports"
        ]
        
        for directory in directories:
            os.makedirs(os.path.join(base_path, directory), exist_ok=True)
        
        # Create index file
        index_content = []
        index_content.append("# Knowledge Base Index\n")
        index_content.append(f"*Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n")
        
        # Scan for files
        for root, dirs, files in os.walk(base_path):
            if files:
                relative_path = os.path.relpath(root, base_path)
                index_content.append(f"## {relative_path}\n")
                
                for file in sorted(files):
                    if file.endswith(('.md', '.pdf', '.txt')):
                        index_content.append(f"- [{file}]({os.path.join(relative_path, file)})")
                
                index_content.append("")
        
        # Write index
        index_path = os.path.join(base_path, "INDEX.md")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(index_content))
        
        logger.info(f"Knowledge base organized and index created at {index_path}")
        return f"Knowledge base organized successfully. Index created at {index_path}"
        
    except Exception as e:
        logger.error(f"Error organizing knowledge base: {e}")
        return f"Error organizing knowledge base: {str(e)}"
