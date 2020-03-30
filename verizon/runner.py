from verizon.code_generator import CodeGenerator

if __name__ == '__main__':

    cg = CodeGenerator()
    random_number = cg.generate_random_number()
    print(f"New 4 digit random code is : {random_number}")
    #cg.get_pi_value(3,4,5,7)
