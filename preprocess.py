import os
from preprocessing_pipeline import preprocess


DATA_PATH = "data"
os.mkdir(f"{DATA_PATH}_preprocessed")


for directory in os.listdir(DATA_PATH):
    os.mkdir(f"{DATA_PATH}_preprocessed/{directory}_preprocessed")
    for file in os.listdir(f"{DATA_PATH}/{directory}"):
        with open(f"{DATA_PATH}/{directory}/{file}", "r", encoding="utf-8") as fr:
            text = fr.read()
            with open(f"{DATA_PATH}_preprocessed/{directory}_preprocessed/{file}", "w", encoding="utf-8") as fw:
                fw.write(preprocess(text))
