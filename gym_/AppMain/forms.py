from django import forms
from .models import Member

class PostForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"