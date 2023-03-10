from django.shortcuts import render
from app.forms import *
from django.http import HttpResponseRedirect
from app.models import *
from django.views.generic import *


# Create your views here.

class UserAddShow(TemplateView):
    template_name = 'app/app_and_show.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = StudentForm() 
        stu = User.objects.all() 
        context = {'form':form,'stu':stu}
        return context
    
    def post(self,request):
        if request.method=='POST':
            form = StudentForm(request.POST)
            
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                password=form.cleaned_data['password']
                reg = User(name=name,password=password,email=email)
                reg.save()
            return HttpResponseRedirect('/')
        
        





class UserDelete(RedirectView):
    url='/'
    
    def get_redirect_url(self,*args,**kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)

class UserUpdateView(View):
    
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentForm(instance=pi)
        return render(request,'app/updatestudent.html',{'form':fm})
    def post(self,request,id):
        if request.method=='POST':
            pi = User.objects.get(pk=id)
            fm = StudentForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
        return HttpResponseRedirect('/')        
                

                 
        