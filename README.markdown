Toolkit for Privacy policy machine learning experiments
================================

This is the toolkit includes many command-line tools to help setup the experiments. <br>
With some refined datasets as well.


Toolkit
================================
**01_google_scraper.py** - gets urls from google search results and stores each url in a newline in txt file. Each txt file contains urls from 5 Google search pages.<br>
**02_excel_url_macro.vb** - transfer url text into hyperlinks automatically in Excel.<br>
**03_googler_scraper_csv** - gets urls and Google page numbers, store into a single csv with two columns.<br>
**04_csv2txt_single** - gets lines from .csv file and write each line into a .txt file.<br>
**05_csv2txt_multi** - gets lines from .csv file and write each line into a .txt file and store .txt files by labels into different folders.<br>
**06_paragraph_parser** - gets all the `<p>` and `<li>` paragraphs from an HTML given its url, stores each paragraph into a separate .txt file.<br>
**07_txt2csv** - translates each .txt files in the current folder into one row in a single .csv.<br>
**08_html2txt** - translates a whole .html page into a whole .txt file.<br>
**09_html2txt_extended** - well-refined version of html2txt, see print __doc__ for details.<br>
**10_html2txt_v3** - further improved version of html2txt, add in the library of html2text, more robust and close to the webpage now, see print __doc__ for details.<br>
**11_html2txt_v3_two_outputs** - v3 of html2txt exports into two files of each url using both HTML2Text and lxml.<br>

Datasets
================================
*Coming.*


Setup boilerpipe-1.2.0 in Python
================================
We use library biolderpipe for the finest way in extracting text from web pages, i.e. html2txt.
It is an open source java library, so, we need to port it in order to use it in Python, below we describe how to setup this up.

*Jython* 



Warning: Below are just sample text for further usage.
================================

Oh, and one thing I cannot stand is the mangling of words with multiple underscores in them like perform_complicated_task or do_this_and_do_that_and_another_thing.

A bit of the GitHub spice
-------------------------

In addition to the changes in the previous section, certain references are auto-linked:

* abc

Example
----------------------

Abc

> Abc

Table Example
-------------

<table>
  <tr>
    <th>ID</th><th>Name</th><th>Rank</th>
  </tr>
  <tr>
    <td>1</td><td>Tom Preston-Werner</td><td>Awesome</td>
  </tr>
  <tr>
    <td>2</td><td>Albert Einstein</td><td>Nearly as awesome</td>
  </tr>
</table>

Links Example
--------------------

[Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"