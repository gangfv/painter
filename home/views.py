from django.views import generic
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from home.models import Lesson
from home.serializer import FormSerializer


class HomeView(generic.ListView):
    model = Lesson
    context_object_name = 'Lessons'
    template_name = 'index.html'


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class FormCreteApi(generics.CreateAPIView):
    serializer_class = FormSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
