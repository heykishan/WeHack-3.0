import re
import csv
import sys

#def csv write

print("isMosFET\n")
isMosFet = input()

print("isMutiplexer\n")
isMultiplexer = input()

print("isAOFET\n")
isAOFET = input()

print("isSMODFET\n")
isSMODFET = input()

print("isBJT\n")
isBJT = input()

row = [isMosFet, isMultiplexer, isAOFET, isSMODFET, isBJT]


with open('test.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(row)

print("c")

writeFile.close()


with open('test.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)

print(lines)

readFile.close()

# from pdf import PdfFileReader, PdfFileWriter

# pdf = pdf.PdfFileReader(open("faultInsertion.pdf", "rb"))
# for page in pdf.pages:
#     print(page.extractText())
