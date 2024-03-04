from django import forms

from news.models import News


class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem",
            "categories": "Categorias",
        }
        widgets = {
            "created_at": forms.DateInput(attrs={"type": "date"}),
            "categories": forms.CheckboxSelectMultiple(),
        }
