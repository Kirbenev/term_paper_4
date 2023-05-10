from abc import ABC, abstractmethod

class GeneralAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    def __init__(self):
        self.get_vacancies()





