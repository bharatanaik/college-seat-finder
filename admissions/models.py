import os
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def student_documents(instance, filename):
    return os.path.join('content', instance.full_name, filename)

class ManagementStudent(models.Model):
    # Every student detail is related to main user
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField("Student Name", max_length=1000, null = True, blank = True)
    # step 1
    dob = models.DateField("Date of Birth", null = True, blank = True)
    guardian_name = models.CharField("Father / Guardian name", max_length=1000, null = True, blank = True)
    contact_no = models.CharField("Contact Number", max_length=20, null = True, blank = True)
    alt_contact_number = models.CharField("ALternate Contact Number", max_length=20, null = True, blank = True)
    email_id = models.EmailField("Email ID", null = True, blank = True)
    # step 2
    course_category = models.CharField("Course Category", max_length=1000, null = True, blank = True)
    course_name = models.CharField("Course Name", max_length=1000, null = True, blank = True)
    # step 3
    college_location = models.CharField("Location of the college", max_length=1000, null = True, blank = True)
    college_name = models.CharField("College name", max_length=1000, null = True, blank = True)
    # step 4
    year_12th = models.CharField("Year in which student passed 12th", max_length=10, null = True, blank = True)
    examination_board = models.CharField("Examination board", max_length=1000, null = True, blank = True)
    college_name_12th = models.CharField("Name of School / College in which you study 12th", max_length=1000, null = True, blank = True)
    grade_12th = models.CharField("12th Passing Grade or Percentage", max_length=10, null = True, blank = True)
    entrance_exam = models.CharField("Have you written any of the Entrance Exam this year?", max_length=1000, null = True, blank = True)
    # step 5 
    identification_proof = models.FileField("Identification Proof", upload_to=student_documents, null = True, blank = True)
    marks_card_12th = models.FileField("12th Marks card", null=True, blank=True, upload_to=student_documents)
    marks_card_10th = models.FileField("10th Marks card", upload_to=student_documents, null = True, blank = True)
    photo = models.FileField("Passport Size Photo", upload_to=student_documents, null = True, blank = True)
    signature = models.FileField("Signature Copy", upload_to=student_documents, null = True, blank = True)
    migration_cert = models.FileField("Migration Certificate:", null=True, blank=True, upload_to=student_documents)
    score_card = models.FileField("KCET, NEET, JEE etc Rank / Score Card", null=True, blank=True, upload_to=student_documents)
    applied = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    



