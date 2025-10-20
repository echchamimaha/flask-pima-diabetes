import requests

print("🔍 Test de l'API Flask\n")

# Test 1: Ping
print("Test 1: Vérification que l'API répond (/ping)")
try:
    response = requests.get("http://127.0.0.1:5000/ping")
    print(f"✅ Status: {response.status_code}")
    print(f"✅ Response: {response.json()}")
except Exception as e:
    print(f"❌ Erreur: {e}")

print("\n" + "="*50 + "\n")

# Test 2: Prédiction
print("Test 2: Prédiction de diabète")
print("Données patient: [2, 120, 70, 30, 0, 33.6, 0.627, 50]")
try:
    data = {
        "instances": [[2, 120, 70, 30, 0, 33.6, 0.627, 50]]
    }
    response = requests.post("http://127.0.0.1:5000/predict", json=data)
    print(f"✅ Status: {response.status_code}")
    result = response.json()
    print(f"✅ Prédiction: {result['predictions'][0]} (0=pas de diabète, 1=diabète)")
    print(f"✅ Probabilité: {result['probabilities'][0][0]:.4f}")
except Exception as e:
    print(f"❌ Erreur: {e}")