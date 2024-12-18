# Digitizing the Global Proficiency Framework

The [Global Proficiency Framework](https://www.edu-links.org/resources/global-proficiency-framework-reading-and-mathematics) describes the global minimum proficiency levels expected of students in grades one to nine in reading and mathematics. This is presented in the form of a detailed long-form PDF document outlining the structure of the framework with example assessment items. For reading, the framework contains a systematic characterisation of skills, in a heirarchy of constructs and subconstructs, across three domains (Comprehension, Decoding and Reading). 

This repository contains a digitized version of the GPF for Reading, to support and enable development of computational tools based on this framework.

### How to use this repository

#### Python package

This repository includes an installable Python package called `gpf`. This includes the core digitized data from the GPF for Reading (Mathematics to follow in a future update), and is installable with `pip`:

- `pip install git+https://github.com/AI-for-Education/global-proficiency-framework`

#### Conda environment

We provide details for a working conda environment, which allows you to get more of the intermediate data and source material. To set up the environment:
- `conda env create -f environment.yml`
- `conda activate gpf`
- `dvc pull`
The conda environment includes [DVC](https://dvc.org/) which is used to version control data files within the repository. DVC pull will add these files to the `data/` folder. 

#### Data format

[Pydantic](https://docs.pydantic.dev/latest/) types for the GPF data are defined in [gpf/gpf_item.py](gpf/gpf_item.py). These can be accessed through the `DataLoader` class in [gpf/item_generation.py](gpf/item_generation.py). See [scripts/demo_load_data.py](scripts/demo_load_data.py) for an example. `data/gpf-reading-processed` contains digitized csv versions of all the tables. 