from django.shortcuts import render
from django.views.generic import View
from mathoperations.forms import ArithmeticForm,CalorieForm

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
        

class SubtractionView(View):

    template_name="subtraction.html"

    form_class=ArithmeticForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            validated_data= form_instance.cleaned_data

            n1=validated_data.get("num1")

            n2=validated_data.get("num2")

            result=n1-n2

            return render(request,self.template_name,{"form":form_instance,"output":result})
        else:

            return render(request,self.template_name,{"form":form_instance})
        
    
    # url:localhost:8000/index/
    # method:GET
    # repose:index.html



class IndexView(View):

    template_name="index.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

# DIET Lens

class CalorieView(View):

    template_name="calorie.html"

    form_class=CalorieForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            validated_data=form_instance.cleaned_data

            print(validated_data)#{'height': 170.0, 'weight': 70.0, 'gender': 'male', 'age': 24}

            # logic
            height=validated_data.get("height")

            weight=validated_data.get("weight")

            gender=validated_data.get("gender")

            age=validated_data.get("age")

            if gender=="male":

                bmr=10 * weight+ 6.25 * height - 5 * age + 5 
            else:
                bmr=10 * weight + 6.25 * height - 5 * age- 161 

            calorie=bmr*1.2

            print(calorie)          
            

            return render(request,self.template_name,{"form":form_instance,"result":calorie})


    








    






