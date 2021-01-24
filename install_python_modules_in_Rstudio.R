library(reticulate)
use_python("/usr/local/bin/python3")
py_available() # TRUE
py_install("biopython") # installed sucessfully
py_module_available("biopython") # FALSE