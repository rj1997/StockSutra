from django import forms
from django.contrib.auth.models import User
from uni.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('contact', 'AAPLvalue','CSCOvalue','CATvalue','BAvalue','CVXvalue',)



class PortfolioForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('AAPLvalue','CSCOvalue','CATvalue','BAvalue','CVXvalue',)

