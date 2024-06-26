from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    word_num = 0

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
            word_num += 1
        else:
            word_dictionary[word] = 1
            word_num += 1

    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'word_num': word_num})