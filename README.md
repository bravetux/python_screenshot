design_md_content = """# python_screenshot
Minimal Python Screenshot Utility - PrintScn Captures to Temp Folder generated using GenAI

## 📘 Design Document: Screenshot Capturer Tool

### 1. Overview
The Screenshot Capturer Tool is a lightweight Windows-based GUI application built using Python. It allows users to:

- Automatically capture screenshots when the Print Screen key is pressed.
- Manually capture screenshots via a button.
- View saved screenshots in a list.
- Print selected screenshots.
- Run silently in the background.

### 2. Technologies Used
- Python 3.x
- Tkinter – GUI framework
- PIL (Pillow) – Image capture and manipulation
- keyboard – Key event monitoring
- win32api – Windows shell operations (printing)
- threading – Background key monitoring

### 4. Functional Components

#### a. Screenshot Directory Setup
- Creates a directory `C:\\Temp\\screenshot` if it doesn't exist.
- Stores all screenshots in JPEG format with timestamped filenames.

#### b. Screenshot Capture
- Uses `ImageGrab.grab()` to capture the current screen.
- Saves the image with a timestamp.
- Updates the GUI listbox with the new filename.

#### c. Key Monitoring
- Runs a background thread that waits for the Print Screen key.
- Automatically triggers screenshot capture when the key is pressed.

#### d. GUI Interface
Displays a list of saved screenshots.  
Provides buttons for:
- Manual screenshot capture
- Printing selected screenshot
- Quitting the application

#### e. Printing Functionality
- Uses `win32api.ShellExecute` to send the selected image to the default printer.
- Handles errors gracefully with message boxes.

#### f. Startup Behavior
- Minimizes the window on launch to run unobtrusively.

### 6. Threading & Responsiveness
- Key monitoring runs in a daemon thread to avoid blocking the GUI.
- GUI remains responsive during background operations.

### 8. Limitations
- Only supports JPEG format.
- No image preview or deletion options.
- Works only on Windows due to `win32api`.
"""

# Save the markdown content to a file
with open("Screenshot_Capturer_Design_Document.md", "w") as md_file:
    md_file.write(design_md_content)

print("Markdown file 'Screenshot_Capturer_Design_Document.md' has been created successfully.")

