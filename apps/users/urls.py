from django.urls import path

from apps.users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", user_views.register, name="Register"),
    path("need-verify/", user_views.need_verify, name="Need Verification"),
    path("verify/<uidb64>/<token>", user_views.activate_account, name="Verify"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="Login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="Logout",
    ),
    path("profile/<str:username>/", user_views.UserProfile.as_view(), name="Profile"),
    path("profile/update", user_views.update_profile, name="Update_Profile"),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="Password_Reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
