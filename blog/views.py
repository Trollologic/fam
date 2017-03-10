from django.shortcuts import render
from django.utils import timezone
from .models import Post, Feedback

def main_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    feedbacks = Feedback.objects.all()
    return render(request, 'blog/main_view.html', {'posts': posts, 'feedbacks': feedbacks})