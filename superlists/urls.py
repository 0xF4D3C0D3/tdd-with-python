from django.conf.urls import include, url

from lists import views as lists_views

urlpatterns = [
    url(r'^$', lists_views.home_page, name='home'),
    url(r'^lists/', include('lists.urls')),
]
