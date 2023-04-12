sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
#Store variable for the original sentence
sentence2 = sentence.replace("!"," ")
# Replacing the exclamation mark with a space
sentence3 = sentence2.upper()
# Turning the previous sentence into capital leters
sentence4 = sentence2[::-1]
# Reversing the entire sentence
print(f"The original sentence: {sentence}")
print(f"Removing the exclamation marks: {sentence2}")
print(f"The same sentence in capitals: {sentence3}")
print(f"The sentence in reverse: {sentence4}")
# Testing use of the f-string to print the sentences - would probsbly be more useful when filling in gaps within sentences