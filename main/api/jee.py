from main.models import JEEORCR

def parser(data:dict)->dict:
    return {x:y[0] for x, y in data.items()}

class JEEAPI:
    OPTIONS = {
            "institute_types":JEEORCR.INSTITUTE_TYPE,
            "seat_types":JEEORCR.SEAT_TYPE,
            "quotas":JEEORCR.QUOTA,
            "years":JEEORCR.YEAR,
            "rounds":JEEORCR.ROUND
    }

    def get_template(self, type):
        templates = {"college":"jee/jee-orcr-college.html", "course":"jee/jee-orcr-course.html"}
        return templates.get(type, "jee/jee-orcr.html")
    
    def _institutes(self, **data):
        return {"institutes": list(JEEORCR.objects.filter(**parser(data)).values_list("institute").distinct())}
    

    def _courses(self, **data):
        return {"courses":list(JEEORCR.objects.filter(**parser(data)).values_list("course").distinct().order_by("-course"))}
    
    def _result(self, **data):
        try:
            result = JEEORCR.objects.get(**parser(data))
            return {"opening_rank":result.opening_rank, "closing_rank":result.closing_rank }
        except Exception as e:
            return {"opening_rank":"Not found", "closing_rank":"Not found"}
        
    def _courses_via_college(self, **data):
        try:
            return {"college_orcr":list(JEEORCR.objects.filter(**parser(data)).values_list("course", "opening_rank", "closing_rank"))}
        except Exception as e:
            return {}
        
    def _colleges_via_course(self, **data):
        try:
            return {"course_orcr" : list(JEEORCR.objects.filter(**parser(data)).distinct().order_by("institute").values_list("institute", "opening_rank", "closing_rank"))}
        except Exception as e:
            return {}