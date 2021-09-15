from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView


def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Welcome! Your account has been created! You now should be able to login.')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,
                                   instance=request.user)
        user_profile_form = UserProfileUpdateForm(request.POST,
                                                  request.FILES,
                                                  instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            messages.success(request, f'Your details have been updated.')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        user_profile_form = UserProfileUpdateForm(instance=request.user.userprofile)
    context = {'user_form': user_form,
               'user_profile_form': user_profile_form}
    return render(request, 'profile.html', context)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/'
    template_name = 'account_app/user_delete.html'
