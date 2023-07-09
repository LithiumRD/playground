from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView


app_name = 'pages'
urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/<slug:slug>/',
         PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PageDeleteView.as_view(), name='delete'),

]
