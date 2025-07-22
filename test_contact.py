#!/usr/bin/env python
import requests

# Probar el formulario de contacto
url = "http://127.0.0.1:8000/contact/submit/"
data = {
    'name': 'Test User',
    'email': 'test@example.com',
    'subject': 'Test Subject',
    'message': 'This is a test message'
}

try:
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
