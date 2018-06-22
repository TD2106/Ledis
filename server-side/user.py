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
        player_info = dict(user_name=user_name, password=password)
        with open(str(path) + "\\json" + "\\" + user_name + ".json", "w") as user_json:
            json.dump(player_info, user_json, indent=2)

    def __init__(self, user_name):
        self.json_path = str(path) + "\\json" + "\\" + user_name + ".json"
        with open(self.json_path, "r") as user_json:
            self.user_info = json.load(user_json)

    def add_key_string(self, key, value):
        self.user_info[key] = value

    def add_key_list(self, key, value):
        if self.user_info[key] is None:
            self.user_info[key] = []
        elif not isinstance(self.user_info[key], list):
            return "Not a list"
        self.user_info[key].append(value)
        return value

    def get_list_length(self, key):
        if self.user_info[key] is None:
            self.user_info[key] = []
        elif not isinstance(self.user_info[key], list):
            return "Not a list"
        return self.user_info[key].length

    def get_list_element(self, start, end, key):
        if start < 0 or end < 0 or start > end or not isinstance(self.user_info[key], list) or end >= self.user_info[key].length :
            return "Not good input"
        else:
            result = []
            for i in range(start, end + 1):
                result.append(self.user_info[key])
            return result

    def add_list_element(self, key, values):
        for value in values:
            self.user_info[key].append(value)

    def lpop(self, key):
        if not isinstance(self.user_info[key], list):
            return "Not a list"
        return self.user_info[key].pop(0)

    def rpop(self, key):
        if not isinstance(self.user_info[key], list):
            return "Not a list"
        return self.user_info[key].pop()

    def save_progress(self):
        with open(self.json_path, "w") as user_json:
            json.dump(self.user_info, user_json, indent=2)
