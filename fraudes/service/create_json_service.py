import json
import datetime

class CreateJsonService:

    def __init__(self, dict) -> None:
        self.mydict = dict
        self.filename = "../fraudes_pix.json"

    
    def write(self):
        with open(self.filename, 'w') as j:
            json.dump(self.mydict, j, ensure_ascii=False, cls=DateTimeEncoder)
    
class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)