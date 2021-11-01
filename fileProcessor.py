import os
import sys
from nltk.tokenize import sent_tokenize

class fileProcessor:
    def __init__(self, filepath):
        self.filepath = filepath;
    def charCounter(self):
        with open(self.filepath) as file:
            data = file.read();
            return len(data);
    def wordCounter(self):
        with open(self.filepath) as file:
            data = file.read();
            words = data.split();
            return len(words);
    def sentenceCounter(self):
        with open(self.filepath) as file:
            data = file.read();
            sentencesArr = sent_tokenize(data);
            return len(sentencesArr);

    
x = fileProcessor("test.txt");

print("Number of characters:", x.charCounter());
print("Number of words:", x.wordCounter());
print("Number of sentences:", x.sentenceCounter());
