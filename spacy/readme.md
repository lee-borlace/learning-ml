# Info
https://spacy.io/usage

# Getting started
`pip install -U spacy`
`pip install -U neuralcoref`
`python -m spacy download en_core_web_s`
`python -m spacy download en_core_web_lg`

Might need the following if there's an error such as 'size changed, may indicate binary incompatibility' when running with neural coref
`pip uninstall neuralcoref`
`pip install neuralcoref --no-binary neuralcoref`