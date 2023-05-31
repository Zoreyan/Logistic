from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib.auth import login
from .models import *



# Create
@login_required(login_url='login')
def driver_create(request):
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('driver-dashboard', pk=request.user.id)
    context = {
        'form': form
    }
    return render(request, 'app/driver_settings.html', context)

@login_required(login_url='login')
def truck_create(request):
    form = TruckForm()
    if request.method == 'POST':
        form = TruckForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.driver = request.user
            form.save()
            return redirect('driver-dashboard', pk=request.user.id)
    context = {
        'form': form
    }
    return render(request, 'app/truck_settings.html', context)

# Read
@login_required(login_url='login')
def driver_dashboard(request, pk):

    context = {
        'driver_data': Driver.objects.get(user_id=pk) if Driver.objects.filter(user_id=pk).exists() else '',
        'truck_data': Truck.objects.get(driver_id=pk) if Truck.objects.filter(driver_id=pk).exists() else '',
        'order_data': Shipment.objects.filter(assigned_truck__driver=request.user),
    }
    return render(request, 'app/driver_dashboard.html', context)

# Update
@login_required(login_url='login')
def driver_update(request, pk):
    driver = Driver.objects.get(user_id=pk)
    form = DriverForm(instance=driver)

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver-dashboard', pk=request.user.id)
        
    context = {
        'form': form
    }
    return render(request, 'app/driver_settings.html', context)

@login_required(login_url='login')
def truck_update(request, pk):
    truck = Truck.objects.get(driver_id=pk)
    form = TruckForm(instance=truck)

    if request.method == 'POST':
        form = TruckForm(request.POST, request.FILES, instance=truck)
        if form.is_valid():
            form.save()
            return redirect('driver-dashboard', pk=request.user.id)
        
    context = {
        'form': form
    }
    return render(request, 'app/truck_settings.html', context)

# Delete
@login_required(login_url='login')
def order_delete(request, pk):
    order = Shipment.objects.get(id=pk)
    if request.method == 'POST':
        order = Shipment.objects.get(id=pk)
        order.delete()
        return redirect('order')
    return render(request, 'app/order_delete.html', {'order': order})

def driver_delete(request, pk):
    driver = Driver.objects.get(id=pk)
    if request.method == 'POST':
        driver = User.objects.get(id=pk)
        driver.delete()
        return redirect('admin-dashboard')
    return render(request, 'app/driver_delete.html', {'driver':driver})

# Account
class SignUpView(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'
    redirect_authenticated_user = True

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(SignUpView, self).get(*args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            return redirect('distribution')
        return super(SignUpView, self).form_valid(form)


class SignInView(LoginView):
    authentication_form = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'app/login.html'
    redirect_authenticated_user = True
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(SignInView, self).get(*args, **kwargs)

# Views
@login_required(login_url='login')
def admin_dashboard(request):
    context = {
        'driver_data': Driver.objects.all(),
        'truck_data': Truck.objects.all(),
        'order_data': Shipment.objects.all()
    }
    return render(request, 'app/admin_panel.html', context)

class OrderView(TemplateView, LoginRequiredMixin):
    template_name = 'app/order_panel.html'
    order_form = OrderForm()

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.instance.user = request.user
            order_form.save()
            return redirect('query-success')
        return redirect('distribution')

    def get(self, request, *args, **kwargs):
        context = {
            'order_form': self.order_form,
            'shipments': Shipment.objects.filter(user=request.user)
        }
        return render(request, self.template_name, context)
