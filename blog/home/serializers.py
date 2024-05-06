from rest_framework import serializers


from .models import Contact,Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         field="__all__"
