from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


class GirisForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class KayitForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        usercheck = User.objects.filter(username=username)
        if usercheck:
            raise forms.ValidationError("Lütfen başka bir kullanıcı adı seçin.")

        if password != confirm:
            raise forms.ValidationError("Şifreler eşleşmiyor.")

        values = {
            'username': username,
            'password': password,
        }
        return values


class ProfilForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['career', 'education', 'interests']
