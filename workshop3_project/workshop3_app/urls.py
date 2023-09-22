from django.urls import path
from .views import AttendListView, AttendSummaryView

urlpatterns = [
    path('attend/', AttendListView.as_view(), name='attend-list'),
    path('attend_summary/', AttendSummaryView.as_view(), name='attend-summary'),
]
