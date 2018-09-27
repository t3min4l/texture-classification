import os 
import sys 

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
CHECKPOINT_DIR = os.path.join(PROJECT_DIR, 'checkpoint')

NUM_LABELS = 6

DATASET_PATH = os.path.join(DATA_DIR, 'subdataset')