from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from chatapplication.views import frontpage,signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='chatapplication/login.html'), name='login'),
    path('room/',include('room.urls'))

]