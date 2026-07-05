from rest_framework import viewsets
from .models import PatientProfile
from .serializers import PatientProfileSerializer

class PatientProfileViewSet(viewsets.ModelViewSet):
    """
    A professional API controller that provides full CRUD operations
    (Create, Read, Update, Delete) for Patient records.
    """
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer