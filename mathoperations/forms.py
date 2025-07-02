
from django import forms

class ArithmeticForm(forms.Form):

    num1=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    num2=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))


# <input type="number" class>
