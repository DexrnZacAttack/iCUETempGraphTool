import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
import os
from dateutil import parser

# user chooses CSV file to be read
file_path = filedialog.askopenfilename(title="Select CSV file")
if not file_path:
    exit()

# specify date and time formats to handle both 12-hour and 24-hour time formats
date_formats = ["%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S"]

# attempt to parse Timestamp using different date formats
df = None
for date_format in date_formats:
    try:
        df = pd.read_csv(file_path, parse_dates=["Timestamp"], date_format=date_format)
        break  # successfully parsed
    except pd.errors.OutOfBoundsDatetime:
        pass  # continue to the next format if parsing fails

# check if parsing was successful
if df is None:
    print("Unable to parse the 'Timestamp' column. Please check the date format in your CSV file.")
    exit()

# make user select output directory
output_directory = filedialog.askdirectory(title="Select Output Directory")
if not output_directory:
    exit()

# select columns to plot but excluding the timestamp
columns_to_plot = df.columns[1:]

# create new figure for every column and save them all seperately
for column in columns_to_plot:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Timestamp'], df[column])
    ax.set_title(f'{column} over Time')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel(column)
    ax.grid(True)

    # rotate bottom time labels for better readability
    plt.xticks(rotation=45)

    
    ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=6))  # adjust the number of ticks as needed

    # generate the filename based on the column name
    filename = f"{column.replace(' ', '_')}.png"
    save_path = os.path.join(output_directory, filename)

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

print("Graphs saved successfully.")
