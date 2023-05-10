from src.vacancy import Vacancy
import requests
import json

def pprint(json_object):
    print(json.dumps(json_object, indent=2,  ensure_ascii=False))


url: str = 'https://api.hh.ru/'

endpoint = "https://api.hh.ru/vacancies"
response = requests.get(endpoint, params={"text": "python"})

#pprint(response.json())
print("/n/n")
#pprint(response.json()["items"])
d = response.json()["items"]
list = []

for i in d:
 #   sl = [i["name"], i.get("salary"), i["alternate_url"]]
    name = i["name"]
    salary = i.get("salary")
    url = i["alternate_url"]
    requirements
    list.append(sl)

for i in list:
    print(i)
print(len(list))

#class Vacancy():
 #   """ Vacancy class """
  #  def __int__(self):
