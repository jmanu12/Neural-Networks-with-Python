import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm
from Hopfield82 import Hopfield82
from processData import ProcessData

# ############### READ DATA ######################
# picture = ProcessData.read_image('Images/paloma.bmp')
#we read the picture as a vector of the individual file
#print(picture)

new_data = ProcessData()
print(new_data.read_train_path('Images/','*.bmp'))
#print(new_data.read_image('Images/paloma.bmp'))

# ############### LEARNING ######################



hopfield = Hopfield82()
#R = w.create_weight_matrix(M)






    #https://github.com/yosukekatada/Hopfield_network/blob/master/hopfield.py
