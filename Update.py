import json
import requests,os
from urllib.request import urlretrieve
def main():
    with open("update.json","r")as f:
        content = json.loads(f.read())
    r_content = requests.get(content['version_url']).json()
    def check_exists(file):
        return os.path.exists(file)
    updated = Falsemr
    if content['version'] < r_content['version']:
        updated = True

    appname = content['name'] + '_new.exe'
    if updated and not check_exists(appname):
        try:
            urlretrieve(content['download_url'], appname)
        except (RuntimeError, ConnectionError):
            urlretrieve(content['download_url'], appname)

    old_name = content['name'] + '.exe'
    if check_exists(old_name):
        os.remove(old_name)
    if check_exists(appname) and not check_exists(old_name):
        os.rename(appname, old_name)
    content['version'] = r_content['version']
    with open("update.json", 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False)