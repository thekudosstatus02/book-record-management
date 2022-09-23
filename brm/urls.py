from django.urls import path
from .import views

urlpatterns = [
    path('view-books',views.viewBooks),
    path('login',views.userLogin),
    path('logout',views.userLogout),
    path('add',views.addBook),
    path('search-book',views.searchBook),
    path('search',views.search),
    path('edit-book',views.editBook),
    path('edit',views.edit),
    path('delete-book',views.deleteBook),
    path('new-book',views.newBook),
]
