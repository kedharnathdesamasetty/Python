import re

text = "apple,banana,grape,orange"
pattern = r","

split_result= re.split(pattern, text)
print("split result:", split_result)