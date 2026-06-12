# Asteroid Spectral Classifier

A Python application for automatic asteroid spectral classification using the Bus-DeMeo taxonomy.

## Features

* Automatic classification of asteroid spectra from FITS files.
* Comparison with Bus-DeMeo spectral templates.
* Mean Squared Error (MSE) fitting.
* Interactive spectral plots.
* Automatic PDF report generation.
* Standalone executable generation with PyInstaller.
* Dark graphical user interface.

## Project structure

```text
Asteroid-Spectral-Classifier
│
├── data/
├── src/
├── gui.py
├── main.py
├── gui.spec
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kevinantonioperezdiaz/Asteroid-Spectral-Classifier.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the graphical interface:

```bash
python gui.py
```

## Building the executable

```bash
python -m PyInstaller --onefile --windowed --add-data "data;data" --hidden-import=tkinter --hidden-import=matplotlib.backends.backend_tkagg gui.py
```

## Methodology

The classification is based on the Bus-DeMeo taxonomy. Each observed spectrum is compared with reference spectra using the Mean Squared Error (MSE). The spectral class corresponding to the minimum error is assigned to the asteroid.

## Author

Kevin Antonio Perez Diaz

## License

MIT License
