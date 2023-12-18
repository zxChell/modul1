from django import forms


class AddMan(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(min_value=0)
