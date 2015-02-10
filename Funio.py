#! /usr/bin/python

import argparse
import re
import sys

class Funio():
  
    def open_file(self, file_name):
      
        qfasta_file = open(file_name, "r")
        all_file = qfasta_file.readlines()
        qfasta_file.close()

        return all_file
    
    def search_primer(self, primseq, all_file_list):
   
        pattern=re.compile(primseq)
        i=0
        result= []
        for i in range(len(all_file_list)):
            if re.match("@", all_file_list[i]) != None:
	        result= pattern.split(all_file_list[i+1], 1)
	        all_file_list[i+1]= primseq + result[1]
	        length= len(result[0])
	        q_line= all_file_list[i+3]
	        all_file_list[i+3]= q_line[length:]
	    i+=1

            print all_file_list
            return all_file_list

    
    def save_file(self, outfile, all_file_list):
      
        output=open(outfile,"w")
        output.writelines(all_file_list)
        output.close()

def main():

    parser = argparse.ArgumentParser( description='\nFunio is a tool designed for removing artificial sequences putted during preparation of library for sequencing. The aim is realized by comparison of the sequence of nucleotides typed in command line and the output file from sequencer in fastq format. Funio requires fastq files, commonly used for storing biological sequences and its quality, to work properly.' )
    parser.add_argument( '-i',
		metavar='<inputfile>', 
		type=str, 
		required=True, 
		nargs=1, 
		help='Specifies the filename of input. The input file should contain one or more sequences. Fastq format is required.' )
    parser.add_argument( '-o',
		metavar='<outputfile>', 
		type=str, 
		required=True, 
		nargs=1, 
		help='Specific the output filename containing the sequences and its quality data after removing specific sequences and corresponding quality data by filtering by given sequences' )
    parser.add_argument( '-f', 
		metavar='<type_sequence>', 
		type=str, 
		default=False, 
		nargs=1, 
		help='Specific the sequence that will be compared with the sequences from the input file. Capital letters are required.' )

    args = parser.parse_args()

    qf = Funio()
    all_file_list = []
    feedback = []
    all_file_list = qf.open_file(args.i[0])
    if args.f != False:
        feedback = qf.search_primer(args.f[0], all_file_list)
        qf.save_file(args.o[0], feedback)
    else:
        qf.save_file(args.o[0], all_file_list)
    print "Data saved in chosen file."

if __name__ == "__main__":
	main()
