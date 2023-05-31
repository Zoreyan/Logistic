from django.urls import path
from .views import *
from django.views import generic
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Create
    path('driver-create/', driver_create, name='driver-create'),
    path('truck-create/', truck_create, name='truck-create'),
    # Read
    path('driver-dashboard/<int:pk>/', driver_dashboard, name='driver-dashboard'),
    # Update
    path('driver-update/<int:pk>/', driver_update, name='driver-update'),
    path('truck-update/<int:pk>/', truck_update, name='truck-update'),
    # Delete
    path('order-delete/<int:pk>/', order_delete, name='order-delete'),
    path('driver-delete/<int:pk>/', driver_delete, name='driver-delete'),
    # Account
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', SignInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # Views
    path('', TemplateView.as_view(template_name='app/index.html'), name='home'),
    path('order/', OrderView.as_view(), name='order'),
    path('distribution/', TemplateView.as_view(template_name='app/distribution.html'), name='distribution'),
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
    path('query-success/', TemplateView.as_view(template_name='app/query_success.html'), name='query-success'),
]