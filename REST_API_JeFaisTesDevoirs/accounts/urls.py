from django.conf.urls import url, include

from .views import SignUpView
from django.contrib.auth import views
from .forms import UserLoginForm, ResetPasswordForm, NewPasswordForm

urlpatterns = [
    url('login/', views.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name="login"),
    url('signup/', SignUpView.as_view(), name='signup'),
    url('password-reset/', views.PasswordResetView.as_view(template_name="registration/reset_password.html", form_class=ResetPasswordForm), name="password_reset"),
    url('password-reset/done/', views.PasswordResetDoneView.as_view(template_name="registration/reset_password_done.html"), name="password_reset_done"),
    url('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="registration/reset_password_confirm.html", form_class=NewPasswordForm), name="password_reset_confirm"),
    url('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name="registration/reset_password_complete.html"), name="password_reset_complete"),
]