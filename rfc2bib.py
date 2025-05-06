#!/usr/bin/env python3
#URL_RFC_XML = 'ftp://ftp.rfc-editor.org/in-notes/rfc-index.xml'
URL_RFC_XML = 'https://www.rfc-editor.org/in-notes/rfc-index.xml'

from lxml import etree
import requests

BIB_ENTRY_FORMAT = """\
@techreport{%(key)s,
  title = {{%(title)s}},
  author = {%(author)s},
  type = {RFC},
  number = {%(number)s},
  institution = {IETF},
  month = %(month)s,
  year = %(year)s,
  url = {%(url)s},
}
"""

def tag_prefix(s):
    return '{https://www.rfc-editor.org/rfc-index}' + s

def normalize_authors(authors):
    # INPUT: a list of authors
    # OUTPUT: bib normalized authors
    # https://github.com/hupili/utility/blob/master/latex/tex-bib-author.py
    authors = filter(lambda a: a != '', map(lambda a: a.strip(), authors))
    authors_reversed = map(lambda a: a.split()[-1] + ', ' + ' '.join(a.split()[0:-1]), authors)
    return ' and '.join(authors_reversed)

index = etree.fromstring(requests.get(URL_RFC_XML).content)
rfcs = index.findall(tag_prefix('rfc-entry'))

#for r in rfcs[0:30]:
for r in rfcs:
    d = {}
    d['key'] = r.find(tag_prefix('doc-id')).text
    d['number'] = int(d['key'][3:])
    d['title'] = r.find(tag_prefix('title')).text
    _a = []
    for a in r.findall(tag_prefix('author')):
        _a += [a.find(tag_prefix('name')).text]
    d['author'] = normalize_authors(_a)
    d['year'] = r.find(tag_prefix('date')).find(tag_prefix('year')).text
    d['month'] = r.find(tag_prefix('date')).find(tag_prefix('month')).text[:3].lower()
    d['url'] = 'https://www.rfc-editor.org/rfc/rfc%s.txt' % d['number']
    #d['obsoletes'] = ','.join([o.find('doc-id').text for o in r.findall(tag_prefix('obsoletes'))])
    print(BIB_ENTRY_FORMAT % d)
