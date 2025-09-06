class MyExceptions(Exception):

    def __init__(self, msg="erro occured"):
        self.msg=msg
                 
                 
        super().__init__(self.msg)

        
    








def sample_test():
    try:
        a=int(input("enter the value a "))
        b=int(input("enter the value b"))
        if a < b:
            raise MyExceptions(f'a{a} value must b greater then b')
        else:
            print('both values test successfully')
    except MyExceptions as e:
        print(f'error occured {e}')        




sample_test()