#!/usr/bin/env python3
"""
Real Arbitrage Betting Setup Guide
Shows how to integrate with The Odds API for live arbitrage detection
"""

import requests
import json
from datetime import datetime
import logging

class RealArbitrageAnalyzer:
    """
    Real arbitrage analyzer using The Odds API
    To use: Sign up at https://the-odds-api.com/ for free API key (500 requests/month)
    """
    
    def __init__(self, api_key=None):
        self.api_key = api_key or "demo_key"  # Replace with real API key
        self.base_url = "https://api.the-odds-api.com/v4"
        
    def get_live_odds(self, sport='americanfootball_nfl'):
        """
        Get live odds from The Odds API
        Free tier: 500 requests/month
        """
        if not self.api_key or self.api_key == "demo_key":
            return self._demo_odds_data()
        
        try:
            url = f"{self.base_url}/sports/{sport}/odds"
            params = {
                'api_key': self.api_key,
                'regions': 'us',  # US bookmakers
                'markets': 'h2h',  # Head-to-head markets
                'oddsFormat': 'decimal'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except Exception as e:
            logging.error(f"Error fetching live odds: {e}")
            return {"error": str(e)}
    
    def _demo_odds_data(self):
        """Demo data showing typical odds structure"""
        return [
            {
                "id": "demo_game_1",
                "sport_key": "americanfootball_nfl",
                "commence_time": "2025-01-26T21:00:00Z",
                "home_team": "Kansas City Chiefs",
                "away_team": "Buffalo Bills",
                "bookmakers": [
                    {
                        "key": "draftkings",
                        "title": "DraftKings",
                        "markets": [{
                            "key": "h2h",
                            "outcomes": [
                                {"name": "Kansas City Chiefs", "price": 1.91},
                                {"name": "Buffalo Bills", "price": 1.95}
                            ]
                        }]
                    },
                    {
                        "key": "fanduel",
                        "title": "FanDuel",
                        "markets": [{
                            "key": "h2h",
                            "outcomes": [
                                {"name": "Kansas City Chiefs", "price": 1.87},
                                {"name": "Buffalo Bills", "price": 2.05}
                            ]
                        }]
                    },
                    {
                        "key": "betmgm",
                        "title": "BetMGM",
                        "markets": [{
                            "key": "h2h",
                            "outcomes": [
                                {"name": "Kansas City Chiefs", "price": 1.93},
                                {"name": "Buffalo Bills", "price": 1.92}
                            ]
                        }]
                    }
                ]
            }
        ]
    
    def find_arbitrage_opportunities(self, odds_data):
        """
        Find arbitrage opportunities in odds data
        """
        opportunities = []
        
        for game in odds_data:
            if isinstance(game, dict) and 'bookmakers' in game:
                arb_result = self._analyze_game_for_arbitrage(game)
                if arb_result['arbitrage_found']:
                    opportunities.append(arb_result)
        
        return opportunities
    
    def _analyze_game_for_arbitrage(self, game):
        """Analyze a single game for arbitrage opportunities"""
        home_team = game.get('home_team', 'Home')
        away_team = game.get('away_team', 'Away')
        bookmakers = game.get('bookmakers', [])
        
        # Track best odds for each team
        best_home = {'odds': 0, 'bookmaker': ''}
        best_away = {'odds': 0, 'bookmaker': ''}
        
        # Find best odds across all bookmakers
        for bookmaker in bookmakers:
            bookmaker_name = bookmaker.get('title', 'Unknown')
            markets = bookmaker.get('markets', [])
            
            for market in markets:
                if market.get('key') == 'h2h':
                    outcomes = market.get('outcomes', [])
                    
                    for outcome in outcomes:
                        team_name = outcome.get('name', '')
                        odds = float(outcome.get('price', 0))
                        
                        if team_name == home_team and odds > best_home['odds']:
                            best_home = {'odds': odds, 'bookmaker': bookmaker_name}
                        elif team_name == away_team and odds > best_away['odds']:
                            best_away = {'odds': odds, 'bookmaker': bookmaker_name}
        
        # Calculate arbitrage
        if best_home['odds'] > 0 and best_away['odds'] > 0:
            home_prob = 1 / best_home['odds']
            away_prob = 1 / best_away['odds']
            total_prob = home_prob + away_prob
            
            arbitrage_found = total_prob < 1.0
            arbitrage_percent = (1 - total_prob) * 100 if arbitrage_found else 0
            
            # Calculate optimal stakes for $1000
            if arbitrage_found:
                total_stake = 1000
                home_stake = (home_prob / total_prob) * total_stake
                away_stake = (away_prob / total_prob) * total_stake
                guaranteed_profit = total_stake * arbitrage_percent / 100
                
                return {
                    'arbitrage_found': True,
                    'game': f"{away_team} @ {home_team}",
                    'arbitrage_percentage': round(arbitrage_percent, 3),
                    'guaranteed_profit': round(guaranteed_profit, 2),
                    'strategy': {
                        'home_bet': {
                            'team': home_team,
                            'bookmaker': best_home['bookmaker'],
                            'odds': best_home['odds'],
                            'stake': round(home_stake, 2)
                        },
                        'away_bet': {
                            'team': away_team,
                            'bookmaker': best_away['bookmaker'],
                            'odds': best_away['odds'],
                            'stake': round(away_stake, 2)
                        }
                    }
                }
        
        return {
            'arbitrage_found': False,
            'game': f"{away_team} @ {home_team}",
            'reason': 'No arbitrage opportunity - bookmaker edge exists'
        }

def demonstrate_real_arbitrage():
    """Demonstrate with realistic data"""
    print("🎯 Real Sports Arbitrage Analysis")
    print("=" * 40)
    
    analyzer = RealArbitrageAnalyzer()
    
    print("📊 Analyzing live NFL odds...")
    odds_data = analyzer.get_live_odds('americanfootball_nfl')
    
    if isinstance(odds_data, dict) and 'error' in odds_data:
        print(f"❌ Error getting odds: {odds_data['error']}")
        return
    
    opportunities = analyzer.find_arbitrage_opportunities(odds_data)
    
    print(f"\n🔍 Analysis Results:")
    print(f"Games analyzed: {len(odds_data)}")
    print(f"Arbitrage opportunities found: {len(opportunities)}")
    
    if opportunities:
        print(f"\n🎉 ARBITRAGE OPPORTUNITIES:")
        for i, opp in enumerate(opportunities, 1):
            print(f"\n#{i}. {opp['game']}")
            print(f"   Arbitrage: {opp['arbitrage_percentage']}%")
            print(f"   Guaranteed profit: ${opp['guaranteed_profit']}")
            print(f"   Strategy:")
            print(f"     • ${opp['strategy']['home_bet']['stake']} on {opp['strategy']['home_bet']['team']}")
            print(f"       at {opp['strategy']['home_bet']['bookmaker']} ({opp['strategy']['home_bet']['odds']})")
            print(f"     • ${opp['strategy']['away_bet']['stake']} on {opp['strategy']['away_bet']['team']}")
            print(f"       at {opp['strategy']['away_bet']['bookmaker']} ({opp['strategy']['away_bet']['odds']})")
    else:
        print(f"\n❌ No arbitrage opportunities found")
        print("This is normal - arbitrage occurs when bookmakers have pricing errors")
        print("Real opportunities typically last only seconds to minutes")
    
    return {
        'games_analyzed': len(odds_data),
        'opportunities_found': len(opportunities),
        'opportunities': opportunities
    }

def show_setup_instructions():
    """Show how to set up real arbitrage monitoring"""
    print(f"\n🔧 Setting Up Live Arbitrage Monitoring:")
    print("=" * 45)
    
    print("1. 📝 Get Free API Key from The Odds API:")
    print("   • Visit: https://the-odds-api.com/")
    print("   • Sign up for free account")
    print("   • Get 500 requests/month free")
    
    print("\n2. 🔑 Configure API Key:")
    print("   • Add THE_ODDS_API_KEY to environment secrets")
    print("   • Update RealArbitrageAnalyzer with your key")
    
    print("\n3. 📈 Production Considerations:")
    print("   • Monitor multiple sports simultaneously")
    print("   • Check odds every 1-2 minutes")
    print("   • Set up alerts for arbitrage opportunities")
    print("   • Account for bookmaker commission/juice")
    print("   • Consider withdrawal limits and bet limits")
    
    print("\n4. 🚀 Advanced Features to Add:")
    print("   • Real-time WebSocket connections")
    print("   • Automated bet placement (requires bookmaker APIs)")
    print("   • Portfolio management and risk analysis")
    print("   • Historical arbitrage tracking")

if __name__ == "__main__":
    result = demonstrate_real_arbitrage()
    show_setup_instructions()
    print(f"\n✅ Arbitrage analysis complete!")