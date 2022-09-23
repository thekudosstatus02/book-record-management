from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Company & Role',max_length=100)
    author=forms.CharField(label='Job Type',max_length=100)
    price=forms.CharField(label='Link',max_length=100)
    publisher=forms.CharField(label='Last Date of registration',max_length=100)

class SearchBook(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
