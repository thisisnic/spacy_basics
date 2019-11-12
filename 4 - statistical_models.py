# Statistical models enable spaCy to predict linguistic attributes in context, e.g.:
#  * part of speech tags
#  * syntactic dependencies
#  * named entities
# They are trained on labelled example texts, and can be fine tuned by updating with more examples.

# Predicting Part-of-speech Tags
import spacy

# Load the small English model
nlp = spacy.load('en_core_web_sm')

# Process a text
doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)

# In addition to the part-of-speech tags, we can also predict how the words are related. For example, whether a word is the subject of the sentence or an object.
# The "dep underscore" attribute returns the predicted dependency label.
# The head attribute returns the syntactic head token. You can also think of it as the parent token this word is attached to.

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

# "She" is nsubj, the nominal subject
# "pizza" is dobj, the direct object
# "the" is det, a determiner (article)

# We can also look at determining the named entities in a text
# Process a text
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)

# The explain method
# We can also get definitions for the most common tags and labels using the spacy dot explain helper function.
spacy.explain('GPE')
spacy.explain('NNP')
spacy.explain('dobj')
