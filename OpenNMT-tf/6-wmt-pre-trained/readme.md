This is based on http://opennmt.net/Models-tf/

Download the files from there

Extract to this current folder. Make sure you don't check them into source control!

There is more info at *Lazy Run* section of https://github.com/OpenNMT/OpenNMT-tf/tree/master/scripts/wmt

Extract *averaged-ende-export500k.tar.gz* directly as it will create its own folder.

Extract *averaged-ende-ckpt500k.tar.gz* into new folder *checkpointdata*

Extract the files buried deep in *wmt_ende_sp_model.tar.gz* to the current folder.

Extract all the files of *wmt_ende_sp.tar.gz* into new *data* folder

Install Sentencepiece from https://github.com/google/sentencepiece/releases/tag/v0.1.4 and put it in PATH

`onmt-main infer --model_type Transformer --config config/wmt_ende.yml --auto_config --checkpoint_path=averaged-ende-export500k/1554540232 --features_file data/test.en > data/test.generated.encoded.de`

`spm_decode --model=data/wmt$sl$tl.model --input_format=piece < data/$testset-src.hyp.$tl > data/$testset-src.hyp.detok.$tl`            

