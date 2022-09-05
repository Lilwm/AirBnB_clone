#!/usr/bin/python3
""" unit tests for base model"""

import unittest
import sys
import io
import json
import models
from os import remove
from os.path import isfile
from models.base_model import BaseModel
from datetime import datetime
