# derridas-margins-archive

Using the Wayback Machine's python tools to archive and deploy
the CDH's Derrida's Margins site.

## Installation

Create a Python 3.7 environment and install dependencies

```sh
pip install -r requirements.txt
```

## Development

After installation, run a server locally:

```sh
wayback
```

Then navigate to http://localhost:8080/derrida/https://derridas-margins.princeton.edu/


**NOTE:** Mac users who have upgraded to Big Sur will run into [an error.](https://github.com/webrecorder/pywb/issues/616) A recommended quick fix is to go to `fakeredis.py` in your virtual environment and swap the line...

```python
_libc_library = find_library('c') or find_library('msvcrt') or find_library('System')
```

...with...

```python
_libc_library = 'libc.dylib'
```
