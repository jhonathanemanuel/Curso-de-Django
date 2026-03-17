from django.shortcuts import render

def index(request):
    """""Página principal do learning_log"""
    return render(request, 'learning_logs/index.html')