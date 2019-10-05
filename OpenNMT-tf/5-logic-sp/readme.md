# Setting up sentencepiece with logic / eng files
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