
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
from products import urls as products_urls
from payment import urls as payment_urls
from deleveryman import urls as deleveryman_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(accounts_urls)),
    path('', include(authority_urls)),
    path('', include(customer_urls)),
    path('', include(home_urls)),
    path('', include(products_urls)),
    path('', include(payment_urls)),
    path('', include(deleveryman_urls)),

]

# Serve Static Files
# for serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, view=serve)
