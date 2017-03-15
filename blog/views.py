from django.shortcuts import render
from django.utils import timezone
from .models import Post, Feedback
from django.core import serializers
from django.views.generic import TemplateView


import json

def main_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    feedbacks = Feedback.objects.all()
    data = serializers.serialize('json', list(feedbacks), fields=('text','id', 'created_date', 'x_position', 'y_position', 'active'))

    #return render(request, "blog/main_view.html", {'posts': posts, 'js_feedbacks': data})
    return render(request, 'blog/main_view.html', {'posts': posts, 'feedbacks': feedbacks, 'js_feedbacks': data})


class PostExample(TemplateView):
    template_name = 'blog/main_view.html'
    def post(self, request):
        #body_unicode = request.body.decode('utf-8')
        #body = json.loads(body_unicode)
        #print 'Raw Data: "%s"' % request.POST['text']
        Feedback(text=request.POST['text'], x_position= request.POST['x_position'], y_position= request.POST['y_position'], active=True).save()
        
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        feedbacks = Feedback.objects.all()
        print feedbacks
        data = serializers.serialize('json', list(feedbacks), fields=('text','id', 'created_date', 'x_position', 'y_position', 'active'))

        #return render(request, "blog/main_view.html", {'posts': posts, 'js_feedbacks': data})
        return render(request, 'blog/main_view.html', {'posts': posts, 'feedbacks': feedbacks, 'js_feedbacks': data})