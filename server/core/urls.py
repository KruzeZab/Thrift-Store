from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "api/",
        include(
            [
                # path("", include(".urls")),
                path("autho/", include("autho.urls")),
            ]
        ),
    ),
]
