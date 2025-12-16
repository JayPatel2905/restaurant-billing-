from bill import amount
def test_bill():
    order=[("coffee",20,2),
           ("tea",10,1)]
    assert amount(order)==52.5