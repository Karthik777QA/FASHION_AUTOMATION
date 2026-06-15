import json

class DataReader:
    @staticmethod
    def json_parser(json_file):
        with open(json_file,"r") as json_data:
            data = json.load(json_data)
            return data
