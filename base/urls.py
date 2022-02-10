from django.urls import path
from . import views
from .views import VideoListView

urlpatterns = [
    path('', views.home, name="Home"),
    path('about/', views.about, name="About"),
    path('speakers/', views.speakers, name="Speakers"),
    path('watchus/', VideoListView.as_view(), name="WatchUs"),
    path('events/', views.events, name="Events"),
    path('contact/', views.contact, name="Contact"),
    path('subscribed/', views.subscribed, name="Subscribed"),
    path('subscribe_email/', views.subscribe_email, name="Subscirbe_Email"),
    path('email_test/', views.test_email, name="TestingEmail"),
    path('unsubscribe/', views.unsubscribe, name="Unsubscribed"),
    path('complete-subscribe/', views.complete_subscribe, name="Subscribed"),
    path('verify/<int:pk>/<uuid:token>',
    views.activate_account, name='Verified'),

    # path('register/', views.register, name="Register"),
]