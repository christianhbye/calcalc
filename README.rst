*******
CalCalc
*******

CalcCalc is a Python utility that serves two purposes:

- Acts as a calculator which returns the answer to basic arithmetic operations
 
- Provides an access point to `Wolfram Alpha <https://www.wolframalpha.com/>`_, allowing the user to ask questions to Wolfram Alpha and return the answer
 
CalCalc is free to use on the `MIT Open Source License <https://github.com/christianhbye/calcalc/blob/main/LICENSE>`_. It is written in its entirety by me, Christian Hellum Bye (<chbye@berkeley.edu>).

Set-up
#######
To use CalCalc, you would need to clone this repository and install it. We suggest installing in a `virtual environment <https://docs.python.org/3/library/venv.html>`_. An minimal example of the suggested installation method (using a virtual environment called .venv) is:

.. code:: bash

    git clone https://github.com/christianhbye/calcalc.git
    cd calcalc
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install .

This install all dependencies in the virtual environment, along with CalCalc.

Quick start
############
CalCalc can either run as an application in the command line or be imported as a Python module.

From the command line, run for example:

.. code:: bash

    python CalCalc.py '2*2'  # 4, using the calculator
    python CalCalc.py 'pi' -d 3 -w True  # 3.142, request the value of pi to 3 decimal digits from Wolfram Alpha
    
Get the full documnetation with :code:`python CalCalc.py --help`.

To import CalCalc as a python module in for example IPython, you'd want to do:

.. code:: Python

    >> import CalCalc as cc
    >> cc.calculate('2*2')  # 4
    >> cc.calculate('pi', decimal_precision=3, wolfram=True)  # 3.142

Contributing
############
Contributions are welcome! Please create an `issue <https://github.com/christianhbye/calcalc/issues>`_ to report bugs or suggest improvements. If you have written code you'd like to contribute, you may also go ahead an make a `pull request <https://github.com/christianhbye/calcalc/pulls>`_. We suggest installing the repositiory in developer mode (using :code:`python -m pip install .[dev]` when installing) to get some extra tools for testing, type hinting, and checking style.
