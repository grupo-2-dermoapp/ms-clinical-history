from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, ForeignKey, String, DateTime, Numeric
from sqlalchemy import Enum
from datetime import datetime
from app.utils.utils import uuid4Str
from app import db, ma

class ClinicalHistory(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    patient_uuid = db.relationship('Patient', backref='clinical_history', uselist=False)
    medical_cases = db.relationship('MedicalCase', backref='clinical_history', lazy=True)

    def update(self):
        self.updated_at = datetime.utcnow()

class Patient(db.Model):
    uuid = Column(String(40), primary_key=True, nullable=False)
    location = Column(String(150), nullable=False)
    clinical_history_uuid = db.Column(String, db.ForeignKey('clinical_history.uuid'), unique=True)

class MedicalCase(db.Model):
    uuid = Column(String(40), primary_key=True, nullable=False)
    location = Column(String(150), nullable=False)
    clinical_history_uuid = db.Column(String, db.ForeignKey('clinical_history.uuid'), nullable=False)

class ClinicalHistorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ClinicalHistory
        exclude = ('uuid',)
        load_instance = True
        include_relationships = True

