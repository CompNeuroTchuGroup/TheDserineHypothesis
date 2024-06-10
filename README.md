# Deciphering the astrocytic contribution to learning and relearning

This repository hosts the code used to produce and analyze the results of the paper *Deciphering the astrocytic contribution to learning and relearning, 2023*.

The repository is organized as follows:
- The folder 'models' contains the definition of the model used in the paper.
- The folder 'scripts' contains the code to run the simulations and collect the data.
- The folder 'notebooks_figures' contains the code to generate the figures of the paper.

Follow this steps to reproduce the figures of the paper:
- Clone the repository. You probably do not need to create virtual environment since the only dependency is numpy.
- With the folder 'scripts' as working directory, run the script `run_and_collect.py`. The script will run the simulations and save the data in the file 'scripts/data.pickle'.
- Run all cells in the notebooks inside the folder 'notebooks_figures' to generate each figure.
