# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class JsonFunction(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////
    # json_file = "gui/settings.json"
    # app_path = os.path.abspath(os.getcwd())
    # file_path = os.path.normpath(os.path.join(app_path, json_file))
    # if not os.path.isfile(file_path):
    #     print(f"WARNING: \"settings.json\" not found! check in the folder {file_path}")

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self, file_path):
        super(JsonFunction, self).__init__()
        self.file_path = file_path

        if not os.path.isfile(file_path):
            raise ValueError(f"WARNING: \"settings.json\" not found! check in the folder {file_path}")

        # DICTIONARY WITH SETTINGS
        # Just to have objects references
        self.items = {}

        # DESERIALIZE
        self.deserialize()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        # WRITE JSON FILE
        with open(self.file_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4, ensure_ascii=False)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        # READ JSON FILE
        with open(self.file_path, "r", encoding='utf-8') as reader:
            json_data = json.loads(reader.read())
            self.items = json_data
