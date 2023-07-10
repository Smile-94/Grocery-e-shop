
from django.contrib import admin
from django.urls import path
from django.urls import include

# Static Files settings import 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve
from django.conf import settings

# Apps Urls
from accounts import urls as accounts_urls
from authority import urls as authority_urls
from customer import urls as customer_urls
from home import urls as home_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(accounts_urls)),
    path('', include(authority_urls)),
    path('', include(customer_urls)),
    path('', include(home_urls)),
]

# Serve Static Files
# for serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, view=serve)
