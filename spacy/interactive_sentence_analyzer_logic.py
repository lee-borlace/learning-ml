# -*- coding: utf-8 -*-
# This program prompts the user for text and anlayzes it. Each sentence is analyzed two ways - once as a complete unit, once on a word by word basis
import spacy
import json
from spacy import displacy

MODEL = "en_core_web_lg"

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load(MODEL)

LEMMA_DICT_PATH = ".\\lemma_dict.json"

with open(LEMMA_DICT_PATH) as json_file:
    lemma_dict = json.load(json_file)

print("\exit or \quit to quit");

def print_token(token):
    print(f"TEXT={token.text},LEMMA={token.lemma_},POS={token.pos_},TAG={token.tag_},DEP={token.dep_},ID={token.i}")

def analyse_token(token) :
    print(f"{token.text} ({token.lemma_})")
    print("-------")
    
    lemma = token.lemma_
    
    if lemma in lemma_dict:
        lemma_entry = lemma_dict[lemma]
        
        for pos in lemma_entry:
            for tag in lemma_entry[pos]:
                print(f"{pos}_{tag}={lemma_entry[pos][tag]}")
    
def get_token_id_as_const(token) :
    return f"Const_{token.i}"

def get_pos_formatted(token):
    return token.pos_.strip().lower().capitalize()

def get_lemma_formatted(token):
    
    lemma = token.lemma_.strip().lower().capitalize()
    
    if lemma == "-pron-":
        lemma = token.text.lower().capitalize()
    
    return lemma

def get_tag_formatted(token):
    return token.tag_.strip().lower().capitalize().replace("$","")

def get_dep_formatted(token):
    return token.dep_.strip().lower().capitalize()

#text = "your dog chased my cat, and he was very scared"
#text = "your dog chased my cat"
text = "your dog chased me"

doc = nlp(text)

print("****************************************")
print("Result from complete sentence analysis")
print("****************************************")

for token in doc:
    print_token(token)

print()

print("****************************************")
print("Conversion to Logic")
print("****************************************")

for token in doc:
    print(f"{get_pos_formatted(token)}({get_token_id_as_const(token)},{get_lemma_formatted(token)},{get_tag_formatted(token)})")
    
    if token.i != token.head.i:
        print(f"{get_dep_formatted(token)}({get_token_id_as_const(token)},{get_token_id_as_const(token.head)})")
        
        
