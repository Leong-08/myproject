# photoapp/views.py
# import to build the CBV for the photoapp
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Photo
from taggit.models import Tag

# create the class for the photoapp
class PhotoListView(ListView):
    model = Photo
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'
    # ordering = ['-date_uploaded']

# declare the class for the photoapp
class PhotoTagListView(PhotoListView):
    template_name = 'photoapp/taglist.html'

    # Custom method
    def get_tags(self):
        return self.kwargs.get('tag')
    
    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag')
        return context
    
#  a simple DetailView that displays all the data related to a unique photo.
class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photoapp/detail.html'
    context_object_name = 'photo'

# Create view to allows users to create a photo object only if they’re logged in
class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photoapp/create.html'
    fields = ['title', 'description', 'image', 'tags']
    success_url = reverse_lazy('photoapp:list')
    
    # Custom method
    def form_valid(self, form):
        form.instance.submitter = self.request.user # set the submitter to the current user ++
        return super().form_valid(form)

# test mixin to check if the user is the author of the photo
class UserIsSubmitter(UserPassesTestMixin):
    # custom method
    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))
    
    # test method
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('You must be logged in to edit this photo.')

# photo update view
class PhotoUpdateView(UserIsSubmitter, UpdateView):
    model = Photo
    template_name = 'photoapp/update.html'
    fields = ['title', 'description', 'image', 'tags']
    success_url = reverse_lazy('photoapp:list')

# photo delete view
class PhotoDeleteView(UserIsSubmitter, DeleteView):
    model = Photo
    template_name = 'photoapp/delete.html'
    success_url = reverse_lazy('photoapp:list')