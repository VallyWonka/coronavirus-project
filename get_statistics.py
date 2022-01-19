import os
from collections import defaultdict
from getting_statistics_pipeline import (
    save_data,
    load_data,
    get_tokens,
    count_unique,
    count_all,
    count_raw_frequency,
    count_ipm,
    sort_by_value,
    merge_dictionaries
)

DATA_PATH = "data_preprocessed"
SAVE_PATH = "stats"

# parse preprocessed texts
os.mkdir(SAVE_PATH)
save_data(get_tokens(DATA_PATH), f"{SAVE_PATH}/tokens_per_wave.json")
tokens = load_data(f"{SAVE_PATH}/tokens_per_wave.json")

# count tokens per wave
quantity = defaultdict(int)
unique_quantity = defaultdict(int)
for key, value in tokens.items():
    quantity[key] = count_all(value)
    unique_quantity[key] = count_unique(value)
save_data(quantity, f"{SAVE_PATH}/number_of_non_unique_tokens.json")
save_data(unique_quantity, f"{SAVE_PATH}/number_of_unique_tokens.json")

# count raw frequencies of tokens per wave
raw_frequencies = {key: count_raw_frequency(value) for key, value in tokens.items()}
for key, value in raw_frequencies.items():
    save_data(sort_by_value(value), f"{SAVE_PATH}/{key}_raw.json")

# count ipm of tokens per wave
ipm_frequencies = {key: {token: count_ipm(value[token], quantity[key]) for token in value}
                   for key, value in raw_frequencies.items()}
for key, value in ipm_frequencies.items():
    save_data(sort_by_value(value), f"{SAVE_PATH}/{key}_ipm.json")

# merge raw frequencies
raw_frequencies_all = merge_dictionaries(dict(value) for value in raw_frequencies.values())
save_data(sort_by_value(raw_frequencies_all), f"{SAVE_PATH}/all_waves_raw.json")

# count ipm
corpus_size = sum(quantity.values())
ipm_frequencies_all = {key: {token: count_ipm(value[token], corpus_size) for token in value}
                       for key, value in raw_frequencies.items()}
for key, value in ipm_frequencies.items():
    save_data(sort_by_value(value), f"{SAVE_PATH}/all_waves_ipm.json")
