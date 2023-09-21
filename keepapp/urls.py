from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.index , name='index'),
    path('api/notes' , views.getNote , name='notes'),
    path('api/delete-notes/<int:id>' , views.delNote , name='delete-note'),
    path('api/add-notes' , views.addNote , name='add-note'),
    path('api/update-notes/<int:id>' , views.updateNote , name='update-Note')
]