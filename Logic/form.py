from django import forms

class Entry(forms.Form):
    getEmail = forms.EmailField(label = "email", max_length = 100)
    getDate = forms.DateField(label = "Введите дату")
    getLine = forms.CharField(label = "Введите строку", max_length = 100)
    getNum = forms.IntegerField(label = "Введите число")
