# Advanced Constructor Team - Unified Setup

## Overview

The Advanced Constructor Team is now unified into a single application that provides:

- **Playground Interface** (Port 7777): Interactive team collaboration
- **AGUI Interface** (Port 8000): Advanced GUI for agent interactions  
- **Persistent Memory**: All conversations and data persist across sessions
- **Data Preservation**: Setup never deletes or overwrites existing data
- **Error Handling**: Comprehensive error recovery and logging

## Quick Start

```powershell
# One command to set up everything
.\setup.ps1
```

This script will:
1. ✅ Only create Docker containers if they don't exist
2. ✅ Only create database tables if they don't exist  
3. ✅ Preserve all existing data and configurations
4. ✅ Launch the unified application (`main.py`)
5. ✅ Provide both Playground and AGUI interfaces

## What's Unified

All functionality from the previous separate scripts is now in `main.py`:

- **From `agui_backend.py`**: Error handling and graceful shutdown
- **From `agui_persistent_backend.py`**: Persistent memory and AGUI interface
- **From `startup.py`**: Database initialization and directory setup
- **Enhanced**: Better session management and unified storage

## Architecture

```
main.py (Single Entry Point)
├── Playground Server (Port 7777)
├── AGUI Server (Port 8000)  
├── Persistent Memory System
├── Advanced Constructor Team
│   ├── Code Architect Agent
│   ├── Code Implementer Agent
│   ├── DevOps Agent
│   ├── Deep Researcher Agent
│   ├── Librarian Agent
│   ├── Rector Agent
│   └── Index-keeper Agent
└── Error Handling & Recovery
```

## Key Features

### Data Preservation
- **Never deletes** existing databases or containers
- **Never overwrites** existing configurations
- **Preserves** all chat history and memories
- **Maintains** session continuity

### Unified Interface
- **Single command** to start everything
- **Both interfaces** available simultaneously
- **Consistent** persistent memory across interfaces
- **Seamless** agent collaboration

### Error Recovery
- **Graceful error handling** throughout
- **Automatic recovery** from common issues
- **Comprehensive logging** for troubleshooting
- **Continues operation** despite individual failures

## Usage

### Starting the Application
```powershell
# Full setup (recommended)
.\setup.ps1

# Or manually after setup
python main.py
```

### Accessing Interfaces
- **Playground**: http://localhost:7777
- **AGUI**: http://localhost:8000
- **Web UI**: https://app.agno.com/playground?endpoint=localhost%3A7777

### Monitoring
```powershell
# Check container status
docker-compose ps

# View logs
docker logs agno-postgres
docker logs agno-redis

# View application logs
Get-Content main_app.log -Tail 50
```

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 7777 and 8000 are available
2. **Database connection**: Verify PostgreSQL container is running
3. **Environment variables**: Check `.env` file has all required values
4. **Dependencies**: Run `pip install -r requirements.txt`

### Clean Restart
```powershell
# Stop all containers
docker-compose down

# Restart setup (preserves data)
.\setup.ps1
```

### Complete Reset (if needed)
```powershell
# WARNING: This will delete all data
docker-compose down -v
docker system prune -f
.\setup.ps1
```

## Migration from Old Setup

If you have the old multi-file setup:

1. **Backup your data** (optional - setup preserves everything)
2. **Run the new setup**: `.\setup.ps1`
3. **Remove old files** (optional): `.\cleanup_old_setup.ps1`

All your existing data, conversations, and configurations will be preserved.

## Benefits of Unification

- ✅ **Simpler deployment**: One command, one process
- ✅ **Better resource usage**: Shared memory and connections
- ✅ **Easier maintenance**: Single codebase to manage
- ✅ **Improved reliability**: Unified error handling
- ✅ **Better performance**: Optimized data sharing
- ✅ **Enhanced features**: More consistent experience

## Team Capabilities

The unified team includes all previous capabilities plus:

- **Full system access** for file operations
- **Advanced reasoning** for complex decisions
- **Persistent memory** across all interactions
- **Research capabilities** with internet access
- **Knowledge management** and organization
- **Teaching and mentoring** features
- **Vector store management** for embeddings
- **Comprehensive documentation** generation

## Support

For issues or questions:
1. Check the logs: `main_app.log`
2. Verify services: `docker-compose ps`
3. Test database: `docker exec agno-postgres pg_isready -U ai -d ai`

The unified setup is designed to be robust and self-healing, but comprehensive logs are available for any troubleshooting needs.