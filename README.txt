# FunioTool
Funio is a tool designed for removing artificial sequences put during preparation of library for sequencing. 
The aim is realized by comparison of the sequence of nucleotides typed in command line and the output file from sequencer in fastq format.
Funio requires fastq files, commonly used for storing biological sequences and its quality, to work properly. 

Command line usage:
Funio is run from the command line as follows:
-i <input file>	// Specifies the filename of input. 
  The input file should contain one or more sequences. Fastq format is required.
-f <sequence> // Specifies the sequence that will be compared with the sequences from the input file. 
  Capital letters are required.
-o <output file> 	// Specifies the output filename.
  Output file containing the sequences and its quality data after removing specific sequences and corresponding quality data by filtering by given sequences.
