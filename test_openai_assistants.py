#!/usr/bin/env python3
"""
Test OpenAI Assistants Integration in OperatorOS
Demonstrates persistent conversation management and multi-agent orchestration
"""

import sys
import os
sys.path.append('.')

import json
from datetime import datetime
import logging
from openai import OpenAI

# Test the AI providers integration
def test_openai_connection():
    """Test basic OpenAI API connection"""
    print("Testing OpenAI API Connection")
    print("=" * 35)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment")
        return False
    
    print(f"✅ OPENAI_API_KEY found: {api_key[:8]}...")
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Test basic completion
        print("🔄 Testing basic chat completion...")
        response = client.chat.completions.create(
            model="gpt-4o",  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
            messages=[
                {"role": "system", "content": "You are a test assistant. Respond briefly."},
                {"role": "user", "content": "Say 'OpenAI connection successful'"}
            ],
            max_tokens=50
        )
        
        result = response.choices[0].message.content
        print(f"✅ Response: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ OpenAI connection failed: {e}")
        return False

def test_assistants_api():
    """Test OpenAI Assistants API for persistent conversations"""
    print("\nTesting OpenAI Assistants API")
    print("=" * 35)
    
    api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ OPENAI_API_KEY required")
        return False
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Create a test assistant
        print("🔄 Creating test assistant...")
        assistant = client.beta.assistants.create(
            name="OperatorOS Test Agent",
            instructions="You are a specialized AI agent in the OperatorOS multi-agent system. Provide concise, helpful responses for testing purposes. Remember context from previous messages.",
            model="gpt-4o"  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
        )
        
        print(f"✅ Assistant created: {assistant.id}")
        
        # Create a thread for conversation
        print("🔄 Creating conversation thread...")
        thread = client.beta.threads.create()
        print(f"✅ Thread created: {thread.id}")
        
        # Test conversation flow
        messages = [
            "Hello, I'm testing the OperatorOS assistant integration.",
            "Can you remember what I just said about testing?",
            "What system are we testing?"
        ]
        
        conversation_history = []
        
        for i, message in enumerate(messages, 1):
            print(f"\n💬 Message {i}: {message}")
            
            # Add message to thread
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=message
            )
            
            # Run the assistant
            run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id
            )
            
            # Wait for completion
            import time
            while run.status in ['queued', 'in_progress']:
                time.sleep(1)
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
            
            if run.status == 'completed':
                # Get the response
                messages_response = client.beta.threads.messages.list(
                    thread_id=thread.id
                )
                
                latest_message = messages_response.data[0]
                assistant_response = latest_message.content[0].text.value
                
                print(f"🤖 Assistant: {assistant_response}")
                
                conversation_history.append({
                    "user": message,
                    "assistant": assistant_response,
                    "timestamp": datetime.now().isoformat()
                })
            else:
                print(f"❌ Run failed with status: {run.status}")
                break
        
        # Clean up - delete the test assistant
        print(f"\n🗑️ Cleaning up test assistant...")
        client.beta.assistants.delete(assistant.id)
        print("✅ Test assistant deleted")
        
        return {
            "success": True,
            "assistant_id": assistant.id,
            "thread_id": thread.id,
            "conversation_history": conversation_history
        }
        
    except Exception as e:
        print(f"❌ Assistants API test failed: {e}")
        return {"success": False, "error": str(e)}

def test_agent_pools_integration():
    """Test integration with agent pools system"""
    print("\nTesting Agent Pools Integration")
    print("=" * 35)
    
    try:
        # Import the agent pools (avoiding circular imports)
        from ai_providers_enhanced import AIProviderManager
        
        print("🔄 Initializing AI Provider Manager...")
        provider = AIProviderManager()
        
        # Test different agent types
        test_queries = [
            {
                "query": "What are the symptoms of a common cold?",
                "expected_agent": "healthcare",
                "context": "medical advice"
            },
            {
                "query": "Should I invest in tech stocks right now?",
                "expected_agent": "financial", 
                "context": "investment advice"
            },
            {
                "query": "Who will win the Super Bowl this year?",
                "expected_agent": "sports",
                "context": "sports prediction"
            },
            {
                "query": "How can I optimize my business workflow?",
                "expected_agent": "business",
                "context": "business consulting"
            }
        ]
        
        results = []
        
        for test in test_queries:
            print(f"\n📝 Testing: '{test['query'][:50]}...'")
            
            try:
                # This would normally route to the appropriate agent
                response = provider.get_agent_response(
                    query=test['query'],
                    agent_type=test['expected_agent'],
                    context=test['context']
                )
                
                print(f"✅ Agent: {test['expected_agent']}")
                print(f"   Response length: {len(response)} characters")
                print(f"   Preview: {response[:100]}...")
                
                results.append({
                    "query": test['query'],
                    "agent_type": test['expected_agent'],
                    "success": True,
                    "response_length": len(response)
                })
                
            except Exception as e:
                print(f"❌ Error with {test['expected_agent']} agent: {e}")
                results.append({
                    "query": test['query'],
                    "agent_type": test['expected_agent'],
                    "success": False,
                    "error": str(e)
                })
        
        return results
        
    except Exception as e:
        print(f"❌ Agent pools integration test failed: {e}")
        return []

