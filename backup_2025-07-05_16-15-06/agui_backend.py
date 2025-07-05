# agui_backend.py
import os
import sys
import signal
import logging
import traceback
from typing import Optional
from dotenv import load_dotenv
import uvicorn

# Configure logging with UTF-8 encoding
import io
import sys

# Create UTF-8 compatible stream handlers
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
        logging.FileHandler('agui_backend.log', encoding='utf-8'),
        UTF8StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class AGUIBackendError(Exception):
    """Custom exception for AGUI backend errors"""
    pass

class ErrorHandler:
    """Centralized error handling"""
    
    @staticmethod
    def handle_error(error: Exception, context: str = "") -> None:
        """Handle errors with proper logging"""
        logger.error(f"Error in {context}: {error}")
        logger.error(f"Traceback: {traceback.format_exc()}")

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

def validate_environment():
    """Validate required environment variables"""
    required_vars = ['OPENAI_API_KEY', 'DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_DATABASE']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
        logger.error(error_msg)
        raise AGUIBackendError(error_msg)

# Import app with error handling
try:
    # Validate environment first
    validate_environment()
    
    # Setup signal handlers
    setup_signal_handlers()
    
    # Import the AGUI app from the persistent backend
    from agui_persistent_backend import app as agui_app
    
    logger.info("[OK] AGUI app imported successfully")
    
except Exception as e:
    ErrorHandler.handle_error(e, "App Import")
    logger.error("Failed to import AGUI app. Please check your configuration.")
    sys.exit(1)

if __name__ == "__main__":
    try:
        logger.info("Starting AGUI Backend with Enhanced Error Handling...")
        
        # Run server with error handling
        uvicorn.run(
            "agui_backend:agui_app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info",
            access_log=True
        )
        
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        ErrorHandler.handle_error(e, "Server Startup")
        logger.error("Server failed to start. Check logs for details.")
        sys.exit(1)
    finally:
        logger.info("AGUI Backend shutdown completed")
