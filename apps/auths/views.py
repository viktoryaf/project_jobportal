from rest_framework import (
    status,
    generics,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import (
    APIView, 
)
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from auths.models import CustomUser
from auths.serializers import (
    LoginSerializer,
    RegistrationSerializer,
    UpdateUserSerializer,
    ChangePasswordSerializer,
)
from auths.renderers import UserJSONRenderer

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import (
    redirect,
)
from django.contrib.auth import logout


class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    Авторизация для существующих пользователей.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    """
    Выход для существующих пользователей.
    """

    def get(self, request: WSGIRequest, *args, **kwargs):
        logout(request)
        return redirect(to="")


# class UpdatePersonalDataView(generics.UpdateAPIView):
#     """
#     Изменение личных данных пользователя.
#     """

#     queryset = CustomUser.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UpdateUserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    Изменение личных данных пользователя.
    """

    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UpdateUserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    """
    Изменение пароля.
    """

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer