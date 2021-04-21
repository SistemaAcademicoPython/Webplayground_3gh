from django.urls import path
from . import views
from pages.views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete

urlpatterns = [
    #path('', views.pages, name='pages'),
    path('', PageListView.as_view(), name='pages'),
    #path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='pagecreate'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
]