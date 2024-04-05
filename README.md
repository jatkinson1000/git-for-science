# pyndulum

Python code for doing pendulum stuff.

## Installation

To use this code, first clone the repository onto your local machine.
This can be done with the following command:
```
git clone git@github.com:jatkinson1000/git-for-science.git pendulum_project
```
This will create a local copy of the code in `pendulum_project/`

It is suggested to use the code from a python virtual environment:
```
python3 -m venv pendulum_venv
source pendulum_venv/bin/activate
```

You need numpy to run the code:
```
pip install numpy
```

## Getting started

After following the above steps run:
```python
import pendulum_equations as peq
```
from within python.
specific functions can then be accessed as, e.g.
```python
peq.get_period(20)
```

## Authors and acknowledgment

This code is written by [Jack Atkinson](https://jackatkinson.net/).
Part of an M2LInES Workshop on 2024/4/5.

## Contribution

Please get in touch to add to this code.
