import json
import time
class Datareader:

    @staticmethod
    def jason_parser(file_path):
        with open(file_path,"r") as file:
            return json.load(file)
    @staticmethod
    def generate_email():
        return f"kartik{int(time.time())}@gmail.com"