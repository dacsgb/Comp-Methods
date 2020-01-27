import LSF_class
import numpy as np
import matplotlib.pyplot as plt

NonLin = LSF_class.NLCF('Tests\Final\sos3.txt')
NonLin.yes()
NonLin.Plot()
NonLin.Coeff()