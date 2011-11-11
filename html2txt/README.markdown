This subfolder is the implementation of the html2txt using boilerpipe library.
================================

The program will read each line from the urls.txt, and convert the html (from the url) to a .txt file and store in the /output folder.<br>
One run of the program will generate X .txt files in the /output folder, given X as number for url lines in the urls.txt<br>

Use the following two command-line to run the programme:<br>

        javac -d . -cp .;boilerpipe.jar  Html2txt.java
        java -cp .;boilerpipe.jar;nekohtml.jar;xerces.jar de.l3s.boilerpipe.demo.Html2txt