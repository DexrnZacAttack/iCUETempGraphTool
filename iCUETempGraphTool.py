import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import os

# user chooses CSV file to be read
file_path = filedialog.askopenfilename(title="Select CSV file")
if not file_path:
    exit()

# do not parse timestamp
df = pd.read_csv(file_path)

# make user select output directory
output_directory = filedialog.askdirectory(title="Select Output Directory")
if not output_directory:
    exit()

# select columns to plot but excluding the timestamp
columns_to_plot = df.columns[1:]

# create new figure for every column and save them all seperately
batch_size = 10 
for i in range(0, len(columns_to_plot), batch_size):
    batch_columns = columns_to_plot[i:i + batch_size]

    for column in batch_columns:
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df['Timestamp'], df[column])
        ax.set_title(f'{column} over Time')
        ax.set_xlabel('Timestamp')
        ax.set_ylabel(column)

        # rotate bottom time labels for better readability
        plt.xticks(rotation=45)

        # get the unique values in the column and sort them
        unique_values = sorted(df[column].unique())

        # set custom y-axis labels with adjusted spacing
        y_ticks = [unique_values[i] for i in range(0, len(unique_values), len(unique_values) // 10)]
        ax.set_yticks(y_ticks)

        # how to explain 2 electric boogaloo
        n = max(len(df) // 10, 1)
        ax.set_xticks(df['Timestamp'].iloc[::n])

        # disable the background grid
        ax.grid(False)

        # calculate highest and lowest value for this column
        highest_value = df[column].max()
        lowest_value = df[column].min()

        # generate file name based on the column name
        filename = f"{column.replace(' ', '_')}.png"
        save_path = os.path.join(output_directory, filename)

        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

print("Graphs saved successfully.")
