Tests for Grader/dector
================================

Excel file that holds the test results for Chrome grader/detector

Columns:
================================
**Page** - page number from Google search<br>
<br>
**PP?** - mark '1' if it is a privacy policy page<br>
**Sum?** - mark '1' if it is a summary page about the company/website's privacy policy.<br>
**Other** - mark '
<br>
**Grade** - grade<br>
**Detect** - dectect score<br>
<br>
**TP** - mark '1' if True Positive <br>
**TN** - mark '1' if True Negative <br>
**FP** - mark '1' if False Positive <br>
**FN** - mark '1' if False Negative <br>
<br>
**SumRecog** - mark '1' if it is chosen as Sum, and it is recoginized by the detector, in this case, also record the grades <br>
**SumUn** - mark '1' if it is chosen as Sum, but this summary is un-recoginizable by the detector<br>
<br>
**NonHTML** - mark '1' when the search result returns some other file formats that are not displayed by the broswer, e.g. pdf or doc.