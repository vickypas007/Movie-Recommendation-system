from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
import csv


def sentiment_analyzer_scores(sentence, pos_correct=0, pos_count=0, neg_correct=0, neg_count=0):
    score = analyser.polarity_scores(sentence)
    if score['compound']> 0:
        pos_correct +=  1
    pos_count +=1
    
    vg =analyser.polarity_scores(sentence)
    if vg['compound'] <= 0:
            neg_correct += 1
    neg_count +=1


    print(" {:-<5}\n {}\n".format('output', str(score)))
    print("Positive accuracy = {}% via {} samples".format(pos_correct / pos_count * 100.0, pos_count))
    print("Negative accuracy = {}% via {} samples".format(neg_correct / neg_count * 100.0, neg_count))

if __name__ == "__main__":
    with open('review.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            print(row)
            sentence = row[0]
        sentiment_analyzer_scores(sentence)

total_positive =0
total_count=0;
pos_correct=0
pos_count=0
neg_correct=0
neg_count=0

# total_positive += pos_correct
# total_count += pos_count
# print(total_positive)