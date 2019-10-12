import os
import argparse


import tensorflow as tf
import opennmt as onmt

from opennmt import constants
from opennmt.utils import decay
from opennmt.utils import losses
from opennmt.utils import misc
from opennmt.utils import optim

import sys

import numpy as np

mode = tf.estimator.ModeKeys.PREDICT

def show_usage():
    print("Runs the specified model interactively.")
    print()
    print("Usage :")
    print()
    print("python.exe infer_test.py RUN_DIR")
    print()
    print("E.g.")
    print()
    print("python.exe infer_test.py run-eng-logic")

if(len(sys.argv) == 2):
    RUN_DIR = str(sys.argv[1])
else:
    RUN_DIR = input("Enter run dir >")    

BASE_EXPORT_PATH = ".\\" + RUN_DIR + "\\export\\latest"

if not os.path.exists(BASE_EXPORT_PATH) :
    print(f"Path {BASE_EXPORT_PATH} doesn't exist. Exiting.")
    exit()

export_folders = os.listdir(BASE_EXPORT_PATH)

if len(export_folders) == 0 :
    print(f"Path {BASE_EXPORT_PATH} doesn't contain any export folders. Exiting.")
    exit()

# Find latest export folder.
latest_export_folder_as_int = 0
latest_export_folder = ""

for export_folder in export_folders :
    folder_name_as_int = int(export_folder)
    
    if folder_name_as_int > latest_export_folder_as_int:
        latest_export_folder_as_int = folder_name_as_int
        latest_export_folder = export_folder

if latest_export_folder_as_int == 0:
    print("Couldn't find latest export folder. Exiting.")
    exit()

export_dir_path = BASE_EXPORT_PATH + "\\" + latest_export_folder

print(f"Using export path {export_dir_path}.")

with tf.Session() as sess:
    meta_graph_def = tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING], export_dir_path)
    
    signature_def = meta_graph_def.signature_def["serving_default"]

    input_tokens = signature_def.inputs["tokens"].name
    input_length = signature_def.inputs["length"].name
    output_tokens = signature_def.outputs["tokens"].name
    output_length = signature_def.outputs["length"].name
    output_log_probs = signature_def.outputs["log_probs"].name

    print("\exit or \quit to exit")

    while True:
        text = input("INPUT > ")
        
        if(text == "\exit" or text == "\quit"):
            break
        
        split = text.split(' ')

        inputs = {
            input_tokens: [split],
            input_length: [len(split)]
        }
        
        batch_tokens, batch_length, batch_log_probs = sess.run([output_tokens, output_length, output_log_probs], feed_dict=inputs)
    
        for tokens, lengths, log_probs in zip(batch_tokens, batch_length, batch_log_probs):
            
            # Convert log probs to normal probs
            probs = np.exp(log_probs)
            
            # Iterate over each hypothesis
            for i in range(len(tokens)):
            
                tokens_this_translation = tokens[i]
                prob_this_translation = probs[i]
                
                #length -= 1  # Ignore </s> token.
                #token_list = tokens[:length].tolist()
                #token_list = tokens.tolist()

                translation=""
                for token in tokens_this_translation:
                    translation += token.decode("utf-8") + " "
                    
                translation = translation.strip()
               
                print("OUTPUT > " + translation + "(" + str(prob_this_translation) + ")")
        
        