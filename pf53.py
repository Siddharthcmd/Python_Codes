# PF-Assgn-53
# This verification is based on string match.
import re

poem = '''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aiching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

# Note: Triple quotes can be used to enclose Strings which has lines of text.

# Write your logic here for question 1

print("number of times on 'v' appreres in the poem:")
pattern = re.compile(r"v")
matches = pattern.findall(poem)
print(len(matches))

print("removing all the new lines:")
print(re.sub("\n", " ", poem))

print("If a word has 'ch' or 'co', replace it with 'Ch' or 'Co'.")
string1 = re.sub(r"co", r"Co", poem)
string2 = re.sub(r"ch", r"Ch", string1)
print(string2)

print("If the pattern has characters 'ai' or 'hi', replace the next three characters with *\*")
print(re.sub(r'(ai|hi)\w{3}', r'\1*\*', poem))
