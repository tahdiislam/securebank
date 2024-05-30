from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login
from django.views.generic import FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from transactions.views import send_transaction_email
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# #  send email
# def send_email(user, amount, subject, template):
#     message = render_to_string(template, {'user': user})
#     send_email = EmailMultiAlternatives(subject, '', to=[user.email])
#     send_email.attach_alternative(message, 'text/html')
#     send_email.send()

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self) -> str:
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class UserUpdateView(View):
    template_name = 'accounts/profile.html'
    
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Profile'
        })
        return context

@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password change successfully')
            update_session_auth_hash(request, form.user)
            send_transaction_email(request.user, 0, 'Password Change Confirmation', 'accounts/password_change_email.html' )
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form':form})