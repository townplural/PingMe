from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import RegistrationForm, EditUserForm, ProfileUserForm
from user.models import CustomUser


class RegisterUser(CreateView):
    template_name = 'user/register_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login_user')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class ProfileUser(LoginRequiredMixin, FormView):
    template_name = 'user/profile_user.html'
    form_class = ProfileUserForm
    
    def get_object(self, queryset = None):
        return super().get_object(queryset)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login_user.html'
    
    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy('user:profile_user')


class EditUser(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = EditUserForm
    template_name = 'user/edit_user.html'
    success_url = reverse_lazy('user:profile_user')
    
    def get_object(self, queryset = None):
        return self.request.user
