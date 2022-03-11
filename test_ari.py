from ari import *
def test_ari_emptychar():
     ret=ari_emptychar('')
     assert ret==0
def test_ari_alphanumeric():
     ret=ari_alphanumeric('!@##$%^')
     assert ret ==False
def test_ari_numcharectors():
     ret=ari_numcharectors('asd23423asd')
     assert ret==11
def test_ari_emptywords():
     ret=ari_emptyword('asdf')
     assert ret==None
def test_ari_numword():
     ret=ari_numword('i am a sick dog')
     assert ret==4
def test_ari_emptysentence():
     ret=ari_emptysentence('asdasfdasfasuhcbweucb asfdawfawfawf asfafaewf')
     assert ret==None
def test_ari_sentence():
     ret=ari_sentences('i am an idiot. what you think of me? dont feel bad. we are one!')
     assert ret==4