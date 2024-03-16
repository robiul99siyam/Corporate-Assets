from rest_framework import serializers
from django.contrib.auth.models import User



""" This company register time """

class userResgisterSerializer(serializers.ModelSerializer):
    confrim_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','email', 'password', 'confrim_password']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['confrim_password']


        
        if password1 != password2:
            raise serializers.ValidationError({"errors": "Don't match password, Try again"})

        

        user = User(username=username, email=email)
        user.set_password(password1)
        user.is_active = False
        user.save()  
        return user


            


""" This is user login serializer """

class UserLoingSerializer(serializers.ModelSerializer):
        
        username = serializers.CharField(required = True)

        password = serializers.CharField(required = True)

        class Meta:
            model = User
            fields = ['username','password']