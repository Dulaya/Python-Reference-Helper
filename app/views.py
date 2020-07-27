from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from app.training_data import *
from app.mapping_data import *

def index(request):
    return render(request, 'index.html')

def user_input(request):
    output = {'output': request.POST['name'] } 
    return JsonResponse(output)

def bot_output(request):
    user_input = request.POST['name']
    user_input.lower() #Convert to lowercase 

    array_key_words = ['array','list','tuple']

    #if user_input in array_key_words : 
    answer = mapping_data[ training(user_input)[0] ][0] #output as array
        #answer = array()

    #else: answer = "<div>Please provide valid input</div>"


    output = {
        'input': user_input,
        'output': answer,
        'code': mapping_data[ training(user_input)[0] ][1],
        }

    return JsonResponse(output)

def array():
    
    output = "<div>Indexing a list using brackets: <br/> list = ['Fish', 'Donkey', 'Whale', 'Sheep', 'Shark'] <br/> print(list[1]) --> 'Donkey'</div>"

    return output

def training(user_input):

    class Review:
        def __init__(self, word, key):
            self.word = word
            self.key = key

    reviews = []
    for review in training_data:
        reviews.append(Review(review['word'],review['key']))

    #Split reviews (array) into test and training, in this case 100% for test and 0% for training
    training, test = train_test_split(reviews, test_size=1, random_state=42)

    #Array of all training words, e.g. ['delete element list', 'append element list', ...]
    train_x = [x.word for x in training]
    train_y = [x.key for x in training]

    test_x = [x.word for x in test]
    test_y = [x.key for x in test]

    #Bag of words; Map reviews as matrix.
    vectorizer = CountVectorizer()
    vectorizer.fit(train_x)
    train_x_vectors = vectorizer.transform(train_x)

    train_x[0]
    train_y[0]

    test_x_vectors = vectorizer.transform(test_x)

    #Support Vector Model
    clf_svm = svm.SVC(kernel='linear',probability=True)
    clf_svm.fit(train_x_vectors, train_y)

    return clf_svm.predict( vectorizer.transform([ user_input ]) )