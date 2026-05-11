from django.shortcuts import redirect
from django.urls import include, path

def root_redirect(request):
    return redirect('/api/todos/')

urlpatterns = [
    path('', root_redirect),
    path('api/', include('todos.urls')),
]
