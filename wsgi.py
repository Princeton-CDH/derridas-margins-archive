# PYWB_CONFIG_FILE in env for wayback to pick it up
import os

os.environ['PYWB_CONFIG_FILE'] = 'config.yaml'
from pywb.apps.wayback import application
