import os
from langchain_community.document_loaders import PyPDFLoader as pdf

data_load = pdf('https://ginger-rag-source.s3.us-west-2.amazonaws.com/EmployeeHandbook.pdf')

data_test = data_load.load_and_split()
print(len(data_test))
print(data_test[2])