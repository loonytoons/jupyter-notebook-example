# Jupyter Notebooks Presentation

## What are Notebooks?

Jupyter Notebooks are interactive, web-based tools that allow developers and data scientists to combine code, visualizations, and narrative text in a single document. 

They are ideal for data analysis, experimentation, and educational purposes. The notebook format enables users to write and execute code in cells, view outputs immediately, and create a narrative around their work, making it accessible and understandable for both technical and non-technical audiences. This makes Jupyter Notebooks a powerful platform for collaboration, teaching, and sharing insights.

Useful for:
- EDA (exploratory data analysis)
- creating AI model POCs
- anything where you want visibility of every step of the process or want to build up and adjust a process without needing to rerun the whole flow from the start

Less useful for:
- creating production ready code
- working on code that a number of people will want to be editing at the same time

## What's in this repo?

Notebooks and example data for an intro presentation on Jupyter notebooks and when they might be a useful tool.

This repo has been set up to be able to run in a number ways:
- as a poetry project. Run `poetry install` and then `poetry run jupyter notebook` to get up and running with this
- as a colab notebook. For this to work you should:
	- open Google colab
	- upload `notebook-example/notebook-intro.ipynb` to colab
	- set the config param `in_colab` near the top to be True
	- follow the instructions in the notebook to get the other dependent files uploaded
- there's also a `requirements.txt` for you to use if you prefer

Files:
- `notebook-example/notebook-example.ipynb` is a more complete annotated file that we'll be looking through.
- `notebook-example/notebook-tips.ipynb` is a reference file that contains some tips and recommendations to help you get the most out of your notebooks.

