from django.urls import path
from main.views import *
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticSiteView
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticSiteView,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),

    path('', IndexView.as_view(), name="index"),
    path('upload', UploadView().main, name="upload"),
    path('delete/<str:name>', UploadView().delete, name="delete"),
    path('disclaimer', TemplateView.as_view(template_name="disclaimer.html"), name="disclaimer"),
    


    # BASIC ROUTES FOR KCET
    path('courses', CourseView().main, name="courses"),    
    path('college/<str:college_name>', CollegeView().main, name="college"),
    # KCET CUTOFF ROUTES
    path('kcet-cutoff', CutoffAnalyserView().main, name="kcet-cutoff"),
    path("kcet-cutoff/ajax/get-courses", CutoffAnalyserView().get_courses),
    path("kcet-cutoff/ajax/get-data", CutoffAnalyserView().get_data),

    # College Cutoff Routes
    path('college-cutoff', CollegeCutoffView().main, name="college-cutoff"),
    path('college-cutoff/ajax/get-colleges', CollegeCutoffView().get_colleges),
    path('college-cutoff/ajax/get-data', CollegeCutoffView().get_data),
    
    # College Seat Analyser
    path("seat-analyser", SeatAnalyserView().main, name = "seat-analyser"),
    path('seat-analyser/ajax/get-courses', SeatAnalyserView().get_courses),
    path('seat-analyser/ajax/get-districts', SeatAnalyserView().get_districts),
    path('seat-analyser/ajax/get-colleges', SeatAnalyserView().get_colleges),
    path('seat-analyser/ajax/get-seat-matrix', SeatAnalyserView().get_seat_matrix),
    
     # JEE ORCR Analyser
    path('jee-orcr', JEEORCRView().main, name="jee-orcr"),
    path('jee-orcr/ajax/get-institutes', JEEORCRView().get_institutes),
    path('jee-orcr/ajax/get-courses', JEEORCRView().get_courses),
    path('jee-orcr/ajax/get-result', JEEORCRView().get_result),
    path('jee-orcr/ajax/get-college-result', JEEORCRView().get_college_result),
    path('jee-orcr/ajax/get-course-result', JEEORCRView().get_course_result),

    # NEET SEAT MATRIX
    path("neet-seat-matrix", NEETSeatMatrixView().main, name="neet-seat-matrix"),
    path("neet-seat-matrix/ajax/get-institutes", NEETSeatMatrixView().get_institutes),
    path("neet-seat-matrix/ajax/get-quota", NEETSeatMatrixView().get_quota),
    path("neet-seat-matrix/ajax/get-seat-data", NEETSeatMatrixView().get_seat_data),

    #Admissions
    path('admissions', TemplateView.as_view(template_name="admissions.html"), name="admissions")
    
    
]