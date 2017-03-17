# coding: utf-8
# Download our data from openneu.ro
# get_ipython().system('git clone https://github.com/OpenNeuroLab/metasearch.git')
# Path('data_not_in_repro').mkdir()
# mv metasearch/ data_not_in_repro/
from pathlib import Path
metasearch_dir = Path('data_not_in_repro/metasearch/')
data_exists = metasearch_dir.exists()
in_repro_course = Path.cwd().name == 'repro_course'
if data_exists and in_repro_course:
    print('Data directory has been downloaded')
else:
    print('Data has NOT been downloaded')
print('This is an added line')
