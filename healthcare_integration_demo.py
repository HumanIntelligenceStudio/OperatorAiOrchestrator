"""
Healthcare Data Integration Demo
Demonstrates CMS and OpenFDA data integration with AI analysis
"""

import json
import logging
from datetime import datetime
from cms_provider import CMSProvider
from openfda_provider import OpenFDAProvider
from claude_provider import ClaudeProvider
from grok_provider import GrokProvider

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_healthcare_apis():
    """Test connectivity to both CMS and OpenFDA APIs"""
    results = {
        'timestamp': datetime.now().isoformat(),
        'test_type': 'healthcare_api_connectivity',
        'results': {}
    }
    
    # Test CMS API
    cms = CMSProvider()
    cms_status = cms.test_connection()
    results['results']['cms'] = {
        'status': 'success' if cms_status else 'failed',
        'api_name': 'Centers for Medicare & Medicaid Services',
        'connection_test': cms_status
    }
    
    # Test OpenFDA API
    fda = OpenFDAProvider()
    fda_status = fda.test_connection()
    results['results']['openfda'] = {
        'status': 'success' if fda_status else 'failed',
        'api_name': 'OpenFDA - Food and Drug Administration',
        'connection_test': fda_status
    }
    
    results['overall_status'] = 'success' if (cms_status and fda_status) else 'partial'
    results['apis_operational'] = sum([cms_status, fda_status])
    results['total_apis_tested'] = 2
    
    return results

def run_healthcare_data_demo():
    """Run comprehensive healthcare data integration demo"""
    demo_results = {
        'timestamp': datetime.now().isoformat(),
        'demo_type': 'healthcare_data_integration',
        'data_sources': ['CMS', 'OpenFDA'],
        'results': {}
    }
    
    # Initialize providers
    cms = CMSProvider()
    fda = OpenFDAProvider()
    
    # 1. CMS Healthcare Quality Data
    logging.info("Fetching CMS hospital quality data...")
    cms_quality = cms.get_hospital_quality_data(limit=5)
    demo_results['results']['cms_hospital_quality'] = cms_quality
    
    # 2. CMS Medicare Spending Data
    logging.info("Fetching CMS Medicare spending data...")
    cms_spending = cms.get_medicare_spending_data(limit=5)
    demo_results['results']['cms_medicare_spending'] = cms_spending
    
    # 3. FDA Drug Adverse Events
    logging.info("Fetching FDA drug adverse events...")
    fda_drug_events = fda.get_drug_adverse_events(limit=5)
    demo_results['results']['fda_drug_adverse_events'] = fda_drug_events
    
    # 4. FDA Drug Recalls
    logging.info("Fetching FDA drug recalls...")
    fda_recalls = fda.get_drug_recalls(limit=5)
    demo_results['results']['fda_drug_recalls'] = fda_recalls
    
    # 5. FDA Device Adverse Events
    logging.info("Fetching FDA device adverse events...")
    fda_device_events = fda.get_device_adverse_events(limit=3)
    demo_results['results']['fda_device_events'] = fda_device_events
    
    # Calculate summary metrics
    total_records = 0
    successful_queries = 0
    
    for result_key, result_data in demo_results['results'].items():
        if result_data.get('status') == 'success':
            successful_queries += 1
            total_records += result_data.get('total_records', 0)
    
    demo_results['summary'] = {
        'total_data_records': total_records,
        'successful_queries': successful_queries,
        'total_queries': len(demo_results['results']),
        'success_rate': f"{(successful_queries / len(demo_results['results']) * 100):.1f}%"
    }
    
    return demo_results

