class eighthgrademath:
    pi = 3.1415
    import math
    import time
    def ymxb():
        ymxb = float(input("Input B "))
        ymxm = float(input("Input M/slope decimal please "))
        ymxx = float(input("Input X "))
        ymxbc = (ymxm * ymxx) + ymxb
        ymxbs = str(ymxbc)
        print("The answer is " + ymxbs)
    def slope():
        y1 = float(input("what is your y1? "))
        y2 = float(input("what is your y2? "))
        x1 = float(input("what is your x1? "))
        x2 = float(input("what is your x2? "))
        s1 = y2 - y1
        s2 = x2 - x1
        s3 = s1 / s2
        print(s3)
    def Y_from_a_table():
        tbx = float(input("Input X "))
        tbs = float(input("Input slope (Decimal please) "))
        yft1 = tbx * tbs
        yft2 = tbx - yft1
        yft2s = str(yft2)
        print("y-int= " + yft2s)
    def X_from_a_table():
        tby = float(input("Input y "))
        tbs = float(input("Input slope "))
        xft1 = tby * tbs
        xft2 = xft1 - tby
        xft2s = str(xft2)
        print("x-int= " + xft2s)
    def Add_two_step_equations():
        preax = float(input("Input Coefficient (No fractions only decimal) "))
        nmtet = float(input("Input number that equation is equal to" ))
        ipctvar = float(input("Input Constant" ))
        prealcal1 = nmtet - ipctvar
        prealcal2 = prealcal1 / preax
        print("Your answer is: " + str(prealcal2))
        
