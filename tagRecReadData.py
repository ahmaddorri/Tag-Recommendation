__author__ = 'ahmaddorri'


import pandas as pd
import numpy as np
df = pd.read_csv("/Users/ahmaddorri/Desktop/tag recomendation/data/mixed/youtube/features_part0",header=None ,sep="|")

df=df.iloc[:,0:4]
#print(df.head())

all_tags = df[2]
#print(all_tags.head())

transaction = []
for tags in all_tags:
    tags = tags.strip()
    split_tags = tags.split(" ")
    tag_numbers = [ int(x) for x in split_tags[1:] ]
    transaction.append(tag_numbers)

#print(transaction)

#df2 = pd.read_csv("/Users/ahmaddorri/Desktop/tag recomendation/data/mixed/youtube.words",header=None ,sep=" ")
#print(df2.head())
sampleTransaction=np.random.choice(transaction,size=2000,replace=False).tolist()
#print(sampleTransaction)

import orangecontrib.associate.fpgrowth as org

T = [["unicef",    "child",  "united" ,"nation"  ],
     [    "education",    "child","game","math"],
     ["unicef","education", "child","job" ]]


#freq_item = org.frequent_itemsets(T,2)

itemsets = dict(org.frequent_itemsets(T,1))

#print(list(freq_item))
print(itemsets)
print(len(itemsets))

rules=org.association_rules(itemsets,min_confidence=0.49)
rules = list(rules)
for r in rules:
    print(r)
    if("unicef" in r[0]):
        print(r[0])
