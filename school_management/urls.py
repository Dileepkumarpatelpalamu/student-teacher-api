
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Student and Teacher For API",
      default_version='v1',
      description="A api for curd operation with authentication user access the all end point with admin and super users.  ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pateldileep51@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schoolapi/', include('schoolapp.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
