from django.urls import path
from admissions.views import CLoginView, RegisterView

urlpatterns = [
    path("admissions", CLoginView.as_view() , name="admissions"),
    path("register", RegisterView.register, name="register"),
    path("register/step1", RegisterView.step1,name="step-1"),
    path("register/step2", RegisterView.step2,name="step-2"),
    path("register/step3", RegisterView.step3,name="step-3"),
    path("register/step4", RegisterView.step4,name="step-4"),
    path("register/step5", RegisterView.step5,name="step-5"),
    path("register/step6", RegisterView.step6,name="step-6"),
    path("register/step7", RegisterView.step7,name="step-7"),
    
]