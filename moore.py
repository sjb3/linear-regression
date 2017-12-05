# funny thing at csv file hence import re was used(?)

import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

# use regex to elimiate non decimal char
non_deciomal = re.compile(r'[^\d+')

for line in open('moore.csv')

