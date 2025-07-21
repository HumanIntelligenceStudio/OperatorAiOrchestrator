# OperatorOS - Enterprise AI Agent Orchestration Platform

## Overview

OperatorOS is an enterprise-grade multi-agent AI orchestration system designed specifically to work with **Replit Agent as the primary user interface**. All user interactions happen through natural language conversations with Replit Agent, which serves as both the development environment and the primary interface for the entire system. The platform manages specialized AI agent pools for different domains (healthcare, financial, sports, business, general) and provides enterprise-level orchestration, monitoring, and automation capabilities.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The system follows an unconventional architecture where Replit Agent acts as the primary UI layer, eliminating the need for traditional web interfaces. The core components include:

- **Conversational Interface**: Replit Agent handles all user interactions through natural language
- **Headless API Backend**: Flask-based REST API without web templates
- **Agent Orchestration Layer**: Multi-agent management and task distribution
- **Specialized AI Pools**: Domain-specific agents for healthcare, finance, sports, business, and general queries
- **Persistent Conversations**: OpenAI Assistants integration for context retention
- **Real-time Monitoring**: System health and performance tracking

## Key Components

### Frontend Architecture
- **Primary Interface**: Replit Agent conversational UI
- **Command Processing**: Natural language command parsing and execution
- **Interactive Demos**: Guided demonstrations through conversation
- **Session Management**: Multi-user conversation state tracking

### Backend Architecture
- **Flask API Server**: Headless backend running on port 8000
- **SQLAlchemy ORM**: Database abstraction with SQLite default
- **RESTful Endpoints**: API routes for system operations
- **Task Queue System**: Priority-based task processing with worker threads

### AI Provider Integration
- **OpenAI GPT-4o**: Primary model for most agent types
- **Anthropic Claude**: Financial and business domain specialists
- **OpenAI Assistants**: Persistent conversation management
- **Provider Routing**: Domain-specific model selection

### Agent Pool Management
- **Healthcare Specialists**: Medical advice and symptom analysis
- **Financial Analysts**: Investment advice and market analysis
- **Sports Experts**: Game predictions and player statistics
- **Business Consultants**: Process optimization and automation
- **General Knowledge**: Comprehensive assistance across topics

## Data Flow

1. **User Input**: Natural language queries through Replit Agent
2. **Command Processing**: Intent recognition and command routing
3. **Agent Selection**: Domain-specific agent pool assignment
4. **AI Processing**: Provider-specific model execution
5. **Response Generation**: Formatted responses back to Replit Agent
6. **Conversation Persistence**: Context storage for future interactions

The system maintains conversation context across sessions and provides real-time status updates through the conversational interface.

## External Dependencies

### AI Providers
- **OpenAI API**: GPT-4o model access and Assistants API
- **Anthropic API**: Claude Sonnet model integration
- **Environment Variables**: `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` required

### Sports Data Integration (NEW)
- **Alpha Vantage API**: Sports betting odds, team performance, player statistics
- **Polygon.io API**: Advanced market data for sports-related stocks
- **Environment Variables**: `ALPHA_API_KEY` and `POLYGON_KEY` integrated
- **Real-time Data**: Live sports scores, betting odds, market analysis

### System Dependencies
- **Flask**: Web framework for API backend
- **SQLAlchemy**: Database ORM and migrations
- **psutil**: System performance monitoring
- **threading**: Concurrent task processing

### Database
- **Default**: SQLite for development and testing
- **Production Ready**: Supports PostgreSQL through DATABASE_URL environment variable
- **Drizzle Compatible**: Can be extended with Drizzle ORM if needed

## Deployment Strategy

### Development Environment
- **Replit Integration**: Designed to run natively in Replit environment
- **Auto-initialization**: Database tables created on first run
- **Hot Reload**: Flask debug mode enabled for development

### Production Considerations
- **Environment Variables**: Secure API key management
- **Database Migration**: SQLite to PostgreSQL transition support
- **Health Monitoring**: Built-in system health checks and alerting
- **Scalability**: Multi-threaded task processing with configurable worker pools

### Startup Process
1. Initialize Flask application and database
2. Create default agent pools and configurations
3. Start agent master controller and health monitoring
4. Launch Replit Agent interface for user interactions
5. Begin background task processing and system monitoring

The system is designed to be fully operational through conversational commands, eliminating the need for traditional web dashboards or configuration interfaces.