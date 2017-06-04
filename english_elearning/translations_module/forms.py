from django.contrib.auth import (authenticate, get_user_model)
from django import forms

# If you don't do this you cannot use Bootstrap CSS


class ChangeEmail(forms.Form):
        email1 = forms.EmailField(label=u'inputEmail')
        email2 = forms.EmailField(label=u'inputEmail2')


class ChangePassword(forms.Form):
        password = forms.EmailField(label=u'inputpassword')
        password2 = forms.EmailField(label=u'inputpassword2')
from django import forms

class TranslationForm(form.ModelForm):
	suggestions = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
	pol_eng = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
	eng_pol = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
