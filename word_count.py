import pandas as pd
import numpy as np

f = open("/Users/arun/Documents/others/Python/extracted.txt", "r")
store = f.read()

cleaned_text = store.replace("🎉", "").replace("\n", " ")

split_text = cleaned_text.split(" ")

print_value = pd.value_counts(np.array(split_text))

print(print_value)

with open('count_word.txt', "w") as file2:
    file2.write(str(print_value))
