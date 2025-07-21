import os
import logging
from replit_interface import ReplitInterface

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Initialize the Replit Agent interface as the primary entry point
replit_interface = ReplitInterface()

def main():
    """
    Main entry point for OperatorOS - Enterprise AI Agent Orchestration Platform
    This serves as the primary interface for Replit Agent interactions
    """
    print("🚀 OperatorOS - Enterprise AI Agent Orchestration Platform")
    print("=" * 60)
    print("✅ System initialized and ready for Replit Agent interactions!")
    print("💬 All interactions happen through Replit Agent conversations")
    print("📋 Type commands like:")
    print("   • 'status' - Show system status")
    print("   • 'help' - Show available commands")
    print("   • 'demo healthcare' - Run healthcare demo")
    print("   • 'I need medical advice about headaches' - Task submission")
    print("=" * 60)
    
    # Start the interactive command loop for Replit Agent
    replit_interface.start_interactive_mode()

if __name__ == "__main__":
    main()
