#!/usr/bin/env python3
"""
Simple Multi-Provider Demo Runner
Runs the multi-agent framework demonstration safely
"""

import subprocess
import sys
import os

def run_demo():
    """Run the multi-agent demo"""
    print("🚀 Starting Multi-Provider Multi-Agent Framework Demo...")
    
    try:
        # Change to workspace directory
        os.chdir('/home/runner/workspace')
        
        # Run the comprehensive demo
        result = subprocess.run([
            sys.executable, '-c', """
import json
import logging
from datetime import datetime
from claude_provider import get_claude_provider
from grok_provider import get_grok_provider

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def quick_demo():
    print('🌟 OperatorOS Multi-Provider Multi-Agent Framework')
    print('=' * 70)
    
    # Initialize providers
    claude = get_claude_provider()
    grok = get_grok_provider()
    
    # Check availability
    print(f'\\nProvider Status:')
    print(f'Claude Sonnet-4: {"✅ Available" if claude.is_available() else "❌ Unavailable"}')
    print(f'Grok-2: {"✅ Available" if grok.is_available() else "❌ Unavailable"}')
    
    # Demo scenario
    financial_query = '''
    Analyze the investment potential of clean energy sector stocks for a retirement portfolio.
    Consider: regulatory support, market trends, risk factors, and 10-year outlook.
    Portfolio context: $300K total value, moderate risk tolerance, 10-year horizon.
    '''
    
    results = {}
    
    # Claude financial analysis
    if claude.is_available():
        print(f'\\n💼 CLAUDE FINANCIAL ANALYST')
        print('-' * 40)
        try:
            claude_result = claude.financial_analysis(financial_query)
            if not claude_result.get('error'):
                analysis = claude_result.get('analysis', '')
                print(f'✅ Analysis Complete - Model: {claude_result.get("model")}')
                print(f'Key Insight: {analysis[:200]}...')
                results['claude'] = {'status': 'success', 'model': claude_result.get('model')}
            else:
                print(f'❌ Analysis failed: {claude_result.get("error")}')
                results['claude'] = {'status': 'error'}
        except Exception as e:
            print(f'❌ Claude error: {e}')
            results['claude'] = {'status': 'error', 'message': str(e)}
    
    # Grok business analysis  
    if grok.is_available():
        print(f'\\n🎯 GROK BUSINESS STRATEGIST')
        print('-' * 40)
        try:
            grok_result = grok.business_analysis(financial_query)
            if not grok_result.get('error'):
                analysis = grok_result.get('analysis', '')
                print(f'✅ Analysis Complete - Model: {grok_result.get("model")}')
                print(f'Key Insight: {analysis[:200]}...')
                results['grok'] = {'status': 'success', 'model': grok_result.get('model')}
            else:
                print(f'❌ Analysis failed: {grok_result.get("error")}')
                results['grok'] = {'status': 'error'}
        except Exception as e:
            print(f'❌ Grok error: {e}')
            results['grok'] = {'status': 'error', 'message': str(e)}
    
    # Multi-provider comparison
    if results:
        print(f'\\n📊 MULTI-PROVIDER ANALYSIS RESULTS')
        print('=' * 50)
        
        successful_providers = [name for name, data in results.items() if data.get('status') == 'success']
        
        if successful_providers:
            print(f'✅ Successful Analyses: {len(successful_providers)}/2')
            for provider in successful_providers:
                model = results[provider].get('model', 'Unknown')
                print(f'  • {provider.upper()}: {model}')
            
            print(f'\\n🎉 Multi-Provider Framework Operational!')
            print('Key Capabilities:')
            print('• Claude Sonnet-4: Advanced financial analysis and risk assessment')
            print('• Grok-2: Business strategy and market intelligence')
            print('• Real-time multi-model analysis and comparison')
            print('• Comprehensive investment research and recommendations')
            
        else:
            print(f'❌ No successful analyses completed')
    
    # Save results
    with open('quick_demo_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f'\\nResults saved to: quick_demo_results.json')

if __name__ == "__main__":
    quick_demo()
"""], capture_output=True, text=True, timeout=120)
        
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("Demo timed out after 2 minutes")
        return False
    except Exception as e:
        print(f"Demo failed: {e}")
        return False

if __name__ == "__main__":
    success = run_demo()
    print(f"\nDemo {'completed successfully' if success else 'failed'}")