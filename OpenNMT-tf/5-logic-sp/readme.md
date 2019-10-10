# Setting up sentencepiece with logic / eng files
`python ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\generate_train_data.py 1000000 0.98 0.01 0.01 0.0001 0.0001 0.00001 C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\vocab.100k.json C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\training_templates.json 0.75 . True`

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
## Mini set
`onmt-main infer --config config.yml --auto_config --checkpoint_path=model --features_file logic-test.encoded.mini.txt > english-test.generated.encoded.mini.txt`

`spm_decode --model=en_logic.model --input_format=piece < english-test.generated.encoded.mini.txt > english-test.generated.decoded.mini.txt`

## Full set

`onmt-main infer --config config.yml --auto_config --checkpoint_path=model --features_file logic-test.encoded.txt > english-test.generated.encoded.txt`
`spm_decode --model=en_logic.model --input_format=piece < english-test.generated.encoded.txt > english-test.generated.decoded.txt`

To calculate BLEU (from BASH) :

`perl multi-bleu-detok.perl english-test.generated.decoded.txt < english-test.txt`

# Log
## 7/10/19

`python ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\generate_train_data.py 1000000 0.98 0.01 0.01 0.0001 0.0001 0.00001 C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\vocab.100k.json C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\training_templates.json 0.75 . True`

`spm_train --input=train.txt --model_prefix=en_logic --vocab_size=32000 --character_coverage=1`

Got pretty low loss, but even so, when evaluating it got a lot of words wrong (usually last word in the sentence)

Ideas for next iteration : 
- Bigger vocab
- Sort by popularity then use normal distribution when choosing random verbs etc - so more popular words tend to be used more. Can then maybe get away with a smaller vocab

## 8/10/19 
run ID 20191009_1
Large files stored here : C:\Users\LeeBorlace\OneDrive - Leecorp\AI\Opennmt-tf\20191009_1 Logic to English

From Anaconda prompt :

`python ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\generate_train_data.py 2000000 0.98 0.01 0.01 0.0001 0.0001 0.00001 C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\vocab.100k.json C:\Users\LeeBorlace\Documents\GitHub\logic-ml-bot\v1\nlu_training_data_generator\training_templates.json 0.75 data True`

`type data\english-train.txt >> data\train.txt`
`type data\logic-train.txt >> data\train.txt`

`spm_train --input=data\train.txt --model_prefix=en_logic --vocab_size=32997 --character_coverage=1`

`encode.bat`

From BASH : 

`cd C:/Users/LeeBorlace/Documents/GitHub/learning-ml/OpenNMT-tf/5-logic-sp`
`cut -f 1 en_logic.vocab | tail -n +2 > en_logic.vocab.tmp`
`sed -i '1i<blank>' en_logic.vocab.tmp`
`perl -pe '$/=""; s/\n\n/\n\t\n/;' en_logic.vocab.tmp > en_logic.vocab`

From Anaconda prompt :

`onmt-main train_and_eval --model_type Transformer --config config.yml --auto_config`

`tensorboard --logdir="model"`

To infer :

`onmt-main infer --config config.yml --auto_config --checkpoint_path=model --features_file data\logic-test.encoded.txt > data\english-test.generated.encoded.txt`

`spm_decode --model=en_logic.model --input_format=piece < data\english-test.generated.encoded.txt > data\english-test.generated.decoded.txt`

From BASH :
`cd C:/Users/LeeBorlace/Documents/GitHub/learning-ml/OpenNMT-tf/5-logic-sp`
`perl multi-bleu-detok.perl data/english-test.txt < data/english-test.generated.decoded.txt`

Result :
BLEU = 85.85, 95.3/91.9/88.1/82.1 (BP=0.962, ratio=0.963, hyp_len=87734, ref_len=91111)

