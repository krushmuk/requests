import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.token = ''

    def get_link(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        name = self.file_path.split('/')[-1]
        print(name)
        params = {'path': f'netology{name}', 'overwrite': True}
        headers = {'content type': 'application/json',
                   'authorization': f'OAuth {self.token}'}
        res = requests.get(url=url, params=params, headers=headers, timeout=3)
        return res.json()

    def upload(self):
        href = self.get_link().get('href', '')
        upload = requests.put(url=href, data=open(self.file_path, 'rb'))
        if upload.status_code != 201:
            print(f'Error {upload.status_code}')
        else:
            print('Success')
