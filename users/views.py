# import all the necessary modules
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
# authentications
from django.contrib.auth.forms import UserCreationForm
# reverse_lazy
from django.urls import reverse_lazy
# login view
from django.contrib.auth.views import LoginView

# Add Sign up view for new user
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('photoapp:list')
    template_name = 'users/signup.html'
    
    # custom method
    def form_valid(self, form):
        to_return = super().form_valid(form)

        user = authenticate(
            username=form.cleaned_data['username'], 
            password=form.cleaned_data['password1']
            )
        
        login(self.request, user)
        return to_return

# Add Login view for existing user
class LoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True # redirect to list if user is already logged in