def test_conversation_persistence():
    """Test conversation persistence system"""
    print("\nTesting Conversation Persistence")
    print("=" * 35)
    
    try:
        from models import Conversation, User
        from app import db, app
        
        with app.app_context():
            print("🔄 Testing database conversation storage...")
            
            # Create test user
            test_user = User.query.filter_by(username='test_user').first()
            if not test_user:
                test_user = User(
                    username='test_user',
                    email='test@operatoros.com'
                )
                db.session.add(test_user)
                db.session.commit()
            
            print(f"✅ Test user: {test_user.username}")
            
            # Create test conversation
            conversation = Conversation(
                user_id=test_user.id,
                assistant_id='test_assistant_123',
                thread_id='test_thread_456',
                title='OpenAI Integration Test',
                agent_type='general',
                status='active'
            )
            
            db.session.add(conversation)
            db.session.commit()
            
            print(f"✅ Conversation created: ID {conversation.id}")
            
            # Test retrieval
            retrieved = Conversation.query.filter_by(id=conversation.id).first()
            print(f"✅ Conversation retrieved: {retrieved.title}")
            
            # Clean up
            db.session.delete(conversation)
            db.session.commit()
            print("🗑️ Test conversation cleaned up")
            
            return {
                "success": True,
                "conversation_id": conversation.id,
                "user_id": test_user.id
            }
            
    except Exception as e:
        print(f"❌ Conversation persistence test failed: {e}")
        return {"success": False, "error": str(e)}

def main():
    """Run all OpenAI integration tests"""
    print("🤖 OperatorOS OpenAI Assistants Integration Test")
    print("=" * 50)
    
    results = {
        "openai_connection": False,
        "assistants_api": False,
        "agent_pools": False,
        "conversation_persistence": False,
        "timestamp": datetime.now().isoformat()
    }
    
    # Test 1: Basic OpenAI connection
    results["openai_connection"] = test_openai_connection()
    
    # Test 2: Assistants API
    if results["openai_connection"]:
        assistants_result = test_assistants_api()
        results["assistants_api"] = assistants_result.get("success", False)
        if assistants_result.get("success"):
            results["assistant_demo"] = assistants_result
    
    # Test 3: Agent pools integration
    agent_results = test_agent_pools_integration()
    results["agent_pools"] = len(agent_results) > 0 and any(r.get("success") for r in agent_results)
    results["agent_tests"] = agent_results
    
    # Test 4: Conversation persistence
    persistence_result = test_conversation_persistence()
    results["conversation_persistence"] = persistence_result.get("success", False)
    
    # Summary
    print(f"\n📊 Test Results Summary")
    print("=" * 30)
    print(f"OpenAI Connection: {'✅ PASS' if results['openai_connection'] else '❌ FAIL'}")
    print(f"Assistants API: {'✅ PASS' if results['assistants_api'] else '❌ FAIL'}")
    print(f"Agent Pools: {'✅ PASS' if results['agent_pools'] else '❌ FAIL'}")
    print(f"Persistence: {'✅ PASS' if results['conversation_persistence'] else '❌ FAIL'}")
    
    success_count = sum([
        results["openai_connection"],
        results["assistants_api"], 
        results["agent_pools"],
        results["conversation_persistence"]
    ])
    
    print(f"\nOverall: {success_count}/4 tests passed")
    
    if success_count == 4:
        print("🎉 All OpenAI integration tests passed!")
        print("OperatorOS multi-agent system is fully operational")
    else:
        print("⚠️ Some tests failed - check configuration and API keys")
    
    return results

if __name__ == "__main__":
    test_results = main()
    
    # Save results for analysis
    with open('openai_test_results.json', 'w') as f:
        json.dump(test_results, f, indent=2)
    
    print(f"\n📄 Results saved to openai_test_results.json")