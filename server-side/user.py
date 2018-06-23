import json
import os
from pathlib import Path


path = os.getcwd()


class User:
    @staticmethod
    def is_login_correct(user_name, password):
        if User.is_user_name_exist(user_name):
            with open(str(path) + "\\json" + "\\" + user_name + ".json", "r") as user_json:
                player_info = json.load(user_json)
                if player_info["password"] == password:
                    return True
                else:
                    return False
        else:
            return False

    @staticmethod
    def is_user_name_exist(user_name):
        user_json = Path(str(path) + "\\json" + "\\" + user_name + ".json")
        return user_json.is_file()

    @staticmethod
    def add_user(user_name, password):
        player_info = dict(user_name=user_name, password=password, data={})
        with open(str(path) + "\\json" + "\\" + user_name + ".json", "w") as user_json:
            json.dump(player_info, user_json, indent=2)

    def __init__(self, user_name):
        self.json_path = str(path) + "\\json" + "\\" + user_name + ".json"
        with open(self.json_path, "r") as user_json:
            self.user_info = json.load(user_json)

    def add_key_string(self, key, value):
        self.user_info["data"][key] = value
        return value

    def get_key_string(self, key):
        if key in self.user_info["data"]:
            return self.user_info["data"][key]
        else:
            return "No key found"

    def add_key_list(self, key, value):
        if self.user_info["data"][key] is None:
            self.user_info["data"][key] = []
        elif not isinstance(self.user_info["data"][key], list):
            return "Not a list"
        self.user_info["data"][key].append(value)
        return value

    def get_list_length(self, key):
        if self.user_info["data"][key] is None:
            self.user_info["data"][key] = []
        elif not isinstance(self.user_info["data"][key], list):
            return "Not a list"
        return str(len(self.user_info["data"][key]))

    def get_list_element(self, start, end, key):
        if start < 0 or end < 0 or start > end or not isinstance(self.user_info["data"][key], list) or\
                end >= len(self.user_info["data"][key]) :
            return "Not good input"
        else:
            result = ""
            for i in range(start, end + 1):
                result += self.user_info["data"][key][i] + " "
            return result

    def add_list_element(self, key, values):
        if key not in self.user_info["data"]:
            self.user_info["data"][key] = []
        if not isinstance(self.user_info["data"][key], list):
            return "Wrong command"
        for value in values:
            self.user_info["data"][key].append(value)
        return self.get_list_element(0, len(self.user_info["data"][key]) - 1, key)

    def lpop(self, key):
        if not isinstance(self.user_info["data"][key], list):
            return "Not a list"
        elif len(self.user_info["data"][key]) == 0:
            return "Nothing to pop"
        return self.user_info["data"][key].pop(0)

    def rpop(self, key):
        if not isinstance(self.user_info["data"][key], list):
            return "Not a list"
        elif len(self.user_info["data"][key]) == 0:
            return "Nothing to pop"
        return self.user_info["data"][key].pop()

    def save_progress(self):
        with open(self.json_path, "w") as user_json:
            json.dump(self.user_info, user_json, indent=2)
        return "Saved"
