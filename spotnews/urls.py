"""
URL configuration for trybe_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from news.views import category_create, category_list, news_details, news_form

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("news.urls")),
    path("news/<int:id>/", news_details, name="news-details-page"),
    path("categories/", category_create, name="categories-form"),
    path("news/", news_form, name="news-form"),
    path("api/categories/", category_list, name="category-list"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
