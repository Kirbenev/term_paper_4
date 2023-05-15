from src.general_api import GeneralAPI
import requests, os

class SJ_API(GeneralAPI):
    """Класс для работы с сайтом superjob"""

    # ключ для работы с superjob

    KEY = os.getenv('SJ_API_KEY')

    # адрес сайта
    URL = 'https://api.superjob.ru/2.0/vacancies/'

    def get_request(self, keyword, page, region_id, count=100):
        """
        Метод для отправки запроса на api superjob
        :param keyword: ключевое слово (название профессии)
        :param region_id: id региона (города или области) 1-Россия
        :param page: номер страницы
        :param count: количество вакансий на странице (100 вакансий)
        :return: список вакансий, соответствующих требованиям в формате json
        """
        params = {'keyword': keyword,
                  'с': region_id,
                  'sort_new (unixtime)': 1,
                  'page': page,
                  'count': count,
                  'no_agreement': 1}

        response = requests.get(self.URL, headers={'X-Api-App-Id': self.KEY},
                                params=params).json()

        return response['objects']

    def get_vacancies(self, keyword, pages, region_id=1):
        """
        Метод для организации постраничной отправки запроса
        :param keyword: ключевое слово
        :param pages: количество страниц (максимальное значение для API - 5 страниц по 100 вакансий)
        :param region_id: id региона
        :return: список вакансий, собранных с сайта superjob по ключевому слову
        """
        if pages > 5:
            pages = 5
        vacancies = []
        for page in range(pages):
            response = self.get_request(keyword, page + 1, region_id)
            vacancies.extend(response)
        return vacancies