import pandas as pd
g= pd.read_csv('codeforsf-updatedfile.txt', sep='\n', header=None) #converted the PDF file to a text file (codeforsf-updatedfile.txt). separating each line, while reading as rows, at newline character.
df=pd.DataFrame(g) #creating a dataframe of the input file.
