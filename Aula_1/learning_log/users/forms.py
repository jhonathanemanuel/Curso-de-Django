# from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         labels = {'username':'Login', 'password':'Senha'}

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput)

    # Se eu precisar pegar dois campos ao mesmo tempo ou mais
    # Utilizo a função clean da seguinte maneira

    """
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        nome = cleaned_data.get('login')
        senha = cleaned_data.get('senha')
        
        validaçao
    """

    def clean_login(self):
        # nome = self.cleaned_data.get('login') # pode dar erro; está diferente do vídeo -> self.cleaned_data['login']
        nome = self.cleaned_data['login']

        if not nome.isalnum():
            raise ValidationError('O nome de usuário não pode ter caractere especial')

        return nome
