from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    original_text = request.GET['usertext']
    reverse_text = original_text[::-1]
    num_of_words = len(original_text.split())

    return render(request, 'reverse.html', {'reversetext': reverse_text,
                                            'originaltext': original_text,
                                            'numwords': num_of_words})

