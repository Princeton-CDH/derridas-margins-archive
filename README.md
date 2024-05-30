# Derrida's Margins (web archive)

This is a web archive of [Derrida's Margins](https://cdh.princeton.edu/projects/derridas-margins/),
a research project sponsored by the Center for Digital Humanities at Princeton.

> Chenoweth, Katie, Alexander Baron-Raiffe, and Rebecca Sutton Koeser (eds.). Derrida’s Margins, version 1.3.3. Center for Digital Humanities at Princeton, 2018. http://derridas-margins.princeton.edu.

The web archive files were created in 2021 with [Browsertrix Crawler](https://github.com/webrecorder/browsertrix-crawler); custom behaviors were used to capture specific interactive
portions of the site.

A version of this web archive is available through Princeton Data Commons,
along with a CSV file of all URLs found by crawling the site.

> Chenoweth, Katie, Koeser, Rebecca Sutton, & Alexander, Baron-Raiffe. (2024). Derrida's Margins web archive [Dataset]. Princeton University. [doi:10.34770/yw3y-ze12](https://doi.org/10.34770/yw3y-ze12)

## License

Software associated with this project is licensed under the [Apache 2.0 License](https://github.com/Princeton-CDH/ppa-django/blob/main/LICENSE).

The web archive and any other content is licensed as [Creative Commons Attribution 4.0 International (CC BY)](https://creativecommons.org/licenses/by/4.0/).

©2024 Trustees of Princeton University.

----

## Installation and development instructions

### Deploying

This web archive is best viewed via nginx proxy with customization using
the [derrida_archive playbook](https://github.com/Princeton-CDH/cdh-ansible/blob/main/playbooks/derrida_archive.yml) in [CDH ansible](https://github.com/Princeton-CDH/cdh-ansible/).

Customizations include disabling or suppressing non-interactive portions of the site, including
search, filtering, and deep-zoom images.

### Running locally

Create a Python 3.11 environment and install dependencies

```sh
pip install -r requirements.txt
```

After installation, start the wayback server:

```sh
wayback
```
Then navigate to http://localhost:8080/derrida/https://derridas-margins.princeton.edu/

