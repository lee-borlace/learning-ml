# Getting it running - quick start
http://opennmt.net/OpenNMT-tf/quickstart.html

`conda activate OpenNMT-tf`
`onmt-build-vocab --size 50000 --save_vocab src-vocab.txt src-train.txt`
`onmt-build-vocab --size 50000 --save_vocab tgt-vocab.txt tgt-train.txt`

## Notes on V2 and Windows Incompatibility
V 2.X has been released now - https://github.com/OpenNMT/OpenNMT-tf/releases/tag/v2.0.1

There is a problem with one of the dependencies though - tensorflow-addons has no Windows version yet - https://github.com/tensorflow/addons/issues/222.

For now, just install the latest 1.X.X version of opennmt-tf and corresponding tensorflow -

`pip install OpenNMT-tf==1.25.1`
``



# Training
`onmt-main train_and_eval --model_type NMTSmall --auto_config --config data.yml`

`tensorboard --logdir="run"` - have to hit at localhost:6006

# Export issue
Was getting this in the process :
`tensorflow.python.framework.errors_impl.NotFoundError: Failed to create a directory: run/export\latest\temp-b'1569242016'; No such file or directory`

Seems to be fixed by using `model_dir: run` instead of `model_dir: run\` in data.yml

# Inferring
`onmt-main infer --auto_config --config data.yml --features_file src-test.txt > tgt-test-temp.txt`