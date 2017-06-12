import PyPDF2
import re
import string
from collections import Counter
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def isint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

print('Enter\n 1. The Fellowship of the Ring\n2. The Two Towers\n3. The Return of the King')

num1=int(input())
if (num1==1):
    str2='fotr.pdf'
    str1='Fellowship of the Ring'
elif (num1==2):
    str2='two_towers.pdf'
    str1='Two Towers'
else:
    str2='return.pdf'
    str1='Return of the King'

print(num1)

pdfFileObj = open(str2, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages=pdfReader.numPages
my_string=""

for i in range (pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    my_string+=pageObj.extractText()

my_string=my_string.lower()
for c in string.punctuation:
    my_string=my_string.replace(c,"")

STOPWORDS.add('Chapter')
#STOPWORDS.add('THE')
#STOPWORDS.add('The')
#STOPWORDS.add('A')

wordcloud = WordCloud(    stopwords=STOPWORDS,
                          random_state=1,
                          background_color='white',
                          width=1200,
                          height=1200
                         ).generate(my_string)

plt.title(str1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

def count_text(text):
  # Split text into words based on whitespace.  Simple but effective.
  words = re.split("\s+", text)
  words=[word for word in words if word not in STOPWORDS]
  words=[word for word in words if (isint(word)==False)]
  for word in words:
      word=word.lower()
      
  # Count up the occurence of each word.; 
  return Counter(words)

x=(count_text(my_string))
print(x.most_common(5))
#print(count_text(my_string).most_common())
