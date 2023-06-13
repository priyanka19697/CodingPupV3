from django.urls import path

from .views import *

app_name = "accounts"

urlpatterns = [
    path('accounts/',AccountListView.as_view()),
    path('accounts/<int:account_id>/', AccountDetailView.as_view()),
    path('users/', UserListView.as_view())
]


