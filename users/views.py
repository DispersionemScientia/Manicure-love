from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import User
from .forms import UserForm, ChangeUserInfoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from records.models import Record

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('records/home.html')

@login_required
def profile(request, user_id):
    records = Record.objects.filter(user=user_id, is_active=True)
    context = {'records': records}
    return render(request, 'users/profile.html', context)

class UserLogoutView(LogoutView, LoginRequiredMixin):
    template_name = 'users/logout.html'

class RegisterUserView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserForm
    success_url = reverse_lazy('records:home')

class ChangeUserInfoView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = User
    template_name = 'users/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('records:home')
    success_message = 'Данные пользователя успешно имзменены!'

    def setup(self, request, *args, **kwargs):     # выполняется самым первым и инициализирует объект контроллера
        self.user_id = request.user.pk             # переопределяя сохраняем первичный ключ юзера
        return super().setup(request, *args, **kwargs)
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class AdministrationView(ListView):
    model = User
    template_name = 'users/administration.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = Record.objects.all()
        return context
