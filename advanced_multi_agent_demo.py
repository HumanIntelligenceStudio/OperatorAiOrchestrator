#!/usr/bin/env python3
"""
Advanced Multi-Agent Framework Demonstration
Showcases complex financial scenarios using Claude, Grok, and OpenAI coordination
"""

import subprocess
import sys
import os
import json
from datetime import datetime

def run_advanced_demo():
    """Run advanced multi-agent demonstration"""
    
    print("🌟 OperatorOS Advanced Multi-Agent Framework Demo")
    print("=" * 70)
    print("Demonstrating Claude + Grok + OpenAI coordination for complex scenarios")
    print("=" * 70)
    
    demo_script = '''
import json
import logging
from datetime import datetime
from claude_provider import get_claude_provider
from grok_provider import get_grok_provider

# Initialize providers
claude = get_claude_provider()
grok = get_grok_provider()

def scenario_1_merger_analysis():
    """Complex M&A Analysis Scenario"""
    print("\\n🏢 SCENARIO 1: M&A ANALYSIS")
    print("=" * 50)
    
    scenario = """
    ABC Tech Corp (Market Cap: $15B) is acquiring XYZ Energy Solutions ($3B)
    - ABC: AI/software company, 15% annual growth, strong cash position
    - XYZ: Clean energy technology, patents in battery storage, regulatory approvals
    - Deal value: $4.2B (40% premium)
    - Synergies claimed: $500M annually
    - Regulatory concerns: Antitrust in EU markets
    - Timeline: 18 months to close
    
    Analyze: Deal valuation, strategic fit, risks, and investment recommendation
    """
    
    results = {}
    
    # Claude: Financial due diligence and regulatory analysis
    if claude.is_available():
        print("\\n📊 Claude: Financial Due Diligence & Regulatory Analysis")
        try:
            claude_result = claude.financial_analysis(scenario, {
                'analysis_type': 'merger_analysis',
                'focus_areas': ['valuation', 'regulatory_risk', 'financial_synergies']
            })
            if not claude_result.get('error'):
                analysis = claude_result.get('analysis', '')
                print(f"✅ Due diligence complete - {len(analysis)} chars")
                print(f"Key finding: {analysis[:150]}...")
                results['claude_ma'] = 'success'
        except Exception as e:
            print(f"❌ Claude analysis failed: {e}")
            results['claude_ma'] = 'error'
    
    # Grok: Strategic business analysis and competitive positioning
    if grok.is_available():
        print("\\n🎯 Grok: Strategic Analysis & Competitive Intelligence")
        try:
            grok_result = grok.business_analysis(scenario, {
                'analysis_type': 'strategic_ma',
                'focus_areas': ['competitive_position', 'market_dynamics', 'integration_risks']
            })
            if not grok_result.get('error'):
                analysis = grok_result.get('analysis', '')
                print(f"✅ Strategic analysis complete - {len(analysis)} chars")
                print(f"Key insight: {analysis[:150]}...")
                results['grok_ma'] = 'success'
                
                # Additional competitive analysis
                comp_result = grok.competitive_analysis("ABC Tech Corp", "AI Software & Clean Energy")
                if not comp_result.get('error'):
                    comp_analysis = comp_result.get('competitive_analysis', '')
                    print(f"✅ Competitive landscape analysis complete")
                    print(f"Market position: {comp_analysis[:100]}...")
                    results['grok_competitive'] = 'success'
        except Exception as e:
            print(f"❌ Grok analysis failed: {e}")
            results['grok_ma'] = 'error'
    
    return results

def scenario_2_portfolio_optimization():
    """Multi-Provider Portfolio Optimization"""
    print("\\n💼 SCENARIO 2: PORTFOLIO OPTIMIZATION")
    print("=" * 50)
    
    portfolio_data = {
        'current_allocation': {
            'US_Large_Cap': 35,
            'US_Small_Cap': 10, 
            'International_Developed': 15,
            'Emerging_Markets': 8,
            'Bonds': 20,
            'REITs': 7,
            'Cash': 5
        },
        'portfolio_value': 850000,
        'investor_profile': {
            'age': 42,
            'risk_tolerance': 'moderate_aggressive',
            'time_horizon': '15+ years',
            'tax_situation': 'high_bracket',
            'goals': ['retirement', 'wealth_preservation']
        },
        'market_conditions': {
            'interest_rates': 'rising',
            'inflation': 'moderating',
            'economic_cycle': 'mid_cycle',
            'volatility_regime': 'normal'
        },
        'constraints': {
            'max_single_position': 25,
            'min_liquidity': 5,
            'esg_preference': True
        }
    }
    
    print(f"Portfolio Value: ${portfolio_data['portfolio_value']:,}")
    print(f"Current Top Holdings: US Large Cap (35%), Bonds (20%)")
    print(f"Investor: Age {portfolio_data['investor_profile']['age']}, {portfolio_data['investor_profile']['risk_tolerance']}")
    
    results = {}
    
    # Claude: Risk assessment and compliance analysis
    if claude.is_available():
        print("\\n⚖️ Claude: Risk Assessment & Tax Optimization")
        try:
            risk_result = claude.risk_assessment(portfolio_data)
            if not risk_result.get('error'):
                assessment = risk_result.get('risk_assessment', '')
                print(f"✅ Risk assessment complete - {len(assessment)} chars")
                print(f"Risk summary: {assessment[:150]}...")
                results['claude_risk'] = 'success'
        except Exception as e:
            print(f"❌ Claude risk assessment failed: {e}")
            results['claude_risk'] = 'error'
    
    # Grok: Strategic asset allocation and market opportunities
    if grok.is_available():
        print("\\n📈 Grok: Strategic Allocation & Market Opportunities") 
        try:
            strategy_result = grok.investment_strategy(portfolio_data)
            if not strategy_result.get('error'):
                strategy = strategy_result.get('investment_strategy', '')
                print(f"✅ Investment strategy complete - {len(strategy)} chars")
                print(f"Strategy summary: {strategy[:150]}...")
                results['grok_strategy'] = 'success'
                
                # Market opportunity analysis
                market_data = {
                    'sectors': ['Technology', 'Healthcare', 'Clean_Energy', 'Infrastructure'],
                    'geographic_regions': ['US', 'Europe', 'Asia_Pacific', 'Emerging'],
                    'market_themes': ['AI_adoption', 'energy_transition', 'demographic_shifts']
                }
                
                opp_result = grok.market_opportunity_analysis(market_data)
                if not opp_result.get('error'):
                    opportunities = opp_result.get('opportunity_analysis', '')
                    print(f"✅ Market opportunities identified")
                    print(f"Top opportunity: {opportunities[:100]}...")
                    results['grok_opportunities'] = 'success'
        except Exception as e:
            print(f"❌ Grok strategy failed: {e}")
            results['grok_strategy'] = 'error'
    
    return results

def scenario_3_compliance_regulatory():
    """Regulatory Compliance Analysis for Financial Services"""
    print("\\n⚖️ SCENARIO 3: REGULATORY COMPLIANCE")
    print("=" * 50)
    
    compliance_scenario = """
    Global Asset Management Firm Expansion:
    
    Current Status:
    - US-based RIA managing $2.8B AUM
    - 150 institutional clients, 800 high-net-worth individuals
    - Quantitative strategies using alternative data and AI models
    - Current registration: SEC Investment Adviser
    
    Expansion Plans:
    - Launch London office targeting UK and EU institutional clients
    - Introduce cryptocurrency investment strategies (5-15% allocation)
    - Add private credit and direct lending capabilities
    - Implement AI-driven portfolio management for retail clients
    - Target additional $1.5B in AUM within 24 months
    
    Regulatory Requirements: UK FCA registration, GDPR compliance, 
    MiFID II requirements, cryptocurrency regulations, cross-border data transfers
    """
    
    print("Firm: Global asset manager expanding to UK/EU")
    print("Current AUM: $2.8B, Target: +$1.5B")
    print("New services: Crypto strategies, AI portfolio management")
    
    results = {}
    
    # Claude: Comprehensive regulatory compliance analysis
    if claude.is_available():
        print("\\n📋 Claude: Comprehensive Compliance Analysis")
        try:
            # US compliance
            us_result = claude.compliance_analysis(compliance_scenario, "US")
            if not us_result.get('error'):
                us_compliance = us_result.get('compliance_analysis', '')
                print(f"✅ US compliance analysis complete - {len(us_compliance)} chars")
                print(f"US requirements: {us_compliance[:120]}...")
                results['claude_us_compliance'] = 'success'
            
            # UK/EU compliance
            uk_result = claude.compliance_analysis(compliance_scenario, "UK")
            if not uk_result.get('error'):
                uk_compliance = uk_result.get('compliance_analysis', '')
                print(f"✅ UK compliance analysis complete - {len(uk_compliance)} chars") 
                print(f"UK requirements: {uk_compliance[:120]}...")
                results['claude_uk_compliance'] = 'success'
                
        except Exception as e:
            print(f"❌ Claude compliance analysis failed: {e}")
            results['claude_compliance'] = 'error'
    
    # Grok: Business strategy and operational planning
    if grok.is_available():
        print("\\n🌍 Grok: International Expansion Strategy")
        try:
            expansion_query = f"""
            Analyze the operational and strategic aspects of this global expansion:
            {compliance_scenario}
            
            Focus on: market entry strategy, competitive positioning,
            operational setup, technology infrastructure, talent acquisition
            """
            
            expansion_result = grok.business_analysis(expansion_query)
            if not expansion_result.get('error'):
                expansion = expansion_result.get('analysis', '')
                print(f"✅ Expansion strategy complete - {len(expansion)} chars")
                print(f"Strategy overview: {expansion[:150]}...")
                results['grok_expansion'] = 'success'
        except Exception as e:
            print(f"❌ Grok expansion analysis failed: {e}")
            results['grok_expansion'] = 'error'
    
    return results

def main():
    """Execute all advanced scenarios"""
    print("Running 3 complex multi-agent scenarios...")
    
    all_results = {
        'timestamp': datetime.now().isoformat(),
        'scenarios': {}
    }
    
    # Run all scenarios
    all_results['scenarios']['merger_analysis'] = scenario_1_merger_analysis()
    all_results['scenarios']['portfolio_optimization'] = scenario_2_portfolio_optimization()  
    all_results['scenarios']['regulatory_compliance'] = scenario_3_compliance_regulatory()
    
    # Summary
    print("\\n🎉 ADVANCED MULTI-AGENT DEMO COMPLETE")
    print("=" * 60)
    
    total_tasks = sum(len(scenario_results) for scenario_results in all_results['scenarios'].values())
    successful_tasks = sum(
        sum(1 for result in scenario_results.values() if result == 'success')
        for scenario_results in all_results['scenarios'].values()
    )
    
    print(f"Scenarios Completed: {len(all_results['scenarios'])}/3")
    print(f"Individual Tasks: {successful_tasks}/{total_tasks} successful")
    
    print("\\n🤖 Multi-Agent Capabilities Demonstrated:")
    print("• Claude Sonnet-4: Financial analysis, risk assessment, regulatory compliance")
    print("• Grok-2: Business strategy, competitive intelligence, market opportunities")  
    print("• Coordinated Analysis: Complex scenarios requiring multiple AI perspectives")
    print("• Real-world Applications: M&A, portfolio optimization, regulatory compliance")
    
    # Save comprehensive results
    with open('advanced_multi_agent_results.json', 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    
    print("\\nDetailed results saved to: advanced_multi_agent_results.json")
    
    return successful_tasks, total_tasks

if __name__ == "__main__":
    main()
    '''
    
    try:
        # Run the advanced demo
        result = subprocess.run([
            sys.executable, '-c', demo_script
        ], capture_output=True, text=True, timeout=300, cwd='/home/runner/workspace')
        
        print(result.stdout)
        
        if result.stderr:
            print("Logs:", result.stderr.split('\n')[-10:])  # Show last 10 log lines
        
        # Check if results file was created
        try:
            with open('/home/runner/workspace/advanced_multi_agent_results.json', 'r') as f:
                results = json.load(f)
                print(f"\n📊 Final Summary:")
                print(f"Demo timestamp: {results.get('timestamp', 'Unknown')}")
                print(f"Scenarios executed: {len(results.get('scenarios', {}))}")
                
        except FileNotFoundError:
            print("Results file not found")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("❌ Advanced demo timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"❌ Advanced demo failed: {e}")
        return False

if __name__ == "__main__":
    success = run_advanced_demo()
    print(f"\n{'🎉' if success else '❌'} Advanced Multi-Agent Demo {'Completed' if success else 'Failed'}")