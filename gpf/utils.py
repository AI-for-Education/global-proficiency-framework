import hashlib

from .item_generation import Item, Question


def hash_stimulus(item: Item):
    newitem = item.model_copy()
    newitem.questions = []
    json_data = newitem.model_dump_json().encode("utf-8").decode("unicode_escape")
    normalized_data = json_data.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized_data.encode("utf-8")).hexdigest()


def hash_question(question: Question):
    json_data = question.model_dump_json().encode("utf-8").decode("unicode_escape")
    normalized_data = json_data.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized_data.encode("utf-8")).hexdigest()
