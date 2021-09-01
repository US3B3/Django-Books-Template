from django import forms
from . models import İletisim

class İletisimFormu(forms.ModelForm):

    ad_soyad = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'placeholder': 'Ad Soyad'
    }))
    numara = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'tel',
        'placeholder': 'Numara'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type' : 'email',
        'placeholder': 'e-mail'
    }))
    mesaj = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'placeholder': 'Mesaj',
        'class' : 'message-box'
    }))

    class Meta:
        model = İletisim
        fields = ['ad_soyad', 'numara', 'email', 'mesaj']



