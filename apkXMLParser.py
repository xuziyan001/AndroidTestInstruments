# -*- coding: utf-8 -*-

RDIR = 'C:\\Users\\ziyan.xzy\\Downloads\\'
WDIR = 'C:\\Users\\ziyan.xzy\\Desktop\\xmls\\'
FILE = 'UUGame.apk'
FILEW = FILE[:-4]+'\\'
WFILE = WDIR+FILEW+'AndroidManifest.xml'

import zipfile
from axmlparser.axmlprinter import AXMLPrinter
from xml.dom import minidom
import os
import re

def mkdir(path):
    path=path.strip()
    isExists = os.path.exists(path)
    if isExists:
        return False
    else:
        os.makedirs(path)
        return True
def findActivities(fileName):
    os.chdir(WFILE)
    stream = open('AndroidManifest.txt','r')
    pattern = r'<activity.*'
    prog = re.compile(pattern)
    for each in stream:
        match = prog.match(each)
        if match:
            print match.string,
    stream.close()
def xmlToTxt(fileName):
    mkdir(WDIR+FILE[:-4])
    with zipfile.ZipFile(RDIR+FILE,'r') as myzip:
        myzip.extract('AndroidManifest.xml',WFILE)
    os.chdir(WFILE)
    ap = AXMLPrinter(open('AndroidManifest.xml','rb').read())
    buf = minidom.parseString(ap.getBuff()).toxml()
    fp = open('AndroidManifest.txt','w+')
    for eachline in buf:
        fp.write(eachline)
    fp.close()
def main():
    #findActivities(FILE)
    xmlToTxt(FILE)
    

if __name__ == "__main__":
    main()
