"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import *
from users.views import *
from events.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Core Views
    path('',home_view,name='home'),
    path('contact/',contact_view,name='contact'),
    # User views
    path('users/signup/',signup_view,name='signup'),
    path('users/login/',login_view,name='login'),
    path('users/profile/',profile_view,name='profile'),
    path('users/logout/',logout_view,name='logout'),
    # Events View
    path('events/',event_list,name='events-list'),
    path('events/create/',create_event,name='create-event'),
    path('events/<int:pk>/',event_detail,name='event-detail'),
    path('events/edit/<int:pk>/',edit_event,name='edit-event'),
    path('events/delete/<int:pk>/',delete_event,name='delete-event'),
    path('events/register/<int:pk>',register_event,name='register-event'),
    path('my-events/',my_events,name='my-events'),
    path('my-registrations/',my_registrations,name='my-registrations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
