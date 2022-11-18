from rest_framework import serializers
from apps.contact.models import Contact 


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            'id',
            'title',
            'status',
        )