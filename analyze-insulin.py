
cut -c 1-24 preproinsulin-seq-clean.txt > lsinsulin-seq-clean.txt
cut -c 25-54 preproinsulin-seq-clean.txt > binsulin-seq-clean.txt
cut -c 55-89 preproinsulin-seq-clean.txt > cinsulin-seq-clean.txt
cut -c 90-110 preproinsulin-seq-clean.txt > ainsulin-seq-clean.txt

#Counting the number of characters in each of the files
wc -m lsinsulin-seq-clean.txt
wc -m binsulin-seq-clean.txt
wc -m cinsulin-seq-clean.txt
wc -m ainsulin-seq-clean.txt