from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def save(self):
        return super().save()

    def to_dict(self):
        # Exclui o campo '_id' do dicionário retornado
        data_copy = self.data.copy()
        data_copy.pop('_id', None)
        return data_copy

    @classmethod
    def list_dicts(cls):
        languages = cls._collection.find()
        return [
            cls.remove_id_from_document(language) for language in languages
        ]

    @classmethod
    def remove_id_from_document(cls, document):
        document.pop('_id', None)
        return document
