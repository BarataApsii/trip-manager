from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from customers.models import Customer
from bookings.models import Booking
from payments.models import Payment


@login_required
def dashboard(request):
    total_customers = Customer.objects.count()
    total_bookings = Booking.objects.count()
    recent_bookings = Booking.objects.select_related('customer', 'payment')[:5]
    total_revenue = sum(
        p.total for p in Payment.objects.all()
    )
    return render(request, 'core/dashboard.html', {
        'total_customers': total_customers,
        'total_bookings': total_bookings,
        'recent_bookings': recent_bookings,
        'total_revenue': total_revenue,
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url:
                return redirect(next_url)
            return redirect('core:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('core:login')


@login_required
def admin_panel(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access the admin panel.')
        return redirect('core:dashboard')

    users = User.objects.all().order_by('-date_joined')
    total_customers = Customer.objects.count()
    total_bookings = Booking.objects.count()
    total_users = User.objects.count()

    return render(request, 'core/admin_panel.html', {
        'users': users,
        'total_customers': total_customers,
        'total_bookings': total_bookings,
        'total_users': total_users,
    })


@login_required
def admin_user_create(request):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission.')
        return redirect('core:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email', '')
        password = request.POST.get('password')
        is_staff = request.POST.get('is_staff') == 'on'

        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username "{username}" already exists.')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.is_staff = is_staff
            user.save()
            messages.success(request, f'User "{username}" created successfully.')
            return redirect('core:admin_panel')

    return render(request, 'core/admin_user_form.html', {
        'title': 'Add User',
    })


@login_required
def admin_user_delete(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission.')
        return redirect('core:dashboard')

    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        if user == request.user:
            messages.error(request, 'You cannot delete your own account.')
        else:
            user.delete()
            messages.success(request, 'User deleted successfully.')
        return redirect('core:admin_panel')

    return render(request, 'core/admin_user_confirm_delete.html', {
        'user_obj': user,
    })
