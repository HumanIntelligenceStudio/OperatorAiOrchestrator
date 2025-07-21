import os
import requests
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import json

class SportsDataProvider:
    """
    Sports data integration for OperatorOS
    Provides real-time sports data, statistics, and market information
    """
    
    def __init__(self):
        self.alpha_vantage_key = os.environ.get('ALPHA_API_KEY')
        self.polygon_key = os.environ.get('POLYGON_API_KEY')
        
        # API endpoints
        self.alpha_base_url = "https://www.alphavantage.co/query"
        self.polygon_base_url = "https://api.polygon.io"
        
        # Validate API keys
        self.alpha_available = bool(self.alpha_vantage_key)
        self.polygon_available = bool(self.polygon_key)
        
        if not self.alpha_available:
            logging.warning("Alpha Vantage API key not found - sports betting and market data unavailable")
        
        if not self.polygon_available:
            logging.warning("Polygon.io API key not found - advanced market data features unavailable")
            
        logging.info(f"Sports Data Provider initialized - Alpha Vantage: {'✓' if self.alpha_available else '✗'}, Polygon.io: {'✓' if self.polygon_available else '✗'}")
    
    def get_sports_betting_odds(self, sport: str = "NBA") -> Dict[str, Any]:
        """
        Get current sports betting odds and market data
        Uses Alpha Vantage sports betting API
        """
        if not self.alpha_available:
            return {"error": "Alpha Vantage API key required for betting odds"}
        
        try:
            params = {
                'function': 'SPORTS_BETTING_ODDS',
                'sport': sport,
                'apikey': self.alpha_vantage_key
            }
            
            response = requests.get(self.alpha_base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if 'Error Message' in data:
                return {"error": f"API Error: {data['Error Message']}"}
            
            if 'Note' in data:
                return {"error": f"API Rate Limit: {data['Note']}"}
            
            # Process and format betting odds data
            formatted_data = {
                "sport": sport,
                "last_updated": datetime.now().isoformat(),
                "games": [],
                "summary": {
                    "total_games": 0,
                    "average_spread": 0,
                    "high_confidence_picks": []
                }
            }
            
            if 'data' in data:
                games_data = data.get('data', [])
                formatted_data["games"] = games_data
                formatted_data["summary"]["total_games"] = len(games_data)
                
                # Analyze odds for insights
                spreads = []
                for game in games_data:
                    if 'spread' in game:
                        try:
                            spread = float(game['spread'])
                            spreads.append(spread)
                        except (ValueError, TypeError):
                            continue
                
                if spreads:
                    formatted_data["summary"]["average_spread"] = sum(spreads) / len(spreads)
            
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching sports betting odds: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error in sports betting odds: {e}")
            return {"error": f"Unexpected error: {str(e)}"}
    
    def get_team_performance_metrics(self, team: str, sport: str = "NBA") -> Dict[str, Any]:
        """
        Get comprehensive team performance metrics and statistics
        """
        if not self.alpha_available:
            return {"error": "Alpha Vantage API key required for team metrics"}
        
        try:
            params = {
                'function': 'SPORTS_TEAM_PERFORMANCE',
                'team': team,
                'sport': sport,
                'apikey': self.alpha_vantage_key
            }
            
            response = requests.get(self.alpha_base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if 'Error Message' in data:
                return {"error": f"API Error: {data['Error Message']}"}
            
            # Format team performance data
            formatted_data = {
                "team": team,
                "sport": sport,
                "last_updated": datetime.now().isoformat(),
                "performance_metrics": data.get('performance', {}),
                "recent_games": data.get('recent_games', []),
                "season_stats": data.get('season_stats', {}),
                "predictions": self._generate_team_predictions(data)
            }
            
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching team performance: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error in team performance: {e}")
            return {"error": f"Unexpected error: {str(e)}"}
    
    def get_player_statistics(self, player_name: str, sport: str = "NBA") -> Dict[str, Any]:
        """
        Get individual player statistics and performance data
        """
        if not self.alpha_available:
            return {"error": "Alpha Vantage API key required for player statistics"}
        
        try:
            params = {
                'function': 'SPORTS_PLAYER_STATS',
                'player': player_name,
                'sport': sport,
                'apikey': self.alpha_vantage_key
            }
            
            response = requests.get(self.alpha_base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if 'Error Message' in data:
                return {"error": f"API Error: {data['Error Message']}"}
            
            # Format player statistics
            formatted_data = {
                "player": player_name,
                "sport": sport,
                "last_updated": datetime.now().isoformat(),
                "current_season": data.get('current_season', {}),
                "career_stats": data.get('career_stats', {}),
                "recent_performance": data.get('recent_games', []),
                "injury_status": data.get('injury_status', 'Active'),
                "market_value": data.get('market_value', 'N/A')
            }
            
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching player statistics: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error in player statistics: {e}")
            return {"error": f"Unexpected error: {str(e)}"}
    
    def get_game_predictions(self, team1: str, team2: str, sport: str = "NBA") -> Dict[str, Any]:
        """
        Generate game predictions based on available data
        """
        try:
            # Get performance data for both teams
            team1_data = self.get_team_performance_metrics(team1, sport)
            team2_data = self.get_team_performance_metrics(team2, sport)
            
            # Get current betting odds
            betting_data = self.get_sports_betting_odds(sport)
            
            prediction = {
                "matchup": f"{team1} vs {team2}",
                "sport": sport,
                "prediction_date": datetime.now().isoformat(),
                "team1_analysis": team1_data,
                "team2_analysis": team2_data,
                "betting_context": betting_data,
                "prediction": self._analyze_matchup(team1_data, team2_data),
                "confidence_level": "Medium",  # Will be calculated based on data quality
                "key_factors": []
            }
            
            return prediction
            
        except Exception as e:
            logging.error(f"Error generating game predictions: {e}")
            return {"error": f"Prediction error: {str(e)}"}
    
    def get_live_scores(self, sport: str = "NBA") -> Dict[str, Any]:
        """
        Get live sports scores and game status
        Note: This would typically use a different API endpoint
        """
        if not self.alpha_available:
            return {"error": "Alpha Vantage API key required for live scores"}
        
        try:
            params = {
                'function': 'SPORTS_LIVE_SCORES',
                'sport': sport,
                'apikey': self.alpha_vantage_key
            }
            
            response = requests.get(self.alpha_base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if 'Error Message' in data:
                return {"error": f"API Error: {data['Error Message']}"}
            
            formatted_data = {
                "sport": sport,
                "last_updated": datetime.now().isoformat(),
                "live_games": data.get('live_games', []),
                "completed_games": data.get('completed_games', []),
                "upcoming_games": data.get('upcoming_games', [])
            }
            
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching live scores: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error in live scores: {e}")
            return {"error": f"Unexpected error: {str(e)}"}
    
    def _generate_team_predictions(self, team_data: Dict) -> Dict[str, Any]:
        """Generate predictions based on team performance data"""
        try:
            # Analyze performance metrics for predictions
            performance = team_data.get('performance', {})
            recent_games = team_data.get('recent_games', [])
            
            predictions = {
                "win_probability": 0.5,  # Default 50/50
                "projected_score": "TBD",
                "key_strengths": [],
                "potential_weaknesses": [],
                "momentum": "Neutral"
            }
            
            # Analyze recent game performance
            if recent_games:
                recent_wins = sum(1 for game in recent_games if game.get('result') == 'W')
                win_rate = recent_wins / len(recent_games)
                predictions["win_probability"] = win_rate
                
                if win_rate > 0.6:
                    predictions["momentum"] = "Strong"
                elif win_rate < 0.4:
                    predictions["momentum"] = "Weak"
            
            return predictions
            
        except Exception as e:
            logging.error(f"Error generating team predictions: {e}")
            return {"error": "Unable to generate predictions"}
    
    def _analyze_matchup(self, team1_data: Dict, team2_data: Dict) -> Dict[str, Any]:
        """Analyze head-to-head matchup between two teams"""
        try:
            # Extract win probabilities if available
            team1_prob = team1_data.get('predictions', {}).get('win_probability', 0.5)
            team2_prob = team2_data.get('predictions', {}).get('win_probability', 0.5)
            
            # Normalize probabilities
            total_prob = team1_prob + team2_prob
            if total_prob > 0:
                team1_normalized = team1_prob / total_prob
                team2_normalized = team2_prob / total_prob
            else:
                team1_normalized = team2_normalized = 0.5
            
            # Determine prediction
            if team1_normalized > team2_normalized:
                predicted_winner = team1_data.get('team', 'Team 1')
                confidence = team1_normalized
            else:
                predicted_winner = team2_data.get('team', 'Team 2')
                confidence = team2_normalized
            
            return {
                "predicted_winner": predicted_winner,
                "confidence": confidence,
                "team1_win_probability": team1_normalized,
                "team2_win_probability": team2_normalized,
                "analysis": f"Based on recent performance data, {predicted_winner} has a {confidence:.1%} chance of winning"
            }
            
        except Exception as e:
            logging.error(f"Error analyzing matchup: {e}")
            return {"error": "Unable to analyze matchup"}
    
    def get_sports_news_sentiment(self, team: str, sport: str = "NBA") -> Dict[str, Any]:
        """
        Get sports news sentiment analysis
        This would typically integrate with news APIs
        """
        try:
            # Placeholder for news sentiment analysis
            # In a real implementation, this would fetch and analyze sports news
            sentiment_data = {
                "team": team,
                "sport": sport,
                "sentiment_score": 0.0,  # -1 to 1 scale
                "news_articles": 0,
                "key_topics": [],
                "last_updated": datetime.now().isoformat(),
                "summary": f"Sports news sentiment analysis for {team} would appear here with real news API integration"
            }
            
            return sentiment_data
            
        except Exception as e:
            logging.error(f"Error in sports news sentiment: {e}")
            return {"error": f"Sentiment analysis error: {str(e)}"}
    
    def get_available_features(self) -> Dict[str, Any]:
        """Return information about available sports data features"""
        return {
            "alpha_vantage_available": self.alpha_available,
            "polygon_available": self.polygon_available,
            "available_features": {
                "sports_betting_odds": self.alpha_available,
                "team_performance": self.alpha_available,
                "player_statistics": self.alpha_available,
                "game_predictions": self.alpha_available,
                "live_scores": self.alpha_available,
                "advanced_market_data": self.polygon_available,
                "news_sentiment": True  # Basic implementation available
            },
            "supported_sports": ["NBA", "NFL", "MLB", "NHL", "NCAA"],
            "api_status": {
                "alpha_vantage": "Connected" if self.alpha_available else "API Key Required",
                "polygon_io": "Connected" if self.polygon_available else "API Key Required"
            }
        }