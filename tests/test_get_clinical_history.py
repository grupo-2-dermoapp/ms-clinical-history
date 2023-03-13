from app.models.models import Patient
from app.utils.utils import uuid4Str
from app import db

def test_get_clinical_history_with_bad_id(client):
    uuid_test = 'test'
    response = client.get("/dermoapp/clinical-history/v1/clincial-history/{}".format(uuid_test))
    data = response.json
    code = response.status
    assert data['message'] == 'No se puede completar la solicitud'
    assert code == '403 FORBIDDEN'


def test_get_clinical_history_with_valid_id(client):
    patient = create_patient(client)
    clinical_history = create_clinical_history(client, patient['uuid'])
    uuid_test = patient['uuid']
    response = client.get("/dermoapp/clinical-history/v1/clincial-history/{}".format(uuid_test))
    data = response.json
    code = response.status
    assert data['message'] == 'Información de historia clinica'
    assert code == '200 OK'

def create_patient(client):
    payload = {}
    payload['uuid'] = uuid4Str()
    payload['location'] = 'test'
    response = client.post("/dermoapp/clinical-history/v1/patients", json=payload)
    if (response.status == '201 CREATED'):
        return payload
    else:
        return {}
    
def create_clinical_history(client, patient_uuid):
    payload = {}
    payload['uuid'] = patient_uuid
    response = client.post("/dermoapp/clinical-history/v1/clincial-history", json=payload)
    print(response.status)
    if (response.status == '201 CREATED'):
        return payload
    else:
        return {}