from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from admissions.models import ManagementStudent
from admissions.utils.register import Register
from django.contrib.auth.views import LoginView
# Create your views here.



class CLoginView(LoginView):
    template_name = "admissions/admission.html"

    def get_success_url(self) -> str:
        return reverse("register")
    
class RegisterView:
    """
    This view serve the purpose of registering the user
    """
    @staticmethod
    def register(request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect(reverse("step-1"))
        else:
            student = ManagementStudent.objects.get(user=request.user)
            if not student.course_category :
                return redirect(reverse("step-2"))
            elif not student.college_location:
                return redirect(reverse("step-3"))
            elif not student.college_name_12th:
                return redirect(reverse("step-4"))
            elif not student.identification_proof:
                return redirect(reverse("step-5"))
            elif not student.applied:
                return redirect(reverse("step-6"))
            else:
                return redirect(reverse("step-7"))

    @staticmethod
    def step1(request:HttpRequest):
        context = {}
        if request.method == "POST":
            error = Register.process_step_1(request)
            if error:
                context["error"] = error
            else:    
                return redirect(reverse("step-2"))
        return render(request, "admissions/register/step1.html", context)
    
    @staticmethod
    def step2(request:HttpRequest):         
        if request.method == "POST":
            Register.process_step_2(request)
            return redirect(reverse("step-3"))
        return render(request, "admissions/register/step2.html")
    
    @staticmethod
    def step3(request:HttpRequest):
        if request.method == "POST":
            Register.process_step_3(request)
            return redirect(reverse("step-4"))
        return render(request, "admissions/register/step3.html")
    
    @staticmethod
    def step4(request:HttpRequest):
        if request.method == "POST":
            Register.process_step_4(request)
            return redirect(reverse("step-5"))
        return render(request, "admissions/register/step4.html")
    
    @staticmethod
    def step5(request):
        if request.method == "POST":
            Register.process_step_5(request)
            return redirect(reverse("step-6"))
        return render(request, "admissions/register/step5.html")
    
    @staticmethod
    def step6(request):
        if request.method == "POST":
            Register.process_step_6(request)
            return redirect(reverse("step-7"))
        return render(request, "admissions/register/step6.html")
    
    @staticmethod
    def step7(request):
        student = ManagementStudent.objects.get(user = request.user)
        return render(request, "admissions/register/step7.html", {
            "college":student.college_name,
            "course":student.course_name,
            "name":student.full_name
        })
