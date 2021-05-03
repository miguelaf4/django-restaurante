from django.urls import path
from . import views 
from .views import BlogTemplateView, BlogDetailView


blog_patterns = [
    path('', BlogTemplateView.as_view(), name="blog"),
    path('<int:pk>/', BlogDetailView.as_view(), name="post"),
    path('category/<int:category_id>', views.category, name="category"),
]
