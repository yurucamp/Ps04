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
 
 
###  We made 3 cases for the data set:
**Case 1**: only retain a small number of the most common words. (here, we limit  dict length into 10)

| keys                         | Type   | Size  |
| ---------------------------- |:------:| -----:|
| cherbonnel-mi-tio_SP.txt     | dict   |   10  |
| eaton-boy-scouts_EN.txt      | dict   |   10  |
| schloemp-tolle-koffer_DE.txt | dict   |   10  |
| unknown-lang.txt             | dict   |   10  |

```python
print(mostFrequent)  # the frequency table of the ten most common words
```

```
  {'schloemp-tolle-koffer_DE.txt': {'der': 0.05649108253836582,
  'und': 0.04545831605143094,
  'die': 0.03782662795520531,
  ...},
  
 'unknown-lang.txt': {'de': 0.09992628388893439,
  'y': 0.06933409779670735,
  'la': 0.06257678761569334,
  ...},
  
 'eaton-boy-scouts_EN.txt': {'the': 0.10231703491238292,
  'and': 0.05445256128714202,
  'a': 0.04067135750459373,
  ...},
  
 'cherbonnel-mi-tio_SP.txt': {'de': 0.08207771609833465,
  'que': 0.06677240285487708,
  'y': 0.057295796986518634,
  ...}}
``` 
**Case 2**: only short words (ie, words with no more than 4 letters.)

| keys                         | Type   | Size  |
| ---------------------------- |:------:| -----:|
| cherbonnel-mi-tio_SP.txt     | dict   |  670  |
| eaton-boy-scouts_EN.txt      | dict   | 1142  |
| schloemp-tolle-koffer_DE.txt | dict   |  818  |
| unknown-lang.txt             | dict   |  869  |

```python
print(small_dicts)  # the frequency table of the short words
```
```
  {'schloemp-tolle-koffer_DE.txt': {'the': 8.295313148071339e-05,
   'der': 0.05649108253836582, 
   'by': 0.00016590626296142678
  ...},
  
 'unknown-lang.txt': {the': 4.095339503644852e-05, 
 'of': 4.095339503644852e-05, 
 'la': 0.06257678761569334,
  ...},
  
 'eaton-boy-scouts_EN.txt': {'boy': 0.0010756061488818177, 
 'at': 0.010666427643078026, 
 'lake': 0.0022184376820687493
  ...},
  
 'cherbonnel-mi-tio_SP.txt': {'the': 3.965107057890563e-05, 
 'of': 3.965107057890563e-05, 
 'mi': 0.032355273592387
  ...}}
``` 

**Case 3**: original data with no limit on maximum word length and preserved dict length

| keys                         | Type   | Size  |
| ---------------------------- |:------:| -----:|
| cherbonnel-mi-tio_SP.txt     | dict   | 8217  |
| eaton-boy-scouts_EN.txt      | dict   | 6958  |
| schloemp-tolle-koffer_DE.txt | dict   | 7023  |
| unknown-lang.txt             | dict   | 9501  |

```python
print(dicts)  # the frequency table of all words
```

```
  {'schloemp-tolle-koffer_DE.txt': {'the': 4.128648693282689e-05, 
  'project': 4.128648693282689e-05, 
  'gutenberg': 4.128648693282689e-05
  ...},
  
 'unknown-lang.txt': {the': 2.302555836979047e-05, 
 'project': 2.302555836979047e-05, 
 'gutenberg': 2.302555836979047e-05, 
  ...},
  
 'eaton-boy-scouts_EN.txt': {project': 1.418359242028821e-05, 
 "gutenberg's": 1.418359242028821e-05, 
 'boy': 0.0006808124361738341,
  ...},
  
 'cherbonnel-mi-tio_SP.txt': {the': 2.2488081316902043e-05, 
 'project': 2.2488081316902043e-05, 
 'gutenberg': 2.2488081316902043e-05, 
  ...}}
``` 
## Results
To determine which known text is most similar to the unknown text, 
we use L1-onrm: absolute values of diff􏰂erences in the word frequencies: 
the most similar one is the one where the sum of diff􏰂erences is the smallest.

### Case 1:
```python
print_result(mostFrequent)  
```
| dictionary                   | total_difference    | 
| ---------------------------- |:-------------------:| 
| cherbonnel-mi-tio_SP.txt     | 0.14697755500632032 | 
| eaton-boy-scouts_EN.txt      | 0.3182874681065777  |
| schloemp-tolle-koffer_DE.txt | 0.31754458730817087 |

> language with smallest total di􏰂fference is Spanish 
### Case 2:
```python
print_result(small_dicts)  
```
| dictionary                   | total_difference    | 
| ---------------------------- |:-------------------:| 
| cherbonnel-mi-tio_SP.txt     | 0.36797232109098493  | 
| eaton-boy-scouts_EN.txt      | 1.070270616943595   |
| schloemp-tolle-koffer_DE.txt | 1.326611964526741   |

> language with smallest total di􏰂fference is Spanish 

### Case 3:
```python
print_result(dicts)  
```
| dictionary                   | total_difference    | 
| ---------------------------- |:-------------------:| 
| cherbonnel-mi-tio_SP.txt     | 0.5391252309312459  | 
| eaton-boy-scouts_EN.txt      | 1.0391277012936015  |
| schloemp-tolle-koffer_DE.txt | 1.1855713272638     |

> language with smallest total di􏰂fference is Spanish 

## Findings
All three cases preddicts the same language: Spanish.
