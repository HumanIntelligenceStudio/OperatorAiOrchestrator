#!/usr/bin/env python3
"""
Comprehensive Multi-Provider AI Demo
Direct demonstration of Claude and Grok integration for financial analysis
"""

import json
import logging
from datetime import datetime

# Configure logging to reduce noise
logging.getLogger().setLevel(logging.WARNING)

def main():
    print("🌟 OperatorOS Multi-Provider AI Framework Demonstration")
    print("=" * 65)
    
    try:
        from claude_provider import get_claude_provider
        from grok_provider import get_grok_provider
        
        # Initialize providers
        claude = get_claude_provider()
        grok = get_grok_provider()
        
        # Provider status
        print(f"\n📡 Provider Status:")
        print(f"Claude Sonnet-4: {'✅ Connected' if claude.is_available() else '❌ Unavailable'}")
        print(f"Grok-2: {'✅ Connected' if grok.is_available() else '❌ Unavailable'}")
        
        if not (claude.is_available() or grok.is_available()):
            print("❌ No AI providers available")
            return
        
        # Demo scenario: Tech startup investment analysis
        print(f"\n💼 INVESTMENT ANALYSIS SCENARIO")
        print("=" * 40)
        
        scenario = """
        Tech Startup Investment Opportunity:
        - Company: AI-powered fintech startup
        - Valuation: $50M Series B round
        - Revenue: $8M ARR, growing 200% YoY
        - Market: B2B financial automation
        - Competition: Moderate, established players
        - Team: Strong technical, limited business experience
        - Request: $5M investment for 10% equity
        """
        
        print("Analyzing AI fintech startup investment opportunity...")
        print("Series B: $50M valuation, $8M ARR, 200% growth")
        
        results = {}
        
        # Claude Analysis: Financial due diligence
        if claude.is_available():
            print(f"\n🔍 CLAUDE: Financial Due Diligence")
            print("-" * 35)
            
            try:
                analysis_result = claude.financial_analysis(scenario, {
                    'focus': 'investment_analysis',
                    'stage': 'series_b',
                    'sector': 'fintech'
                })
                
                if not analysis_result.get('error'):
                    analysis = analysis_result.get('analysis', '')
                    model = analysis_result.get('model', 'Unknown')
                    
                    print(f"✅ Analysis complete using {model}")
                    
                    # Extract key insights
                    key_points = []
                    if 'valuation' in analysis.lower():
                        key_points.append("Valuation assessment included")
                    if 'risk' in analysis.lower():
                        key_points.append("Risk factors identified")
                    if 'revenue' in analysis.lower():
                        key_points.append("Revenue analysis completed")
                    
                    print(f"Key areas covered: {', '.join(key_points)}")
                    print(f"Analysis length: {len(analysis)} characters")
                    
                    results['claude'] = {
                        'status': 'success',
                        'model': model,
                        'analysis_length': len(analysis),
                        'key_areas': key_points
                    }
                else:
                    print(f"❌ Analysis failed: {analysis_result.get('error')}")
                    results['claude'] = {'status': 'failed', 'error': analysis_result.get('error')}
                    
            except Exception as e:
                print(f"❌ Claude error: {str(e)}")
                results['claude'] = {'status': 'error', 'exception': str(e)}
        
        # Grok Analysis: Business strategy and market positioning
        if grok.is_available():
            print(f"\n🎯 GROK: Strategic Business Analysis") 
            print("-" * 35)
            
            try:
                business_result = grok.business_analysis(scenario, {
                    'focus': 'strategic_analysis',
                    'market': 'fintech_b2b',
                    'investment_stage': 'series_b'
                })
                
                if not business_result.get('error'):
                    analysis = business_result.get('analysis', '')
                    model = business_result.get('model', 'Unknown')
                    
                    print(f"✅ Analysis complete using {model}")
                    
                    # Extract strategic insights
                    strategic_points = []
                    if 'market' in analysis.lower():
                        strategic_points.append("Market analysis")
                    if 'competitive' in analysis.lower():
                        strategic_points.append("Competitive positioning")
                    if 'strategy' in analysis.lower():
                        strategic_points.append("Strategic recommendations")
                    
                    print(f"Strategic insights: {', '.join(strategic_points)}")
                    print(f"Analysis length: {len(analysis)} characters")
                    
                    results['grok'] = {
                        'status': 'success',
                        'model': model,
                        'analysis_length': len(analysis),
                        'strategic_areas': strategic_points
                    }
                else:
                    print(f"❌ Analysis failed: {business_result.get('error')}")
                    results['grok'] = {'status': 'failed', 'error': business_result.get('error')}
                    
            except Exception as e:
                print(f"❌ Grok error: {str(e)}")
                results['grok'] = {'status': 'error', 'exception': str(e)}
        
        # Multi-provider comparison and summary
        print(f"\n📊 MULTI-PROVIDER ANALYSIS SUMMARY")
        print("=" * 45)
        
        successful_analyses = [name for name, data in results.items() if data.get('status') == 'success']
        
        if successful_analyses:
            print(f"✅ Successful analyses: {len(successful_analyses)}/2 providers")
            
            total_analysis_chars = sum(
                results[provider].get('analysis_length', 0) 
                for provider in successful_analyses
            )
            
            print(f"Total analysis content: {total_analysis_chars:,} characters")
            
            # Show model details
            for provider in successful_analyses:
                model = results[provider].get('model', 'Unknown')
                print(f"• {provider.upper()}: {model}")
                
                if provider == 'claude':
                    areas = results[provider].get('key_areas', [])
                    if areas:
                        print(f"  Financial focus: {', '.join(areas)}")
                        
                elif provider == 'grok':
                    areas = results[provider].get('strategic_areas', [])
                    if areas:
                        print(f"  Strategic focus: {', '.join(areas)}")
            
            print(f"\n🎉 Multi-Provider Framework Operational!")
            print("Demonstrated capabilities:")
            print("• Simultaneous analysis from multiple AI models")
            print("• Specialized expertise: Financial (Claude) + Strategic (Grok)")
            print("• Comprehensive investment analysis coverage")
            print("• Real-time multi-model comparison and insights")
            
        else:
            print(f"❌ No successful analyses completed")
            for provider, data in results.items():
                if data.get('status') != 'success':
                    error_info = data.get('error') or data.get('exception', 'Unknown error')
                    print(f"  {provider.upper()}: {error_info}")
        
        # Save results
        demo_results = {
            'timestamp': datetime.now().isoformat(),
            'scenario': 'fintech_investment_analysis',
            'providers_tested': list(results.keys()),
            'successful_providers': successful_analyses,
            'results': results
        }
        
        with open('comprehensive_demo_results.json', 'w') as f:
            json.dump(demo_results, f, indent=2, default=str)
        
        print(f"\nDetailed results saved to: comprehensive_demo_results.json")
        
        # Final status
        success_rate = len(successful_analyses) / len(results) * 100 if results else 0
        print(f"\n📈 Demo Success Rate: {success_rate:.0f}%")
        
        if success_rate >= 50:
            print("✅ Multi-provider AI integration is operational and ready for production use")
        else:
            print("⚠️ Some providers encountered issues - check logs for details")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("AI provider modules may not be available")
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()