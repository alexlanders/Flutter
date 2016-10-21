from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from flutz.models import Member, Post
from flutz.forms import PostForm
from django.views.decorators.csrf import csrf_exempt


def home(request):
    flutts = Post.objects.order_by('-id')
    context = {'flutts': flutts}
    return render(request, 'index.html', context)


@csrf_exempt
def post_flut(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'index.html', context)

def post_ack(request):
    pass


def search(request):
    pass