import os
import sys
import pandas as pd
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Training_Mgmt.Person import Person, calculate, record
from Training_Mgmt.Exercise import Record as Exercise_Record