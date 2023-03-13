from django import forms


class TodpCreateform(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.CharField()
