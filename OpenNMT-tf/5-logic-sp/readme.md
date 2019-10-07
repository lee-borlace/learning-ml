# Setting up sentencepiece with logic / eng files
`python ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\generate_train_data.py 1000000 0.98 0.01 0.01 0.0001 0.0001 0.00001 C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\vocab.100k.json C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\training_templates.json 0.75`

First, concat all files into one - train.txt

`type english-train.txt >> train.txt`
`type logic-train.txt >> train.txt`

Build up the SP model

`spm_train --input=train.txt --model_prefix=en_logic --vocab_size=32000 --character_coverage=1`

Encode the various train, val, test files with that model. The following is also done via encode.bat.

`spm_encode --model=en_logic.model < english-train.txt > english-train.encoded.txt`
`spm_encode --model=en_logic.model < logic-train.txt > logic-train.encoded.txt`
`spm_encode --model=en_logic.model < english-val.txt > english-val.encoded.txt`
`spm_encode --model=en_logic.model < logic-val.txt > logic-val.encoded.txt`
`spm_encode --model=en_logic.model < english-test.txt > english-test.encoded.txt`
`spm_encode --model=en_logic.model < logic-test.txt > logic-test.encoded.txt`

Process the vocab file in BASH shell -

First, back up the vocab file

`cut -f 1 en_logic.vocab | tail -n +2 > en_logic.vocab.tmp`

`sed -i '1i<blank>' en_logic.vocab.tmp`

`perl -pe '$/=""; s/\n\n/\n\t\n/;' en_logic.vocab.tmp > en_logic.vocab`

Now we can train

`onmt-main train_and_eval --model_type Transformer --config config.yml --auto_config`

# Inference
`onmt-main infer --config config.yml --auto_config --checkpoint_path=model --features_file logic-test.encoded.txt > english-test.generated.encoded.txt`

`spm_decode --model=en_logic.model --input_format=piece < english-test.generated.encoded.txt > english-test.generated.decoded.txt`


# Log
## 7/10/19

`python ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\generate_train_data.py 1000000 0.98 0.01 0.01 0.0001 0.0001 0.00001 C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\vocab.100k.json C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\training_templates.json 0.75`

`spm_train --input=train.txt --model_prefix=en_logic --vocab_size=32000 --character_coverage=1`