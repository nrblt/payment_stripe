from django.urls import include, path, re_path

from payments import views

urlpatterns = [
    re_path(r'^test-payment/$', views.test_payment),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
]
