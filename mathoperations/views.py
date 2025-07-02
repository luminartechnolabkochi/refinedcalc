from django.shortcuts import render
from django.views.generic import View
from mathoperations.forms import ArithmeticForm

# Create your views here.


# url:localhost:8000/add/
# method:
    #GET
    #post

class AdditionView(View):

    def get(self,request,*args,**kwrags):

        form_instance=ArithmeticForm()

        return render(request,"additon.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=ArithmeticForm(form_data)

        if form_instance.is_valid():

            validated_data=form_instance.cleaned_data

            n1=validated_data.get("num1")

            n2=validated_data.get("num2")

            result=n1+n2

            return render(request,"additon.html",{"form":form_instance,"output":result})
        else:
            return render(request,"additon.html",{"form":form_instance})
        
