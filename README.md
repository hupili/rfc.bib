# RFC .bib

Output a `rfc.bib` readily for incorporation in your paper publications.

## Usage

Download [rfc.bib](https://raw.github.com/hupili/rfc.bib/master/rfc.bib)
and put in your paper directly.

OR

Generate `rfc.bib` yourself:

```
./prepare.sh
python rfc2bib.py > rfc.bib
```

## Resources

   * RFC Editor: <http://www.rfc-editor.org/rfc.html> 
   * The XML index: ftp://ftp.rfc-editor.org/in-notes/rfc-index.xml

## Why Yet Another?

There are several `rfc.bib` on the Internet.
However, they are not up-to-date.
GitHub is a good place for a community maintained `rfc.bib`.
When you find the `rfc.bib` is obsolete, you can:

   * File an issue to notify me.
   * Run the above commands to generate the new `rfc.bib` yourself.
   Even better: fork -- generate -- send pull request!
