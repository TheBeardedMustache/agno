# Real-time monitoring dashboard

import streamlit as st
import psutil
import time
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os

def create_monitoring_dashboard():
    st.set_page_config(page_title="Advanced Constructor Team Monitor", layout="wide")
    
    st.title("🔍 Advanced Constructor Team - Real-time Monitor")
    
    # System metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        cpu_percent = psutil.cpu_percent()
        st.metric("CPU Usage", f"{cpu_percent}%", delta=f"{cpu_percent-50}%")
    
    with col2:
        memory = psutil.virtual_memory()
        st.metric("Memory Usage", f"{memory.percent}%", delta=f"{memory.percent-50}%")
    
    with col3:
        disk = psutil.disk_usage('.')
        st.metric("Disk Usage", f"{disk.percent}%", delta=f"{disk.percent-50}%")
    
    with col4:
        # Check if main.py is running
        running_processes = [p.info['name'] for p in psutil.process_iter(['name'])]
        python_running = any('python' in name.lower() for name in running_processes)
        st.metric("System Status", "Running" if python_running else "Stopped")
    
    # Agent activity logs
    st.subheader("📋 Recent Agent Activity")
    
    if os.path.exists("main_app.log"):
        with open("main_app.log", "r", encoding="utf-8") as f:
            logs = f.readlines()[-50:]  # Last 50 lines
        
        for log in logs:
            if "ERROR" in log:
                st.error(log.strip())
            elif "WARNING" in log:
                st.warning(log.strip())
            else:
                st.info(log.strip())
    
    # Human approvals
    st.subheader("✋ Pending Human Approvals")
    
    if os.path.exists("human_approvals.log"):
        with open("human_approvals.log", "r", encoding="utf-8") as f:
            approvals = f.readlines()[-10:]  # Last 10 approvals
        
        for approval in approvals:
            st.warning(approval.strip())
    
    # Auto-refresh
    time.sleep(5)
    st.rerun()

if __name__ == "__main__":
    create_monitoring_dashboard()