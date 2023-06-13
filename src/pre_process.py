import sys
import re
import random
import pandas as pd

from data.vocab import load_vocab

df_train = pd.read_csv('/Users/poojarani/Downloads/data.tsv', sep='\t', header=None)

test_buggy = open("/Users/poojarani/Downloads/shirin_code2code/test.submitted-fixed.submitted",'w')
test_fixed = open("/Users/poojarani/Downloads/shirin_code2code/test.submitted-fixed.fixed",'w')

train_buggy = open("/Users/poojarani/Downloads/shirin_code2code/train.submitted-fixed.submitted",'w')
train_fixed = open("/Users/poojarani/Downloads/shirin_code2code/train.submitted-fixed.fixed",'w')

valid_buggy = open("/Users/poojarani/Downloads/shirin_code2code/valid.submitted-fixed.submitted",'w')
valid_fixed = open("/Users/poojarani/Downloads/shirin_code2code/valid.submitted-fixed.fixed",'w')

for i in range(len(df_train)):
	pair = df_train.iloc[i]
	rand_num = random.random()
	if rand_num <= 0.1:
		test_buggy.write(pair[0] + '\n')
		test_fixed.write(pair[1] + '\n')
	elif rand_num > 0.1 and rand_num <= 0.2:
		valid_buggy.write(pair[0] + '\n')
		valid_fixed.write(pair[1] + '\n')
	elif rand_num > 0.2:
		train_buggy.write(pair[0] + '\n')
		train_fixed.write(pair[1] + '\n')

	print(i)

test_buggy.close()
test_fixed.close()

train_buggy.close()
train_fixed.close()

valid_buggy.close()
valid_fixed.close()
