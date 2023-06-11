from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import product


def home(request):
    # return HttpResponse("hi, this is priyannka")
    return render(request, 'home.html')


# there are 2 wayto write views  by functions and by class
# now using class  to write view code for catogery

class categoryview(View):
    def get(self, request, val):
        xyz = product.objects.filter(category=val)
        title = product.objects.filter(category=val).values('title')
        return render(request, 'category.html', locals())  # we have only display data sp that get method used
#
# class categorytitleview(View):
#     def get(self,request,val):
#         product1=product.objects.filter(title=val)
#         title=product.objects.filter(category=product1[0].category).values('title')
#         print(title)
#         return render(request,"category.html",locals())

class productdetailsview(View):
    def get(self, request, pk):
        pqr=product.objects.get(pk=pk)
        return render(request, 'productdetails.html', locals())
