# ReadTheDocs

To generate documentation for your Python package, you can use a tool called Sphinx. Sphinx is a powerful documentation generator that can create high-quality documentation in multiple formats like HTML, PDF, and others. Here's a step-by-step guide on how to set up and use Sphinx for your Python package:

1. Install Sphinx and the Read the Docs theme:

```
pip install sphinx sphinx_rtd_theme
```

2. Create a docs directory in your package's root directory:

```
mkdir docs
cd docs
```

3. Run the Sphinx quickstart command:

```
sphinx-quickstart
# C:\Python3.11\python.exe -m sphinx.cmd.quickstart
```


Follow the prompts and answer the questions. This command will generate the necessary configuration files and a basic structure for your documentation.

4. Update the `conf.py` file in the docs directory:

Open `conf.py` and locate the line with `extensions = []`. Add the `'sphinx.ext.autodoc'` and `'sphinx.ext.napoleon'` extensions to enable automatic documentation generation and support for Google-style docstrings:

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
```

Also, add the following line to use the Read the Docs theme:

```python
html_theme = 'sphinx_rtd_theme'
```

5. Create the API documentation:

In the docs directory, create a new file called `api.rst` with the following content:

```
API Documentation
=================

.. automodule:: your_package_name
   :members:
   :undoc-members:
   :show-inheritance:
```

Replace `your_package_name` with the name of your package.

6. Update the `index.rst` file:

Edit the `index.rst` file to include the API documentation:

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
```

7. Generate the documentation:

In the docs directory, run the following command:

```
make html
# docs/make.bat html
```

This will generate the HTML documentation in the `_build/html` directory.

8. View the documentation:

Open `_build/html/index.html` in your web browser to view the generated documentation.

9. (Optional) Publish the documentation online:

If you want to publish your documentation online, you can use Read the Docs. Sign up for a free account, connect your repository, and follow their instructions to automatically build and host your documentation.

Remember to keep your docstrings up-to-date and follow a standard format like Google or NumPy style. This will ensure your documentation is clear, informative, and easy to maintain.



---------------------------------------------------------------

## Auto-derive the project structure

```
C:\Python3.11\python.exe -m sphinx.ext.apidoc -o docs/ doc_test_py/
```

Generates
  - docs/doc_test_py.rst
  - docs/doc_test_py.roulette.rst
  - docs/modules.rst
You may have to move everything exept `docs/modules.rst` to `docs/source/` for the make command to work.

Now replace the contents of `docs/source/index.rst` with the following:

```
API Documentation
=================

.. toctree::
   :maxdepth: 1

   doc_test
   doc_test.functions
   doc_test.roulette
```

