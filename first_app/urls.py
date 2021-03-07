from django.urls import path
from django.conf.urls import url
from first_app import views
from first_app.views import SeqListView, SeqDetailView, HomeView

app_name = 'first_app'

urlpatterns = [
    path('', SeqListView.as_view(), name='Seqlist'),
    url(r'^(?P<pk>[-\w]+)/$', SeqDetailView.as_view(), name='Seqdetail'),
    path('clac', HomeView.as_view(), name='Seqper'),
]
