"""AI Service for predictions and recommendations"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

class AIService:
    """AI Service for disease prediction and recommendations"""
    
    def __init__(self):
        self.disease_mapping = {
            'chest pain': ['Coronary Artery Disease', 'Angina', 'Heart Disease'],
            'dizziness': ['Vertigo', 'Vertebrobasilar Insufficiency', 'Inner Ear Disorder'],
            'diabetes': ['Type 2 Diabetes', 'Type 1 Diabetes', 'Gestational Diabetes'],
            'allergy': ['Allergic Reaction', 'Allergic Rhinitis', 'Food Allergy'],
            'cough': ['Common Cold', 'Bronchitis', 'Pneumonia', 'COVID-19'],
            'rash': ['Dermatitis', 'Eczema', 'Psoriasis', 'Urticaria'],
            'joint pain': ['Arthritis', 'Osteoarthritis', 'Rheumatoid Arthritis'],
        }
        
        self.doctor_specialization_mapping = {
            'Coronary Artery Disease': 'Cardiologist',
            'Angina': 'Cardiologist',
            'Heart Disease': 'Cardiologist',
            'Vertigo': 'Neurologist',
            'Dizziness': 'Neurologist',
            'Type 2 Diabetes': 'Diabetologist',
            'Type 1 Diabetes': 'Diabetologist',
            'Skin Rash': 'Dermatologist',
            'Arthritis': 'Orthopedic',
            'Joint Pain': 'Orthopedic',
        }
        
        self.drug_mapping = {
            'Coronary Artery Disease': [
                {'medicine': 'Aspirin', 'dosage': '100 mg', 'frequency': 'Once daily', 'side_effects': 'Stomach upset'},
                {'medicine': 'Atorvastatin', 'dosage': '40 mg', 'frequency': 'Once daily', 'side_effects': 'Muscle pain'}
            ],
            'Type 2 Diabetes': [
                {'medicine': 'Metformin', 'dosage': '500 mg', 'frequency': 'Twice daily', 'side_effects': 'GI upset'},
                {'medicine': 'Glipizide', 'dosage': '5 mg', 'frequency': 'Twice daily', 'side_effects': 'Hypoglycemia'}
            ],
            'Hypertension': [
                {'medicine': 'Lisinopril', 'dosage': '10 mg', 'frequency': 'Once daily', 'side_effects': 'Cough'},
                {'medicine': 'Amlodipine', 'dosage': '5 mg', 'frequency': 'Once daily', 'side_effects': 'Ankle swelling'}
            ]
        }
    
    def predict_disease(self, symptom_text, patient_data):
        """Predict disease from symptoms"""
        symptom_lower = symptom_text.lower()
        predictions = []
        
        for symptom_key, diseases in self.disease_mapping.items():
            if symptom_key in symptom_lower:
                for disease in diseases:
                    predictions.append({
                        'disease': disease,
                        'confidence': 85.0 + len(diseases) * 2,
                        'severity': 'Moderate' if 'severe' in symptom_lower else 'Mild',
                        'requires_doctor_visit': True,
                        'is_rare': False
                    })
        
        if not predictions:
            predictions.append({
                'disease': 'General Illness',
                'confidence': 45.0,
                'severity': 'Mild',
                'requires_doctor_visit': False
            })
        
        return predictions[:3]  # Return top 3
    
    def recommend_drugs(self, disease, patient_data):
        """Recommend drugs for disease"""
        drugs = self.drug_mapping.get(disease, [])
        
        if not drugs:
            drugs = [{
                'medicine': 'Consult your doctor',
                'dosage': 'As prescribed',
                'frequency': 'As recommended',
                'side_effects': 'Consult doctor'
            }]
        
        return drugs
    
    def recommend_doctors(self, disease):
        """Recommend doctor specialization"""
        specialization = self.doctor_specialization_mapping.get(disease, 'General Physician')
        return [{'specialization': specialization, 'recommendation': f'See a {specialization} for {disease}'}]


ai_service = AIService()

def predict_disease(symptom_text, patient_data):
    """Predict disease wrapper"""
    return ai_service.predict_disease(symptom_text, patient_data)

def recommend_drugs(disease, patient_data):
    """Recommend drugs wrapper"""
    return ai_service.recommend_drugs(disease, patient_data)

def recommend_doctors(disease):
    """Recommend doctors wrapper"""
    return ai_service.recommend_doctors(disease)
