from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login
from django.views.generic import FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

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