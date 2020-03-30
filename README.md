This is for verizon test.

#Verizon Random Number Generator

## Steps to run the program:

``` bash
$ cd verizon
$ python runner.py
```

or
If your default version is not python 3 use:
``` bash
$ cd verizon
$ python runner.py
```
Example output:
``` bash
C:\Users\md\AppData\Local\Programs\Python\Python38\python.exe C:/Users/md/PycharmProjects/Verizon/verizon/runner.py
New 4 digit random code is : 2868
```
## Steps to run the unittest program:
``` bash
$ cd tests
$ python test_code_generator.py
```

Example output:
``` bash
Testing started at 9:17 PM ...
C:\Users\md\AppData\Local\Programs\Python\Python38\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.1\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py" --path C:/Users/md/PycharmProjects/Verizon/tests/test_code_generator.py
Launching unittests with arguments python -m unittest C:/Users/md/PycharmProjects/Verizon/tests/test_code_generator.py in C:\Users\md\PycharmProjects\Verizon\tests

Ran 8 tests in 0.011s

OK
```

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`

└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```



