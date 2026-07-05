from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PatientProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class PatientProfileSerializer(serializers.ModelSerializer):
    # Nesting the user data right inside the profile payload
    user = UserSerializer(read_only=True)
    # Exposing our dynamic property field to the API output
    current_age = serializers.ReadOnlyField()

    class Meta:
        model = PatientProfile
        fields = [
            'id', 'user', 'date_of_birth', 'current_age', 'gender', 
            'blood_group', 'address', 'emergency_contact_name', 'emergency_contact_phone'
        ]