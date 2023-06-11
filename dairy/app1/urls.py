from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("category/<slug:val>",views.categoryview.as_view(),name='category'),
    path("product-detail/<int:pk>",views.productdetailsview.as_view(),name='product-detail'),
    #path("category/<title:val>",views.categorytitleview.as_view(),name="category-title")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
