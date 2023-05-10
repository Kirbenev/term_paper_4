class Vacancy:


    def __init__(self, name, url, salary, requirements):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirements = requirements

    def __repr__(self):
        return f'{self.name}, {self.url }, {self.salary }, {self.requirements}\n'


    def __lt__(self, objeckt_2):
        return self.salary < objeckt_2.salary

    def __le__(self, objeckt_2):
        return self.salary <= objeckt_2.salary

    def __gt__(self, objeckt_2):
        return self.salary > objeckt_2.salary

    def __ge__(self, objeckt_2):
        return self.salary >= objeckt_2.salary

    def __eq__(self, objeckt_2):
        return self.salary == objeckt_2.salary