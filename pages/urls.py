from django.urls import path
from .views import PageTemplateView

page_patterns = [
    path('<int:page_id>/<slug:page_slug>', PageTemplateView.as_view(), name="page"),
]