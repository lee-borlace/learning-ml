# Getting it running - quick start
http://opennmt.net/OpenNMT-tf/quickstart.html

`conda activate OpenNMT-tf`
`onmt-build-vocab --size 50000 --save_vocab src-vocab.txt src-train.txt`
`onmt-build-vocab --size 50000 --save_vocab tgt-vocab.txt tgt-train.txt`
`onmt-main train_and_eval --model_type NMTSmall --auto_config --config data.yml`

`tensorboard --logdir="run"` - have to hit at localhost instead of using host name

`onmt-main train_and_eval --model_type Transformer --auto_config --config data.yml`

Error I got back :

```
  (1) Resource exhausted: OOM when allocating tensor with shape[122,25,35820] and type float on /job:localhost/replica:0/task:0/device:GPU:0 by allocator GPU_0_bfc
         [[node one_hot (defined at c:\users\leeborlace\anaconda3\envs\opennmt-tf\lib\site-packages\opennmt\utils\losses.py:14) ]]
Hint: If you want to see a list of allocated tensors when OOM happens, add report_tensor_allocations_upon_oom to RunOptions for current allocation info.
```

Tried to address by changing config to use this :

train:
  batch_size: 64



