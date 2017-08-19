from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='05YgxbyHyGZmlQ',
                     client_secret='OI3RqQKPfjb1Y0lgaJQlCjhtQ1c',
                     user_agent='my user agent')

# Top submissions in /r/bitcoin
submissions = reddit.subreddit('bitcoin').hot(limit=15)


# Average the sentiment scores to get a -1 to 1 score
def average_scores(sentiments, total_count):
    for key in sentiments:
        sentiments[key] = sentiments[key]/total_count

analyzer = SentimentIntensityAnalyzer()
overallSentiment = {'positive': 0, 'negative': 0, 'neutral': 0, 'compound': 0}
totalSubmissions = 0
for submission in submissions:
    if submission.stickied:
        continue
    totalSubmissions += 1
    submissionSentiment = {'positive': 0, 'negative': 0, 'neutral': 0, 'compound': 0}
    totalComments = 0
    for comment in submission.comments.list():
        # some comments are a pagination object MoreComments, maybe follow these threads in the future
        if hasattr(comment, 'body'):
            vs = analyzer.polarity_scores(comment.body)
            submissionSentiment['positive'] += vs['pos']
            submissionSentiment['negative'] += vs['neg']
            submissionSentiment['neutral']  += vs['neu']
            submissionSentiment['compound'] += vs['compound']
            totalComments += 1

    average_scores(submissionSentiment, totalComments)

    print("{:-<65} {}".format(submission.title, str(submissionSentiment)))

    overallSentiment['positive'] += submissionSentiment['positive']
    overallSentiment['negative'] += submissionSentiment['negative']
    overallSentiment['neutral']  += submissionSentiment['neutral']
    overallSentiment['compound'] += submissionSentiment['compound']


# Average the score to get a -1 to 1 score
average_scores(overallSentiment, totalSubmissions)
print("{:-<65} {}".format('Overall Sentiment from /r/bitcoin', str(overallSentiment)))
