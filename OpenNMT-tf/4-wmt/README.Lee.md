# Installing Sentencepiece
For more info see \scripts\wmt\README.md in main opennmt-tf project.

Clone https://github.com/google/sentencepiece#c-from-source

Created new conda environment opennmt-tf-sp from conda activate opennmt-tf

Install cmake 64 bit Windows from https://cmake.org/download/

Hmm this might be hard

Can we install for Windows direcly from here - https://github.com/google/sentencepiece/releases/tag/v0.1.4?

Downloaded it, put in program files, added to path. I.e. C:\Program Files\sentencepiece-0.1.4-win64\bin.


# Running scripts
Using git bash

This is needed for curl : https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058

Replace instances of wget with curl, and redirect output 

e.g. curl http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz > training-parallel-commoncrawl.tgz

cd C:/Users/LeeBorlace/Documents/GitHub/learning-ml/OpenNMT-tf/4-wmt

Was able to run my modified prepare_data.sh OK from bash shell.

The actual training I triggered manually from conda CMD prompt via

`onmt-main train_and_eval --model_type Transformer --config config/wmt_ende.yml --auto_config`.

Had to reduce batch size in the config first.