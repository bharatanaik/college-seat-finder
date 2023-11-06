from main.models import Cutoff, SeatMatrix
from main.api.jee import parser

class CutoffAPI:
    def _types(self)->list:
        return Cutoff.objects.values_list("_type", flat=True).distinct()
    
    def _categories(self):
         return Cutoff._meta.fields[8:]
     
    def _courses(self, **data):
        return {"courses":list(Cutoff.objects.filter(**parser(data)).distinct().values_list("_course_name", flat=True).order_by("-_course_name"))}

    def _colleges(self, **data):
        return {"colleges":list(Cutoff.objects.filter(**parser(data)).distinct().values_list("_college_code","_college_name").order_by("_college_name"))}

    def _cutoff(self, **data):
        try:
            category = data.pop("category")[0]
            rank = data.pop("rank")[0]
            return {"data":list(Cutoff.objects.filter(**{**parser(data), category+"__gte" : rank}).values_list("_college_code", category, "_college_name").order_by(category))}
        except Exception as e:
            print(e)
            return {"error":e.args}

    def _college_cutoff(self, **data): 
        try:
            category = data.pop("category")[0]
            return {"data" : list(Cutoff.objects.filter(**parser(data)).order_by("_course_name").values_list("_course_name", category))}
        except Exception as e:
            return {"error":e.args}

class SeatAPI:
    def _types(self)->list:
        return SeatMatrix.objects.values_list("_course_type", flat=True).distinct().order_by("_course_type") 

    def _categories(self):
        return SeatMatrix._meta.fields[18:-3]

    def _seat_types(self):
        return SeatMatrix.objects.values_list("_seat_type", flat=True).distinct()
        
    
    def _courses(self, **data):
        return {'courses':list(SeatMatrix.objects.filter(**parser(data)).distinct().values_list("_course_name", flat=True).order_by("-_course_name"))}

    def _districts(self, **data):
        return {'districts':list(SeatMatrix.objects.filter(**parser(data)).distinct().values_list("_district", flat=True).order_by("_district"))}

    def _colleges(self, **data):
        return {'colleges':list(SeatMatrix.objects.filter(**parser(data)).distinct().values_list("_college_name", flat=True).order_by("_college_name"))}

    def _matrix(self, **data):
        try:     
            seatType = data["_seat_type"][0]
            if seatType == "None":
                del data["_seat_type"]
            data = SeatMatrix.objects.get(**parser(data)).__dict__
        
            data.pop("_state")
            return data
        except Exception as e:
            print(e)
            return {"error":e.args}
