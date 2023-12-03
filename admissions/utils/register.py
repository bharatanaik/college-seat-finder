import re, random, string
from django.http import HttpRequest
from admissions.models import User, ManagementStudent
from django.contrib.auth import login


def convert_to_username(name):
    username = re.sub(r'\s+', '_', name.lower())
    username += ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return username

class Register:

    def process_step_1(request:HttpRequest):
        try:
            User.objects.get(username = request.POST.get("email"))
            return {"error":"User already Exist"}
        except User.DoesNotExist:
            pass
        name:str = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        student = ManagementStudent()
        user_instance = User.objects.create_user( username = email, email=email)
        user_instance.first_name = name
        user_instance.set_password(password)
        user_instance.save()
        student.user = user_instance
        student.full_name = name
        student.dob = request.POST.get("birth_date")
        student.guardian_name = request.POST.get("guardian_name")
        student.contact_no = request.POST.get("contact")
        student.alt_contact_number = request.POST.get("alt_contact")
        student.email_id = email
        student.save()
        login(request, user_instance)
        return {}
    
    def process_step_2(request:HttpRequest):
        student = ManagementStudent.objects.get(user = request.user)
        student.course_name = request.POST.get("course")
        student.course_category = request.POST.get("course_category")
        student.save()
        return {}
    
    def process_step_3(request:HttpRequest):
        student = ManagementStudent.objects.get(user = request.user)
        student.college_name = request.POST.get("college")
        student.college_location = request.POST.get("college_location")
        student.save()
        return {}
    
    def process_step_4(request:HttpRequest):
        student = ManagementStudent.objects.get(user = request.user)
        student.year_12th = request.POST.get("year")
        student.examination_board = request.POST.get("board")
        student.college_name_12th = request.POST.get("school")
        student.grade_12th = request.POST.get("percentage")
        student.entrance_exam = request.POST.get("entrance")
        student.save()
        return {}
    
    def process_step_5(request:HttpRequest):
        student = ManagementStudent.objects.get(user = request.user)
        student.identification_proof = request.FILES.get("identification_file")
        student.marks_card_12th = request.FILES.get("12th_marks_card")
        student.marks_card_10th = request.FILES.get("10th_marks_card")
        student.photo = request.FILES.get("passport_size_photo")
        student.signature = request.FILES.get("signature")
        student.migration_cert = request.FILES.get("migration_certificate")
        student.score_card = request.FILES.get("score_card")
        student.save()
        return {}
    
    def process_step_6(request:HttpRequest):
        student = ManagementStudent.objects.get(user = request.user)
        student.applied = True
        student.save()
        return {}
    

       



