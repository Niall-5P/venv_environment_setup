from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QyVszR5oY7UpMNEvQxhyxxy4mgF2WcH5tiwpS3xAjGZnn6fbKs8xx2FhW09BZrYqPq8op1z368Hj1SAh0y8CcKb00jkZwsDbD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)