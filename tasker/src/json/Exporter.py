import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        try:
            with open("taski.json", 'w') as json_file:
                json.dump(tasks, json_file)
        except IOError:
            print("Błąd zapisu danych do pliku.")
        pass
