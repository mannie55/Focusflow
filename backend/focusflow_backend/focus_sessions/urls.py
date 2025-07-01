from django.urls import path
from .views import (
    StartSessionView,
    StopSessionView,
    ActiveSessionView,
    SessionHistoryView,
)

urlpatterns = [
    path('start/', StartSessionView.as_view(), name='start-session'),
    path('stop/', StopSessionView.as_view(), name='stop-session'),
    path('active/', ActiveSessionView.as_view(), name='active-session'),
    path('history/', SessionHistoryView.as_view(), name='session-history'),
]
