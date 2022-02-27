from django.http import HttpResponse
from django.shortcuts import render

#Backend:
def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    text1=request.POST.get('text', 'default')

    # Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercount = request.POST.get('charactercount','off')
    changefont = request.POST.get('changefont', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in text1:
            if char not in punctuations:
                analyzed=analyzed+char

        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        text1 = analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in text1:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        text1 = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in text1:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
            print("pre", analyzed)
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        text1 = analyzed

    if(spaceremover == "on"):
        analyzed = ""
        for char in text1:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        text1 = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(text1):
            if not(text1[index] == " " and text1[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        text1 = analyzed

    if (changefont=="on"):
        analyzed=text1
        params={'purpose':'Change Font','analyzed_text':analyzed,'a':'24'}
        text1=analyzed


    if(charactercount == "on"):
        analyzed=f"The length of your string is {len(text1)}"
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}


    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and extraspaceremover != "on" and charactercount != "on" and changefont != "on"):
        return HttpResponse("Please Select Atleast One Operation And Try Again")

    return render(request, 'analyze.html', params)
