import requests
import json

API_URL = 'https://fiapdiagnosisapi.azurewebsites.net/Diagnostics'


def message(data):
    symps = data.selectedSymptoms.split(',')

    newData = {
        'selectedSymptoms': symps,
        'gender': data.gender,
        'yearOfBirth': data.yearOfBirth
    }

    response = requests.post(API_URL, data=newData)

    if response.status_code == 200:
        return { 'result': response.text }
    else:
        returun { 'result': '' }