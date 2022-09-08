import re

txt = "The rain in Spain"
x = re.search(r"\bi\w+", txt)
print(x.group())