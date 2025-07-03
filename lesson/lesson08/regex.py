import re

text = """
SoftServe Academy is a part of the Talent Acceleration Center at SoftServe University.

Here you can find different learning solutions and get job-ready skills to start a career in IT. Take it as a challenge! Come for experience and build your future with us!
"""

pattern = "IT"

resul = re.match(pattern, text)
print(resul)

pattern = "SoftServe"

resul = re.search(pattern, text)
print(resul)
print(resul.group(0))
print(resul.group(0))


pattern = "[a-z]{3} "

resul = re.findall(pattern, text)
print(resul)

reg = re.compile(" [a-z]{3} ")

print(reg.findall(text))

print(re.findall("[youcans]{2,4}", text))