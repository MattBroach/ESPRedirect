from django.conf.urls import url, include
from django.conf.urls.static import static

from redirect.urls import urlpatterns
from redirect.dev_settings import STATIC_URL, MEDIA_URL, STATIC_ROOT, MEDIA_ROOT

import debug_toolbar

urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)


