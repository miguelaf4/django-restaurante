from django.shortcuts import render
from .models import Post, Category
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView


class BlogTemplateView(TemplateView):
    template_name = "blog/blog.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class BlogDetailView(DetailView):
    model = Post


def category(request, category_id):
    #category=get_object_or_404(Category,id=category_id)
    category = Category.objects.get(id=category_id)
    #posts = category.post_set.all()
    #posts= Post.objects.filter(categories=category)
    return render(request, "blog/category.html", {"category": category})