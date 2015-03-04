#!/usr/bin/python

import Funio
from Tkinter import *
from tkFileDialog import *

if __name__ == "__main__":

    class layout:
    
        def __init__(self, parent):

# Separator (start)
            sep = Frame(parent, width=2, bd=2, bg='grey')
            sep.pack(fill=X, expand=1)    
# Separator (end)

# Filter section.
            self.frmFilt = Frame(parent, bd=5)
            self.frmFilt.pack()

            self.labelFilt = Label(self.frmFilt, text='\nType sequence (capital letters required)\n', width=35)
            self.labelFilt.pack(side=LEFT) 

            self.userexp = StringVar()
            self.boxExp = Entry(self.frmFilt, width=22, textvariable=self.userexp)
            self.boxExp.pack(side=LEFT) 

# Separator (start)
            sep = Frame(parent, width=2, bd=2, bg='grey')
            sep.pack(fill=X, expand=1)    
# Separator (end)

# Input file section.
            self.frmInfile = Frame(parent, bd=5)         
            self.frmInfile.pack()

            self.labelIn = Label(self.frmInfile, text='Input File', width=15)
            self.labelIn.pack(side=LEFT)

            self.inFilePath = StringVar()
            self.boxIn = Entry(self.frmInfile, width=22, textvariable=self.inFilePath)
            self.boxIn.pack(side=LEFT)

            self.bInFile = Button(self.frmInfile, text='Browse', command=self.bBrowseInClick)
            self.bInFile.pack(side=LEFT)

# Output file section.
            self.frmOutfile = Frame(parent, bd=5)
            self.frmOutfile.pack()

            self.labelOut = Label(self.frmOutfile, text='Output File', width=15)
            self.labelOut.pack(side=LEFT) 

            self.outFilePath = StringVar()
            self.boxOut = Entry(self.frmOutfile, width=22, textvariable=self.outFilePath)
            self.boxOut.pack(side=LEFT) 

            self.bOutFile = Button(self.frmOutfile, text='Browse', command=self.bBrowseOutClick)
            self.bOutFile.pack(side=LEFT) 

# Separator (start)
            sep = Frame(parent, width=2, bd=2, bg='grey')
            sep.pack(fill=X, expand=1)    
# Separator (end)

# "Run" button section
            self.frmRun = Frame(parent, bd=5)
            self.frmRun.pack()

            self.bRun = Button(self.frmRun, text='Run', command=self.bRunClick) 
	    self.bRun.pack()

# Browse input_file button
        def bBrowseInClick(self):             
            rFilepath = askopenfilename(
		defaultextension='*', 
		initialdir='.', 
		initialfile='', 
		parent=self.frmInfile, 	
		title='Select input file')
            self.inFilePath.set(rFilepath)
            print self.boxIn.get()

# Browse output_file button    
        def bBrowseOutClick(self):
            rFilepath = asksaveasfilename(
		defaultextension='*', 
		initialdir='.', 
		initialfile='', 
		parent=self.frmInfile, 
		title='Select output file') 
            self.outFilePath.set(rFilepath)
            print self.boxOut.get()
            
# "Help" button  
        def bRunClick(self):
            inputFilePath = str(self.inFilePath.get())
            outputFilePath = str(self.outFilePath.get())
            typed_seq = str(self.userexp.get())
            qf= Funio.Funio()

            try:
                all_file_list = qf.open_file(inputFilePath)
                if len(typed_seq) == 0:
                    print "\nType sequence to compare with data."
                else:
                    iupac_marks = qf.code_reco(typed_seq)
                    if not iupac_marks:
                        feedback = qf.search_primer(typed_seq, all_file_list)
                    else:
                        new_sequences = qf.sequence_generator(typed_seq)
                        feedback = qf.find_matches(new_sequences, all_file_list)
                    try:
                        qf.save_file(outputFilePath, feedback)
                        print "\nData saved in chosen file."
                    except IOError:
                        print "Choose output file to save currently display data." 
            except IOError:
                print "Choose input file"


    root = Tk()
    root.title("Funio")
    root.geometry("500x250+100+40")
    gui = layout(root)
    root.mainloop()
