# Freemind Auto Link

The Freemind mind mapping program allows to link nodes to files. For my master
thesis, I have the PDF files I read in a single directory. The file names
(without the `.pdf`) are used as child nodes when I want to cite that PDF.

Manually creating the links is a waste of time. This program will read in the
mind map and automatically create the links for all the files on nodes that are
not linked properly yet.

Needs Python 3 and lxml.
