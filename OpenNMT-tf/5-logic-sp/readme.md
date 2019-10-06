# Setting up sentencepiece with logic / eng files
Run the vocab gen again with 500K words

`python ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\generate_train_data.py 4000000 0.63 0.19 0.18 0.0001 0.0001 0.00001 C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\vocab.json C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\training_templates.json 0.75`


First, concat all files into one - train.txt

`type english-train.txt >> train.txt`
`type logic-train.txt >> train.txt`
`type english-val.txt >> train.txt`
`type logic-val.txt >> train.txt`


`spm_train --input=train.txt --model_prefix=en_logic --vocab_size=30000 --character_coverage=1`

`spm_encode --model=en_logic.model < english-train.txt > english-train.encoded.txt`
`spm_encode --model=en_logic.model < logic-train.txt > logic-train.encoded.txt`
`spm_encode --model=en_logic.model < english-val.txt > english-val.encoded.txt`
`spm_encode --model=en_logic.model < logic-val.txt > logic-val.encoded.txt`

# Training
`onmt-main train_and_eval --model_type Transformer --config config.yml --auto_config`

# Batch file
generate_encode_train.bat