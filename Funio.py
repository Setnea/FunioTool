#! /usr/bin/python

import argparse
import re
import sys
import string
from itertools import product
from collections import OrderedDict

class Funio():
  
    def open_file(self, file_name):
      
        qfasta_file = open(file_name, "r")
        all_file = qfasta_file.readlines()
        qfasta_file.close()

        return all_file

    def save_file(self, outfile, all_file_list):
      
        output=open(outfile,"w")
        output.writelines(all_file_list)
        output.close()

#fast&easy method1 (only ACTG)  
    def search_primer(self, primseq, all_file_list):
   
        pattern=re.compile(primseq)
        i=0
        result= []
        for i in range(len(all_file_list)):
            if re.match("@", all_file_list[i]) != None:
	        result= pattern.split(all_file_list[i+1], 1)
	        all_file_list[i+1]= primseq + result[1]
	        length= len(result[0])
#	        print length
	        q_line= all_file_list[i+3]
	        all_file_list[i+3]= q_line[length:]
	    i+=1

        print all_file_list
        return all_file_list

#method2 (iupac code allowed)
    def find_matches(self, new_sequences, all_file_list):
        i=0
        result= []
        proba = []
        for i in range(len(all_file_list)):
            if re.match("@", all_file_list[i]) != None:
                j= 0
                tmp = []
                for j in range(len(new_sequences)):
                    tmp_seq = new_sequences[j]
                    pattern = re.compile(tmp_seq)
                    if pattern.findall(all_file_list[i+1]):
	                result= pattern.split(all_file_list[i+1], 1)
	                length= len(result[0])
                        tmp.append(length)     
                    j += 1
                if not tmp:
                    temp_line = all_file_list[i]
                    expl = "FUNIO NOTE= Unable to find typed sequence in:\n"
                    all_file_list[i] = expl + temp_line 
                else:
                   tmp.sort()
                   new_len= tmp[0]
	           q_line= all_file_list[i+1]
                   all_file_list[i+1]= q_line[new_len:]
	           seq_line= all_file_list[i+3]
                   all_file_list[i+3]= seq_line[new_len:]           
	    i+=1

        print all_file_list
        return all_file_list  

    def code_reco(self, sequence):
        iupac_marks = ""
        for i in sequence:
	    if (i != "A") and (i != "T") and (i != "C") and (i != "G"):
                iupac_marks += i
        return iupac_marks    

    def sequence_generator(self, sequence):
        str = sequence
        new_sequences = []
        new_sequences.append(''.join(str))
        i = 0
        for i in range(len(sequence)):
            if sequence[i] == "R":
                changed1 = [j.replace("R", "A") for j in new_sequences]
                changed2 = [j.replace("R", "G") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2              
            if sequence[i] == "Y":
                changed1 = [j.replace("Y", "C") for j in new_sequences]
                changed2 = [j.replace("Y", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2
            if sequence[i] == "S":
                changed1 = [j.replace("S", "G") for j in new_sequences]
                changed2 = [j.replace("S", "C") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2 
            if sequence[i] == "W":
                changed1 = [j.replace("W", "A") for j in new_sequences]
                changed2 = [j.replace("W", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2
            if sequence[i] == "K":
                changed1 = [j.replace("K", "G") for j in new_sequences]
                changed2 = [j.replace("K", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2
            if sequence[i] == "M":
                changed1 = [j.replace("M", "A") for j in new_sequences]
                changed2 = [j.replace("M", "C") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2
            if sequence[i] == "B":
                changed1 = [j.replace("B", "C") for j in new_sequences]
                changed2 = [j.replace("B", "G") for j in new_sequences]
                changed3 = [j.replace("B", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2 
                new_sequences += changed3
            if sequence[i] == "D":
                changed1 = [j.replace("D", "A") for j in new_sequences]
                changed2 = [j.replace("D", "G") for j in new_sequences]
                changed3 = [j.replace("D", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2 
                new_sequences += changed3
            if sequence[i] == "H":
                changed1 = [j.replace("H", "A") for j in new_sequences]
                changed2 = [j.replace("H", "C") for j in new_sequences]
                changed3 = [j.replace("H", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2 
                new_sequences += changed3
            if sequence[i] == "V":
                changed1 = [j.replace("V", "A") for j in new_sequences]
                changed2 = [j.replace("V", "C") for j in new_sequences]
                changed3 = [j.replace("V", "G") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2 
                new_sequences += changed3
            if sequence[i] == "N":
                changed1 = [j.replace("N", "A") for j in new_sequences]
                changed2 = [j.replace("N", "C") for j in new_sequences]
                changed3 = [j.replace("N", "G") for j in new_sequences]
                changed4 = [j.replace("N", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2 
                new_sequences += changed3
                new_sequences += changed4
            if sequence[i] == "-":
                changed1 = [j.replace("-", "A") for j in new_sequences]
                changed2 = [j.replace("-", "C") for j in new_sequences]
                changed3 = [j.replace("-", "G") for j in new_sequences]
                changed4 = [j.replace("-", "T") for j in new_sequences]
                new_sequences += changed1
                new_sequences += changed2 
                new_sequences += changed3
                new_sequences += changed4
            i += 1
# tidy-up       
        new_sequences = list(OrderedDict.fromkeys(new_sequences))
        del new_sequences[0]

        return new_sequences


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
    iupac_marks = []
    all_file_list = []
    feedback = []
    all_file_list = qf.open_file(args.i[0])
    if args.f != False:
        iupac_marks = qf.code_reco(args.f[0])
        if not iupac_marks:
                feedback = qf.search_primer(args.f[0], all_file_list)
        else:
                new_sequences = qf.sequence_generator(args.f[0])
                feedback = qf.find_matches(new_sequences, all_file_list)
        qf.save_file(args.o[0], feedback)
    else:
        qf.save_file(args.o[0], all_file_list)
    print "Data saved in chosen file."

if __name__ == "__main__":
	main()
