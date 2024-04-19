**Links From Pc reasearch:**
https://github.com/ggerganov/llama.cpp
https://github.com/abetlen/llama-cpp-python

Llama download
- https://llama.meta.com/llama-downloads/

I found python Inbuilt liberaries
 - https://pypi.org/project/aitextgen/


Youtube video I found to be Usefull
 - https://youtu.be/C3-SkB1s9bs?si=mhUM5W1aDq4dNF80

**Commands I used:**
- pip install llama-cpp-python
- pip install llama-index

update the python above 3.9

python3 -m torch.distributed.run --nproc_per_node 1 example_chat_completion.py --ckpt_dir llama-2-7b-chat/ --tokenizer_path tokenizer.model --max_seq_len 512 --max_batch_size 6
