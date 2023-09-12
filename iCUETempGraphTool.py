import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import os
import matplotlib.ticker as ticker

# Ask the user to select a CSV file using a file dialog
file_path = filedialog.askopenfilename(title="Select CSV file")

# If the user cancels the file dialog, exit the program
if not file_path:
    exit()

# Define the date format used in the CSV file
date_format = "%m/%d/%Y %H:%M:%S %p"

# Read the CSV file into a DataFrame and parse the "Timestamp" column as dates
df = pd.read_csv(file_path, parse_dates=["Timestamp"])

# Ask the user to select an output directory using a directory dialog
output_directory = filedialog.askdirectory(title="Select Output Directory")

# If the user cancels the directory dialog, exit the program
if not output_directory:
    exit()

# Get a list of columns in the DataFrame to create plots for
columns_to_plot = df.columns[1:]

# Loop through each column and create a plot
for column in columns_to_plot:
    # Create a new figure for each plot with specified dimensions
    plt.figure(figsize=(12, 6))

    # Plot the data using the "Timestamp" column as x-axis and the current column as y-axis
    plt.plot(df['Timestamp'], df[column])

    # Set the title, x-axis label, and y-axis label for the plot
    plt.title(f'{column} over Time')
    plt.xlabel('Timestamp')
    plt.ylabel(column)

    # Add a grid to the plot
    plt.grid(True)

    # Adjust the layout of the plot
    plt.tight_layout()

    # Format the x-axis labels as dates
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%m/%d/%Y %H:%M:%S %p'))

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=10)

    # Get unique labels from the current column and sort them numerically
    y_labels = df[column].unique()
    sorted_y_labels = sorted(y_labels, key=lambda label: float(''.join(filter(str.isdigit, label))))

    # Configure the y-axis tick locations and labels
    loc = ticker.MultipleLocator(base=max(1, len(sorted_y_labels) // 10))
    plt.gca().yaxis.set_major_locator(loc)
    plt.gca().set_yticklabels(sorted_y_labels)

    # Generate the filename for the saved plot
    filename = f"{column.replace(' ', '_')}.png"
    save_path = os.path.join(output_directory, filename)

    # Save the plot as an image file
    plt.savefig(save_path)

    # Close the current plot to free up resources
    plt.close()

# Inform the user that the graphs have been saved successfully
print("Graphs saved successfully.")


# The comments were added by an AI because I am horrible at leaving code comments.
