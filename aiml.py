import random
import time

# Simulated AI Diagnostic Engine
def ai_diagnose(symptoms):
    diagnosis_db = {
        "fever,cough": "You may have a mild respiratory infection or flu.",
        "headache,blurred vision": "Possible migraine or high blood pressure. Please consult a neurologist.",
        "chest pain,shortness of breath": "Warning: Possible heart-related condition. Seek emergency care.",
        "fatigue,weight loss": "Could be related to thyroid imbalance or diabetes. Recommend blood tests.",
        "stomach pain,nausea": "Might be gastritis or food poisoning. Suggest hydration and observation.",
    }
    
    for key, value in diagnosis_db.items():
        key_symptoms = set(key.split(','))
        input_symptoms = set(symptoms.lower().split(','))
        if key_symptoms.issubset(input_symptoms):
            return value
    
    return "Symptoms are not specific enough. Please consult a healthcare provider."

# Virtual Consultation Simulation
def virtual_consultation():
    print("\n🌐 Welcome to MetaHealth AI Diagnostic System 🌐")
    print("Simulated consultation in a virtual clinic...")

    patient_name = input("👤 Enter Patient Name: ")
    age = int(input("🎂 Enter Age: "))
    print("📝 Enter symptoms (comma separated, e.g., fever,cough):")
    symptoms = input("Symptoms: ")

    print("\n🧠 AI is analyzing your inputs in the metaverse...")
    time.sleep(2)

    diagnosis = ai_diagnose(symptoms)

    print("\n📋 Diagnostic Report")
    print(f"Patient: {patient_name}, Age: {age}")
    print(f"Symptoms: {symptoms}")
    print(f"AI Diagnosis: {diagnosis}")

    # Simulated Metaverse Room Suggestion
    room_id = random.randint(1000, 9999)
    print(f"\n🚪 Please join Virtual Consultation Room #{room_id} for follow-up.")

# Run the simulation
if __name__ == "__main__":
    virtual_consultation()
