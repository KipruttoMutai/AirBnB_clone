#!/usr/bin/python3
"""
module: file_storage.py
resources: class FileStorage
"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """creates FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """returns the stored dictionary"""
        return FileStorage.__objects

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        all_objs = FileStorage.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects only if the file path exist
        does nothing  If the file doesn’t exist.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

