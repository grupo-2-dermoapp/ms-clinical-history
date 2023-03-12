from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from app import create_app
from flask import jsonify
from app.views.views import Health, PatientView, MedicalCaseView
from app.views.views import ClinicalHistoryView, ClinicalHistoryByPatientIdView
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

api.add_resource(Health, "/dermoapp/clinical-history/v1/health")
api.add_resource(PatientView, "/dermoapp/clinical-history/v1/patients")
api.add_resource(MedicalCaseView, "/dermoapp/clinical-history/v1/medical-cases")
api.add_resource(ClinicalHistoryView, "/dermoapp/clinical-history/v1/clincial-history")
api.add_resource(ClinicalHistoryByPatientIdView, "/dermoapp/clinical-history/v1/clincial-history/<string:patient_uuid>")





if __name__ == '__main__':
    app.run()