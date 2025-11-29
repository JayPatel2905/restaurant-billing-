from bill import amount
from databaseconn import get_connection
def test_bill():
    order=[("coffee",20,2),
           ("tea",10,1)]
    assert amount(order)==52.5
def test_connection():
    conne=get_connection()
    assert conne.is_connected()
    conne.close