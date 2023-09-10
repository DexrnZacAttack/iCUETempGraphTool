import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
import os

# user chooses CSV file to be read
file_path = filedialog.askopenfilename(title="Select CSV file")
if not file_path:
    exit()

df = pd.read_csv(file_path)

# set timestamp as index
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

# make user select output directory
output_directory = filedialog.askdirectory(title="Select Output Directory")
if not output_directory:
    exit()

# select columns to plot
columns_to_plot = df.columns[1:]

# plot graphs
for column in columns_to_plot:
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df[column])
    plt.title(f'{column} over Time')
    plt.xlabel('Timestamp')
    plt.ylabel(column)
    plt.grid(True)
    plt.tight_layout()

    # generate the filename based on the column name
    filename = f"{column.replace(' ', '_')}.png"
    save_path = os.path.join(output_directory, filename)

    plt.savefig(save_path)
    plt.close()

print("Graphs saved successfully.")
