from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        if 'bot' in username:
            raise forms.ValidationError("Foydalanuvchi ismida bot so'zi mavjud")
        else:
            return username

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if 'gmail.com' in email:
            return email
        else:
            raise forms.ValidationError("Foydalanuvchi 'gmail.com' ni kiritmadi")

    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 == password2:
            return self.cleaned_data
        else:
            self.add_error('password2', "Parollar bir biriga teng emas ")

    def clean_password1(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        x = password1.isalpha()
        n = password1.isalnum()
        if len(password1) < 7:
            msg = "Parol kamida 7 ta belgidan iborat bo'lishi kerak"
            self.add_error('password2', msg)

        elif n or x == False:
            msg = "Parolda kamida 1 raqam bo'lishi kerak."
            self.add_error('password1', msg)

        elif password1 != password2:
            msg = "Parollar bir biriga teng emas. "
            self.add_error('password2', msg)

        return password1

    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error('first_name', "Ism familiya bir xil kiritildi")

        else:
            return self.cleaned_data

    def clean_password2(self, *args, **kwargs):
        password2 = self.cleaned_data.get('password2')

        if password2 == "qwerty12345" "admin12345":
            self.add_error('password1', "Bunday parol mavjud")

        else:
            return password2
