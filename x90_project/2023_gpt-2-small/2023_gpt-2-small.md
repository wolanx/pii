# doc

废话生成，给一小段话，然后接着往下写。
[encoder.json](models%2F124M%2Fencoder.json)
- 深度好文 [GPT in 60 Lines of NumPy](https://jaykmody.com/blog/gpt-from-scratch)
- 作者的 tiny 版本 [picoGPT](https://github.com/jaymody/picoGPT)

# pip install

```text
numpy==1.24.1 # used for the actual model code/weights
regex==2017.4.5 # used by the bpe tokenizer
requests==2.27.1 # used to download gpt-2 files from openai
tensorflow==2.11.0 # used to load the gpt-2 weights from the open-ai tf checkpoint
tqdm==4.64.0 # progress bar to keep your sanity
fire==0.5.0 # easy CLI creation
```

## use

```shell
python gpt2.py "Alan Turing theorized that computers would one day become"
# output
ERROR:tensorflow:Couldn't match files for checkpoint models\124M\model.ckpt
Fetching checkpoint: 1.00kit [00:00, 1.24Mit/s]                                                     
Fetching encoder.json: 1.04Mit [00:00, 1.23Mit/s]                                                   
Fetching hparams.json: 1.00[encoder.cpython-39.pyc](__pycache__%2Fencoder.cpython-39.pyc)kit [00:00, 966kit/s]                                                    
Fetching model.ckpt.data-00000-of-00001: 498Mit [05:21, 1.55Mit/s]                                  
Fetching model.ckpt.index: 6.00kit [00:00, 2.54Mit/s]                                               
Fetching model.ckpt.meta: 472kit [00:01, 332kit/s]                                                  
Fetching vocab.bpe: 457kit [00:02, 162kit/s]

# result
generating: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 40/40 [00:22<00:00,  1.80it/s]
 the most powerful machines on the planet.

The computer is a machine that can perform complex calculations, and it can perform these calculations in a way that is very similar to the human brain.
```

