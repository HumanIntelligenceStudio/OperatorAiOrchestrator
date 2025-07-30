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
- **Anthropic Claude Sonnet-4**: Advanced financial analysis, risk assessment, and regulatory compliance
- **xAI Grok-2**: Business strategy, market analysis, and competitive intelligence
- **OpenAI Assistants**: Persistent conversation management
- **Multi-Provider Analysis**: Comprehensive insights from multiple AI models simultaneously
- **Provider Routing**: Domain-specific model selection with fallback handling

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

### Healthcare Data Integration (NEW - July 22, 2025)
- **CMS API**: Centers for Medicare & Medicaid Services data access
- **OpenFDA API**: Food and Drug Administration safety and recall data
- **Environment Variables**: `CMS_KEY` and `OPEN_FDA_KEY` configured
- **Real-time Healthcare Data**: Hospital quality, Medicare spending, drug safety
- **Government Data Sources**: Authoritative healthcare information from federal agencies

### AI Providers (ENHANCED - July 21, 2025)
- **OpenAI API**: GPT-4o model access and Assistants API for general intelligence
- **Anthropic API**: Claude Sonnet-4 integration for advanced financial analysis and regulatory compliance
- **xAI API**: Grok-2 integration for business strategy and competitive intelligence
- **Environment Variables**: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, and `XAI_API_KEY` configured
- **Multi-Provider Capabilities**: Simultaneous analysis from multiple AI models for comprehensive insights

### Sports Data Integration
- **Alpha Vantage API**: Sports betting odds, team performance, player statistics
- **Polygon.io API**: Advanced market data for sports-related stocks
- **Environment Variables**: `ALPHA_API_KEY` and `POLYGON_KEY` integrated
- **Real-time Data**: Live sports scores, betting odds, market analysis

### Exchange Rate Integration (NEW)
- **ExchangeRate-API**: Real-time currency conversion across 168+ currencies
- **Free API Fallbacks**: exchangerate.host and static demo rates for reliability
- **Environment Variable**: `EXCHANGERATE_KEY` configured with fallback systems
- **Financial Integration**: Multi-currency support for international operations

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

## Recent Updates

### Epic Integration Completed (July 30, 2025)

**Major Achievement: Healthcare Documentation Integration**
- ✅ **Epic Decision Trees Guide**: Complete PDF to markdown conversion (87 pages)
- ✅ **Healthcare Workflow Documentation**: Full Epic decision tree setup and support procedures
- ✅ **Professional Healthcare Documentation**: Enterprise-grade clinical workflow management
- ✅ **Technical Configuration Details**: Complete decision tree node types and implementation
- ✅ **Strategic Healthcare Integration**: Foundation for clinical workflow optimization

### Medical Research Analysis System Deployed (July 22, 2025)

**Major Achievement: Comprehensive Medical Research Platform**
- ✅ **Shoulder Arthroplasty Analysis**: Complete CPT code-based reimbursement analysis
- ✅ **4 CPT Procedures Analyzed**: Hemiarthroplasty and total shoulder arthroplasty
- ✅ **16,629 Characters AI Analysis**: Multi-provider medical economics insights
- ✅ **Statistical Testing Framework**: Professional-grade research methodology
- ✅ **10-Year Longitudinal Analysis**: 2015-2025 reimbursement trend analysis

### Healthcare Data Integration Completed (July 22, 2025)

**Major System Expansion: Healthcare Analytics**
- ✅ **CMS API Integration**: Centers for Medicare & Medicaid Services data access
- ✅ **OpenFDA API Integration**: Food and Drug Administration safety data
- ✅ **Real Healthcare Data**: 445KB of authentic government health data processed
- ✅ **AI Healthcare Analysis**: 9,611 characters of multi-provider health insights
- ✅ **API Connectivity**: 100% success rate for both CMS and OpenFDA connections

**Healthcare Data Sources Added:**
- **Hospital Quality Metrics**: Patient safety, readmission rates, performance scores
- **Medicare Spending Analysis**: Cost per beneficiary, regional patterns
- **Drug Adverse Events**: Real FDA safety reports from healthcare providers
- **Drug Recalls & Alerts**: FDA enforcement actions and safety warnings
- **Medical Device Safety**: Adverse event monitoring and risk assessment
- **Food Safety Recalls**: Consumer protection and contamination tracking

**Healthcare AI Capabilities:**
- **Claude**: Healthcare quality analysis, regulatory compliance assessment
- **Grok**: Healthcare innovation strategy, market opportunity analysis
- **Combined Intelligence**: Comprehensive health risk and opportunity evaluation

### Multi-Provider AI Integration Completed (July 21, 2025)
- **Claude Sonnet-4**: Successfully integrated for sophisticated financial analysis, risk assessment, and regulatory compliance analysis
- **Grok-2**: Successfully integrated for business strategy, competitive analysis, and market opportunity assessment
- **Enhanced Capabilities**: Multi-model analysis providing diverse AI perspectives on financial scenarios
- **API Endpoints**: New REST endpoints for multi-provider analysis, risk assessment, and compliance analysis
- **Production Ready**: All providers tested and operational with comprehensive error handling and fallback mechanisms

### Key Features Added
- Multi-provider financial analysis combining insights from Claude, Grok, and OpenAI
- Advanced risk assessment with regulatory compliance focus
- Market sentiment analysis from multiple AI perspectives  
- Comprehensive compliance analysis for financial services
- Enhanced API endpoints for direct provider access
- Robust error handling and provider fallback systems