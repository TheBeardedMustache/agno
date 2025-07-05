#!/usr/bin/env python3
"""
Startup script to ensure proper initialization of persistent components
"""
import os
import sys
import logging
import time
from dotenv import load_dotenv
import psycopg
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import io

# Load environment variables
load_dotenv()

# Configure logging with UTF-8 encoding
class UTF8StreamHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)
        if stream is None:
            stream = sys.stdout
        # Ensure UTF-8 encoding for console output
        if hasattr(stream, 'buffer'):
            self.stream = io.TextIOWrapper(stream.buffer, encoding='utf-8', errors='replace')
        else:
            self.stream = stream

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main_app.log', encoding='utf-8'),
        UTF8StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def wait_for_database():
    """Wait for database to be ready"""
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    
    max_retries = 30
    retry_interval = 2
    
    for attempt in range(max_retries):
        try:
            # Use SQLAlchemy for consistency with agno
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
            # Read and execute init-db.sql
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
                        logger.warning(f"SQL statement failed (continuing): {e}")
                        logger.warning(f"Statement: {statement[:100]}...")
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
        "data",
        "logs"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
    logger.info("[OK] Required directories created")

if __name__ == "__main__":
    logger.info("Starting initialization...")
    
    ensure_directories()
    
    if wait_for_database() and ensure_database_tables():
        logger.info("[OK] Initialization completed successfully")
        
        # Start all applications in sequence
        import subprocess
        import time
        
        try:
            logger.info("Starting AGUI backend...")
            subprocess.Popen([sys.executable, "agui_backend.py"])
            time.sleep(2)
            
            logger.info("Starting persistent AGUI backend...")
            subprocess.Popen([sys.executable, "agui_persistent_backend.py"])
            time.sleep(2)
            
            logger.info("Starting Advanced Constructor Team (main.py)...")
            subprocess.run([sys.executable, "main.py"])
            
        except Exception as e:
            logger.error(f"Failed to start applications: {e}")
            sys.exit(1)
    else:
        logger.error("[ERROR] Initialization failed")
        sys.exit(1)
