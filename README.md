# Jupyter Notebooks Presentation

This repo contains the notebooks and example data for an intro presentation on Jupyter notebooks and when they might be a useful tool.

This repo has been set up to be able to run in a number ways:
- as a poetry project. Run `poetry install` and then `poetry run jupyter notebook` to get up and running with this
- as a colab notebook. For this to work you should:
	- open Google colab
	- upload `notebook-example/notebook-example.ipynb` to colab
	- set the config param `in_colab` near the top to be True
	- follow the instructions in the notebook to get the other dependent files uploaded
- there's also a `requirements.txt` for you to use if you prefer

`notebook-example/notebook-example.ipynb` is the main file that we'll be walking through.

`notebook-example/presentation.ipynb` is a reference file that contains some tips and recommendations to help you get the most out of your notebooks.