from rest_framework.authtoken.models import Token 
from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.models import User
from .serializer import userResgisterSerializer,UserLoingSerializer
from rest_framework.views import APIView
from django.contrib.auth import login,logout,authenticate



# send the email user email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives



""" This is company resgister views  here """

class userResgisterViews(APIView):

    serializer_class = userResgisterSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            token = default_token_generator.make_token(user)
            print(token)


            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)


            confirm_link = f"http://127.0.0.1:8000/authentication/active/{uid}/{token}"

            email_subject = "Company User Resgister Verfiy "
            email_body = render_to_string('index.html',{'confirm_link' : confirm_link})

            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()

            print(user)
            return Response("Dear User, Please check your email to verify your registration")
        return Response(serializer.errors)





""" This is company user acitve  views  here """
def activete(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(user.DoesNotExist):
        user = None
    

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

""" This is company resgister views  here """

class LoginAPIView(APIView):
    serializer_class = UserLoingSerializer  

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token,"HOw are kasdfk")
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({"errors": "Invalid Data"})
        else:
            return Response(serializer.errors)


class LogOutApiview(APIView):
    def get(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            pass 

        logout(request)
        return redirect('login')