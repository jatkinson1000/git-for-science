# pyndulum

Python package to provide an implementation of simple pendulum equations


## Installation

To install this code clone the repository using:
```
git clone https://github.com/jatkinson1000/git-for-science.git git4sci
```
Navigate inside and then install using pip:
```
cd git4sci
pip install .
```
It is recommended to use a virtual environment.

This will install _pyndulum_ and its dependencies


### Getting Started

To start, enter the python repl using:
```
python
```

From there you can import the _pyndulum_ package and use the equations.\
For example:
```python
from pyndulum import equations as peq
peq.get_period(2)
2.837006706885775
peq.check_small_angle(0.0002)
True
```

### Authors and Acknowledgment

_pyndulum_ is written by Jack Atkinson.\
Please provide acknowledgment if your project uses _pyndulum_


### Contributing

Contributions are welcome.

To contribute to _pyndulum_ please raise an issue or feature request on the board and
open a pull/merge request.
