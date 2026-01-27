# ==============================================================================
# PROJECT: SENTIMENT-ANALYZER
# AUTHORS: AMEY THAKUR & MEGA SATISH
# GITHUB (AMEY): https://github.com/Amey-Thakur
# GITHUB (MEGA): https://github.com/msatmod
# REPOSITORY: https://github.com/Amey-Thakur/SENTIMENT-ANALYZER
# RELEASE DATE: January 26, 2026
# LICENSE: MIT License
# DESCRIPTION: A professionally architected Sentiment Analysis engine utilizing 
#              Linguistic Pattern Recognition via the TextBlob framework.
# ==============================================================================

import sys
import warnings
from textblob import TextBlob

# Suppression of non-critical runtime warnings to maintain a clean console log
warnings.filterwarnings("ignore")

class SentimentEngine:
    """
    A scholarly implementation of a Sentiment Analysis Engine.
    
    This class encapsulates the logic for performing probabilistic sentiment 
    classification on textual data, leveraging the semantic analysis 
    capabilities of the TextBlob library.
    """
    
    def __init__(self):
        """Initializes the SentimentEngine with default configurations."""
        pass

    def classify_sentiment(self, text: str) -> str:
        """
        Analyzes the provided text and classifies its underlying sentiment.
        
        The classification is determined by the polarity score:
            - Polarity < 0  : Negative Sentiment
            - Polarity == 0 : Neutral Sentiment
            - Polarity > 0  : Positive Sentiment

        Args:
            text (str): The input string to be analyzed for semantic affect.

        Returns:
            str: A formal classification string representing the sentiment outcome.
        """
        if not text.strip():
            return "Neutral (Empty Input)"

        # Perform semantic analysis using the TextBlob linguistic pipeline
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        # Apply deterministic classification boundaries
        if polarity < 0:
            return "Negative"
        elif polarity == 0:
            return "Neutral"
        else:
            return "Positive"

def main():
    """
    The primary execution entry point for the Sentiment-Analyzer system.
    Provides a Scholarly Terminal Interface for recursive text analysis.
    """
    engine = SentimentEngine()
    
    print("\n" + "="*80)
    print(" " * 25 + "SENTIMENT ANALYSIS ENGINE v1.0")
    print(" " * 20 + "Developed by Amey Thakur & Mega Satish")
    print("="*80 + "\n")
    
    print("[SYSTEM]: Initialization complete. Enter text for analysis.")
    print("[SYSTEM]: Type 'exit' or use Ctrl+C to terminate the session.\n")

    try:
        while True:
            # Procure user input through the standard input stream
            user_input = input("Analyze Sentiment: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("\n[SYSTEM]: Terminating session. Goodbye.")
                break
                
            if not user_input:
                continue

            # Execute classification through the logic engine
            sentiment_result = engine.classify_sentiment(user_input)
            
            # Display the statistical result with formal clarity
            print(f"| Outcome: {sentiment_result}")
            print("-" * 30)

    except KeyboardInterrupt:
        print("\n\n[SYSTEM]: Critical interrupt detected. Gracefully exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()