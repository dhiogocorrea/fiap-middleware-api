import requests
import json

API_URL = 'https://fiapdiagnosisapi.azurewebsites.net/Diagnosis'


def get_diagnostics_and_specializations(data):
    diags = []
    specialisations = []
    for d in data:
        if d['issue']['profNameTranslated']  not in diags:
            diags.append(d['issue']['profNameTranslated'])
        
        for s in d['specialisation']:
            if s['name'] not in specialisations:
                specialisations.append(s['name'])
    
    return diags, specialisations

def message(data):
    symps = data.selectedSymptoms.split(',')

    path = []
    alreadySeen = []
    for s in symps:
        if s not in alreadySeen:
            path.append(f'selectedSymptoms={s}')
            alreadySeen.append(s)


    url = API_URL + '?' + '&'.join(path) + f'&gender={data.gender}&yearOfBirth={data.yearOfBirth}'
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        diags, specs = get_diagnostics_and_specializations(data)
        return {
            'diagnostics': (', ').join(diags),
            'specialisation': (', ').join(specs)
        }
    else:
        return { 'result': '' }