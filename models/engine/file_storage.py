#!/usr/bin/python3
"""Module that contain file storage class"""
from models.base_model import BaseModel
from models.user import User
import os.path
import json

class FileStorage():
    """FileStorage    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all        """
        return FileStorage.__objects

    def new(self, obj):
        """new
        Args:
            obj ([type]): [description]
        """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """save     """
        d = {}
        for key, obj in FileStorage.__objects.items():
            d[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            json.dump(d, json_f)

    def reload(self):
        """reload        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as js_f:
                for key, obj in json.loads(js_f.read()).items():
                    obj = eval(obj['__class__'])(**obj)
                    FileStorage.__objects[key] = obj
