from django.contrib import admin
from django.urls import path
from ShopBackend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.get_product),
    path('api/v1/products/<int:id>/', views.get_detail),
    path('api/v1/products/reviews/', views.get_review),
    path('api/v1/products/tags/', views.get_tags),

    # path('/api/v1/products/tags/', views.tags_list_view),

]