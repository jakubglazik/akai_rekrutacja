import json


class Importer:
    tasks = []

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        try:
            with open("taski.json", 'r') as json_file:
                self.tasks = json.load(json_file)
        except IOError:
            print("Błąd odczytu danych z pliku.")
        pass

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.tasks
        pass