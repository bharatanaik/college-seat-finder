# Generated by Django 4.2.7 on 2023-12-03 07:45

import admissions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managementstudent',
            name='alt_contact_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ALternate Contact Number'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='college_location',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Location of the college'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='college_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Name of School / College in which you study 12th'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='contact_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='course_category',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Course Category'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='course_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='email_id',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email ID'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='entrance_exam',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Have you written any of the Entrance Exam this year?'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='examination_board',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Examination board'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='full_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Student Name'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='grade_12th',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='12th Passing Grade or Percentage'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Father / Guardian name'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='identification_proof',
            field=models.FileField(blank=True, null=True, upload_to=admissions.models.student_documents, verbose_name='Identification Proof'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='marks_card_10th',
            field=models.FileField(blank=True, null=True, upload_to=admissions.models.student_documents, verbose_name='10th Marks card'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=admissions.models.student_documents, verbose_name='Passport Size Photo'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='signature',
            field=models.FileField(blank=True, null=True, upload_to=admissions.models.student_documents, verbose_name='Signature Copy'),
        ),
        migrations.AlterField(
            model_name='managementstudent',
            name='year_12th',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Year in which student passed 12th'),
        ),
    ]
