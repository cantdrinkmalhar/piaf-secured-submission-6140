from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.urls import include, path


urlpatterns = [
    path("", include("authentification.urls")),
    path("", RedirectView.as_view(url="/app"), name="index"),
    path("app/", include("piaf.urls", namespace="app")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("v1/", include("api.urls")),
    path("api/", include ("api.urls")),


    path(
        "password_reset/",
         auth_views.PasswordResetView.as_view(
             template_name="password_reset_form.html", 
             email_template_name="password_reset_email.html",
             subject_template_name="password_reset_subject.txt",
         ),
         name="password_reset",
    ),
    path(
        "password_reset/done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset_done.html",
         ),
         name="password_reset_done",
     ),
     path(
         "reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="password_reset_confirm.html",
         ),
         name="password_reset_confirm",
     ),
     path(
         "reset/done/",
          auth_views.PasswordResetCompleteView.as_view(
              template_name="password_reset_complete.html",
         ),
         name="password_reset_complete",
     ),
]

if "cloud_browser" in settings.INSTALLED_APPS:
    urlpatterns.append(path("cloud-storage/", include("cloud_browser.urls")))
