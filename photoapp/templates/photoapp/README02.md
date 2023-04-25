### The taglist.html template will inherit from the list.html we just created:
```
<!-- photoapp/templates/photoapp/taglist.html -->
{% extends 'photoapp/list.html' %}

{% block body %}

<div class="alert alert-primary">
    <h2 class="text-center">Photos with the tag {{tag}}</h2>
</div>

{{ block.super }}

{% endblock body %}
```