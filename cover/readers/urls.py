from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import ReaderDetailView, ReadingCreateView, ReaderCreateView, ReaderListView, ReadingUpdateView, ReadingDetailView

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('reader/<int:pk>/',ReaderDetailView.as_view(),name='reader-detail'),
    path('reading/<int:pk>/',ReadingDetailView.as_view(),name='reading-detail'),
    path('login/',auth_views.LoginView.as_view(template_name='readers/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='readers/logout.html'),name='logout'),
    path('reading/create/',views.reading,name='reading-create'),
    path('reader/create',ReaderCreateView.as_view(),name='reader-create'),
    path('readers/',ReaderListView.as_view(),name='readers-list'),
    path('reading/<int:pk>/update',ReadingUpdateView.as_view(),name='reading-update'),
    path('list/',views.listview,name='list-view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)