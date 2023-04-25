## Detail photo template
### Let’s edit the detail.html template to be able to see our photos in detail:
```
<!-- photoapp/templates/photoapp/detail.html -->
{% extends 'base.html' %} 

{% block body %}
<div class="mx-auto">
  <h1 class="text-center">{{ photo.title }}</h1>
  <p class="text-center fw-light">Uploaded on: {{photo.created}} <br> By {{photo.submitter.username}}</p>
  {% if user == photo.submitter %}
    <p class="text-center">
      <span><a href="{% url 'photo:update' photo.id %}" class="text-primary px-2">Update</a></span>
      <span><a href="{% url 'photo:delete' photo.id %}" class="text-danger px-2">Delete</a></span>
    </p>
  {% endif %}
</div>
<div class="row pb-5">
  <div class="col-md-8">
    <img src="{{photo.image.url}}" alt="" width="100%" />
  </div>
  <div class="col-md-4">
    <h4>More about this photo:</h4>
    <ul class="list-group list-group-horizontal-lg list-unstyled py-4">
      {% for tag in photo.tags.all %}
        <li><a href="{% url 'photo:tag' tag.slug %}" class="btn btn-sm list-group-item list-group-item-primary">{{tag.name}}</a></li>
      {% endfor %}
    </ul>
    <p>{{ photo.description }}</p>
  </div>
</div>

{% endblock body %}
```
## Create the photo template

The next template will include a crispy form, so that we don’t have to display the forms manually. Django will do that for us:
```
<!-- photoapp/templates/photoapp/create.html -->
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block body %}
<div class="mx-auto">
  <h1 class="mt-3 text-center">Add photo</h1>
</div>
<div class="form-group">
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit" class="btn btn-success mb-3">Add Photo</button>
  </form>
</div>
{% endblock body %}
```

## Update and delete templates
Let’s finish the photo-sharing app before heading to the authentication templates.

The following update template is a simple form where the user can update the title, description, and tags of the photo:

<!-- photoapp/templates/photoapp/update.html -->
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block body %}
<div class="mx-auto">
  <h1 class="mt-3 text-center">Edit photo {{photo}}</h1>
</div>
<div class="form-group">
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit" class="btn btn-success mb-3">Edit Photo</button>
  </form>
</div>
{% endblock body %}
```
# Old files will be deleted
```
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
```
# chatGPT
```
# photoapp/views.py

from django.views.generic import ListView
from taggit.models import Tag

from .models import Photo


class TaggedPhotoListView(ListView):
    model = Photo
    template_name = 'photoapp/taglist.html'
    context_object_name = 'photos'
    paginate_by = 12

    def get_queryset(self):
        tag_slug = self.kwargs['tag']
        tag = Tag.objects.get(slug=tag_slug)
        queryset = Photo.objects.filter(tags=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context
```