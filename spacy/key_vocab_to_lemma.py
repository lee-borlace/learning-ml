# -*- coding: utf-8 -*-
# This program imports vocab.json as generated previously and builds up a multi-layered dict to map each kemma to its various forms. The first level
# maps to pos e.g. NOUN, VERB, the 2nd level maps to tag e.g. NN.

import json
import sys

# VOCAB_PATH = ".\\vocab.100k.json"
VOCAB_PATH = ".\\vocab.500k.json"

with open(VOCAB_PATH) as json_file:
    vocab_items = json.load(json_file)

lemma_dict = {}

# Vocab is a multi-layered dict where first layer is POS, 2nd is tag, 3rd is list of tokens. We will traverse that tree.
for pos_item_key in vocab_items:
    
    pos_item = vocab_items[pos_item_key]
    
    for tag_item_key in pos_item:
        
        tag_item = pos_item[tag_item_key]
        
        for token in tag_item:
            
            text = token["t"].strip()
            lemma = token["l"].strip()
            pos = token["p"].strip()
            tag = token["tg"].strip()
            
            # Make sure we have everything
            if not text or not lemma or not pos or not tag:
                continue
            
            # Get a dict for this lemma
            if lemma not in lemma_dict :
                lemma_dict[lemma] = {}
            entry_for_lemma = lemma_dict[lemma]
            
            # Get a dic for this lemma + pos
            if pos not in entry_for_lemma:
                entry_for_lemma[pos] = {}
            entry_for_lemma_and_pos = entry_for_lemma[pos]
                
            # Get store text against lemma + pos + tag
            entry_for_lemma_and_pos[tag] = text
            
out_file = open("lemma_dict.json", "w+")
out_file.write(json.dumps(lemma_dict))

print("Done!")
        
    

