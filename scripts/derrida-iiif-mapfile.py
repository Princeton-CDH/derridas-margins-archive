# one-off script to generate mapping file for derrida iiif image urls to iiif server
# from https://gist.github.com/kmcelwee/4de37dd3ebad4fcad3d06a1d1670086a

# goal is to map from
# /library/levi-strauss-anthropologie-structurale-1958/gallery/images/front-cover/iiif/
# ..to..
# https://iiif-cloud.princeton.edu/iiif/2/########intermediate_file

import json
from django.urls import reverse
from derrida.books.models import Instance
from derrida.common.utils import absolutize_url


def localize_iiif_image(canvas, work_instance):
    # given a djiffy canvas and associated work,
    # # use the piffle image api client for the canvas image and
    # replace original iiif api endpoint and image id with local proxy iiif url
    img = canvas.image
    img.api_endpoint = absolutize_url(
        reverse(
            "books:canvas-detail",
            kwargs={"slug": work_instance.slug, "short_id": "images"},
        )
    ).rstrip("/")
    img.image_id = "%s/iiif" % canvas.short_id
    return img


def parse_pul_image_url(url_string):
    return url_string.split("/info.json")[0]


def parse_local_image_url(url_string):
    return url_string.split("https://derridas-margins.princeton.edu")[1].split(
        "full/full/0/default.jpg"
    )[0]


all_instances = Instance.objects.filter(digital_edition__isnull=False)

mapping = {}

for instance in all_instances:
    instance_canvases = []
    instance_canvases.extend(instance.overview_images())
    instance_canvases.extend(instance.annotated_pages())
    instance_canvases.extend(instance.insertion_images())
    for canvas in instance_canvases:
        local_image_url = str(localize_iiif_image(canvas, instance))
        local_image_url = parse_local_image_url(local_image_url)
        pul_image_url = canvas.image.info()
        pul_image_url = parse_pul_image_url(pul_image_url)
        mapping[local_image_url] = pul_image_url

with open("iiif-proxy.map", "w") as f:
    for local_image_url, pul_image_url in mapping.items():
        f.write(f"{local_image_url} {pul_image_url};\n")
