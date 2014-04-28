__author__ = 'jp242'
import os

def consolidateDocs(inDir,outFile):
    outFile = open(outFile, 'w')
    i = len(os.listdir(inDir))
    outFile.write(str(i) + "\n")
    for f in os.listdir(inDir):
        file = open(inDir + '/' + f, 'r')
        line = file.readline()
        tokens = []
        while line:
            tokens += line.split("\t")
            line = file.readline()
        ##outFile.write(f + " ")
        file.close()
        for token in tokens:
            outFile.write(token + " ")
        outFile.write("\n")
    outFile.close()



if __name__ == "__main__":
    inDir = "/Users/jp242/Documents/Projects/Lumi/decompressedFiles"
    outFile = "/Users/jp242/Documents/PhD-LDA/JGibbLDA-v.1.0/decompressed-files.txt"
    consolidateDocs(inDir,outFile)
