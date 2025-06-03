# xbpm-models

**xbpm-models** is a Python library for defining and analyzing X-ray Beam Position Monitors (XBPMs) across various geometries and materials. It provides modular classes, material definitions, and calculation routines to help beamline scientists and engineers prototype new XBPM designs, compare performance, and integrate custom materials.

---

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Repository Structure](#repository-structure)  
- [Usage](#usage)  
  - [Defining an XBPM Geometry](#defining-an-xbpm-geometry)  
  - [Setting Material Properties](#setting-material-properties)  
  - [Running Calculations](#running-calculations)  
  - [Example Scripts](#example-scripts)  
- [Development](#development)  
  - [Adding a New Geometry](#adding-a-new-geometry)  
  - [Adding a New Material](#adding-a-new-material)  
- [Dependencies](#dependencies)  
- [Contributing](#contributing)  
- [License](#license)  

---

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
  - Simple thermal load approximations (steady-state heating)  

- **Example Scripts & Notebooks**  
  - Demonstrations of instantiating multiple XBPM configurations  
  - Parameter sweeps over material or geometry variables  
  - Plotting predicted signal outputs using NumPy + Matplotlib  

---
