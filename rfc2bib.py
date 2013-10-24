#-*-coding:utf-8-*-

# One sample entry
#>>> print lxml.etree.tostring(r)
#<rfc-entry xmlns="http://www.rfc-editor.org/rfc-index" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
#        <doc-id>RFC6918</doc-id>
#        <title>Formally Deprecating Some ICMPv4 Message Types</title>
#        <author>
#            <name>F. Gont</name>
#        </author>
#        <author>
#            <name>C. Pignataro</name>
#        </author>
#        <date>
#            <month>April</month>
#            <year>2013</year>
#        </date>
#        <format>
#            <file-format>ASCII</file-format>
#            <char-count>13639</char-count>
#            <page-count>8</page-count>
#        </format>
#        <keywords>
#            <kw>IANA</kw>
#            <kw>IPv4 Options</kw>
#        </keywords>
#        <abstract><p>A number of ICMPv4 message types have become obsolete in practice, but have never been formally deprecated.  This document deprecates such ICMPv4 message types, thus cleaning up the corresponding IANA registry.  Additionally, it updates RFC 792 and RFC 950, obsoletes RFC 1788, and requests the RFC Editor to change the status of RFC 1788 to Historic.</p></abstract>
#        <draft>draft-gp-obsolete-icmp-types-iana-01</draft>
#        <obsoletes>
#            <doc-id>RFC1788</doc-id>
#        </obsoletes>
#        <updates>
#            <doc-id>RFC0792</doc-id>
#            <doc-id>RFC0950</doc-id>
#        </updates>
#        <current-status>PROPOSED STANDARD</current-status>
#        <publication-status>PROPOSED STANDARD</publication-status>
#        <stream>IETF</stream>
#        <wg_acronym>NON WORKING GROUP</wg_acronym>
#    </rfc-entry>

from lxml import etree
import jinja2

def tag_prefix(s):
    return '{http://www.rfc-editor.org/rfc-index}' + s

def normalize_authors(authors):
    # INPUT: a list of authors
    # OUTPUT: bib normalized authors
    # https://github.com/hupili/utility/blob/master/latex/tex-bib-author.py
    authors = filter(lambda a: a != u'', map(lambda a: unicode.strip(a.decode('utf-8')), authors))
    authors_reversed = map(lambda a: a.split()[-1] + u', ' + u' '.join(a.split()[0:-1]), authors)
    return unicode(u' and '.join(authors_reversed))

# ref: https://raw.github.com/hupili/tutorial/master/README.tpl.md
#      https://github.com/hupili/tutorial/blob/master/render_readme.py
#
template = jinja2.Template(open('bib-entry.tpl').read())
def render_bib(data):
    return template.render(data)

index = etree.fromstring(open('rfc-index.xml').read())
rfcs = index.findall(tag_prefix('rfc-entry'))

#for r in rfcs[0:30]:
for r in rfcs:
    d = {}
    d['key'] = r.find(tag_prefix('doc-id')).text
    d['title'] = r.find(tag_prefix('title')).text
    _a = []
    for a in r.findall(tag_prefix('author')):
        _a += [a.find(tag_prefix('name')).text]
    d['author'] = normalize_authors(_a)
    d['year'] = r.find(tag_prefix('date')).find(tag_prefix('year')).text
    d['month'] = r.find(tag_prefix('date')).find(tag_prefix('month')).text
    #d['obsoletes'] = ','.join([o.find('doc-id').text for o in r.findall(tag_prefix('obsoletes'))])
    print render_bib(d)
