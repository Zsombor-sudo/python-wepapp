# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

#loading the saved model
loaded_model = pickle.load(open('D:/SULI/EGYETEM/bevgépi tanulás/proj/web/trained_model_jobs.sav','rb'))

