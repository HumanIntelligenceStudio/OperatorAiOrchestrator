# OperatorOS - Enterprise AI Agent Orchestration Platform

## Overview

OperatorOS is an enterprise-grade multi-agent AI orchestration system designed to work with Replit Agent as the primary user interface. All user interactions happen through natural language conversations with Replit Agent, which serves as both the development environment and the primary interface. The platform manages specialized AI agent pools for different domains (healthcare, financial, sports, business, general) and provides enterprise-level orchestration, monitoring, and automation capabilities. Its business vision is to eliminate the need for traditional web interfaces, streamlining AI interaction directly within the development environment.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The system follows an unconventional architecture where Replit Agent acts as the primary UI layer, eliminating the need for traditional web interfaces.

### Core Architecture
- **Conversational Interface**: Replit Agent handles all user interactions.
- **Headless API Backend**: Flask-based REST API without web templates.
- **Agent Orchestration Layer**: Multi-agent management and task distribution.
- **Specialized AI Pools**: Domain-specific agents for healthcare, finance, sports, business, and general queries.
- **Persistent Conversations**: OpenAI Assistants integration for context retention.
- **Real-time Monitoring**: System health and performance tracking.

### Design Principles
- **UI/UX**: Replit Agent conversational UI is the sole interface, handling command processing, interactive demos, and multi-user session management.
- **Backend**: Flask API server on port 8000, using SQLAlchemy ORM (default SQLite, PostgreSQL support), and a priority-based task queue system with worker threads.
- **AI Provider Integration**: Primary models include OpenAI GPT-4o, Anthropic Claude Sonnet-4 for finance, and xAI Grok-2 for business. OpenAI Assistants manage persistent conversations. The system supports multi-provider analysis and domain-specific model routing with fallbacks.
- **Agent Pool Management**: Includes specialists for healthcare (e.g., medical advice, Epic workflow), financial analysis (e.g., investment, personal finance), sports experts, business consultants, and general knowledge.
- **Data Flow**: User input via Replit Agent -> command processing and intent recognition -> agent selection -> AI processing -> response generation -> conversation persistence.

### Feature Specifications
- **Personal Finance Management**: Comprehensive budget management, expense tracking, and financial goal setting with AI-powered insights, multi-currency support, and database persistence per user.
- **Epic Healthcare System Integration**: Full Epic documentation conversion (PDF to Markdown) across 21 major modules, enabling healthcare workflow management, technical configuration details, and strategic integration for clinical optimization.
- **Medical Research Analysis**: CPT code-based reimbursement analysis (e.g., shoulder arthroplasty), multi-provider medical economics insights, statistical testing, and longitudinal analysis.

## External Dependencies

- **AI Providers**:
    - **OpenAI API**: GPT-4o, Assistants API (`OPENAI_API_KEY`)
    - **Anthropic API**: Claude Sonnet-4 (`ANTHROPIC_API_KEY`)
    - **xAI API**: Grok-2 (`XAI_API_KEY`)
- **Healthcare Data Integration**:
    - **CMS API**: Centers for Medicare & Medicaid Services data (`CMS_KEY`)
    - **OpenFDA API**: Food and Drug Administration safety and recall data (`OPEN_FDA_KEY`)
- **Sports Data Integration**:
    - **Alpha Vantage API**: Sports betting odds, player statistics (`ALPHA_API_KEY`)
    - **Polygon.io API**: Sports-related stock market data (`POLYGON_KEY`)
- **Exchange Rate Integration**:
    - **ExchangeRate-API**: Real-time currency conversion (`EXCHANGERATE_KEY`) with fallbacks to exchangerate.host.
- **System Dependencies**:
    - **Flask**: Web framework
    - **SQLAlchemy**: Database ORM
    - **psutil**: System performance monitoring
    - **threading**: Concurrent task processing
- **Database**:
    - Default: SQLite
    - Production: PostgreSQL (via `DATABASE_URL`)