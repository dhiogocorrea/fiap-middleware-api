import requests

API_URL = 'https://fiapdiagnosisapi.azurewebsites.net/Diagnostics'


def message(data):
    return { 'symps': data.selectedSymptoms }