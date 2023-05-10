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
vacancies = []



for i in d:
 #   sl = [i["name"], i.get("salary"), i["alternate_url"]]
    name = i["name"]
    salary = i.get("salary")
    print(type(salary))
    url = i["alternate_url"]
    requirements = i.get('snippet')
    requirementss = requirements.get('requirement')
    vacancies.append(Vacancy(name, url, salary, requirementss))

print(vacancies)

#class Vacancy():
 #   """ Vacancy class """
  #  def __int__(self):
