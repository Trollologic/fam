from django.shortcuts import render
from django.utils import timezone
from .models import Post, Feedback
from django.core import serializers

def main_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    feedbacks = Feedback.objects.all()
    data = serializers.serialize('json', list(feedbacks), fields=('text','id', 'created_date', 'x_position', 'y_position', 'active'))

    #return render(request, "blog/main_view.html", {'posts': posts, 'js_feedbacks': data})
    return render(request, 'blog/main_view.html', {'posts': posts, 'feedbacks': feedbacks, 'js_feedbacks': data})