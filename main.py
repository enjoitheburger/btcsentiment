from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from newspaper import Article

# TODO: Find a way to get a reliable number of sources to feed into the sentiment analyzer
url = "https://www.cnbc.com/2017/08/18/bitcoin-cash-surges-as-investors-bet-on-its-faster-processing-speeds.html"

article = Article(url)
article.download()
article.parse()
print("{:-<65}".format("This is the text I'm going to analyze"))
print(article.text)
print("{:-<65}".format("End of text"))

# --- examples -------
sentences = ["VADER is smart, handsome, and funny.",      # positive sentence example
            "VADER is not smart, handsome, nor funny.",   # negation sentence example
            "VADER is smart, handsome, and funny!",       # punctuation emphasis handled correctly (sentiment intensity adjusted)
            "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
            "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
            "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
            "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",# booster words & punctuation make this close to ceiling for score
            "The book was good.",                                     # positive sentence
            "The book was kind of good.",                 # qualified positive sentence is handled correctly (intensity adjusted)
            "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
            "At least it isn't a horrible book.",         # negated negative sentence with contraction
            "Make sure you :) or :D today!",              # emoticons handled
            "Today SUX!",                                 # negative slang with capitalization emphasis
            "Today only kinda sux! But I'll get by, lol"  # mixed sentiment example with slang and constrastive conjunction "but"
             ]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))

btc = analyzer.polarity_scores(article.text)
print("{:-<65} {}".format('Our custom BTC article', str(btc)))

# TODO: Aggregate sentiments and decide to buy/sell

