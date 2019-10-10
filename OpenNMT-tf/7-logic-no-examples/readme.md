# Intro
This folder is all about testing the learning of English > logic, but without example substitutions. So the learned examples will just contain un-substituted POS tokens.

# Logic to English
## Log
### 10/10/19
Note - the last flag stops it from substituting examples

`python ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\generate_train_data.py 100000 0.7 0.15 0.15 0.0001 0.0001 0.00001 ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\vocab.100k.json ..\..\..\logic-ml-bot\v1\nlu_training_data_generator\training_templates.json 0.75 data 0`

`onmt-build-vocab --size 40 --save_vocab data\english-vocab.txt data\english-train.txt`
`onmt-build-vocab --size 40 --save_vocab data\logic-vocab.txt data\logic-train.txt`

`onmt-main train_and_eval --model_type Transformer --auto_config --config Transformer_logic_eng.yml`

`tensorboard --logdir="run-logic-eng"`
