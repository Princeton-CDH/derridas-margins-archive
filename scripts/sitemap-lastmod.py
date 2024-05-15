#!/usr/bin/env python
""""
script to populate all entries in a sitemap.xml file with
a specified last modification date

setup:
- `pip install lxml`

"""
import csv
import argparse
import re
from pathlib import Path
from eulxml import xmlmap

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


class SitemapURL(xmlmap.XmlObject):
    ROOT_NAMESPACES = {"s": SITEMAP_NS}
    lastmod = xmlmap.StringField("s:lastmod")


class SitemapXML(xmlmap.XmlObject):
    ROOT_NAMESPACES = {"s": SITEMAP_NS}
    urls = xmlmap.NodeListField("s:url", SitemapURL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update sitemap.xml files with last-modification times"
    )
    parser.add_argument(
        "last_mod", help="Last modification date to add in YYYY-MM-DD form"
    )
    parser.add_argument(
        "sitemap_files", nargs="+", help="List of sitemap.xml files to update"
    )
    args = parser.parse_args()
    if not re.match("\d{4}(-\d{2}(-\d{2})?)?", args.last_mod):
        print(f"Last modification date must be in YYYY-MM-DD/YYYY-MM/YYYY format")

    for sitemap in args.sitemap_files:
        sitemapxml = xmlmap.load_xmlobject_from_file(sitemap, SitemapXML)
        updated = 0
        for url in sitemapxml.urls:
            if not url.lastmod:
                url.lastmod = args.last_mod
                updated += 1

        if updated:
            print(
                f"Updating {sitemap}; updated {updated} urls with last modification time"
            )
            with open(sitemap, "wb") as outfile:
                sitemapxml.serializeDocument(outfile, pretty=True)
