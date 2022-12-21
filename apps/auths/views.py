# from rest_framework import (
#     status,
#     generics,
# )
# from rest_framework.permissions import (
#     AllowAny,
#     IsAuthenticated,
# )
# from rest_framework.response import Response
# from rest_framework.views import (
#     APIView, 
# )
# from rest_framework.generics import UpdateAPIView
# from rest_framework.generics import RetrieveUpdateAPIView

# from auths.models import CustomUser
# from auths.serializers import (
#     LoginSerializer,
#     RegistrationSerializer,
#     UpdateUserSerializer,
#     ChangePasswordSerializer,
# )
# from auths.renderers import UserJSONRenderer
# from auths.backends import JWTAuthentication

# from abstracts.mixins import (
#     ResponseMixin,
#     ValidationMixin,
# )

# from django.core.handlers.wsgi import WSGIRequest
# from django.shortcuts import (
#     redirect,
# )
# from django.core.exceptions import ValidationError
# from django.db import IntegrityError
# from django.contrib.auth import logout, login


# class RegistrationAPIView(
#     ResponseMixin,
#     APIView
# ):
#     """
#     Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
#     """
#     # permission_classes = [AllowAny]
#     # serializer_class = RegistrationSerializer
#     # renderer_classes = (UserJSONRenderer,)

#     def post(self, request):
#         serializer: RegistrationSerializer = RegistrationSerializer(data=request.data)
        
#         if not serializer.is_valid():
#             return Response(
#                 {
#                     'message': 'Пользователь не был зарегистрирован',
#                     'payload': serializer.errors
#                 }, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         serializer.save()

#         return Response(
#         {
#             'message': 'Пользователь был зарегистрирован',
#             'payload': serializer.data
#         }, 
#         status=status.HTTP_201_CREATED
#     )
#         # except IntegrityError:
#         #     raise BaseException('Пользователь с таким email уже существует')

# # from rest_framework import generics
# # from rest_framework_api_key.permissions import HasAPIKey
# # from rest_framework import status

# # class LoginAPIView(generics.GenericAPIView):
# #     permission_classes = [HasAPIKey]
# #     serializer_class = LoginSerializer
# #     queryset = CustomUser.objects.all().order_by('-id')

# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             return Response(serializer.validated_data,status=status.HTTP_200_OK)
# #         else:
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = LoginSerializer
#     # authentication_classes = (TokenAuthentication, )
#     queryset = CustomUser.objects.all()

#     # def post(self, request):
#     #     user = request.data.get('user', {})

#     #     # Обратите внимание, что мы не вызываем метод save() сериализатора, как
#     #     # делали это для регистрации. Дело в том, что в данном случае нам
#     #     # нечего сохранять. Вместо этого, метод validate() делает все нужное.
#     #     serializer = self.serializer_class(data=user)
#     #     serializer.is_valid(raise_exception=True)

#     #     return Response(serializer.data, status=status.HTTP_200_OK)


# # class LoginAPIView(APIView, JWTAuthentication):
# #     """
# #     Авторизация для существующих пользователей.
# #     """
# #     permission_classes = [AllowAny]
# #     serializer_class = LoginSerializer
# #     renderer_classes = (UserJSONRenderer,)

# #     def post(self, request):
# #         """
# #         Checks is user exists.
# #         Email and password are required.
# #         Returns a JSON web token.
# #         """

# #         # serializer: LoginSerializer = LoginSerializer(data=request.data)

# #         # serializer.is_valid(raise_exception=True)
# #         serializer = self.serializer_class(data=request.data)
# #         serializer.is_valid(raise_exception=True)

# #         return Response(serializer.data, status=status.HTTP_200_OK)

#         # if serializer.is_valid():
#         #     return Response(
#         #         {
#         #             'message': 'вошел', 
#         #             'data': serializer.data
#         #         }, 
#         #         status=status.HTTP_200_OK
#         #     )
#         # else:
#         #     return Response(
#         #         {
#         #             'message': 'не вошел',
#         #             'data': serializer.errors
#         #         }, 
#         #         status=status.HTTP_400_BAD_REQUEST
#         #     )

#         # if not serializer.is_valid():
#         #     return Response(
#         #         {
#         #             'message': 'Пользователь не зарегистрирован',
#         #             'payload': serializer.errors
#         #         }
#         #     )

#         # login(request, serializer)
#         # return Response(
#         #     {
#         #         'message': 'Вакансия была обновлена',
#         #         'payload': serializer.data
#         #     },
#         #     status=status.HTTP_200_OK
#         # )

#         # user = CustomUser.objects.get(serializer)

#         # if user.is_valid():
#         #     if user.is_active:
#         #         login(request, user)

#         #         return Response(status=status.HTTP_200_OK)
#         #     else:
#         #         return Response(status=status.HTTP_404_NOT_FOUND)
#         # else:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         # return Response(serializer.data, status=status.HTTP_200_OK)

# from rest_framework import permissions

# class IsNotAuthenticated(permissions.IsAuthenticated):
#     """
#     Restrict access only to unauthenticated users.
#     """
#     def has_permission(self, request, view, obj=None):
#         if request.user and request.user.is_authenticated():
#             return False
#         else:
#             return True



# from rest_framework import generics
# from rest_framework import exceptions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from .serializers import *


# class AccountLogin(generics.GenericAPIView):

#     authentication_classes = (TokenAuthentication, SessionAuthentication)
#     permission_classes = (IsNotAuthenticated, )
#     serializer_class = LoginSerializer
    
#     def post(self, request, format=None):
#         """ authenticate """
#         serializer = self.serializer_class(data=request.DATA)
        
#         if serializer.is_valid():
#             login(request, serializer.instance)
        
#             # if request.DATA.get('remember'):
#             #     request.session.set_expiry(60 * 60 * 24 * 7 * 3)
#             # else:
#             #     request.session.set_expiry(0)
                
#             return Response({
#                 'detail': _(u'Logged in successfully'),
#                 # TODO: maybe more user info in the request would have sense
#                 'username': serializer.instance.username
#             })
        
#         return Response(serializer.errors, status=400)
    
#     def permission_denied(self, request):
#         raise exceptions.PermissionDenied(_("You are already authenticated"))

# account_login = AccountLogin.as_view()


# class LogoutAPIView(APIView):
#     """
#     Выход для существующих пользователей.
#     """

#     def get(self, request: WSGIRequest, *args, **kwargs):
#         logout(request)
#         return redirect(to="http://localhost:8000/api/login/")


# # class UpdatePersonalDataView(generics.UpdateAPIView):
# #     """
# #     Изменение личных данных пользователя.
# #     """

# #     queryset = CustomUser.objects.all()
# #     permission_classes = (IsAuthenticated,)
# #     serializer_class = UpdateUserSerializer


# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     """
#     Изменение личных данных пользователя.
#     """

#     permission_classes = (IsAuthenticated,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = UpdateUserSerializer

#     def retrieve(self, request, *args, **kwargs):
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         serializer_data = request.data.get('user', {})

#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_200_OK)


# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     Изменение пароля.
#     """

#     queryset = CustomUser.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer