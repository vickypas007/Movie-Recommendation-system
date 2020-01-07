from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import matplotlib.pyplot as plt
totalPos=0;
totalNeg=0;
sumpos = 0
sumneg = 0
sumneu = 0


def sentiment_scores(sentence):

    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    negatives=sentiment_dict['neg'] * 100
    # sumneg+=negatives
    print("sentence was rated as ",negatives , "% Negative")
    neutral=sentiment_dict['neu'] * 100
    print("sentence was rated as ",neutral , "% Neutral")
    positves=sentiment_dict['pos'] * 100
    print("sentence was rated as ",positves , "% Positive")

    print("Sentence Overall Rated As", end=" ")


    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
        #count +=sentiment_dict['neg'] * 100

    elif sentiment_dict['compound'] <= - 0.05:
       # print(sentiment_dict['compound'])
        print("Negative")


    else:
        print("Neutral")
    return negatives,neutral,positves
    # totalPos += int(sentiment_dict['pos'] *100)
    # print("Total Positive =" + str(totalPos))
    # Driver code
    #
    # totalNeg += int(sentiment_dict['neg'] *100)
    # print("Total nagetive=" +str(totalNeg))



if __name__ == "__main__":
    print("\n1st statement :")
#     sentence = "Geeks For Geeks is the best portal for \
#     the computer science engineering students."
#
#     # function calling
#
# neg,neu,pos=sentiment_scores(sentence)
# sumpos +=pos
# sumneg +=neg
# sumneu +=neu
#
# print("\n2nd Statement :")
# sentence = "study is going on as usual"
# neg,neu,pos=sentiment_scores(sentence)
# sumpos +=pos
# sumneg +=neg
# sumneu +=neu
#
# print("\n3rd Statement :")
# sentence = "I am vey sad today."


i=0
with open('cleaning4.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        neg, neu, pos = sentiment_scores(row[0])
        sumpos += pos
        sumneg += neg
        sumneu += neu
        i+=1
       # print(row)
        # sentence = row[0]
        # sentiment_analyzer_scores(sentence)
#
tp=sumpos/i
tneg=sumneg/i
tneu=sumneu/i
print()
print("Sum of Pos" ,tp," ")
print("Sum of Neg",tneg," ")
print("Sum of neu", tneu," ")

# calculate the rating of the movie

rating = ((tp)/( tp+tneg))*10
print("raing ",rating)

if rating<2.0 and rating >=0:
    print("1 star")

if rating>=2 and rating<3:
    print(" 2 star")

if rating>=3 and rating<4:
    print("2.5 star")

if rating>=4 and rating<5 :
    print("3 star")

if rating>=5 and rating<6 :
    print("3.5 star")

if rating>=6 and rating<8:
    print("4 star")

if rating>=8 and rating<9:
    print("4.5 star")

if rating>=9 and rating <=10:
    print("5 star")

print()
left = [1, 2, 3]

# heights of bars
height = [tp, tneg, tneu]

# labels for bars
tick_label = ['Positive', 'Nagetive', 'Neutral']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['green', 'red','yellow'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('Movies Review bar chart!')

# function to show the plot
plt.show()