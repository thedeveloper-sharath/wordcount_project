from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request,'home.html', {'hithere':'This is me'})
def count(request):
    fulltext = request.GET['Full_text']
    wordlsit = fulltext.split()
    worddictionary = {}
    for i in wordlsit:
        if i in worddictionary:
            worddictionary[i] += 1
        else:
            worddictionary[i] = 1


    maxnumber = max(list(worddictionary.values()))
    maxword = list(worddictionary.keys())[list(worddictionary.values()).index(maxnumber)]
    wordslist = list(worddictionary.keys())
    countlist = list(worddictionary.values())

    finallist = list(zip(wordslist, countlist))

    hash = '-'

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlsit), 'worddictionary' : worddictionary, 'maxword' : maxword, 'maxnumber':maxnumber, 'finallist':finallist, 'hash':hash, 'wordsl':wordslist})
def about(request):
    return render(request, 'about.html')
