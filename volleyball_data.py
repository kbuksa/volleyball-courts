import pandas as pd

df = pd.read_csv('activeplacescsvs/sportshalls.csv', low_memory=False)

df[df[0"Volleyball Courts"] > 1]