def run_ai_healthcare_analysis():
    """Run AI analysis of healthcare data using Claude and Grok"""
    analysis_results = {
        'timestamp': datetime.now().isoformat(),
        'analysis_type': 'multi_provider_healthcare_analysis',
        'ai_providers': ['Claude', 'Grok'],
        'results': {}
    }
    
    # Initialize AI providers
    claude = ClaudeProvider()
    grok = GrokProvider()
    
    # Get healthcare data for analysis
    cms = CMSProvider()
    fda = OpenFDAProvider()
    
    # Collect comprehensive healthcare data
    healthcare_data = {
        'cms_trends': cms.analyze_healthcare_trends(),
        'fda_safety': fda.analyze_safety_trends()
    }
    
    # Prepare data summary for AI analysis
    data_summary = f"""
    Healthcare Data Analysis Request:
    
    CMS Data Summary:
    - Healthcare trends analysis: {healthcare_data['cms_trends'].get('status', 'unknown')}
    - Total CMS data points: {healthcare_data['cms_trends'].get('total_data_points', 0)}
    - Focus areas: Quality metrics, Medicare spending, Provider comparison
    
    FDA Data Summary:
    - Safety trends analysis: {healthcare_data['fda_safety'].get('status', 'unknown')}
    - Total FDA data points: {healthcare_data['fda_safety'].get('total_data_points', 0)}
    - Focus areas: Drug adverse events, recalls, device safety
    
    Please analyze these healthcare data trends and provide insights on:
    1. Healthcare quality and safety patterns
    2. Cost and spending trend implications
    3. Risk factors and safety concerns
    4. Recommendations for healthcare providers and patients
    """
    
    # Claude Analysis - Healthcare Quality Focus
    logging.info("Running Claude analysis on healthcare data...")
    try:
        claude_prompt = f"""
        As a healthcare data analyst, analyze the following healthcare data and provide insights focused on quality of care, regulatory compliance, and patient safety:
        
        {data_summary}
        
        Provide a comprehensive analysis covering healthcare quality metrics, regulatory compliance patterns, and patient safety recommendations.
        """
        
        claude_response = claude.financial_analysis(claude_prompt)
        analysis_results['results']['claude'] = {
            'status': 'success',
            'model': claude.default_model,
            'focus': 'healthcare_quality_and_safety',
            'analysis_length': len(str(claude_response)) if claude_response else 0,
            'response': claude_response
        }
    except Exception as e:
        analysis_results['results']['claude'] = {
            'status': 'error',
            'error': str(e)
        }
    
    # Grok Analysis - Healthcare Innovation Focus
    logging.info("Running Grok analysis on healthcare data...")
    try:
        grok_prompt = f"""
        As a healthcare innovation strategist, analyze the following healthcare data and provide insights focused on market opportunities, healthcare technology trends, and strategic recommendations:
        
        {data_summary}
        
        Provide strategic insights on healthcare innovation opportunities, market trends, and technology adoption recommendations.
        """
        
        grok_response = grok.business_analysis(grok_prompt)
        analysis_results['results']['grok'] = {
            'status': 'success',
            'model': grok.default_model,
            'focus': 'healthcare_innovation_and_strategy',
            'analysis_length': len(str(grok_response)) if grok_response else 0,
            'response': grok_response
        }
    except Exception as e:
        analysis_results['results']['grok'] = {
            'status': 'error',
            'error': str(e)
        }
    
    # Calculate combined analysis metrics
    total_analysis_length = 0
    successful_analyses = 0
    
    for provider, result in analysis_results['results'].items():
        if result.get('status') == 'success':
            successful_analyses += 1
            total_analysis_length += result.get('analysis_length', 0)
    
    analysis_results['summary'] = {
        'total_analysis_characters': total_analysis_length,
        'successful_analyses': successful_analyses,
        'total_providers': len(analysis_results['results']),
        'healthcare_data_integration': 'CMS + OpenFDA',
        'ai_coordination': 'Multi-provider healthcare analysis'
    }
    
    return analysis_results

if __name__ == "__main__":
    print("=== OperatorOS Healthcare Integration Demo ===")
    print()
    
    # 1. Test API Connectivity
    print("1. Testing Healthcare API Connectivity...")
    api_tests = test_healthcare_apis()
    print(f"APIs Operational: {api_tests['apis_operational']}/{api_tests['total_apis_tested']}")
    print(f"Overall Status: {api_tests['overall_status']}")
    print()
    
    # 2. Healthcare Data Integration Demo
    print("2. Running Healthcare Data Integration Demo...")
    data_demo = run_healthcare_data_demo()
    print(f"Data Queries: {data_demo['summary']['successful_queries']}/{data_demo['summary']['total_queries']}")
    print(f"Total Records: {data_demo['summary']['total_data_records']}")
    print(f"Success Rate: {data_demo['summary']['success_rate']}")
    print()
    
    # 3. AI Healthcare Analysis
    print("3. Running Multi-Provider AI Healthcare Analysis...")
    ai_analysis = run_ai_healthcare_analysis()
    print(f"AI Analyses: {ai_analysis['summary']['successful_analyses']}/{ai_analysis['summary']['total_providers']}")
    print(f"Total Analysis: {ai_analysis['summary']['total_analysis_characters']} characters")
    print()
    
    # Save results
    results_file = f"healthcare_integration_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    all_results = {
        'api_tests': api_tests,
        'data_demo': data_demo,
        'ai_analysis': ai_analysis
    }
    
    with open(results_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"Results saved to: {results_file}")
    print("=== Healthcare Integration Demo Complete ===")