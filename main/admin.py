from django.contrib import admin
from main.models import Cutoff, SeatMatrix, JEEORCR, NEETSeatMatrix
from django.contrib.admin import VERTICAL, HORIZONTAL


admin.site.site_header = "College Seat Finder admin"  
admin.site.site_title  = "College Seat Finder admin site"
admin.site.index_title = "College Seat Finder Admin"

@admin.register(Cutoff)
class CutoffAdmin(admin.ModelAdmin):
    list_filter = ("_round",)
    search_fields = ('_college_name',)    
    list_display = ('_college_name', '_course_name')    

@admin.register(SeatMatrix)
class SeatMatrixAdmin(admin.ModelAdmin):
    list_filter = ( '_seat_type',)
    search_fields = ('_college_name',)    
    list_display = ('_college_name', '_course_name')    


@admin.register(JEEORCR)
class JEEORCRAdmin(admin.ModelAdmin):
    list_filter = ("institute_type","year", "gender", "round", "seat_type", "quota")
    radio_fields = {
        "institute_type":VERTICAL,
        "year":HORIZONTAL,
        "gender":VERTICAL,
    }
    search_fields = ['institute']

@admin.register(NEETSeatMatrix)
class NEETSeatMatrix(admin.ModelAdmin):
    list_display = ("institute", "college_code")
    list_filter = ("program", "quota", "institute_type")

