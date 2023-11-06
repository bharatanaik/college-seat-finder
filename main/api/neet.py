from main.models import NEETSeatMatrix
from main.api.jee import parser

class NEETSeatMatrixAPI:
    OPTIONS = {
        "institute_type":NEETSeatMatrix.INSTITUTE_TYPE,
        "program":NEETSeatMatrix.PROGRAM,
        "quotas":NEETSeatMatrix.QUOTA,
        "state":NEETSeatMatrix.STATES
    }

    def _institutes(self, **data):
        return {"institutes":list(NEETSeatMatrix.objects.filter(**parser(data)).distinct().values_list("institute", flat=True))}

    def _quota(self, **data):
        return {"quotas":list(NEETSeatMatrix.objects.filter(**parser(data)).distinct().values_list("quota", flat=True))}

    def _seat_data(self, **data):
        try:
            data = NEETSeatMatrix.objects.get(**parser(data)).__dict__
            data.pop("_state")
            return data    
        except Exception as e:
            print(e)
            return {"error":e.args}