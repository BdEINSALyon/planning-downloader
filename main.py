import requests

def main():
    PHPSESSID = 'oflbncfl7e2pk5rhhir703ruf3'
    URL = 'http://planning.gala.bde-insa-lyon.fr/orga/{id}/print'

    orgas = [
        {'id': 1, 'name': 'SUPER ADMIN'}
    ]

    for o in orgas:
        print(o['name'])
        r = requests.get(URL.format(id=o['id']), cookies={'PHPSESSID': PHPSESSID})
        path = o['name'] + '.pdf'
        if r.status_code == 200:
            print('OK')
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
                print('WRITTEN')
        else:
            print('ERROR')


if __name__ == '__main__':
    main()
