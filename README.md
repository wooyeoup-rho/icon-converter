# ICO Converter
Simple app that allows users to drag and drop images and convert them into .ico files.

- Choose from standard icon sizes (16, 32, 64, 128, and 256)
- Drag and drop functionality
- .ico file created under same directory as image

## Disclaimer
The application *may be flagged as malicious* by certain security vendors and antivirus programs (11/70 on VirusTotal).

This is a false positive likely due to:
- The executable being unsigned
- Application's file-writing capabilities
- PyInstaller packaging everything in to one executable

**The application does not transmit any data. You are encouraged to inspect the code and build it yourself. Steps below.**

---
### Download the executable:
- You can download the precompiled executable directly (Windows):
[Download](https://github.com/wooyeoup-rho/icon-converter/releases/download/v1.0/icon-converter.exe)

- Or check out the releases page:
[Icon converter releases](https://github.com/wooyeoup-rho/icon-converter/releases/tag/v1.0)

---
### Requirements
1. Python
2. PyInstaller (For creating the executable)

### Installation
Clone the repository:

```commandline
git clone https://github.com/wooyeoup-rho/icon-converter.git
```

### Running the application:
```commandline
cd icon-converter
python main.py
```

### Creating an executable
1. Install PyInstaller
```commandline
pip install pyinstaller
```
2. Create the executable:
```commandline
pyinstaller --onefile --add-data "assets;assets" --name icon-converter --windowed --icon=assets/images/icon.ico main.py --additional-hooks-dir=.
```
- `--onefile` bundles everything into a single executable.
- `--add-data "assets;assets"` includes everything in the `assets` file into the executable.
- `--name icon-converter` names the executable file.
- `--windowed` prevents a command-line window from appearing.
- `--icon=assets/images/icon.ico` specifies the application icon.
- `main.py` specifies the Python script to bundle.
- `--additional-hooks-dir=.` specifies hook file for tkinterdnd2

3. Locate and run the executable:

The executable will be located in the `dist` folder. You can now open the `icon-converter.exe` inside to open the application.
