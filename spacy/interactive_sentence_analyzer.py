# -*- coding: utf-8 -*-
# This program prompts the user for text and anlayzes it. Each sentence is analyzed two ways - once as a complete unit, once on a word by word basis
import spacy
import json

MODEL = "en_core_web_lg"

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load(MODEL)

LEMMA_DICT_PATH = ".\\lemma_dict.json"

with open(LEMMA_DICT_PATH) as json_file:
    lemma_dict = json.load(json_file)

print("\exit or \quit to quit");

def print_token(token):
    print(f"TEXT={token.text},LEMMA={token.lemma_},POS={token.pos_},TAG={token.tag_},DEP={token.dep_}")

def analyse_token(token) :
    print(f"{token.text} ({token.lemma_})")
    print("-------")
    
    lemma = token.lemma_
    
    if lemma in lemma_dict:
        lemma_entry = lemma_dict[lemma]
        
        for pos in lemma_entry:
            for tag in lemma_entry[pos]:
                print(f"{pos}_{tag}={lemma_entry[pos][tag]}")
    
        
while True:
    text = input("Input>")
    
    if(text == "\exit" or text == "\quit"):
        break
    
    doc = nlp(text)
    
    print()
    
    print("****************************************")
    print("Result from complete sentence analysis")
    print("****************************************")
    
    for token in doc:
        print_token(token)
        
    print("___________")
    
    for token in doc:
        analyse_token(token) 
        print()
    
        
    print("****************************************")
    print("Result from token by token analysis")
    print("****************************************")

    tokens = []
    for token in doc:
        lone_token = nlp(token.text)[0]
        print_token(lone_token)
        tokens.append(lone_token)

    print("___________")

    for token in tokens:
        analyse_token(token) 
        print()