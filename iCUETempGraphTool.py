import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import os
import matplotlib.ticker as ticker

# Ask the user to select a CSV file using a file dialog
print("[MESSAGE] Please select a CSV file.")
file_path = filedialog.askopenfilename(title="Select CSV file")

# If the user cancels the file dialog, exit the program
if not file_path:
    print("[ERROR] No file selected, Exiting.")
    exit()
 
    

# Define the date format used in the CSV file
date_format = "%m/%d/%Y %H:%M:%S %p"

# Define ColumnsDefined
ColumnsComplete = 0

# Read the CSV file into a DataFrame and parse the "Timestamp" column as dates
df = pd.read_csv(file_path, parse_dates=["Timestamp"])

# Get a list of columns in the DataFrame to create plots for
columns_to_plot = df.columns[1:]

# Define and print column and row amount
ColumnAmount = len(columns_to_plot)
RowAmount = df.shape[0]
FileSize = os.path.getsize(file_path)
print(f'[DEBUG] There are {ColumnAmount} columns in the CSV file.')
print(f'[DEBUG] There are {RowAmount} rows in the CSV file.')
print(f'[DEBUG] The file is {FileSize}b in size.')

# Ask the user to select an output directory using a directory dialog
print("[MESSAGE] Please select a output folder.")
output_directory = filedialog.askdirectory(title="Select Output Directory")

# If the user cancels the directory dialog, exit the program
if not output_directory:
    print("[ERROR] No folder selected, Exiting.")
    exit()

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
    
    # Increment ColumnsComplete so that the print command will show when each column is complete.
    ColumnsComplete += 1
    print(f'[DEBUG] Column {ColumnsComplete} Complete')
    
    # Generate the filename for the saved plot
    filename = f"{column.replace(' ', '_')}.png"
    save_path = os.path.join(output_directory, filename)

    # Save the plot as an image file
    plt.savefig(save_path)

    # Close the current plot to free up resources
    plt.close()

# Inform the user that the graphs have been saved successfully
print("[SUCCESS] Graphs saved successfully.")


# The comments were added by an AI because I am horrible at leaving code comments.
