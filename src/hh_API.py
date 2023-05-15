from src.general_api import GeneralAPI
import requests

class HH_api(GeneralAPI):
    """Класс запроса вакансий на HH"""

    URL = 'https://api.hh.ru/vacancies'

    @staticmethod
    def get_region_id(region, town=None) -> str:
        """
        Получение ID региона по его названию
        :param region: название региона
        :param town: название города
        :return: id региона и id города
        """
        regions_response = requests.get('https://api.hh.ru/areas')
        for r in regions_response.json()[0]['areas']:
            if region.capitalize() in r['name']:

                # если задан город
                if town:
                    for t in r['areas']:
                        if region.capitalize() in t['name']:
                            return f"id области {region} - {r['id']}; id города {town} - {t['id']}"
                else:
                    return f"id региона {region} - {r['id']}"
        return 'Некорректный запрос'

    def get_request(self, keyword, page, area, per_page=100):
        """
        Отправка запроса на API
        :param keyword: ключевое слово (название вакансии)
        :param page: номер страницы
        :param per_page: количество вакансий на одной странице
        :param area: ID региона из справочника
        :return: json со списком вакансий
        """

        # в параметрах задана сортировка по дате и только с указанной зарплатой в рублях по России
        params = {'text': keyword,
                  'page': page,
                  'per_page': per_page,
                  'only_with_salary': True,
                  'order_by': "publication_time",
                  'area': area,
                  'currency': 'RUR'
                  }

        response = requests.get(self.URL, params=params).json()
        return response['items']

    def get_vacancies(self, keyword: str, pages, area=113):
        """
        Делает запросы, изменяя номер страницы
        :param keyword: ключевое слово (название вакансии)
        :param area: ID региона из справочника (по умолчанию 113 - Вся Россия) 1716 - Владимирская область, 1 - Москва
        2019 - Московская область, 2 - Санкт-Петербург
        :param pages: количество страниц для парсинга
        :return: список с вакансиями на соответствующей странице
        """
        # Максимальное количество вакансий для парсинга - 2000
        if pages > 20:
            raise ValueError('Вы превысили максимальное число вакансий, возможных для парсинга по API')

        vacancies = []  # список с вакансиями
        for page in range(pages):
            page = self.get_request(keyword, page, area)
            vacancies.extend(page)

        return vacancies