from django import forms
from .models import Contacto, Plan
from .models import Usuario

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

class UsuarioRegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña")
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'password', 'password2', 'tipo_usuario']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data
