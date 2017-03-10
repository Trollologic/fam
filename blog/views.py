from django.shortcuts import render

def main_view(request):
    return render(request, 'blog/main_view.html', {})