from django.shortcuts import render

def home(r):
    return render(r, 'home.html',{"i":"Рады приветствовать Вас!"})

def reverse(request):
    user_text = request.GET['username']
    reversed_text=user_text[::-1] #задом на перед с шагом -1
    return render(request, 'reverse.html',{'word':reversed_text})