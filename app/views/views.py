# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request, current_app
import validators
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from app.models.models import Patient, MedicalCase, ClinicalHistory, db
from app.models.models import ClinicalHistorySchema
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended import get_jwt_identity, get_jwt
import random
import json
import app


class Health(Resource):
    def get(self):
        data = {
            "message" : "OK"
        }
        return data, 200
    
class PatientView(Resource):
    def post(self):
        request_data = request.json
        try:
            patient =  Patient(
                uuid = request_data['uuid'],
                location = request_data['location']
            )
            db.session.add(patient)
            db.session.commit()
            data = {
                "message" : "OK"
            }
            return data, 201
        except IntegrityError:
            data = {
                "message" : "fail"
            }
            return data, 400 
        finally:
            db.session.close()

class MedicalCaseView(Resource):
    def post(self):
        request_data = request.json
        try:
            clinical_history = ClinicalHistory.query.filter(
                ClinicalHistory.patient_uuid.has(uuid=request_data['patient_uuid'])
            ).first()

            medical_case = MedicalCase(
                uuid = request_data['uuid'],
                location = request_data['location'],
                clinical_history_uuid = clinical_history.uuid
             )
            db.session.add(medical_case)
            clinical_history.update()
            db.session.commit()

            


            data = {
                "message" : "OK"
            }
            return data, 201
        except IntegrityError:
            data = {
                "message" : "fail"
            }
            return data, 400 
        finally:
            db.session.close()

class ClinicalHistoryView(Resource):
    def post(self):
        request_data = request.json
        try:
            patient = Patient.query.filter_by(
                uuid=request_data['uuid']
            ).first()
            clinical_history = ClinicalHistory(
                patient_uuid = patient
            )
            db.session.add(clinical_history)
            db.session.commit()
            data = {
                "message" : "OK"
            }
            return data, 201
        except IntegrityError:
            data = {
                "message" : "fail"
            }
            return data, 400 
        finally:
            db.session.close()

class ClinicalHistoryByPatientIdView(Resource):

    def get(self, patient_uuid):
        clinical_history = ClinicalHistory.query.filter(
            ClinicalHistory.patient_uuid.has(uuid=patient_uuid)
        ).first()
        
        if clinical_history:
            data = {
                "code" : "",
                "message" : "Información de historia clinica",
                "clinical_history" : ClinicalHistorySchema().dump(clinical_history)
            }

            return data, 200
        else:
            data = {
                "code": "",
                "message": "No se puede completar la solicitud",
            }
            return data, 403



