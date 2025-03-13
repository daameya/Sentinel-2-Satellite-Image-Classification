# Sentinel-2-Satellite-Image-Classification
The Sentinel-2 satellite images are openly and freely accessible provided in the Earth observation program Copernicus. We provide benchmarks for this novel dataset with its spectral bands using state-of-the-art deep Convolutional Neural Network (CNNs).

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/daameya/Sentinel-2-Satellite-Image-Classification.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n satellite python=3.8 -y
```

```bash
conda activate satellite
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```