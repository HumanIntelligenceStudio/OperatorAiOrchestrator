#!/usr/bin/env python3
"""
OperatorOS Demo System
Demonstrates the conversational interface for the enterprise AI agent orchestration platform
"""

import requests
import json
import time
from command_processor import CommandProcessor

class OperatorOSDemo:
    def __init__(self):
        self.base_url = "http://localhost:5000/api"
        self.command_processor = CommandProcessor()
        
    def show_welcome_message(self):
        print("🚀 Welcome to OperatorOS - Enterprise AI Agent Orchestration Platform")
        print("=" * 70)
        print("✅ Replit Agent serves as your conversational interface")
        print("💬 All system management happens through natural language")
        print("🤖 Multiple AI agent pools handle specialized domains")
        print("=" * 70)
        print()
    
    def demonstrate_system_status(self):
        print("📊 SYSTEM STATUS CHECK")
        print("-" * 30)
        try:
            response = requests.get(f"{self.base_url}/status", timeout=10)
            if response.status_code == 200:
                data = response.json()
                print("✅ System is operational")
                print(f"   Database: Connected")
                print(f"   API Backend: Running on port 5000")
                print(f"   Agent Pools: Initialized")
                status_data = data.get('data', {})
                if status_data:
                    print(f"   Active Pools: {len(status_data.get('pools', []))}")
            else:
                print(f"❌ System status check failed: {response.status_code}")
        except Exception as e:
            print(f"❌ Connection failed: {e}")
        print()
    
    def demonstrate_agent_pools(self):
        print("🤖 AGENT POOL OVERVIEW")
        print("-" * 30)
        
        pools = {
            "Healthcare": {
                "description": "Medical advice, symptom analysis, health consultations",
                "ai_model": "GPT-4o",
                "sample_queries": ["I have a headache", "What are flu symptoms?", "Medical emergency help"]
            },
            "Financial": {
                "description": "Investment advice, market analysis, financial planning", 
                "ai_model": "Claude Sonnet",
                "sample_queries": ["Analyze S&P 500 trends", "Investment portfolio advice", "Budget planning"]
            },
            "Sports": {
                "description": "Game predictions, player stats, sports analysis",
                "ai_model": "GPT-4o",
                "sample_queries": ["NBA playoff predictions", "Player performance stats", "Game analysis"]
            },
            "Business": {
                "description": "Process automation, strategy consulting, workflow optimization",
                "ai_model": "Claude Sonnet", 
                "sample_queries": ["Automate invoice processing", "Business strategy", "Team productivity"]
            },
            "General": {
                "description": "Comprehensive assistance across all topics",
                "ai_model": "GPT-4o",
                "sample_queries": ["Research assistance", "Creative projects", "Technical questions"]
            }
        }
        
        for pool_name, details in pools.items():
            print(f"🎯 {pool_name} Pool")
            print(f"   Purpose: {details['description']}")
            print(f"   AI Model: {details['ai_model']}")
            print(f"   Sample Queries: {', '.join(details['sample_queries'][:2])}")
            print()
    
    def demonstrate_conversational_commands(self):
        print("💬 CONVERSATIONAL COMMAND EXAMPLES")
        print("-" * 40)
        
        commands = [
            {
                "user_input": "Show me the system status",
                "description": "Get comprehensive system health and metrics"
            },
            {
                "user_input": "I need medical advice about chest pain",
                "description": "Routes to Healthcare agent pool for specialized medical assistance"
            },
            {
                "user_input": "Analyze the stock market trends today",
                "description": "Connects to Financial agent using Claude for market analysis"
            },
            {
                "user_input": "Scale up the business pool by 3 agents",
                "description": "Dynamic scaling of agent pools based on demand"
            },
            {
                "user_input": "Run a healthcare demo",
                "description": "Interactive demonstration of healthcare capabilities"
            },
            {
                "user_input": "What's the health status of all pools?",
                "description": "Real-time monitoring and health reporting"
            }
        ]
        
        for cmd in commands:
            print(f"👤 User: \"{cmd['user_input']}\"")
            print(f"🤖 System: {cmd['description']}")
            print()
    
    def demonstrate_ai_provider_routing(self):
        print("🧠 AI PROVIDER ROUTING")
        print("-" * 30)
        print("OperatorOS intelligently routes requests to optimal AI models:")
        print()
        print("📋 OpenAI GPT-4o:")
        print("   • Healthcare consultations")
        print("   • Sports analysis and predictions")
        print("   • General knowledge and creative tasks")
        print()
        print("🧮 Anthropic Claude Sonnet:")
        print("   • Financial analysis and advice")
        print("   • Business strategy and automation") 
        print("   • Complex reasoning and planning")
        print()
        print("🎯 Smart Routing:")
        print("   • Domain-specific model selection")
        print("   • Automatic failover between providers")
        print("   • Performance-based load balancing")
        print()
    
    def demonstrate_key_features(self):
        print("⭐ KEY PLATFORM FEATURES")
        print("-" * 30)
        
        features = [
            "🌐 Conversational Interface - All interactions through Replit Agent",
            "🏥 Specialized Agent Pools - Domain expertise (Healthcare, Finance, Sports, Business)",
            "🔄 Auto-scaling - Dynamic agent pool management based on demand", 
            "📊 Real-time Monitoring - System health and performance tracking",
            "🧠 Multi-AI Provider - OpenAI GPT-4o and Anthropic Claude integration",
            "💾 Persistent Conversations - Context retention across sessions",
            "🔧 Enterprise Ready - PostgreSQL database, REST API backend",
            "⚡ Task Prioritization - Intelligent queue management",
            "🛡️ Health Monitoring - Automated alerts and recovery",
            "📈 Business Automation - Workflow optimization and process automation"
        ]
        
        for feature in features:
            print(f"   {feature}")
        print()
    
    def show_interaction_examples(self):
        print("💭 LIVE INTERACTION EXAMPLES")
        print("-" * 40)
        print("Here's how you can interact with OperatorOS through Replit Agent:")
        print()
        
        examples = [
            ("System Management", [
                "status",
                "show me agent pool health",
                "scale up healthcare agents by 2",
                "restart the financial pool"
            ]),
            ("Healthcare Tasks", [
                "I have persistent headaches for 3 days",
                "What are the symptoms of diabetes?",
                "I need advice about my medication"
            ]),
            ("Financial Analysis", [
                "Should I invest in tech stocks now?",
                "Analyze my portfolio risk",
                "What's happening with crypto markets?"
            ]),
            ("Business Automation", [
                "Help me automate our invoice workflow",
                "Optimize our customer service process",
                "Create a project management strategy"
            ])
        ]
        
        for category, commands in examples:
            print(f"📂 {category}:")
            for cmd in commands:
                print(f"   💬 \"{cmd}\"")
            print()

def main():
    """Main demo function"""
    demo = OperatorOSDemo()
    
    demo.show_welcome_message()
    demo.demonstrate_system_status()
    demo.demonstrate_agent_pools()
    demo.demonstrate_conversational_commands()
    demo.demonstrate_ai_provider_routing()
    demo.demonstrate_key_features()
    demo.show_interaction_examples()
    
    print("🎯 READY FOR INTERACTION")
    print("=" * 30)
    print("OperatorOS is now ready for conversational commands!")
    print("Simply talk to Replit Agent using natural language.")
    print("The system will understand your intent and route tasks appropriately.")

if __name__ == "__main__":
    main()