#Sorts integers provided via a file named 'data.txt' via insert sort and exports the 
# sorted list to a file named 'insert.txt'
#Author: Shawn McMannis
#Last mod date: 4/5/19

toSort = []

#open the export file
exportFile = open("insert.txt", "w")

#open import file 'data.txt'
with open("data.txt", "r") as importFile:
    for line in importFile:

        #save the value string as a list, delimited by ' '
        toSort = line.split()

        #remove the first integer value from the list
        del toSort[0]

        #sort the list with insertion sort
        for i in range(1, len(toSort)):
            key = int(toSort[i])
            j = i - 1
            while j >= 0 and key < int(toSort[j]):
                toSort[j + 1] = toSort[j]
                j -= 1
            toSort[j + 1] = key

        #save the sorted list to 'insert.txt'
        for num in toSort:
            exportFile.write(str(num))
            exportFile.write(" ")
        exportFile.write("\n")

#close export file
exportFile.close()