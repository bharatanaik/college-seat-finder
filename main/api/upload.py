import openpyxl
from main.models import *


class UploadAPI:
    '''
    Upload API used to upload excel files
    '''
    DATABASE = {
        "kcet-data":Cutoff,
        "seat-data":SeatMatrix,
        "jee-data":JEEORCR,
        "neet-seat-data":NEETSeatMatrix
    }

    def __init__(self, file:str, type:str) -> None:
        self.wb = openpyxl.load_workbook(file, read_only=True, data_only=True).active
        self.model = self.DATABASE[type]

    def run(self):
        fields = [i.name for i in self.model._meta.fields]
        print(fields)
        fields.remove("id")
        objects = []
        for row in self.wb.iter_rows(min_row=2, values_only = True):
            data = dict(zip(fields, row))   
            print(data)         
            objects.append(self.model(**data))
        self.model.objects.bulk_create(objects)
        return {"count":self.model.objects.count()}