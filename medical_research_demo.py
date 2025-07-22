#!/usr/bin/env python3
"""
OperatorOS Medical Research System Demonstration
Shows complete capabilities for shoulder arthroplasty analysis
"""

import json
import requests
from datetime import datetime
from shoulder_arthroplasty_analysis import run_shoulder_arthroplasty_analysis

def demonstrate_medical_research_capabilities():
    """
    Comprehensive demonstration of OperatorOS medical research capabilities
    """
    print("=== OperatorOS Medical Research System Demonstration ===")
    print()
    
    print("🏥 MEDICAL RESEARCH ANALYSIS PLATFORM")
    print("Comprehensive shoulder arthroplasty reimbursement analysis")
    print()
    
    # Execute the shoulder arthroplasty analysis
    print("📊 EXECUTING COMPREHENSIVE ANALYSIS...")
    print("CPT Codes: 23470, 23472, 23473, 23474")
    print("Analysis Period: 2015-2025")
    print("AI Providers: Claude Sonnet-4 + Grok-2")
    print()
    
    results = run_shoulder_arthroplasty_analysis()
    
    print()
    print("✅ ANALYSIS COMPLETE - DETAILED RESULTS:")
    print()
    
    # Display key metrics
    if results.get('execution_summary'):
        summary = results['execution_summary']
        print(f"📋 CPT Codes Analyzed: {summary.get('total_cpt_codes_analyzed', 0)}")
        print(f"🔬 Analysis Phases: {summary.get('analysis_phases_completed', 0)}/4")
        print(f"🤖 AI Providers: {summary.get('ai_providers_utilized', 0)}")
        print(f"📊 Data Sources: {len(summary.get('data_sources', []))}")
        print(f"📈 Statistical Tests: {len(summary.get('statistical_tests_performed', []))}")
        print(f"🗺️ Geographic Coverage: {summary.get('geographic_coverage', 'Unknown')}")
        print(f"✅ Status: {summary.get('status', 'Unknown').upper()}")
    
    print()
    
    # Display AI analysis metrics
    if results.get('ai_insights', {}).get('summary'):
        ai_summary = results['ai_insights']['summary']
        print(f"🧠 Total AI Analysis: {ai_summary.get('total_analysis_characters', 0):,} characters")
        print(f"🔬 Providers Analyzed: {ai_summary.get('providers_analyzed', 0)}")
        print(f"📝 Analysis Type: {ai_summary.get('analysis_completeness', 'Unknown')}")
    
    print()
    
    # Show economic analysis findings
    if results.get('economic_analysis', {}).get('key_findings'):
        econ_findings = results['economic_analysis']['key_findings']
        print("💰 ECONOMIC ANALYSIS FINDINGS:")
        print(f"   Medical Inflation Premium: {econ_findings.get('medical_inflation_premium', 'N/A')}")
        print(f"   Analysis Significance: {econ_findings.get('analysis_significance', 'N/A')}")
    
    print()
    
    # Show statistical results
    if results.get('statistical_analysis', {}).get('significance_testing'):
        stats = results['statistical_analysis']['significance_testing']
        print("📊 STATISTICAL ANALYSIS RESULTS:")
        
        if 'primary_vs_revision_reimbursement' in stats:
            primary_rev = stats['primary_vs_revision_reimbursement']
            significance = "✅ SIGNIFICANT" if primary_rev.get('statistically_significant') else "❌ NOT SIGNIFICANT"
            print(f"   Primary vs Revision: p={primary_rev.get('p_value', 'N/A')} - {significance}")
            print(f"   Finding: {primary_rev.get('finding', 'N/A')}")
        
        if 'inflation_vs_reimbursement' in stats:
            inflation_stats = stats['inflation_vs_reimbursement']
            if 'all_items_cpi_comparison' in inflation_stats:
                cpi_comp = inflation_stats['all_items_cpi_comparison']
                cpi_significance = "✅ SIGNIFICANT" if cpi_comp.get('statistically_significant') else "❌ NOT SIGNIFICANT"
                print(f"   Reimbursement vs General Inflation: p={cpi_comp.get('p_value', 'N/A')} - {cpi_significance}")
    
    print()
    
    # Show AI provider results
    if results.get('ai_insights', {}).get('providers'):
        providers = results['ai_insights']['providers']
        print("🤖 AI PROVIDER ANALYSIS:")
        
        for provider_name, provider_data in providers.items():
            if provider_data.get('status') == 'success':
                analysis_length = provider_data.get('analysis_length', 0)
                focus = provider_data.get('focus', 'Unknown')
                print(f"   {provider_name.title()}: {analysis_length:,} characters - {focus}")
    
    print()
    print("🎯 MEDICAL RESEARCH CAPABILITIES DEMONSTRATED:")
    print("   ✅ CPT Code-based procedure analysis")
    print("   ✅ Multi-year longitudinal trend analysis")
    print("   ✅ Statistical significance testing") 
    print("   ✅ Economic inflation adjustment methodology")
    print("   ✅ Geographic variation assessment")
    print("   ✅ Multi-provider AI medical economics analysis")
    print("   ✅ Professional research-grade documentation")
    
    print()
    print("📋 RESEARCH USE CASES SUPPORTED:")
    print("   🏥 Healthcare Provider Reimbursement Planning")
    print("   🏭 Medical Device Company Market Intelligence")
    print("   📚 Academic Medical Research Publications")
    print("   🏛️ Healthcare Policy Analysis")
    print("   💼 Healthcare Economics Consulting")
    
    print()
    print(f"📄 Results saved with timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=== Medical Research System Demonstration Complete ===")
    
    return results

if __name__ == "__main__":
    demonstrate_medical_research_capabilities()