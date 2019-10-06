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

# Missing test / val data
This all worked quite well, except I realised there was no val / test data, so that part was failing (BLEU validation).

input-from-sgm.perl is empty, so I assume these all did nothing :

```
if true; then
 perl input-from-sgm.perl < $TEST_PATH/$validset-src.$sl.sgm \
    | spm_encode --model=wmt$sl$tl.model > data/valid.$sl
 perl input-from-sgm.perl < $TEST_PATH/$validset-ref.$tl.sgm \
    | spm_encode --model=wmt$sl$tl.model > data/valid.$tl
 perl input-from-sgm.perl < $TEST_PATH/$testset-src.$sl.sgm \
    | spm_encode --model=wmt$sl$tl.model > data/test.$sl
 perl input-from-sgm.perl < $TEST_PATH/$testset-ref.$tl.sgm \
    | spm_encode --model=wmt$sl$tl.model > data/test.$tl
fi
```

This is where it should have been : https://raw.githubusercontent.com/OpenNMT/OpenNMT-tf/master/third_party/input-from-sgm.perl. Doesn't exist any more!

I found that file here from main opennmt-tf repo : \OpenNMT-tf\third_party and copied into this current folder.

I backed up previous data folders and created copy of main data prep script to re-prep the test and train data.

prepare_data_test_val._only.sh

It also needed to re-generate the SP model first (more complex!) as those lines above needed it, but it had been deleted!

Run it :

`.\prepare_data_limited.sh raw_data`


