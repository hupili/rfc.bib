# RFC .bib

Output a `rfc.bib` readily for incorporation in your paper publications.

## Usage

Download [rfc.bib](https://raw.github.com/hupili/rfc.bib/master/rfc.bib)
and put in your paper directly.

OR

Generate `rfc.bib` yourself:

   * Install dependencies: `[sudo] pip install -r requirements.txt`
   * Generate: `python rfc2bib.py > rfc.bib`

The script download XML version of RFC from the website.
It may take some time to finish.

## Resources

   * RFC Editor: <http://www.rfc-editor.org/rfc.html>
   * The XML index:
   [ftp](ftp://ftp.rfc-editor.org/in-notes/rfc-index.xml)
   [http](http://www.rfc-editor.org/in-notes/rfc-index.xml)

## Why Yet Another?

There are several `rfc.bib` on the Internet.
However, they are not up-to-date.
GitHub is a good place for a community maintained `rfc.bib`.
When you find the `rfc.bib` is obsolete, you can:

   * File an issue to notify me.
   * Run the above commands to generate the new `rfc.bib` yourself.
   * Even better: fork -- generate -- send pull request!

## License

MIT
