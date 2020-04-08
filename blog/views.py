from django.shortcuts import render,get_object_or_404
from .models import Post
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.



def home(request):
    context = {
        'posts':Post.objects.all(),
    }
    return render(request,'blog/home.html',context)


# CBV for home page
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app_name>/<model>_<viewtype>.html
    context_object_name = 'posts'  # default context is 'object'
    ordering = ['-date_posted']  # newest to oldest
    # pagination
    paginate_by = 3
    
    
class UserPostListView(ListView):
    ''' if user clicks on on author it displays the all post by that author with pagination '''
    model = Post
    template_name = 'blog/user_posts.html'  
    context_object_name = 'posts' 
    # ordering = ['-date_posted'] -> mention in the below function as this can be overriden 
    # pagination
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):   # with cbv conventions for template and context as above mentioned
    model = Post
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']    
    
    # for setting the current logged author
    def form_valid(self, form):
        # if self.request.user.is_authenticated():
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']    
    
    # for setting the current logged author
    def form_valid(self, form):
        # if self.request.user.is_authenticated():
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # function for updation of post  that is person who has posted can only update that post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):   
    model = Post
    success_url = '/'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request,'blog/about.html',{'title':'About'})