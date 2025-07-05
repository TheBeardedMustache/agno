# Enhanced Human-in-the-Loop and Advanced Tools - Python 3.13 Compatible

from agno.tools import tool
from typing import Optional, List, Dict, Any
import json
import subprocess
import os
import time
import requests
from pathlib import Path

@tool(requires_confirmation=True)
def human_approval_required(action: str, details: str, risk_level: str = "medium") -> str:
    """Request human approval for critical actions
    
    Args:
        action: The action being requested
        details: Detailed explanation of what will happen
        risk_level: low, medium, high, critical
    """
    approval_request = f"""
    🔍 HUMAN APPROVAL REQUIRED
    
    Action: {action}
    Risk Level: {risk_level.upper()}
    Details: {details}
    
    Please review and confirm this action.
    """
    
    # Log the request
    try:
        with open("human_approvals.log", "a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {action} - {risk_level} - REQUESTED\n")
    except Exception:
        pass  # Don't fail if logging fails
    
    return approval_request

@tool
def create_project_template(project_name: str, project_type: str, location: str) -> str:
    """Create a complete project template with best practices
    
    Args:
        project_name: Name of the project
        project_type: Type (web, api, desktop, mobile, data, ai)
        location: Where to create the project
    """
    templates = {
        "web": {
            "dirs": ["src", "public", "tests", "docs", "config"],
            "files": {
                "README.md": f"# {project_name}\n\nWeb application project",
                "package.json": json.dumps({"name": project_name, "version": "1.0.0"}, indent=2),
                ".gitignore": "node_modules/\n.env\ndist/\n*.log"
            }
        },
        "api": {
            "dirs": ["src", "tests", "docs", "config", "migrations"],
            "files": {
                "README.md": f"# {project_name}\n\nAPI project",
                "requirements.txt": "fastapi>=0.104.0\nuvicorn>=0.24.0\npydantic>=2.11.2",
                ".gitignore": "__pycache__/\n.env\n*.pyc\n.venv/"
            }
        },
        "ai": {
            "dirs": ["src", "data", "models", "notebooks", "tests", "docs"],
            "files": {
                "README.md": f"# {project_name}\n\nAI/ML project",
                "requirements.txt": "numpy>=1.24.0\npandas>=2.0.0\nscikit-learn>=1.3.0\ntorch>=2.0.0\njupyter>=1.0.0",
                ".gitignore": "*.pyc\n.env\ndata/raw/\nmodels/trained/\n.ipynb_checkpoints/"
            }
        }
    }
    
    template = templates.get(project_type, templates["api"])
    project_path = Path(location) / project_name
    
    try:
        # Create directories
        for dir_name in template["dirs"]:
            (project_path / dir_name).mkdir(parents=True, exist_ok=True)
        
        # Create files
        for file_name, content in template["files"].items():
            (project_path / file_name).write_text(content, encoding="utf-8")
        
        return f"Project template created at {project_path}"
    except Exception as e:
        return f"Error creating project template: {e}"

@tool
def smart_code_review(file_path: str, review_type: str = "comprehensive") -> str:
    """Perform intelligent code review with recommendations
    
    Args:
        file_path: Path to the file to review
        review_type: basic, security, performance, comprehensive
    """
    try:
        if not os.path.exists(file_path):
            return f"File not found: {file_path}"
            
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        issues = []
        suggestions = []
        
        # Basic checks
        lines = code.split('\n')
        if len(lines) > 500:
            issues.append("File is very long (>500 lines) - consider splitting")
        
        if 'TODO' in code or 'FIXME' in code:
            issues.append("Contains TODO/FIXME comments")
        
        # Security checks
        if review_type in ["security", "comprehensive"]:
            security_patterns = ["eval(", "exec(", "input(", "raw_input("]
            for pattern in security_patterns:
                if pattern in code:
                    issues.append(f"Security concern: Found {pattern}")
        
        # Performance checks
        if review_type in ["performance", "comprehensive"]:
            if "for i in range(len(" in code:
                suggestions.append("Consider using enumerate() instead of range(len())")
        
        # Check for proper error handling
        if "try:" in code and "except:" in code:
            suggestions.append("Good: Error handling present")
        elif "try:" in code:
            suggestions.append("Consider adding more specific exception handling")
        
        review_report = f"""
Code Review Report for {file_path}

Issues Found: {len(issues)}
{chr(10).join(f"• {issue}" for issue in issues)}

Suggestions: {len(suggestions)}
{chr(10).join(f"• {suggestion}" for suggestion in suggestions)}

File Stats:
- Lines of code: {len(lines)}
- File size: {len(code)} characters
        """
        
        return review_report
        
    except Exception as e:
        return f"Error reviewing code: {e}"

