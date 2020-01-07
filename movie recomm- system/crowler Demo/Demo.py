from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
import csv



def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print(" {:-<5}\n {}\n".format('output', str(score)))


with open('review.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
        sentence = row[0]
        sentiment_analyzer_scores(sentence)