from django.urls import path
from .views import *

urlpatterns = [
    path('', user_save),
    path('FAQ/', sub_user_save_faq),
    path('Media-And-Insights/', sub_user_save_media),

]