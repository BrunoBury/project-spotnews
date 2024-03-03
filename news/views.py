from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from news.forms import CreateCategoryForm
from .models import Category, News


def home_page(request):
    news_list = News.objects.all()
    return render(request, "home.html", {"news_list": news_list})


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    categories = news.categories.all()
    return render(
        request, "news_details.html", {"news": news, "categories": categories}
    )


def category_create(request):
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            Category.objects.create(name=name)
            return redirect(reverse("home-page"))
    else:
        form = CreateCategoryForm()
    return render(request, "categories_form.html", {"form": form})
