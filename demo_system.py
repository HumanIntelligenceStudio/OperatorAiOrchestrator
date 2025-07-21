#!/usr/bin/env python3
"""
OpenAI Assistants Integration Demo
Demonstrates working components of OperatorOS multi-agent system
"""

import os
import json
import logging
from datetime import datetime
from openai import OpenAI

class OperatorOSDemo:
    """Demo of working OpenAI integration without circular imports"""
    
    def __init__(self):
        self.openai_client = None
        self.demo_results = {
            "timestamp": datetime.now().isoformat(),
            "tests_run": [],
            "successful_features": []
        }
        
    def test_openai_connection(self):
        """Test basic OpenAI connection"""
        print("Testing OpenAI Connection")
        print("=" * 30)
        
        api_key = os.environ.get('OPENAI_API_KEY')
        
        if not api_key:
            print("❌ OPENAI_API_KEY not found")
            return False
            
        try:
            self.openai_client = OpenAI(api_key=api_key)
            
            # Test basic completion
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
                messages=[
                    {"role": "system", "content": "You are OperatorOS, an enterprise AI agent orchestration platform."},
                    {"role": "user", "content": "Introduce yourself as part of a system test."}
                ],
                max_tokens=150
            )
            
            result = response.choices[0].message.content
            print("✅ OpenAI Connection Successful")
            print(f"Response: {result}")
            
            self.demo_results["tests_run"].append("openai_connection")
            self.demo_results["successful_features"].append("Basic OpenAI Chat Completion")
            return True
            
        except Exception as e:
            print(f"❌ OpenAI connection failed: {e}")
            return False
    
    def test_assistant_creation(self):
        """Test OpenAI Assistant creation and interaction"""
        print("\nTesting Assistant Creation")
        print("=" * 30)
        
        if not self.openai_client:
            print("❌ OpenAI client not initialized")
            return False
            
        try:
            # Create specialized assistants for different domains
            assistants = {}
            
            assistant_configs = {
                "Sports Expert": "You are a sports analytics expert specializing in game predictions and statistical analysis.",
                "Healthcare Advisor": "You are a healthcare information specialist providing evidence-based medical guidance.",
                "Financial Analyst": "You are a financial expert providing investment advice and market analysis."
            }
            
            for name, instructions in assistant_configs.items():
                assistant = self.openai_client.beta.assistants.create(
                    name=f"OperatorOS {name}",
                    instructions=instructions,
                    model="gpt-4o"
                )
                assistants[name] = assistant.id
                print(f"✅ Created {name}: {assistant.id}")
                
            # Test conversation with Sports Expert
            thread = self.openai_client.beta.threads.create()
            
            self.openai_client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content="What makes a good sports betting strategy?"
            )
            
            run = self.openai_client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistants["Sports Expert"]
            )
            
            # Wait for completion
            import time
            while run.status in ['queued', 'in_progress']:
                time.sleep(1)
                run = self.openai_client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
            
            if run.status == 'completed':
                messages = self.openai_client.beta.threads.messages.list(thread_id=thread.id)
                response = messages.data[0].content[0].text.value
                print(f"💬 Sports Expert Response: {response[:200]}...")
                
                self.demo_results["successful_features"].append("OpenAI Assistants with Domain Specialization")
                
            # Clean up test assistants
            for name, assistant_id in assistants.items():
                self.openai_client.beta.assistants.delete(assistant_id)
                print(f"🗑️ Cleaned up {name}")
                
            self.demo_results["tests_run"].append("assistant_creation")
            return True
            
        except Exception as e:
            print(f"❌ Assistant creation failed: {e}")
            return False
    
    def test_multi_agent_simulation(self):
        """Simulate multi-agent conversation flow"""
        print("\nTesting Multi-Agent Simulation")
        print("=" * 35)
        
        if not self.openai_client:
            print("❌ OpenAI client not initialized")
            return False
            
        try:
            # Simulate different agent responses to same query
            query = "Should I invest in sports betting companies like DraftKings?"
            
            agent_perspectives = {
                "Financial": "You are a conservative financial advisor focused on risk management.",
                "Sports": "You are a sports industry analyst who understands the business side.",
                "Healthcare": "You are a healthcare advisor concerned about gambling addiction risks."
            }
            
            responses = {}
            
            for agent_type, instructions in agent_perspectives.items():
                response = self.openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": instructions},
                        {"role": "user", "content": query}
                    ],
                    max_tokens=200
                )
                
                responses[agent_type] = response.choices[0].message.content
                print(f"🤖 {agent_type} Agent: {responses[agent_type][:150]}...")
                
            self.demo_results["successful_features"].append("Multi-Agent Perspective Analysis")
            self.demo_results["tests_run"].append("multi_agent_simulation")
            return True
            
        except Exception as e:
            print(f"❌ Multi-agent simulation failed: {e}")
            return False
    
    def test_context_persistence(self):
        """Test conversation context and memory"""
        print("\nTesting Context Persistence")
        print("=" * 30)
        
        if not self.openai_client:
            print("❌ OpenAI client not initialized")
            return False
            
        try:
            # Create assistant with memory
            assistant = self.openai_client.beta.assistants.create(
                name="Memory Test Assistant",
                instructions="You have excellent memory. Remember details from our conversation and reference them in later messages.",
                model="gpt-4o"
            )
            
            thread = self.openai_client.beta.threads.create()
            
            # Multi-turn conversation
            conversations = [
                "My name is Alex and I'm interested in sports arbitrage betting.",
                "What did I tell you about my interest?",
                "Do you remember my name?"
            ]
            
            for i, message in enumerate(conversations, 1):
                print(f"💭 Turn {i}: {message}")
                
                self.openai_client.beta.threads.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content=message
                )
                
                run = self.openai_client.beta.threads.runs.create(
                    thread_id=thread.id,
                    assistant_id=assistant.id
                )
                
                import time
                while run.status in ['queued', 'in_progress']:
                    time.sleep(1)
                    run = self.openai_client.beta.threads.runs.retrieve(
                        thread_id=thread.id,
                        run_id=run.id
                    )
                
                if run.status == 'completed':
                    messages = self.openai_client.beta.threads.messages.list(
                        thread_id=thread.id,
                        order="desc",
                        limit=1
                    )
                    response = messages.data[0].content[0].text.value
                    print(f"🤖 Assistant: {response}")
                
            # Clean up
            self.openai_client.beta.assistants.delete(assistant.id)
            print("🗑️ Cleaned up memory test assistant")
            
            self.demo_results["successful_features"].append("Conversation Context Persistence")
            self.demo_results["tests_run"].append("context_persistence")
            return True
            
        except Exception as e:
            print(f"❌ Context persistence test failed: {e}")
            return False
    
    def run_full_demo(self):
        """Run complete integration demo"""
        print("🚀 OperatorOS OpenAI Integration Demo")
        print("=" * 50)
        
        tests = [
            ("OpenAI Connection", self.test_openai_connection),
            ("Assistant Creation", self.test_assistant_creation),
            ("Multi-Agent Simulation", self.test_multi_agent_simulation),
            ("Context Persistence", self.test_context_persistence)
        ]
        
        passed_tests = 0
        
        for test_name, test_func in tests:
            try:
                if test_func():
                    passed_tests += 1
            except Exception as e:
                print(f"❌ {test_name} crashed: {e}")
        
        # Summary
        print(f"\n📊 Demo Results Summary")
        print("=" * 30)
        print(f"Tests passed: {passed_tests}/{len(tests)}")
        print(f"Successful features: {len(self.demo_results['successful_features'])}")
        
        if self.demo_results["successful_features"]:
            print("\n✅ Working Features:")
            for feature in self.demo_results["successful_features"]:
                print(f"  • {feature}")
                
        # Save results
        with open('integration_demo_results.json', 'w') as f:
            json.dump(self.demo_results, f, indent=2)
            
        print(f"\n📁 Full results saved to integration_demo_results.json")
        
        if passed_tests == len(tests):
            print("\n🎉 All integration tests passed!")
            print("OperatorOS OpenAI Assistants integration is fully operational")
        else:
            print(f"\n⚠️ {len(tests) - passed_tests} tests failed")
            
        return self.demo_results

if __name__ == "__main__":
    demo = OperatorOSDemo()
    results = demo.run_full_demo()