@tool
def system_health_monitor() -> str:
    """Monitor system health and performance"""
    try:
        import psutil
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        
        # Memory usage
        memory = psutil.virtual_memory()
        
        # Disk usage
        disk = psutil.disk_usage('.')
        
        # Process count
        process_count = len(psutil.pids())
        
        health_report = f"""
System Health Report - {time.strftime('%Y-%m-%d %H:%M:%S')}

CPU Usage: {cpu_percent}%
Memory Usage: {memory.percent}% ({memory.used / (1024**3):.1f}GB / {memory.total / (1024**3):.1f}GB)
Disk Usage: {disk.percent}% ({disk.used / (1024**3):.1f}GB / {disk.total / (1024**3):.1f}GB)
Running Processes: {process_count}

Status: {'🟢 Healthy' if cpu_percent < 80 and memory.percent < 80 else '🟡 High Usage' if cpu_percent < 95 and memory.percent < 95 else '🔴 Critical'}
        """
        
        return health_report
        
    except ImportError:
        return "Install psutil for system monitoring: pip install psutil"
    except Exception as e:
        return f"Error monitoring system: {e}"

@tool
def automated_testing_suite(directory: str, test_type: str = "unit") -> str:
    """Run automated tests and generate reports
    
    Args:
        directory: Directory containing tests
        test_type: unit, integration, performance, security
    """
    try:
        if not os.path.exists(directory):
            return f"Directory not found: {directory}"
            
        test_commands = {
            "unit": "python -m pytest -v --tb=short",
            "integration": "python -m pytest -v -m integration --tb=short",
            "performance": "python -m pytest -v -m performance --tb=short",
            "security": "python -m bandit -r ."
        }
        
        command = test_commands.get(test_type, test_commands["unit"])
        
        result = subprocess.run(
            command,
            shell=True,
            cwd=directory,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        test_report = f"""
Test Results ({test_type}) - {time.strftime('%Y-%m-%d %H:%M:%S')}

Return Code: {result.returncode}
Status: {'✅ PASSED' if result.returncode == 0 else '❌ FAILED'}

STDOUT:
{result.stdout[:2000]}{'...' if len(result.stdout) > 2000 else ''}

STDERR:
{result.stderr[:1000]}{'...' if len(result.stderr) > 1000 else ''}
        """
        
        # Save report
        try:
            report_path = os.path.join(directory, f"test_report_{test_type}_{int(time.time())}.txt")
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(test_report)
            
            return f"Test completed. Report saved to {report_path}\n\n{test_report}"
        except Exception:
            return f"Test completed but couldn't save report.\n\n{test_report}"
            
    except subprocess.TimeoutExpired:
        return f"Test timed out after 300 seconds for {test_type} tests"
    except Exception as e:
        return f"Error running tests: {e}"

@tool
def intelligent_documentation_generator(directory: str, output_format: str = "markdown") -> str:
    """Generate comprehensive documentation from code
    
    Args:
        directory: Directory to analyze
        output_format: markdown, html, txt
    """
    try:
        if not os.path.exists(directory):
            return f"Directory not found: {directory}"
            
        docs = []
        docs.append(f"# Documentation for {Path(directory).name}\n")
        docs.append(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Collect all code files
        code_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.java', '.cpp', '.cs', '.go', '.rs')):
                    code_files.append(os.path.join(root, file))
        
        if not code_files:
            return f"No code files found in {directory}"
        
        docs.append(f"## File Overview\n")
        docs.append(f"Found {len(code_files)} code files:\n")
        
        for file_path in code_files:
            relative_path = os.path.relpath(file_path, directory)
            docs.append(f"- {relative_path}")
        
        docs.append("\n## File Details\n")
        
        for file_path in code_files[:10]:  # Limit to first 10 files
            relative_path = os.path.relpath(file_path, directory)
            docs.append(f"### {relative_path}\n")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                lines = content.split('\n')
                docs.append(f"- **Lines of code:** {len(lines)}")
                docs.append(f"- **File size:** {len(content)} characters")
                
                # Extract function/class definitions (simple pattern matching)
                functions = [line.strip() for line in lines if line.strip().startswith(('def ', 'class ', 'function '))]
                if functions:
                    docs.append(f"- **Functions/Classes:** {len(functions)}")
                    for func in functions[:5]:  # Show first 5
                        docs.append(f"  - {func}")
                
                docs.append("")
                
            except Exception as e:
                docs.append(f"Error reading file: {e}\n")
        
        if len(code_files) > 10:
            docs.append(f"... and {len(code_files) - 10} more files\n")
        
        doc_content = '\n'.join(docs)
        
        # Save documentation
        timestamp = int(time.time())
        output_path = os.path.join(directory, f"AUTO_DOCS_{timestamp}.{output_format}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        return f"Documentation generated at {output_path}\n\nPreview:\n{doc_content[:500]}..."
        
    except Exception as e:
        return f"Error generating documentation: {e}"