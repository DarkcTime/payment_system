from django.urls import path,re_path
from stripe_api.views import index,buy_item,info_item

urlpatterns = [
    path('item/<int:id>', info_item, name='info'),
    path('buy/<int:id>', buy_item, name='buy'),
    path('', index, name='home')
]
