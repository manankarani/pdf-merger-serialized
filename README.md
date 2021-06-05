# PDF Merger (Serialized)
This software can be used to merge N pdf with N pdfs, all serialized, the second file must have the tag "_A" at the end of the file name.
The file name from first and second folder should match with "_A" appended. To store the results the result folder is to be specified.

Eg. Folders
Folder A/
├ file1.pdf
├ file2.pdf
├ file3.pdf

Folder A/
├ file1_A.pdf
├ file2_A.pdf
├ file3_A.pdf

result_folder/

## Run
` pip install PyPDF2`
<br>
<br>
`python pdfmerger.py`

With this select folders from GUI and Merge the pdfs



