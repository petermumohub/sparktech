from django import forms

class Searchform(forms.Form):
    query=forms.CharField(label=" ",max_length=100)