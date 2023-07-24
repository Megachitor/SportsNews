from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('teams/', team, name='team'),
    path('news', news, name='news'),
    path('contact/', contact, name='contact'),
    path('post/<int:id>', single, name='single'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('command/<int:id>', command, name='command'),
    # path('player/<int:id>', player, name='player'),
    path('article/<int:id>', article, name='article'),
    
    
    # path('contact/', contact, name='contact'),

]
