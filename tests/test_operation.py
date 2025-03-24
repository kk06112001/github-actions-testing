from src.maths_operation import add,sub

def test_add():
    assert add(2,4)==5
    assert add(1,1)==2
    assert add(2,4)==6
    
def test_sub():
    assert sub(9,2)==7
    assert sub(8,4)==4
    
    