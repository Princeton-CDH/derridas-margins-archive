# Derrida's Margins (web archive)

This is a web archive [Derrida's Margins](https://cdh.princeton.edu/projects/derridas-margins/),
a research project sponsored by the Center for Digital Humanities at Princeton.

> Chenoweth, Katie, Alexander Baron-Raiffe, and Rebecca Sutton Koeser (eds.). Derrida’s Margins, version 1.3.3. Center for Digital Humanities at Princeton, 2018. http://derridas-margins.princeton.edu.

The web archive files were created in 2021 with [Browsertrix Crawler](https://github.com/webrecorder/browsertrix-crawler); custom behaviors were used to capture specific interactive
portions of the site.

## Running locally

Create a Python 3.11 environment and install dependencies

```sh
pip install -r requirements.txt
```

After installation, start the wayback server:

```sh
wayback
```
Then navigate to http://localhost:8080/derrida/https://derridas-margins.princeton.edu/

