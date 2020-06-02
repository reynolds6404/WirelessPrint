from time import sleep
import os
#installed with "sudo apt-get install python-cups"
import cups

#main function to runn program. Not currently needed, but anticipating future functionality
def main():
	fileManagement('/home/pi/Printer/Queue')

#prints files in the queue (filepath) then deletes them
def fileManagement(filepath):
	for fileToPrint in os.listdir(filepath):
		printFile(filepath + str(fileToPrint))
		os.remove(filepath + str(fileToPrint))
	
#function for printing files. Called in fileManagement function	
def printFile(fileToPrint):
	conn = cups.Connection()
	printers = conn.getPrinters()
	printer_name = printers.keys()[0]
	conn.printFile(printer_name,fileToPrint, "", {}) 


main()
