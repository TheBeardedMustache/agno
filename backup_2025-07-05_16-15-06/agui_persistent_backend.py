#!/usr/bin/env python3
"""
AGUI Backend with Persistent Memory and Chat History
This backend ensures that chat sessions and user memories persist across server restarts.
"""

import os
import sys
from typing import Optional
from dotenv import load_dotenv
import psycopg

from agno.agent import Agent
from agno.team.team import Team
from agno.models.openai import OpenAIChat
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.storage.postgres import PostgresStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from agno.app.agui import AGUIApp

# Load environment variables
load_dotenv()

# Validate required environment variables
required_vars = ['OPENAI_API_KEY', 'DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_DATABASE']
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    sys.exit(1)

# Database configuration
DB_URL = f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"

# Test database connection
try:
    test_conn = psycopg.connect(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}")
    test_conn.close()
    print("[OK] Database connection successful")
except Exception as e:
    print(f"[ERROR] Database connection failed: {e}")
    print("Please ensure PostgreSQL is running and the database/user exists.")
    sys.exit(1)

# Memory and Storage setup for persistent chat history and user memories
try:
    # Create shared memory for all agents and teams
    memory_db = PostgresMemoryDb(table_name="agui_memory", db_url=DB_URL)
    shared_memory = Memory(db=memory_db)
    
    # Create separate storage instances
    team_storage = PostgresStorage(table_name="agui_team_sessions", db_url=DB_URL, auto_upgrade_schema=True)
    agent_storage = PostgresStorage(table_name="agui_agent_sessions", db_url=DB_URL, auto_upgrade_schema=True)
    
    print("[OK] Memory and storage initialized for AGUI")
except Exception as e:
    print(f"[ERROR] Failed to initialize memory/storage: {e}")
    sys.exit(1)

# Advanced Code Architect Agent with persistent memory
code_architect = Agent(
    name="Code Architect",
    role="System architecture and design specialist",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "You are a senior software architect with expertise in system design and architecture patterns.",
        "Your responsibilities include designing comprehensive system architectures, creating project structures,",
        "defining coding standards, and planning development workflows.",
        "Always use reasoning tools to think through complex architectural decisions.",
        "Remember user preferences and project contexts from previous conversations.",
        "Provide detailed documentation and maintain consistency across sessions.",
    ],
    tools=[ReasoningTools(add_instructions=True)],
    memory=shared_memory,
    storage=agent_storage,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_messages=True,
    num_history_responses=5,
    add_datetime_to_instructions=True,
    markdown=True,
    monitoring=True
)

# Advanced Code Implementer with persistent memory
code_implementer = Agent(
    name="Code Implementer",
    role="Code implementation and development specialist",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "You are a senior software developer with expertise in multi-language programming.",
        "Your responsibilities include implementing complex algorithms, writing clean code,",
        "debugging issues, and optimizing performance.",
        "Always use reasoning tools to plan implementation approaches.",
        "Remember coding patterns and user preferences from previous sessions.",
        "Maintain code quality standards and provide comprehensive documentation.",
    ],
    tools=[ReasoningTools(add_instructions=True)],
    memory=shared_memory,
    storage=agent_storage,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_messages=True,
    num_history_responses=5,
    add_datetime_to_instructions=True,
    markdown=True,
    monitoring=True
)

# Advanced DevOps Agent with persistent memory
devops_agent = Agent(
    name="DevOps Agent",
    role="DevOps and system integration specialist",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "You are a senior DevOps engineer with expertise in CI/CD, containerization, and cloud infrastructure.",
        "Your responsibilities include setting up environments, creating pipelines,",
        "configuring deployments, and integrating systems.",
        "Always use reasoning tools to plan deployment strategies.",
        "Remember infrastructure preferences and deployment patterns from previous sessions.",
        "Implement security best practices and comprehensive monitoring.",
    ],
    tools=[ReasoningTools(add_instructions=True)],
    memory=shared_memory,
    storage=agent_storage,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_messages=True,
    num_history_responses=5,
    add_datetime_to_instructions=True,
    markdown=True,
    monitoring=True
)

# Deep Researcher with persistent memory
deep_researcher = Agent(
    name="Deep Researcher",
    role="Research and knowledge specialist",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "You are an expert researcher specializing in finding best practices and current trends.",
        "Search the internet for up-to-date information and industry standards.",
        "Provide comprehensive research with reliable sources and actionable insights.",
        "Remember research topics and user interests from previous sessions.",
        "Maintain a knowledge base of research findings across conversations.",
    ],
    tools=[DuckDuckGoTools(), ReasoningTools(add_instructions=True)],
    memory=shared_memory,
    storage=agent_storage,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_messages=True,
    num_history_responses=5,
    add_datetime_to_instructions=True,
    markdown=True,
    monitoring=True
)

# Advanced Constructor Team with persistent memory
constructor_team = Team(
    name="Advanced Constructor Team",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        code_architect,
        code_implementer,
        devops_agent,
        deep_researcher
    ],
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
        "- Complex projects: Coordinate multiple agents as needed",
        
        "Quality assurance:",
        "- Ensure all code follows best practices",
        "- Verify proper testing and documentation",
        "- Confirm deployment readiness and security",
        "- Maintain consistency across all deliverables",
        
        "Always provide comprehensive project summaries and maintain context across sessions.",
    ],
    memory=shared_memory,
    storage=team_storage,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_messages=True,
    enable_agentic_context=True,
    show_members_responses=True,
    add_datetime_to_instructions=True,
    markdown=True,
    monitoring=True
)

# Create AGUI App with persistent memory configuration
agui_app = AGUIApp(
    team=constructor_team,
    name="Advanced Constructor Team",
    app_id="advanced_constructor_team",
    description="A sophisticated team of AI agents with persistent memory for complex technical projects",
)

# Get the FastAPI app
app = agui_app.get_app()

if __name__ == "__main__":
    print("Starting Advanced Constructor Team AGUI Backend...")
    print("Frontend should connect to: http://localhost:8000")
    print("Memory and chat history will persist across server restarts")
    
    try:
        # Start the AGUI server
        agui_app.serve(
            app="agui_persistent_backend:app",
            host="0.0.0.0",
            port=8000,
            reload=True
        )
    except Exception as e:
        print(f"Failed to start AGUI server: {e}")
        sys.exit(1)

