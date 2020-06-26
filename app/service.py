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
                specialisations.append(s['nameTranslated'])
    
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
            'specialisation': (', ').join(specs),
            'doctors': doctors(specs[0])
        }
    else:
        return { 'result': '' }


def doctors(spec):
    return {
        'name': 'Dr. José Luiz',
        'specialisation': spec,
        'link_google': '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d19526.16873180093!2d-46.69553786958027!3d-23.56755907037668!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce577802a420bd%3A0x70a3d35a4dbd0699!2sAv.%20Rebou%C3%A7as%2C%20S%C3%A3o%20Paulo%20-%20SP!5e0!3m2!1spt-BR!2sbr!4v1593103282773!5m2!1spt-BR!2sbr" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>' 
    }