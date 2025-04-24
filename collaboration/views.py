# collaboration/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail          # optional
from django.conf import settings

from .forms import CollaborationRequestForm


def collaborate(request):
    """Display & process CollaborationRequestForm."""
    if request.method == 'POST':
        form = CollaborationRequestForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            # OPTIONAL e-mail notification  ----------------------------
            send_mail(
                subject=f"New collab enquiry from {inquiry.full_name}",
                message=inquiry.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            # ----------------------------------------------------------
            messages.success(request, "Thank you! We’ll be in touch shortly.")
            return redirect('collaborate_thanks')
    else:
        form = CollaborationRequestForm()

    return render(request, 'collaboration/collaborate.html', {'form': form})


def thanks(request):
    """Simple thank-you page after successful submit."""
    return render(request, 'collaboration/thanks.html')
