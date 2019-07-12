# Ps04
IMT511 Problem Set 4 Machine Learning

# Data
The data is given in the data folder and contains four files: 
_cherbonnel-mi-tio_SP.txt (Spanish), schloemp- tolle-ko􏰂er_DE.txt (German), 
eaton-boy-scouts_EN.txt (English) and unknown-lang.txt._ 
These fi􏰃les are books, downloaded from **Project Gutenberg**.

# Approach

## Data processing
 First, we load data files in using for loop, storing each file as a string.
 Then split the string into words, and remove punctuation and other special characters
 from the words. Following up, we frequency table of words.
 
 
###  we made 3 cases for the data set:
* Case 1: only retain a small number of the most common words. (here, we limit  dict length into 10)
    - 'mostFrequent' , the frequency table of the ten most common words
'''
  {'schloemp-tolle-koffer_DE.txt': {'der': 0.05649108253836582,
  'und': 0.04545831605143094,
  'die': 0.03782662795520531,
  'sie': 0.03293239319784322,
  'ich': 0.02978017420157611,
  'in': 0.027208627125673995,
  'ein': 0.02372459560348403,
  'er': 0.023060970551638325,
  'den': 0.021816673579427622,
  'das': 0.019245126503525507},
 'unknown-lang.txt': {'de': 0.09992628388893439,
  'y': 0.06933409779670735,
  'la': 0.06257678761569334,
  'que': 0.05868621508723073,
  'el': 0.05291178638709149,
  'a': 0.04111720861659431,
  'en': 0.03763617003849619,
  'no': 0.02330248177573921,
  'los': 0.0221148333196822,
  'se': 0.021705299369317716},
 'eaton-boy-scouts_EN.txt': {'the': 0.10231703491238292,
  'and': 0.05445256128714202,
  'a': 0.04067135750459373,
  'to': 0.04062654058172366,
  'of': 0.03134943754761798,
  'they': 0.019024783758347152,
  'in': 0.018666248375386545,
  'was': 0.017501008380764578,
  'he': 0.017411374535024424,
  'it': 0.01649262761618787},
 'cherbonnel-mi-tio_SP.txt': {'de': 0.08207771609833465,
  'que': 0.06677240285487708,
  'y': 0.057295796986518634,
  'la': 0.044885011895321174,
  'a': 0.03842188739095956,
  'el': 0.03643933386201428,
  'en': 0.03441712926249009,
  'no': 0.034060269627279934,
  'mi': 0.032355273592387,
  'me': 0.025812846946867564}}
''' 
* Case 2: only short words (ie, words with no more than 4 letters.)
* Case 3: original data with no limit on maximum word length and preserved dict length

