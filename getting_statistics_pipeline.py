import os
import json
from collections import defaultdict, Counter
from typing import List, Iterable


def save_data(data: dict, path: str):
    with open(path, "w", encoding="utf-8") as fw:
        json.dump(data, fw, ensure_ascii=False, indent=4)


def load_data(path: str):
    with open(path, "r", encoding="utf-8") as fr:
        return json.load(fr)


def get_tokens(path: str):
    tokens = defaultdict(list)
    for directory in os.listdir(path):
        for file in os.listdir(f"{path}/{directory}"):
            with open(f"{path}/{directory}/{file}", "r", encoding="utf-8") as fr:
                tokens[directory].extend(fr.read().split(" "))
    return tokens


def count_all(data: list):
    return len(data)


def count_unique(data: list):
    return len(set(data))


def count_raw_frequency(data: list):
    return Counter(data)


def count_ipm(raw_frequency: int, corpus_size: int):
    return raw_frequency / corpus_size * 1000000


def sort_by_value(data: dict):
    return dict(sorted(data.items(), key=lambda x: -x[1]))


def merge_dictionaries(args: Iterable[dict]):
    merged_dictionary = {}
    for dictionary in args:
        for key, value in dictionary.items():
            if not key in merged_dictionary:
                merged_dictionary[key] = value
            else:
                merged_dictionary[key] += value
    return merged_dictionary
