
from django import forms

class ArithmeticForm(forms.Form):

    num1=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    num2=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))


# <input type="number" class>

# Sub,muli,div

# BMI

# EmiForm: loan_amount,interest_rate,tenure


class EmiForm(forms.Form):

    loan_amount=forms.FloatField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    interest_rate=forms.FloatField()

    tenure=forms.IntegerField()

# BMR 
# MODELS


# Height,Weight,gender,age,activity_level


class CalorieForm(forms.Form):

    height=forms.FloatField()

    weight=forms.FloatField()

    GENDER_CHOICES=(
        ("male","male"),
        ("female","female")
    )

    gender=forms.ChoiceField(choices=GENDER_CHOICES)

    age=forms.IntegerField()



