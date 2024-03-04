from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from news.forms import CreateCategoryForm, CreateNewsForm
from .models import Category, News, User


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


def news_form(request):
    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            news = News.objects.create(
                title=cleaned_data["title"],
                content=cleaned_data["content"],
                author=cleaned_data["author"],
                created_at=cleaned_data["created_at"],
                image=cleaned_data["image"],
            )
            for category in cleaned_data["categories"]:
                news.categories.add(category)
            return redirect(reverse("home-page"))
    else:
        form = CreateNewsForm()
        users = User.objects.all()
        categories = Category.objects.all()
        return render(
            request,
            "news_form.html",
            {"form": form, "users": users, "categories": categories},
        )
