# Practical 11: Privacy-Aware Intelligent AIoT System
import json
import random
import hashlib
import base64
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

random.seed(3)
np.random.seed(3)

# Simple XOR/Symmetric encryption token generator (demonstrates cryptographic confidentiality)
KEY = b"SecretKeyForAIoTTransmission2025"

def encrypt_payload(data_dict):
    raw = json.dumps(data_dict).encode()
    enc = bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(raw)])
    return base64.b64encode(enc).decode()

def decrypt_payload(token_str):
    enc = base64.b64decode(token_str.encode())
    raw = bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(enc)])
    return json.loads(raw.decode())

def device_read(seq):
    return {
        "device": hashlib.sha256(b"node01").hexdigest()[:8],
        "seq": seq,
        "temperature": round(random.uniform(24, 42), 1),
        "gas": random.randint(150, 700)
    }

# Train ML model
X = np.column_stack([np.random.uniform(20, 45, 500), np.random.randint(100, 800, 500)])
y = ((X[:, 0] > 36) | (X[:, 1] > 450)).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = RandomForestClassifier(n_estimators=50, random_state=0)
model.fit(X_train, y_train)

acc = round(accuracy_score(y_test, model.predict(X_test)), 3)
print(f"Model accuracy: {acc}")

for i in range(1, 7):
    packet = device_read(i)
    token = encrypt_payload(packet)
    print(f"[Device] Packet {i} encrypted: {token[:28]}...")
    data = decrypt_payload(token)
    unsafe = model.predict([[data["temperature"], data["gas"]]])[0]
    result = "ALERT: UNSAFE" if unsafe else "SAFE"
    print(f"[Cloud] Decrypted: Temp = {data['temperature']}C, Gas = {data['gas']} -> {result}\n")
