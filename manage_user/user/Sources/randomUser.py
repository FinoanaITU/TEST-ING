import requests

class RandomUser():
    def __init__(self):
        self.domaine = 'https://randomuser.me/api/1.2/?'
        
    def getAllUserRandom(self, seed, country, count):
        url = f'{self.domaine}seed={seed}&nat={country}&results={count}'
        print(url)
        try:
            req = requests.get(url)
            result = eval(req.text) if req.status_code == 200 or req.status_code == 201 else {"status" : str(req.status_code)}
            if "status" not in result:
                result = {'status': 200,'content':result}
        except Exception as e:
            result = {"status":'error'}
        return result