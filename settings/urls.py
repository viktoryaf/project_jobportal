"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )

from django.contrib import admin
from django.urls import (
    base,
    path,
    include,
)

from django.conf import settings
from django.conf.urls.static import static

from apps.auths.views import (
    RegistrationAPIView,
    LoginAPIView,
    UpdatePersonalDataView,
    ChangePasswordView,
)

from apps.resume.views import (
    ResumeAPIView,
)

from apps.vacancies.views import (
    VacanciesView,
    VacancyView,
)

from apps.responses.views import (
    ResponsesView,
)


urlpatterns = [
    # path(settings.ADMIN_SITE_URL, admin.site.urls),
    path('admin/', admin.site.urls),
    path('api/registration/', RegistrationAPIView.as_view()),
    path('api/login/', LoginAPIView.as_view()),
    path('api/update/', UpdatePersonalDataView.as_view()),
    path('api/changepass/', ChangePasswordView.as_view()),
    path('api/resume/', ResumeAPIView.as_view()),
    path('api/vacancies/', VacanciesView.as_view()),
    path('api/vacancy/<int:id>', VacancyView.as_view()),
    path('api/responses/', ResponsesView.as_view()),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
# ------------------------------------------------
# API-Endpoints
#
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
# router.register(
#     'vacancies', VacanciesViewSet
# )
# router.register(
#     'vacancies', VacancyViewSet
# )
# urlpatterns += [
#     path(
#         'api/vacancy/<int:id>',
#         include(router.urls)
#     ),
#     path(
#         'api/vacancies',
#         include(router.urls)
#     )
# ]