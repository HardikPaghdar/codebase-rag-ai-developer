import pytest
from codebase_rag.core import index,search

def test_cited_retrieval():
    chunks=index('examples/sample_repo'); hits=search('where is customer input validated',chunks)
    assert hits and hits[0]['path']=='customers.py' and hits[0]['start_line']>0

def test_bad_root():
    with pytest.raises(ValueError): index('not-a-real-repository')
