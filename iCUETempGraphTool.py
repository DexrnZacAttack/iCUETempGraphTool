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
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df[column])
    ax.set_title(f'{column} over Time')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel(column)
    ax.grid(True)

    # idek how to explain this lmao
    ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=6))  # adjust number of ticks as needed

    # generate the filename based on the column name
    filename = f"{column.replace(' ', '_')}.png"
    save_path = os.path.join(output_directory, filename)

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

print("Graphs saved successfully.")
