# Import necessary modules
import os  # For file and directory operations
import time  # For timestamping screenshots
import threading  # For running background tasks
import tkinter as tk  # For GUI components
from tkinter import Listbox, END, Button, messagebox  # Specific GUI widgets and utilities
from PIL import ImageGrab  # For capturing screenshots
import keyboard  # For detecting keyboard events
import win32api  # For invoking Windows shell operations (like printing)

# Directory where screenshots will be saved
screenshot_dir = r"C:\Temp\screenshot"
os.makedirs(screenshot_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Function to capture a screenshot and save it to the directory
def capture_screenshot():
    timestamp = time.strftime("%m%d%Y_%H%M%S")  # Create a timestamp for the filename
    filename = f"screenshot_{timestamp}.jpg"  # Construct the filename
    filepath = os.path.join(screenshot_dir, filename)  # Full path to save the screenshot
    screenshot = ImageGrab.grab()  # Capture the screen
    screenshot.save(filepath, "JPEG")  # Save the screenshot as a JPEG file
    listbox.insert(END, filename)  # Add the filename to the GUI listbox

# Function to monitor the Print Screen key in the background
def monitor_key():
    while True:
        keyboard.wait('print screen')  # Wait for the Print Screen key to be pressed
        capture_screenshot()  # Capture screenshot when key is pressed

# Function to print the selected screenshot from the listbox
def print_selected():
    selected = listbox.curselection()  # Get the selected item index
    if not selected:
        messagebox.showwarning("No Selection", "Please select a screenshot to print.")
        return
    filename = listbox.get(selected[0])  # Get the filename from the listbox
    filepath = os.path.join(screenshot_dir, filename)  # Full path of the selected file
    try:
        win32api.ShellExecute(0, "print", filepath, None, ".", 0)  # Send the file to the default printer
    except Exception as e:
        messagebox.showerror("Print Error", f"Failed to print the file.\n{e}")  # Show error if printing fails

# GUI setup using Tkinter
root = tk.Tk()
root.title("Screenshot Capturer")  # Set window title

# Create a listbox to display saved screenshots
listbox = Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

# Populate the listbox with existing screenshots in the directory
for file in sorted(os.listdir(screenshot_dir)):
    if file.lower().endswith(".jpg"):
        listbox.insert(END, file)

# Add buttons for capturing, printing, and quitting
Button(root, text="Capture Screenshot", command=capture_screenshot).pack(pady=5)
Button(root, text="Print Selected", command=print_selected).pack(pady=5)
Button(root, text="Quit", command=root.quit).pack(pady=5)

# Start a background thread to monitor the Print Screen key
threading.Thread(target=monitor_key, daemon=True).start()

# Minimize the window when the application starts
root.update_idletasks()
root.iconify()

# Start the Tkinter event loop
root.mainloop()
