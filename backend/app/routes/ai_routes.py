"""AI routes for disease prediction and recommendations"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Patient, DiseasePrediction, DrugRecommendation, Symptom
from app.services.ai_service import predict_disease, recommend_drugs, recommend_doctors

bp = Blueprint('ai', __name__, url_prefix='/api/ai')

@bp.route('/predict-disease', methods=['POST'])
@jwt_required()
def predict():
    """Predict disease based on symptoms"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        data = request.get_json()
        symptom_text = data.get('symptom_text')
        
        if not symptom_text:
            return jsonify({'error': 'Symptom text required'}), 400
        
        # Save symptom
        symptom = Symptom(
            patient_id=patient.id,
            symptom_text=symptom_text,
            severity=data.get('severity', 'Mild'),
            duration_days=data.get('duration_days')
        )
        db.session.add(symptom)
        db.session.flush()
        
        # Get AI predictions
        predictions = predict_disease(symptom_text, patient.to_dict())
        
        # Save predictions
        saved_predictions = []
        for pred in predictions:
            prediction = DiseasePrediction(
                patient_id=patient.id,
                symptom_id=symptom.id,
                predicted_disease=pred['disease'],
                confidence_percentage=pred['confidence'],
                severity_level=pred['severity'],
                requires_doctor_visit=pred['requires_doctor_visit'],
                is_rare_disease=pred.get('is_rare', False)
            )
            db.session.add(prediction)
            saved_predictions.append(prediction)
        
        db.session.commit()
        
        return jsonify({
            'message': 'Disease prediction completed',
            'symptom': symptom.to_dict(),
            'predictions': [p.to_dict() for p in saved_predictions]
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/recommend-drugs', methods=['POST'])
@jwt_required()
def recommend():
    """Get drug recommendations"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        data = request.get_json()
        disease = data.get('disease')
        
        if not disease:
            return jsonify({'error': 'Disease required'}), 400
        
        # Get recommendations
        recommendations = recommend_drugs(disease, patient.to_dict())
        
        # Save recommendations
        saved_recs = []
        for rec in recommendations:
            drug_rec = DrugRecommendation(
                patient_id=patient.id,
                medicine_name=rec['medicine'],
                dosage=rec['dosage'],
                frequency=rec['frequency'],
                side_effects=rec.get('side_effects'),
                food_restrictions=rec.get('food_restrictions')
            )
            db.session.add(drug_rec)
            saved_recs.append(drug_rec)
        
        db.session.commit()
        
        return jsonify({
            'recommendations': [r.to_dict() for r in saved_recs]
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/recommend-doctors', methods=['POST'])
@jwt_required()
def recommend_doc():
    """Get doctor recommendations"""
    try:
        data = request.get_json()
        disease = data.get('disease')
        
        if not disease:
            return jsonify({'error': 'Disease required'}), 400
        
        doctors = recommend_doctors(disease)
        
        return jsonify({
            'doctors': doctors
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
