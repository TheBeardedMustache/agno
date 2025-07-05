<div align="center" id="top">
  <a href="https://docs.agno.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg">
      <img src="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg" alt="Agno">
    </picture>
  </a>
</div>
<div align="center">
  <a href="https://docs.agno.com">📚 Documentation</a> &nbsp;|&nbsp;
  <a href="https://docs.agno.com/examples/introduction">💡 Examples</a> &nbsp;|&nbsp;
  <a href="https://github.com/agno-agi/agno/stargazers">🌟 Star Us</a>
</div>

## Session Persistence Fixes Applied

The following improvements have been made to fix session persistence issues in the Agno web UI:

### 🔧 **Session Management Improvements**

1. **Enhanced Session Creation**
   - Added proper session ID generation with timestamps
   - Improved session retrieval from multiple storage locations
   - Added fallback mechanisms for robust session handling

2. **Storage Configuration**
   - Fixed PostgreSQL storage initialization
   - Added proper session objects (TeamSession) for storage operations
   - Enhanced error handling for storage operations

3. **Session Monitoring**
   - Added background session monitoring thread
   - Real-time logging of session activity
   - Automatic session health checks every 60 seconds

4. **Debugging Tools**
   - `debug_session_info()` - Check current session status
   - `force_session_persistence()` - Test session storage functionality
   - Enhanced logging for session operations

### 🛠 **Key Features**

- **Persistent Sessions**: Sessions now properly persist across page navigation
- **Dual Storage**: Both team storage and AGUI storage are maintained
- **Error Resilience**: Graceful handling of storage failures
- **Real-time Monitoring**: Background monitoring of session health
- **Debug Capabilities**: Built-in tools to diagnose session issues

### 📊 **Session Dashboard Recording**

The Web UI dashboard should now properly record:
- Session creation and continuation
- Agent interactions and responses
- Team coordination activities
- Memory and storage persistence

### 🔍 **Troubleshooting**

If sessions still don't persist:
1. Check logs for session monitor reports
2. Use `debug_session_info()` tool to check session status
3. Verify PostgreSQL database connection
4. Check storage table creation in logs

The session persistence system is now more robust and should maintain state across all pages in the Agno web UI.

<p align="left">
  <a href="#top">⬆️ Back to Top</a>
</p>
