from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('my-files/', files_view, name='files'),
    path('team/', Index.as_view(), name='team'),
    path('profile/', Index.as_view(), name='profile'),
    path('visualization/<int:file_id>/', visualization_view, name='visualization'),
    path('visualization/<int:file_id>/data', get_node_html_by_filters, name="selfdata"),
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)