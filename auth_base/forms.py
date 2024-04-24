from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Логин", "class":"input_field"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "class":"input_field"}))

    class Meta:
        model = User

    def save(self, commit=True):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username, '', password)
        if commit:
            user.save()
        return user