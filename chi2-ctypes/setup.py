import os

from distutils.core import setup
from distutils import ccompiler

def build_ctypes_ext(name,sources):
    compiler=ccompiler.new_compiler()
    compiler.compile(sources)
    
    def get_onames(sources):
        o_names=[]
        for source in sources:
            (head,tail)=os.path.split(source)
            o_name=os.path.splitext(tail)[0]+'.o'
            o_names.append(os.path.join(head,o_name))
        
        return o_names
        
    compiler.link_shared_object(get_onames(sources),name+'.so')

build_ctypes_ext("_chi2",["_chi2.c"])

setup()
