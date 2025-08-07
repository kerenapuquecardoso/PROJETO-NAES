from django.urls import path

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'managment/login.html', extra_context={"titulo": "Login","subTitulo": "Login permitido apenas para administradores",}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name = 'managment/form.html', extra_context={"titulo": "Alterar Senha","subTitulo": "Altere sua senha",}), name='password-change'),
]

