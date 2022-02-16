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

Contributing
############
Contributions are welcome! Please create an `issue <https://github.com/christianhbye/calcalc/issues>`_ to report bugs or suggest improvements. If you have written code you'd like to contribute, you may also go ahead an make a `pull request <https://github.com/christianhbye/calcalc/pulls>`_. We suggest installing the repositiory in developer mode (using :code:`python -m pip install .[dev]` when installing) to get some extra tools for testing, type hinting, and checking style.
