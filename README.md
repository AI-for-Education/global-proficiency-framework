# Digitizing the Global Proficiency Framework

The [Global Proficiency Framework](https://www.edu-links.org/resources/global-proficiency-framework-reading-and-mathematics) describes the global minimum proficiency levels expected of students in grades one to nine in reading and mathematics. This is presented in the form of a detailed long-form PDF document outlining the structure of the framework with example assessment items. For reading, the framework contains a systematic characterisation of skills, in a heirarchy of constructs and subconstructs, across three domains (Comprehension, Decoding and Reading). 

This repository contains a digitized version of the GPF for Reading, including the example assessment items, to support and enable development of computational tools based on this framework.

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

### Data format

[Pydantic](https://docs.pydantic.dev/latest/) types for the GPF data are defined in [gpf/gpf_item.py](gpf/gpf_item.py). These can be accessed through the `DataLoader` class in [gpf/item_generation.py](gpf/item_generation.py). See [scripts/demo_load_data.py](scripts/demo_load_data.py) for an example. `data/gpf-reading-processed` contains digitized csv versions of all the tables. 

## About the GPF for Reading

The GPF is a structured collection of foundational language skills across grades 2-9. Each skill is clearly defined and skills are organised in a heirarchy of construct and subconstruct across three domains. For example, the first skill in the reading domain is coded as *R1.1.1: Recognise the meaning of common grade-level words*. This skill applies to all grade levels 2-9. In this case, it is the only skill under subconstruct *R1.1*, which is part of construct *R1: Retrieve information*. This example illustrates the heirarchical structure of skills, but also the interdependence between the grade-level of the material and the definition of the skill. 

### Heirarchical structure of GPF Reading Skills

<table class=" lightable-paper" style='color: black; font-family: "Arial Narrow", arial, helvetica, sans-serif; width: auto !important; margin-left: auto; margin-right: auto;'>

 <thead>

<tr>

<th style="empty-cells: hide;border-bottom:hidden;" colspan="3"></th>

<th style="border-bottom:hidden;padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="9"><div style="border-bottom: 1px solid #ddd; padding-bottom: 5px; ">Grade</div></th>

</tr>

  <tr>

   <th style="text-align:left;"> Domain </th>

   <th style="text-align:left;"> Construct </th>

   <th style="text-align:left;"> Subconstruct </th>

   <th style="text-align:left;"> 1 </th>

   <th style="text-align:left;"> 2 </th>

   <th style="text-align:left;"> 3 </th>

   <th style="text-align:left;"> 4 </th>

   <th style="text-align:left;"> 5 </th>

   <th style="text-align:left;"> 6 </th>

   <th style="text-align:left;"> 7 </th>

   <th style="text-align:left;"> 8 </th>

   <th style="text-align:left;"> 9 </th>

  </tr>

 </thead>

<tbody>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 22em; min-width: 22em; vertical-align: middle !important;" rowspan="4"> Comprehension of spoken or signed language </td>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; vertical-align: middle !important;" rowspan="2"> Retrieve information at word level </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Comprehend spoken and signed language at the word or phrase level </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Recognize the meaning of common grade-level words in a short, grade-level continuous text read to or signed for the learner </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; "> Retrieve information at sentence or text level </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Retrieve explicit information in a short grade-level continuous text read to or signed for the learner </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; "> Interpret information at sentence or text level </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Interpret information in a short grade-level continuous text read to or signed for the learner </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 22em; min-width: 22em; vertical-align: middle !important;" rowspan="3"> Decoding </td>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; vertical-align: middle !important;" rowspan="2"> Precision </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Identify symbol-sound/fingerspelling and/or symbol-morpheme correspondences </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Decode isolated words </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; "> Fluency </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Say or sign a grade-level continuous text at pace and with accuracy </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 22em; min-width: 22em; vertical-align: middle !important;" rowspan="10"> Reading comprehension </td>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; vertical-align: middle !important;" rowspan="3"> Retrieve information </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Recognize the meaning of common grade-level words </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Retrieve explicit information in a grade-level text by direct- or close-word matching </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Retrieve explicit information in a grade-level text by synonymous word matching </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; vertical-align: middle !important;" rowspan="3"> Interpret information </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Identify the meaning of unknown words and expressions in a grade-level text </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Make inferences in a grade-level text </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Identify the main and secondary ideas in a grade-level text </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 20em; min-width: 15em; vertical-align: middle !important;" rowspan="4"> Reflect on information </td>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Identify the purpose and audience of a text </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Evaluate a text with justification </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Evaluate the status of claims made in a text </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

  <tr>

   <td style="text-align:left;font-size: 10px;width: 50em; min-width: 15em; "> Evaluate the effectiveness of a text </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; ">  </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

   <td style="text-align:left;font-size: 10px;width: 3em; "> X </td>

  </tr>

</tbody>

</table>

Each skill is defined for three different levels of acheivement: *partially meets* (P), *meets* (M), or *exceeds* (E).
Difference subconstructs have different numbers of skills. The distribution of skills across the heirarchy is illustrated below with red circles:

![Hierarchical structure of GPF](plots/overview-tree-counts.svg)

The digitized table of skills is available at [data/gpf-reading-processed/read-skills.csv](data/gpf-reading-processed/read-skills.csv) (after running `dvc pull`).

## Assessing GPF Reading Skills

The purpose of carefully defining this structured heirarchy of skills is to inform assessment and better understand student reading acheivements. The GPF document includes example assessment items to illustrate how each skill would be assessed. However, the GPF is not a test instrument; most skills have only one or two example items, and some skills don't have any. These are illustrative examples to help expert raters align or design assesments for the specific GPF skills, so results from different contexts and countries can be compared (for example, percentage of students at grade 4 who meet or exceed a certain skill).

### GPF example assessments

We have extracted all the example assessment questions. Each stimulus text is represented as an `Item` object. There are 29 example stimulus items in the GPF:

```python
from gpf.item_generation import DataLoader

dl = DataLoader()
items = dl.get_items()
print(f"Loaded {len(items)} items")
```

Each `Item` object holds a list of all the questions for that text in the `questions` attribute. The questions can also be loaded directly. There are 243 questions. 

```python
all_questions = get_all_items_flat()
print(f"Loaded {len(all_questions)} questions")
```

### Grade level text definitons

The submodule `gpf.grade_defs` includes the parts of Appendix B which deal with establishing the grade level of an assessment text. 

```python
from gpf.grade_defs import (
    feature_tables_by_grade, # dict with keys [2, 3, 6, 9]
    feature_table, # combined feature table with rows for each feature
    appendix_b_intro_text, # introduction text to appendix B
    grade_text_descriptions, # additional text descriptions of grade levels
)
```