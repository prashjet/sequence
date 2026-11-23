.. sequence documentation master file, created by
   sphinx-quickstart on Mon Nov 16 12:35:10 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sequence
=========

Generate numerical sequences with a small Python package.

Installation
------------

From a clone, in your own Python environment::

    pip install .

First result
------------

Start with five non-negative even numbers::

    from sequence import even
    print(even(5))

Expected output::

    [0. 2. 4. 6. 8.]

The sequence starts at zero; five is the number of values, not the endpoint.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   example
