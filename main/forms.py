from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # Указывайте здесь фактические поля вашей модели
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomLoginForm:
    pass


class CustomLoginView(auth_views.LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html' # Путь к шаблону
