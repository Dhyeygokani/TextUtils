
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
# def charcount(request):
#     return HttpResponse('Character counts<br><br><a href="http://127.0.0.1:8000/">Home</a> ')
#
# def spaceremove(request):
#     return HttpResponse('Space removal<br><br><a href="http://127.0.0.1:8000/">Home</a> ')
#
# def removepunc(request):
#     getpractice=request.GET.get('text', 'default')
#     print(getpractice)
#     return HttpResponse('Punc remove<br><br><a href="http://127.0.0.1:8000/">Home</a> ')
#
# def capitalfirst(request):
#     return HttpResponse('<h1>Capital first</h1><br><br><a href="http://127.0.0.1:8000/">Home</a> ')
#
# def newlineremove(request):
#     return HttpResponse('New line removal<br><br><a href="http://127.0.0.1:8000/">Home</a> ')

def analyze(request):
    #get the text
    getpractice = request.GET.get('text', 'default')

    #checkbox values
    removepunc = request.GET.get('removepunc', 'OFF')
    fullcaps = request.GET.get('fullcaps', 'OFF')
    newlineremoval = request.GET.get('newlineremover', 'OFF')
    spaceremover = request.GET.get('extraspaceremover', 'OFF')
    charcount = request.GET.get('charcount', 'OFF')

    #check which checkbox are on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in getpractice:
            if char not in punctuations:
                analyzed=analyzed+char
        param = {'purpose': 'remove punctuations','analyzed_text': analyzed}
        return render(request,'analyze.html',param)

    elif(fullcaps == 'on'):
        analyzed=""
        for char in getpractice:
            analyzed=analyzed+char.upper()
        param = {'purpose': 'Make all Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif(newlineremoval == 'on'):
        analyzed = ""
        for char in getpractice:
            if(char!="\n" and char!="\r"):
                analyzed = analyzed + char
        param = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif (spaceremover == 'on'):
        analyzed = ""
        # print('Hi')
        for index,char in enumerate(getpractice):
            if getpractice[index]==" " and getpractice[index+1]==" ":
                # print('d')
                pass
            else:
                analyzed=analyzed+char
        # print(analyzed)
        param = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif (charcount == 'on'):
        analyzed = ""
        k=0
        for char in getpractice:
            k=k+1
        analyzed=analyzed+"character count is "+str(k)
        param = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    else:
        return HttpResponse('Error')
    #remove render(request)