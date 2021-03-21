from flask_restful import Resource

class WellcomeOllivander(Resource):
    def get(self):
        return {"Wellcome": "to Ollivanders"}
    
    

    

    


