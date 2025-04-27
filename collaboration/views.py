from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from .forms import CollaborationRequestForm
from .models import CollaborationRequest


def collaborate(request):
    """
    Display & process the public CollaborationRequestForm.
    """
    if request.method == 'POST':
        form = CollaborationRequestForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            send_mail(
                subject=f"New collab enquiry from {inquiry.full_name}",
                message=inquiry.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
            messages.success(request, "Thank you! We’ll be in touch shortly.")
            return redirect('collaborate:collaborate_thanks')
    else:
        form = CollaborationRequestForm()

    return render(request, 'collaboration/collaborate.html', {'form': form})


def thanks(request):
    """
    Simple thank-you page after successful submit.
    """
    return render(request, 'collaboration/thanks.html')


class StaffOnlyMixin(UserPassesTestMixin):
    """
    Mixin to restrict access to staff users.
    """
    def test_func(self):
        return self.request.user.is_staff


class CollabListView(StaffOnlyMixin, ListView):
    """
    Staff-only list of all collaboration requests.
    """
    model               = CollaborationRequest
    template_name       = 'collaboration/manage.html'
    context_object_name = 'requests'


class CollabUpdateView(StaffOnlyMixin, UpdateView):
    """
    Staff-only edit form for CollaborationRequest,
    including full_name, email, brand_name, website & message.
    """
    model         = CollaborationRequest
    fields        = ['full_name', 'email', 'brand_name', 'website', 'message']
    template_name = 'collaboration/form.html'


class CollabDeleteView(StaffOnlyMixin, DeleteView):
    """
    Staff-only delete confirmation for CollaborationRequest.
    """
    model         = CollaborationRequest
    template_name = 'collaboration/confirm_delete.html'
    success_url   = reverse_lazy('collaborate:manage')
