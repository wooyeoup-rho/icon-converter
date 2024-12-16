# ICO Converter
Simple app that allows users to drag and drop images and convert them into .ico files.

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
