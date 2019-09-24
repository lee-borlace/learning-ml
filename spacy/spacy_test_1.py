import spacy

# MODEL = "en_core_web_sm"
MODEL = "en_core_web_lg"

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load(MODEL)

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

# Process whole documents
# text = ("When Sebastian Thrun started working on self-driving cars at "
#         "Google in 2007, few people outside of the company took him "
#         "seriously. “I can tell you very senior CEOs of major American "
#         "car companies would shake my hand and turn away because I wasn’t "
#         "worth talking to,” said Thrun, in an interview with Recode earlier "
#         "this week.")

text = "The man chased the boy with his gun"
doc = nlp(text)


for token in doc:
    print(f"TEXT={token.text},LEMMA={token.lemma_},POS={token.pos_},TAG={token.tag_},DEP={token.dep_}")
