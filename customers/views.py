from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    query = request.GET.get('q', '')
    if query:
        customers = customers.filter(
            first_name__icontains=query
        ) | customers.filter(
            last_name__icontains=query
        ) | customers.filter(
            email__icontains=query
        )
    return render(request, 'customers/customer_list.html', {
        'customers': customers,
        'query': query,
    })


@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customer_detail.html', {
        'customer': customer,
    })


@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Customer "{customer.full_name}" created successfully.')
            return redirect('customers:customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {
        'form': form,
        'title': 'Add Customer',
    })


@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f'Customer "{customer.full_name}" updated successfully.')
            return redirect('customers:customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {
        'form': form,
        'title': 'Edit Customer',
        'customer': customer,
    })


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully.')
        return redirect('customers:customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {
        'customer': customer,
    })
