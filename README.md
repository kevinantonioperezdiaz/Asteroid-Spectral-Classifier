# Asteroid Spectral Classifier (Bus-DeMeo System)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain: Planetary Science](https://img.shields.io/badge/Domain-Planetary%20Science%20%26%20Spectroscopy-orange.svg)](#)

An automated scientific software tool designed for the spectral classification of minor Solar System bodies based on the **Bus-DeMeo taxonomic system** (DeMeo et al., 2009). The application processes observational reflectance spectra stored in astronomical FITS formats, normalizes continuum features, and assigns spectral classes via minimum distance metrics in functional space, featuring an automated diagnostic PDF reporting engine.

---

## Scientific Overview & Taxonomy

Spectroscopic taxonomy provides direct insights into the mineralogical composition, surface weathering, and evolutionary history of asteroids. The **Bus-DeMeo taxonomic system** classifies reflectance spectra across the visible to near-infrared wavelength range (0.45 to 2.45 $\mu\text{m}$), identifying 24 distinct spectral classes organized into major complexes:

- **S-Complex (Siliceous):** Inner belt objects showing pronounced 1 $\mu\text{m}$ and 2 $\mu\text{m}$ absorption bands due to olivine and pyroxene (S, Sa, Sq, Sr, Sv).
- **C-Complex (Carbonaceous):** Volatile-rich and primitive outer-belt bodies displaying low albedos and relatively flat or reddish featureless spectra (C, Cb, Cg, Cgh, Ch).
- **X-Complex (Metallic & Enstatite-rich):** Featureless spectra characterized by continuous slope variations (X, Xc, Xe, Xk).
- **End-member Classes:** Highly specialized mineralogies, including basaltic/Vesta-like surfaces (V-type), extremely red D/T-types, and olivine-dominated A-types.

---

## Pipeline Architecture & Methods

```
  [ Observational Spectrum (FITS) ]
                 │
                 ▼
     [ Astropy FITS Parser ] ──────> Extract Wavelength (λ) & Reflectance (R)
                 │
                 ▼
 [ Continuum Spline / Resampling ] ──> Match Grid with Bus-DeMeo Standard Templates
                 │
                 ▼
 [ Spectral Metric Evaluation ] ────> Compute Least-Squares Residuals / MSE
                 │
                 ▼
  ┌──────────────────────────────┴──────────────────────────────┐
  ▼                                                             ▼
[ Interactive Visualization (Tk/Matplotlib) ]     [ Comprehensive PDF Synthesis (ReportLab) ]
```

### 1. Data Ingestion & Wavelength Alignment
Spectroscopic tables are read from standard FITS formats using `astropy.io.fits`. Observational channels are aligned and resampled to the standard Bus-DeMeo template grid using spline interpolation to ensure scale invariance at 0.55 $\mu\text{m}$.

### 2. Metric Assignment (v1 Baseline)
The current production version evaluates the functional distance between the normalized observed spectrum $R_{\text{obs}}(\lambda)$ and each reference template $R_{\text{ref}, k}(\lambda)$:

$$\text{MSE}_k = \frac{1}{N} \sum_{i=1}^N \left[ R_{\text{obs}}(\lambda_i) - R_{\text{ref}, k}(\lambda_i) \right]^2$$

The predicted class corresponds to $\arg\min_k (\text{MSE}_k)$, providing a transparent, deterministic baseline.

---

## Graphical User Interface & Reporting

The software includes a standalone graphical environment (`gui.py`) constructed with Tkinter and Matplotlib:
- **Interactive Inspection:** Side-by-side comparison of the target spectrum with best-fit templates, displaying residual margins and top taxonomic matches.
- **Automated Reporting:** Generates publication-ready PDF summaries (`src/report_generator.py`) containing metadata headers, best-fit classes, quantitative deviation metrics, and diagnostic plots.
- **Portability:** Configured with `PyInstaller` specifications (`gui.spec`) to build self-contained executables across desktop environments.

---

## Repository Structure

```bash
Asteroid-Spectral-Classifier/
├── data/
│   ├── demeo/                   # 24 Bus-DeMeo reference spectral templates (FITS)
│   └── examples/                # Benchmark asteroid spectra for validation
├── src/
│   ├── classifier.py            # Optimization routines and spectral distance algorithms
│   ├── fits_loader.py           # Astropy-based spectral ingestion engine
│   ├── plotter.py               # Scientific plotting tools
│   ├── report_generator.py      # Automated PDF generation with ReportLab
│   └── taxonomy.py              # Class definitions and taxonomic metadata
├── gui.py                       # Graphical user interface application
├── main.py                      # Headless CLI entry point
├── gui.spec                     # PyInstaller distribution configuration
├── requirements.txt             # Scientific software dependencies
└── README.md                    # Project documentation
```

---

## Installation & Execution

### Prerequisites
Clone the repository and install dependencies:

```bash
git clone https://github.com/kevinantonioperezdiaz/Asteroid-Spectral-Classifier.git
cd Asteroid-Spectral-Classifier
pip install -r requirements.txt
```

### Run Graphical Interface
Launch the interactive classification environment:

```bash
python gui.py
```

### Build Standalone Executable
Compile a platform-independent binary:

```bash
python -m PyInstaller --onefile --windowed --add-data "data;data" --hidden-import=tkinter --hidden-import=matplotlib.backends.backend_tkagg gui.py
```

---

## Roadmap & Planned Deep Learning Extensions (v2)

To scale beyond deterministic template matching toward large-scale survey pipelines (e.g., Vera C. Rubin Observatory / LSST, Gaia DR3), the next release cycle incorporates:
- **Deep Neural Classifiers:** 1D Convolutional Neural Networks (1D-CNN) and Residual Multi-Layer Perceptrons (MLP) trained on synthetic and noisy real spectra to capture subtle continuum inflections and mineralogical absorption profiles.
- **Uncertainty Quantification:** Bayesian neural layers / Monte Carlo Dropout to produce calibrated class probability vectors rather than rigid point assignments.
- **Photometric-to-Spectroscopic Inversion:** Neural mapping from multi-band photometric colors directly into Bus-DeMeo latent representations.

---

## Author & Academic Context

**Kevin Antonio Pérez Díaz**  
*Electronic Engineer | Master's Student in Astronomy & Astrophysics*  
Repository: [github.com/kevinantonioperezdiaz](https://github.com/kevinantonioperezdiaz)

---

## References

1. DeMeo, F. E., Binzel, R. P., Slivan, S. M., & Bus, S. J. (2009). *An extension of the Bus asteroid taxonomy into the near-infrared*. Icarus, 202(1), 160-180.
2. Bus, S. J., & Binzel, R. P. (2002). *Phase II of the Small Main-Belt Asteroid Spectroscopic Survey: A feature-based taxonomy*. Icarus, 158(1), 146-177.
