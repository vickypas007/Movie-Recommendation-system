import string
from nltk.corpus import stopwords
import csv

# import panda

def cleaning():
    with open('Avengers.csv', 'r') as inFile:
        outFile = open('cleaning4.csv', 'w')
        # removingwords = open('review1.csv', 'r')
        # remove = removingwords.read()
        reader = csv.reader(inFile, delimiter=',')

        for row in reader:
            content0 = row[0]
            content1 = row[0] + " " + row[0]

            print( (
                " ".join([word for word in content1.lower().translate(str.maketrans('', '', string.punctuation)).split()
                          if len(word) >= 1 and word not in stopwords.words('english')])), file=outFile)


cleaning()
# print("".join(string.punctuation))

import sys

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        cleaning(sys.argv[1])
    else:
        print("Usage stmt")

# https: // machinelearningmastery.com / clean - text - machine - learning - python /