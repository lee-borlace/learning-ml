# Getting it running - quick start
http://opennmt.net/OpenNMT-tf/quickstart.html

`conda activate OpenNMT-tf`
`onmt-build-vocab --size 50000 --save_vocab src-vocab.txt src-train.txt`
`onmt-build-vocab --size 50000 --save_vocab tgt-vocab.txt tgt-train.txt`
`onmt-main train_and_eval --model_type NMTSmall --auto_config --config data.yml`

`tensorboard --logdir="run"` - have to hit at localhost:6006

## Export issue
Will often get this late in the process :
`tensorflow.python.framework.errors_impl.NotFoundError: Failed to create a directory: run/export\latest\temp-b'1569242016'; No such file or directory`

Maybe run as administrator? Here is manual export command :

`onmt-main export --model_type NMTSmall --auto_config --config data.yml --export_dir_base export`

Hmm no, the above works even when not running as admin - must behave differently when exporting automatically


