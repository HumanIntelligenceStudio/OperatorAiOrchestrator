#!/usr/bin/env python3
"""
Sports Arbitrage Betting Finder
Uses Alpha Vantage API to find arbitrage opportunities
"""

import sys
import os
sys.path.append('.')

from sports_data_provider import SportsDataProvider
import json
from datetime import datetime
import logging

class ArbitrageFinder:
    def __init__(self):
        self.sports_provider = SportsDataProvider()
        
    def calculate_arbitrage(self, odds_data):
        """
        Calculate if arbitrage opportunity exists
        Returns arbitrage percentage and recommended bet amounts
        """
        arbitrage_opportunities = []
        
        try:
            if not isinstance(odds_data, dict) or 'data' not in odds_data:
                return {"error": "Invalid odds data format"}
            
            games = odds_data.get('data', [])
            if not games:
                return {"message": "No games available for arbitrage analysis"}
            
            for game in games[:5]:  # Analyze first 5 games
                try:
                    home_team = game.get('home_team', 'Unknown')
                    away_team = game.get('away_team', 'Unknown')
                    
                    # Extract odds from different bookmakers if available
                    bookmaker_odds = game.get('bookmakers', [])
                    
                    if len(bookmaker_odds) >= 2:
                        # Find best odds for each outcome
                        best_home_odds = 0
                        best_away_odds = 0
                        best_home_book = ""
                        best_away_book = ""
                        
                        for book in bookmaker_odds:
                            book_name = book.get('name', 'Unknown')
                            markets = book.get('markets', [])
                            
                            for market in markets:
                                if market.get('key') == 'h2h':  # Head to head market
                                    outcomes = market.get('outcomes', [])
                                    
                                    for outcome in outcomes:
                                        if outcome.get('name') == home_team:
                                            odds = float(outcome.get('price', 0))
                                            if odds > best_home_odds:
                                                best_home_odds = odds
                                                best_home_book = book_name
                                        
                                        elif outcome.get('name') == away_team:
                                            odds = float(outcome.get('price', 0))
                                            if odds > best_away_odds:
                                                best_away_odds = odds
                                                best_away_book = book_name
                        
                        # Calculate arbitrage if we have odds
                        if best_home_odds > 0 and best_away_odds > 0:
                            # Convert to implied probabilities
                            home_prob = 1 / best_home_odds
                            away_prob = 1 / best_away_odds
                            total_prob = home_prob + away_prob
                            
                            # Check for arbitrage (total probability < 1)
                            if total_prob < 1.0:
                                arbitrage_percent = (1 - total_prob) * 100
                                
                                # Calculate optimal bet amounts for $100 total
                                total_stake = 100
                                home_stake = (home_prob / total_prob) * total_stake
                                away_stake = (away_prob / total_prob) * total_stake
                                
                                # Calculate potential profit
                                profit = total_stake * arbitrage_percent / 100
                                
                                arbitrage_opportunities.append({
                                    "game": f"{away_team} @ {home_team}",
                                    "arbitrage_percentage": round(arbitrage_percent, 2),
                                    "profit_per_100": round(profit, 2),
                                    "betting_strategy": {
                                        "home_bet": {
                                            "team": home_team,
                                            "bookmaker": best_home_book,
                                            "odds": best_home_odds,
                                            "stake": round(home_stake, 2)
                                        },
                                        "away_bet": {
                                            "team": away_team,
                                            "bookmaker": best_away_book,
                                            "odds": best_away_odds,
                                            "stake": round(away_stake, 2)
                                        }
                                    }
                                })
                
                except Exception as e:
                    logging.warning(f"Error processing game: {e}")
                    continue
            
            return {
                "arbitrage_opportunities": arbitrage_opportunities,
                "total_opportunities": len(arbitrage_opportunities),
                "analysis_time": datetime.now().isoformat()
            }
            
        except Exception as e:
            logging.error(f"Error in arbitrage calculation: {e}")
            return {"error": f"Arbitrage calculation failed: {str(e)}"}
    
    def find_today_arbitrage(self):
        """Find arbitrage opportunities for today's games"""
        print("🔍 Searching for Arbitrage Betting Opportunities")
        print("=" * 50)
        
        # Check API availability
        features = self.sports_provider.get_available_features()
        
        if not features.get('alpha_vantage_available'):
            return {
                "error": "Alpha Vantage API required for betting odds",
                "message": "Please ensure ALPHA_API_KEY is configured"
            }
        
        print("✅ Alpha Vantage API connected")
        
        # Get betting odds for major sports
        sports_to_check = ['NBA', 'NFL', 'MLB', 'NHL']
        all_arbitrage = []
        
        for sport in sports_to_check:
            print(f"\n🏈 Checking {sport} games...")
            
            try:
                odds_data = self.sports_provider.get_sports_betting_odds(sport)
                
                if odds_data and not odds_data.get('error'):
                    arbitrage_result = self.calculate_arbitrage(odds_data)
                    
                    if arbitrage_result.get('arbitrage_opportunities'):
                        opportunities = arbitrage_result['arbitrage_opportunities']
                        all_arbitrage.extend(opportunities)
                        print(f"   Found {len(opportunities)} arbitrage opportunities")
                    else:
                        print(f"   No arbitrage found for {sport}")
                else:
                    print(f"   ❌ Could not get odds for {sport}: {odds_data.get('error', 'Unknown error')}")
                    
            except Exception as e:
                print(f"   ❌ Error checking {sport}: {e}")
        
        return {
            "total_arbitrage_opportunities": len(all_arbitrage),
            "opportunities": sorted(all_arbitrage, key=lambda x: x['arbitrage_percentage'], reverse=True),
            "search_completed": datetime.now().isoformat(),
            "sports_checked": sports_to_check
        }

def main():
    finder = ArbitrageFinder()
    results = finder.find_today_arbitrage()
    
    print(f"\n📊 ARBITRAGE ANALYSIS RESULTS")
    print("=" * 50)
    
    if results.get('error'):
        print(f"❌ Error: {results['error']}")
        print(f"   {results.get('message', '')}")
        return
    
    opportunities = results.get('opportunities', [])
    
    if not opportunities:
        print("❌ No arbitrage opportunities found today")
        print("   This is normal - arbitrage opportunities are rare and quickly disappear")
        print("   Consider checking again later or expanding to more bookmakers")
    else:
        print(f"🎉 Found {len(opportunities)} arbitrage opportunities!")
        
        for i, opp in enumerate(opportunities, 1):
            print(f"\n📈 Opportunity #{i}")
            print(f"   Game: {opp['game']}")
            print(f"   Arbitrage: {opp['arbitrage_percentage']}%")
            print(f"   Profit per $100: ${opp['profit_per_100']}")
            
            strategy = opp['betting_strategy']
            print(f"   Strategy:")
            print(f"     • Bet ${strategy['home_bet']['stake']} on {strategy['home_bet']['team']}")
            print(f"       at {strategy['home_bet']['bookmaker']} (odds: {strategy['home_bet']['odds']})")
            print(f"     • Bet ${strategy['away_bet']['stake']} on {strategy['away_bet']['team']}")
            print(f"       at {strategy['away_bet']['bookmaker']} (odds: {strategy['away_bet']['odds']})")
    
    print(f"\n⏰ Analysis completed at {results['search_completed']}")

if __name__ == "__main__":
    main()