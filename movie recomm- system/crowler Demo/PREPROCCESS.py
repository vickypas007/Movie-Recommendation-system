import nltk.classify.util
import matplotlib.pyplot as plt
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import csv

def word_feats(words):
    return dict([(word, True) for word in words])


positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(', 'worst','no']
neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set)

# Predict

totalneg=0
totalpos=0
neg = 0
pos = 0
with open('cleaning.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
        sentence = row[0]
        #sentence = sentence.lower()
        words = sentence.split(" ")
        for word in words:
            classResult = classifier.classify(word_feats(word))
            if classResult == 'neg':
                neg = neg + 1
            if classResult == 'pos':
                pos = pos + 1

        print('Positive: ' + str(float(pos) / len(words)))
        print('Negative: ' + str(float(neg) / len(words)))
        totalneg=int(totalneg)+ int(float(neg)/ len(words))
        totalpos=int(totalpos)+ int(float(pos)/ len(words))

print()
tp =totalpos/100
tn=totalneg/100
print("Total positive ="+str(tp))
print("Total nagetive ="+ str(tn))

print()
left = [1, 2]

# heights of bars
height = [tp, tn]

# labels for bars
tick_label = ['Positive', 'Nagetive']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['green', 'red'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()
# print("Total  ="+str((totalpos)/ (totalneg)))