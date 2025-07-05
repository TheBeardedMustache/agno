-- Initialize database with required extensions and tables
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create tables for session persistence (legacy playground tables)
CREATE TABLE IF NOT EXISTS playground_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255) UNIQUE NOT NULL,
    user_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    data JSONB,
    active BOOLEAN DEFAULT true
);

CREATE TABLE IF NOT EXISTS playground_memory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255),
    user_id VARCHAR(255),
    content TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS playground_team_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255),
    team_id VARCHAR(255),
    data JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS playground_agent_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255),
    agent_id VARCHAR(255),
    data JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create unified storage tables (modern Agno storage schema)
CREATE TABLE IF NOT EXISTS unified_team_sessions (
    session_id VARCHAR PRIMARY KEY NOT NULL,
    user_id VARCHAR,
    memory JSONB,
    session_data JSONB,
    extra_data JSONB,
    created_at BIGINT DEFAULT EXTRACT(epoch FROM now())::bigint,
    updated_at BIGINT,
    agent_id VARCHAR,
    team_session_id VARCHAR,
    agent_data JSONB,
    team_id VARCHAR,
    team_data JSONB
);

CREATE TABLE IF NOT EXISTS unified_agent_sessions (
    session_id VARCHAR PRIMARY KEY NOT NULL,
    user_id VARCHAR,
    memory JSONB,
    session_data JSONB,
    extra_data JSONB,
    created_at BIGINT DEFAULT EXTRACT(epoch FROM now())::bigint,
    updated_at BIGINT,
    agent_id VARCHAR,
    team_session_id VARCHAR,
    agent_data JSONB,
    team_id VARCHAR,
    team_data JSONB
);

CREATE TABLE IF NOT EXISTS unified_memory (
    session_id VARCHAR,
    user_id VARCHAR,
    memory JSONB,
    session_data JSONB,
    extra_data JSONB,
    created_at BIGINT DEFAULT EXTRACT(epoch FROM now())::bigint,
    updated_at BIGINT,
    agent_id VARCHAR,
    team_session_id VARCHAR,
    agent_data JSONB,
    team_id VARCHAR,
    team_data JSONB
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_playground_sessions_session_id ON playground_sessions(session_id);
CREATE INDEX IF NOT EXISTS idx_playground_memory_session_id ON playground_memory(session_id);
CREATE INDEX IF NOT EXISTS idx_playground_team_sessions_session_id ON playground_team_sessions(session_id);
CREATE INDEX IF NOT EXISTS idx_playground_agent_sessions_session_id ON playground_agent_sessions(session_id);

-- Create indexes for unified storage tables
CREATE INDEX IF NOT EXISTS ix_ai_unified_team_sessions_user_id ON unified_team_sessions(user_id);
CREATE INDEX IF NOT EXISTS ix_ai_unified_team_sessions_agent_id ON unified_team_sessions(agent_id);
CREATE INDEX IF NOT EXISTS ix_ai_unified_team_sessions_team_session_id ON unified_team_sessions(team_session_id);
CREATE INDEX IF NOT EXISTS ix_ai_unified_team_sessions_team_id ON unified_team_sessions(team_id);

CREATE INDEX IF NOT EXISTS ix_ai_unified_agent_sessions_user_id ON unified_agent_sessions(user_id);
CREATE INDEX IF NOT EXISTS ix_ai_unified_agent_sessions_agent_id ON unified_agent_sessions(agent_id);
CREATE INDEX IF NOT EXISTS ix_ai_unified_agent_sessions_team_session_id ON unified_agent_sessions(team_session_id);
CREATE INDEX IF NOT EXISTS ix_ai_unified_agent_sessions_team_id ON unified_agent_sessions(team_id);