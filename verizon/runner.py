from verizon.code_generator import CodeGenerator

if __name__ == '__main__':

    cg = CodeGenerator()
    random_number = cg.generate_random_number()
    print(f"New 4 digit random code is : {random_number}")
    # obj1.calculate_n1()
    # obj1.calculate_n2()
    # obj1.calculate_n3()
    # obj1.calculate_n4()
    # obj1.generate_random_number()