from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Order
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def index(request):
    orders = Order.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/index.html', {'orders': orders})


def order_list(request):
    orders = Order.objects.filter(author=request.user, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'app/order_detail.html', {'order': order})

@login_required
def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.published_date = timezone.now()
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'app/order_edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/') 
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.published_date = timezone.now()
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'app/order_edit.html', {'form': form})