# Info
https://spacy.io/usage
https://github.com/huggingface/neuralcoref

# Getting started
`pip install spacy==2.1.0`
`pip install neuralcoref --no-binary neuralcoref`

See these issues as to why spacy and neuralcoref needed to be installed that way -

https://github.com/huggingface/neuralcoref/issues/158
https://github.com/huggingface/neuralcoref/issues/103
https://github.com/explosion/spaCy/issues/2798

Several differently-sized language models -
`python -m spacy download en_core_web_sm`
`python -m spacy download en_core_web_lg`