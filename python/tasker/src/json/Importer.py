import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open("taski.json", "r") as f:
            self.data = json.load(f)
        f.close()
            
    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.data
