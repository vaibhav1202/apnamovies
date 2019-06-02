from django.shortcuts import render, redirect
from college.models import Movie
import re
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.api import success
from django.contrib.auth.views import redirect_to_login
from django.db.models import Q
from rest_framework import viewsets
from college.serializers import MovieSerializer, UserSerializer
from django.contrib.auth.models import User
from college.permissions import MyUserPers, MyObjPer


def home(request):    
    return render(request, "index.html", {'actHome': 'active'})

def about(request):    
    return render(request, "about.html",  {'actAbt': 'active'})

def contact(request):
    return render(request, "contact.html",  {'actCnt': 'active'})

def notallow(request):
    return render(request, "notallow.html")


@method_decorator(login_required, name='dispatch')
class MovieList(ListView):
        model = Movie
        def get_queryset(self):
            si = self.request.GET.get('si')
            if si==None:
                si=''   
            return Movie.objects.filter(Q(name__icontains = si) | Q(star_cast__icontains = si)).order_by('-id')        
        def get_context_data(self, **kwargs):
            ctx = ListView.get_context_data(self, **kwargs)
            ctx['actMovie'] = 'active'
            return ctx        

@method_decorator(login_required, name='dispatch')
class MovieDetails(DetailView):
        model = Movie

def check_self_or_super(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                self.object = self.get_object()
                if  (self.object.user != request.user) and not request.user.is_superuser:
                    return redirect("/college/notallow/")
    
@method_decorator(login_required, name='dispatch')
class MovieCreate(CreateView):
        model = Movie
        fields = ("name", "star_cast", "description", "img", "ulink", "language", "genre")
        success_url ="/college/movie/"
        def form_valid(self, form):
            #https://www.youtube.com/watch?v=TcMBFSGVi1c
            #https://www.youtube.com/embed/TcMBFSGVi1c
                ulink = form.instance.ulink.replace(r"watch?v=", r"embed/")
                form.instance.ulink = ulink
                form.instance.user = self.request.user
                return super(MovieCreate, self).form_valid(form)        
        
        def get_context_data(self, **kwargs):
            ctx = CreateView.get_context_data(self, **kwargs)
            ctx['actCreate'] = 'active'
            return ctx        

@method_decorator(login_required, name='dispatch')
class MovieUpdate(UpdateView):        
        model = Movie
        fields = "__all__"
        success_url ="/college/"
        def form_valid(self, form):
                ulink = form.instance.ulink.replace(r"watch?v=", r"embed/")
                form.instance.ulink = ulink
                return super(MovieUpdate, self).form_valid(form)
        def dispatch(self, request, *args, **kwargs):
            ret = check_self_or_super(self, request, *args, **kwargs)
            if ret != None:
                return ret
            return UpdateView.dispatch(self, request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class MovieDelete(DeleteView):
        model = Movie
        success_url ="/college/"
        def dispatch(self, request, *args, **kwargs):
            ret = check_self_or_super(self, request, *args, **kwargs)
            if ret != None:
                return ret
            return DeleteView.dispatch(self, request, *args, **kwargs)

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer
    def get_queryset(self):
            si = self.request.GET.get('si')
            if si==None:
                si=''   
            return Movie.objects.filter(Q(name__icontains = si) | Q(star_cast__icontains = si)).order_by('-id')            
    permission_classes= (MyObjPer,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes= (MyUserPers,)

