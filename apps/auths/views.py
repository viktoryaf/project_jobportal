from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import (
    APIView, 
    UpdateAPIView,
)

from .models import CustomUser
from auths.serializers import (
    LoginSerializer,
    RegistrationSerializer,
    UpdateUserSerializer,
    ChangePasswordSerializer,
)


from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import (
    redirect,
)
from django.contrib.auth import logout

from rest_framework.permissions import IsAuthenticated


class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Phone_number, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    """
    Logs out an existing user.
    """

    def get(self, request: WSGIRequest, *args, **kwargs):
        logout(request)
        return redirect(to="/auth/login")


class UpdatePersonalData(UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class ChangePasswordView(UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer