from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def createPost(request):
	form = PostForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'adminSide/create_post.html', context)

def updatePost(request, pk):

	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'adminSide/create_post.html', context)