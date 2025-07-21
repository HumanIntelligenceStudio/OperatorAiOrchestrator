#!/usr/bin/env python3
"""
Demo Arbitrage Analysis using available data sources
"""

import json
import requests
from datetime import datetime
import logging

def demonstrate_arbitrage_concept():
    """
    Demonstrate arbitrage betting concept with sample data
    """
    print("🔍 Sports Arbitrage Betting Analysis")
    print("=" * 45)
    
    print("\n📚 What is Sports Arbitrage?")
    print("Arbitrage betting involves placing bets on all possible outcomes")
    print("of a sporting event across different bookmakers to guarantee profit.")
    print("This works when bookmakers offer different odds for the same event.")
    
    # Sample arbitrage calculation with realistic odds
    print("\n📊 Sample Arbitrage Calculation:")
    print("Game: Lakers vs Warriors")
    print("-" * 25)
    
    # Sample odds from different bookmakers
    bookmaker_a_odds = {"Lakers": 2.10, "Warriors": 1.85}  # Bookmaker A
    bookmaker_b_odds = {"Lakers": 1.95, "Warriors": 2.00}  # Bookmaker B
    
    # Find best odds for each team
    best_lakers_odds = max(bookmaker_a_odds["Lakers"], bookmaker_b_odds["Lakers"])
    best_warriors_odds = max(bookmaker_a_odds["Warriors"], bookmaker_b_odds["Warriors"])
    
    print(f"Best Lakers odds: {best_lakers_odds} (Bookmaker A)")
    print(f"Best Warriors odds: {best_warriors_odds} (Bookmaker B)")
    
    # Calculate implied probabilities
    lakers_prob = 1 / best_lakers_odds
    warriors_prob = 1 / best_warriors_odds
    total_prob = lakers_prob + warriors_prob
    
    print(f"\nImplied probabilities:")
    print(f"Lakers: {lakers_prob:.3f} ({lakers_prob*100:.1f}%)")
    print(f"Warriors: {warriors_prob:.3f} ({warriors_prob*100:.1f}%)")
    print(f"Total: {total_prob:.3f} ({total_prob*100:.1f}%)")
    
    if total_prob < 1.0:
        arbitrage_percent = (1 - total_prob) * 100
        print(f"\n✅ ARBITRAGE OPPORTUNITY FOUND!")
        print(f"Arbitrage percentage: {arbitrage_percent:.2f}%")
        
        # Calculate optimal bet amounts for $1000 total
        total_stake = 1000
        lakers_stake = (lakers_prob / total_prob) * total_stake
        warriors_stake = (warriors_prob / total_prob) * total_stake
        
        print(f"\nOptimal betting strategy for ${total_stake}:")
        print(f"• Bet ${lakers_stake:.2f} on Lakers at {best_lakers_odds}")
        print(f"• Bet ${warriors_stake:.2f} on Warriors at {best_warriors_odds}")
        
        # Calculate guaranteed profit
        lakers_payout = lakers_stake * best_lakers_odds
        warriors_payout = warriors_stake * best_warriors_odds
        guaranteed_profit = min(lakers_payout, warriors_payout) - total_stake
        
        print(f"\nGuaranteed profit: ${guaranteed_profit:.2f}")
        print(f"Return on investment: {(guaranteed_profit/total_stake)*100:.2f}%")
        
    else:
        print(f"\n❌ No arbitrage opportunity")
        print(f"Total probability > 100% (bookmaker edge)")
    
    return {
        "arbitrage_found": total_prob < 1.0,
        "arbitrage_percentage": (1 - total_prob) * 100 if total_prob < 1.0 else 0,
        "sample_game": "Lakers vs Warriors",
        "analysis_time": datetime.now().isoformat()
    }

def check_live_sports_data():
    """Check what live sports data we can access"""
    print(f"\n🔄 Checking Live Sports Data Sources...")
    
    # Check our sports API
    try:
        response = requests.get("http://localhost:5000/api/sports/features", timeout=5)
        if response.status_code == 200:
            data = response.json()
            features = data.get('data', {})
            
            print("✅ OperatorOS Sports API Status:")
            print(f"   Alpha Vantage: {'Connected' if features.get('alpha_vantage_available') else 'Disconnected'}")
            print(f"   Polygon.io: {'Connected' if features.get('polygon_available') else 'Disconnected'}")
            
            available_features = [f for f, v in features.get('available_features', {}).items() if v]
            print(f"   Available features: {len(available_features)}")
            
            if available_features:
                print("   • " + "\n   • ".join(available_features))
        
    except Exception as e:
        print(f"❌ Could not check API status: {e}")
    
    # Check free sports data sources
    print(f"\n🆓 Free Sports Data Alternatives:")
    print("   • ESPN API (limited)")
    print("   • TheSportsDB (free tier)")
    print("   • API-Sports (limited free calls)")
    print("   • Official league APIs (some free data)")

def main():
    print("🎯 OperatorOS Sports Arbitrage Demo")
    print("=" * 40)
    
    # Run arbitrage demonstration
    demo_result = demonstrate_arbitrage_concept()
    
    # Check available data sources
    check_live_sports_data()
    
    print(f"\n💡 Key Takeaways:")
    print("• Arbitrage opportunities are rare but profitable when found")
    print("• Requires access to multiple bookmaker odds")
    print("• Opportunities disappear quickly (seconds to minutes)")
    print("• Professional arbitrage requires dedicated odds monitoring")
    print("• Most effective with automated systems and multiple accounts")
    
    print(f"\n🔧 Next Steps for Live Arbitrage:")
    print("• Integrate with multiple odds providers (The Odds API, etc.)")
    print("• Set up real-time odds monitoring")
    print("• Add automated arbitrage detection")
    print("• Include commission calculations")
    
    return demo_result

if __name__ == "__main__":
    result = main()
    print(f"\n📈 Demo completed successfully!")