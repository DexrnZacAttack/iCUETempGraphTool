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

# plot graphs
devices = df.columns[1:]  # exclude timestamp option
for device in devices:
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df[device].str.rstrip('°C').astype(float))
    plt.title(f'Temperature for {device}')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.tight_layout()

    # generate filename based on the device name from the CSV file
    filename = f"{device.replace(' ', '_')}_temperature.png"
    save_path = os.path.join(output_directory, filename)

    plt.savefig(save_path)
    plt.close()

print("Graphs saved successfully.")
