from app.views.views import Health, PatientView, MedicalCaseView
from app.views.views import ClinicalHistoryView, ClinicalHistoryByPatientIdView

from flask_restful import Api
from flask_cors import CORS
from app import create_app
from flask_migrate import upgrade
from app import db

import pytest

@pytest.fixture()
def app():

    # settings_module = os.getenv('APP_SETTINGS_MODULE')
    settings_module = 'config.develop.Test'
    app = create_app(settings_module)
    db.init_app(app)

    api = Api(app)
    CORS(app)

    api.add_resource(Health, "/dermoapp/clinical-history/v1/health")
    api.add_resource(PatientView, "/dermoapp/clinical-history/v1/patients")
    api.add_resource(MedicalCaseView, "/dermoapp/clinical-history/v1/medical-cases")
    api.add_resource(ClinicalHistoryView, "/dermoapp/clinical-history/v1/clincial-history")
    api.add_resource(ClinicalHistoryByPatientIdView, "/dermoapp/clinical-history/v1/clincial-history/<string:patient_uuid>")

    # Completarlo con lo del entrypoint
    
    # with app.app_context():
    #         upgrade()

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()