from django import forms
class studentforms(forms.Form):
    name=forms.CharField()
    age=forms.IntergerField()
