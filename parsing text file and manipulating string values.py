import pandas as pd
g= pd.read_csv('codeforsf-updatedfile.txt', sep='\n', header=None) #Converted the PDF file to a text file (codeforsf-updatedfile.txt). Separating each line, while reading, at newline character.
df=pd.DataFrame(g) #Creating a dataframe of the input file.
df['val']=g[0] #Just to create a column with a name 'val'. Two columns exist at this stage: [0] and ['val']
df['Action'], df['Description']= df['val'].str.split('.' and ' ', 1).str #Splitting the values in column 'val' using string.split at one position: a period ('.') followed by a space ' ' The number 1 in str.split specifies how many times should the splitting happen. Splitting at a position will give two columns of values and therefore saved those values in two columns: 'Action' and 'Description'																															
df['Resolution Letter']= df['Action'].str.strip('.') #Stripping period '.' from column 'Action' and saving, just the alphabets in the case in point, in a new column by name 'Resolution Letter'
col_to_keep=['Resolution Letter', 'Description'] #Keeping the necessary columns
df=df[col_to_keep] #Broadcasting the necessary columns directly to the dataframe. The dataframe, at this stage, consists of two columns: 'Resolution Letter' and 'Description'