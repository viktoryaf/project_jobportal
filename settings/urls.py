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

from django.contrib import admin
from django.urls import (
    path,
    include,
)

from django.conf import settings
from django.conf.urls.static import static

# from apps.vacancies.views import (
#     VacanciesViewSet,
#     VacancyViewSet,
# )

from apps.vacancies import views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', views.VacanciesViewSet, name="vacancies"),
    path('vacancy/<int:id>', views.VacancyViewSet, name="vacancy_detail"),
]


# urlpatterns = [
#     path(settings.ADMIN_SITE_URL, admin.site.urls),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
# ] + static(
#     settings.STATIC_URL,
#     document_root=settings.STATIC_ROOT
# ) + static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT
# )
# # ------------------------------------------------
# # API-Endpoints
# #
# router: DefaultRouter = DefaultRouter(
#     trailing_slash=False
# )
# router.register(
#     'vacancies', VacanciesViewSet
# )
# urlpatterns += [
#     path(
#         'api/v1/',
#         include(router.urls)
#     ),
#     path(
#         'api/vacancy/<int:id>',
#         include(router.urls)
#     ),
#     path(
#         'api/vacancies_list',
#         include(router.urls)
#     )
# ]