import os
from box.exceptions import BoxValueError
import yaml
from ChickenDiseaseClassifier import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64