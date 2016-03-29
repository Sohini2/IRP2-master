import json
from pprint import pprint
import urllib2
from textblob import TextBlob

'''
import goslate
gs = goslate.Goslate()
print(gs.translate('hello world', 'de'))
'''
text = "violin"
blob = TextBlob(text)

text_new = blob.translate(to="de") #german
text_new_french = blob.translate(to="fr") #french
print 'german - '+str(text_new)
print 'french - '+str(text_new_french)