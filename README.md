# xbpm-models

**xbpm-models** is a Python library for defining and analyzing X-ray Beam Position Monitors (XBPMs) across various geometries and materials. It provides modular classes, material definitions, and calculation routines to help beamline scientists and engineers prototype new XBPM designs, compare performance, and integrate custom materials.

## Features

- **Modular Geometry Classes**  
  - Predefined sensor types (blade-style, quadrant, custom electrode layouts)  
  - Parameterized dimensions (length, width, gap spacing) and orientation  

- **Material Definitions**  
  - Built-in entries for commonly used substrates (diamond, silicon, metal alloys)  
  - Material properties: density, absorption coefficient, thermal conductivity, electron yield  

- **Calculation Routines**  
  - Photocurrent generation algorithms  
  - Spatial resolution estimates based on beam-size and charge distribution  
  - Simple thermal load approximations

- **Example Scripts & Notebooks**  
  - Demonstrations of instantiating multiple XBPM configurations  
  - Parameter sweeps over material or geometry variables  
  - Plotting predicted signal outputs using NumPy + Matplotlib  

---
