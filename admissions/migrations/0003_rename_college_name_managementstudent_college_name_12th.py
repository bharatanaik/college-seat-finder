# Generated by Django 4.2.7 on 2023-12-03 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0002_alter_managementstudent_alt_contact_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managementstudent',
            old_name='college_name',
            new_name='college_name_12th',
        ),
    ]
