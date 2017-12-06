# funny thing at csv file hence import re was used(?)

import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

# use regex to elimiate non decimal characters
non_deciomal = re.compile(r'[^\d]+')

for line in open('moore.csv'):
  r = line.split('\t')
  x = int(non_deciomal.sub())

