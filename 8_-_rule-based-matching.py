# Why not just match based on regex?
#  Compared to regular expressions, the matcher works with Doc and Token objects instead of only strings.
#  It's also more flexible: you can search for texts but also other lexical attributes.
#  You can even write rules that use the model's predictions.
#  For example, find the word "duck" only if it's a verb, not a noun.

# We can match on exact token texts:
# [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]

# or match on lexical attributes, e.g. two tokens whose lowercase forms are "iphone" and "x"
# [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# we can also match based on attributes predicted by the model

# [{'LEMMA': 'buy'}, {'POS

import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a model and create the nlp object
nlp = spacy.load('en_core_web_sm')

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]

# The parameters here are:
# 1) a unique ID to identify which pattern is matched
# 2) an optional callback
# 3) the pattern itself
matcher.add('IPHONE_PATTERN', None, pattern)

# Process some text
doc = nlp("New iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)

# The matcher returns a list of tuples.  Each tuple consists of three values:
# 1) the match ID
# 2) the start index
# 3) the end index of the matched span.

# This means we can iterate over the matches and create a Span object: a slice of the doc at the start and end index.

# Call the matcher on the doc
doc = nlp("New iPhone X release date leaked")
matches = matcher(doc)

print(matches)

# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)
