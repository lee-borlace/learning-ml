import spacy

# Comment in a large or small model depending on how long you want to wait :)
#MODEL = "en_core_web_sm"
MODEL = "en_core_web_lg"

# Load English tokenizer, tagger, parser, NER and word vectors
print(f"Loading spaCy model {MODEL}...")
nlp = spacy.load(MODEL)
print("Done")

print("************ Mucking around with parsing ************")

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

# text = "The man chased the boy with his arm"
text = "what did the green cat eat?"

doc = nlp(text)

for token in doc:
    print(f"TEXT={token.text},LEMMA={token.lemma_},POS={token.pos_},TAG={token.tag_},DEP={token.dep_}")




print("************ Mucking around with co-reference ************")

print(f"Coref clusters : {doc._.coref_clusters}")
print(f"Doc with resolved references : '{doc._.coref_resolved}'")







print("************ Mucking around with vector similarity ************")
doc1 = nlp("I want to order a bike")
doc2 = nlp("I'd like to request a bicycle")
doc3 = nlp("quack quack quack")

print(f"Similarity between '{doc1}' and '{doc2}' : {doc1.similarity(doc2)}")
print(f"Similarity between '{doc1}' and '{doc3}' : {doc1.similarity(doc3)}")


