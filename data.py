# -*- coding: utf-8 -*-
import os
import datetime


def getDate(strDate):
    print(str(strDate))
    return datetime.datetime.strptime(str(strDate), '%Y%m%d').date()

def iter_documents(top_directory, source, fromDate, toDate):
    """
    Generator: iterate over all relevant documents, yielding one
    document (=list of utf8 tokens) at a time.
    """
    print("iter_document")
    # find all .json documents, no matter how deep under top_directory
    for root, dirs, files in os.walk(top_directory):
        print("root::" + str(root))
        print("dirs::" + str(dirs))
        if( source in root):
            print("files ::" + str(files))
            for fname in filter(lambda fname: fname.endswith('.json'), files):
                # read each document as one big string
                print(fname)
                splitfilename = fname.split('.json')
                fileDate = getDate(splitfilename[0])
                frmDate = getDate(fromDate)
                tDate = getDate(toDate)
                if(fileDate >= frmDate and fileDate <= tDate ):
                    document = open(os.path.join(root, fname)).read()
                    # break document into utf8 tokens
                    yield document
                else:
                    continue
        else:
            continue
        
class TxtSubdirsCorpus(object):
    """
    Iterable: on each iteration, return bag-of-words vectors,
    one vector for each document.
 
    Process one document at a time using generators, never
    load the entire corpus into RAM.
 
    """
    def __init__(self, top_dir, source, fromDate, toDate):
        self.top_dir = top_dir
        self.source = source
        self.toDate = toDate
        self.fromDate = fromDate
        # create dictionary = mapping for documents => sparse vectors
        self.dictionary = iter_documents(top_dir, source, fromDate, toDate)
 
    def __iter__(self):
        """
        Again, __iter__ is a generator => TxtSubdirsCorpus is a streamed iterable.
        """
        for tokens in iter_documents(self.top_dir, self.source, self.fromDate, self.toDate):
            # transform tokens (strings) into a sparse vector, one at a time
            yield tokens

if __name__ == "__main__":
 
# that's it! the streamed corpus of sparse vectors is ready
    corpus = TxtSubdirsCorpus('rawdata', 'Reuters', '20180524', '20180526')
 
# print the corpus vectors
    for vector in corpus:
        print(vector)
 