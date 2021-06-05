# PDF Merger (Serialized)
This software can be used to merge N pdf with N pdfs, all serialized, the second file must have the tag "_A" at the end of the file name.
The file name from first and second folder should match with "_A" appended. To store the results the result folder is to be specified.

Eg. Folders <br>
Folder A/ <br>
├ file1.pdf <br>
├ file2.pdf <br>
├ file3.pdf <br>
<br>
Folder A/ <br>
├ file1_A.pdf <br>
├ file2_A.pdf <br>
├ file3_A.pdf <br>

result_folder/

## Run
` pip install PyPDF2`
<br>
<br>
`python pdfmerger.py`

With this select folders from GUI and Merge the pdfs



