class eighth_grade_math_solver:
    pi = 3.1415
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
    def Subtract_two_step_equations():
        print("Input Coefficient (No fractions only decimal)")
        preax = float(input())
        print("Input number that equation is equal to")
        nmtet = float(input())
        print("Input Constant")
        ipctvar = float(input())
        prealcal1 = nmtet + ipctvar
        prealcal2 = prealcal1 / preax
        print("Your awnser is: " + str(prealcal2))
    def Slope_to_standerd_form():
        print("Y = A/Bx + b --> Ax + By = C")
        time.sleep(1)
        y = float(input("enter y value "))
        A = float(input("enter M as fraction A/B - A "))
        B = float(input("enter M as fraction A/B - B "))
        b = float(input("enter b "))
        ys = str(y)
        As = str(A)
        Bs = str(B)
        bs = str(b)
        print("equation: "+ys+"y = " + As + "/" + Bs + "x + " + bs)
        time.sleep(1)
        print("\n-----------------\n")
        time.sleep(1)
        print("equation: -"+As+"/"+Bs+"x + "+ys+"y = "+bs)
        time.sleep(1)
        print("\n-----------------\n")
        time.sleep(1)
        ys1 = str(y*B)
        bs1 = str(b*B)
        print("final equation: -"+As+"x + "+ys1+"y = "+bs1)
        time.sleep(2)
        print("\n-----------------\n")
        time.sleep(2)
    def translations():
        print("Translations")
        print("Input X cordnate")
        xcor = float(input())
        print("Input Y cordnate")
        ycor = float(input())
        print("Input Horizontal shift")
        hshift = float(input())
        print("Input Vertical shift")
        vshift = float(input())
        yshiftcal = ycor + vshift
        xshiftcal = xcor + hshift
        xstrcon = str(xshiftcal)
        ystrcon = str(yshiftcal)
        print("Your cordnets are: ( " + xstrcon + ", " + ystrcon + " )")
    def dialations():
        print("Dilations")
        print("Input X cordnet")
        xcor = float(input())
        print("Input Y cordnet")
        ycor = float(input())
        print("Input Dilation factor in decimal")
        dxyfactor = float(input())
        calx1 = xcor * dxyfactor
        caly2 = ycor * dxyfactor
        calxstrcon = str(calx1)
        calystrcon = str(caly2)
        print("Your awnswer is: (" + calxstrcon + ", " + calystrcon + ")")
    def rotaions():
        print("Rotations")
        print("Input X cordnate")
        xcor = float(input())
        print("Input Y cordnate")
        ycor = float(input())
        print("Input CLOCKWISE rotation (90, 180, 270)")
        rot = input()
        if rot == "90":
            cal1 = xcor * -1
            calstrx = str(cal1)
            calstry = str(ycor)
            print("The answer is: (" + calstry + ", " + calstrx + ")")
        elif rot == "180":
            cal1 = xcor * -1
            cal2 = ycor * -1
            calstrx = str(cal1)
            calstry = str(cal2)
            print("The answer is: (" + calstrx + ", " + calstry + ")")
        elif rot == "270":
            cal2 = ycor * -1
            calstrx = str(xcor)
            calstry = str(cal2)
            print("The answer is: (" + calstry + ", " + calstrx + ")")
    def reflections():
        print("What would you like to reflect across")
        print("[1] X axis")
        print("[2] Y axis")
        print("[3] Y = X")
        print("[4] Y = -X")
        xory = input()
        if xory == "1":
            print("Input X cordnet")
            xcor = float(input())
            print("Input Y cordnet")
            ycor = float(input())
            varcal2 = ycor * -1
            finalcal1 = str(xcor)
            finalcal2 = str(varcal2)
            print("The awnser is: ( " + finalcal1 + ", " + finalcal2 + ")")
        elif xory == "2":
            print("Input X cordnet")
            xcor = float(input())
            print("Input Y cordnet")
            ycor = float(input())
            varcal2 = xcor * -1
            finalcal1 = str(ycor)
            finalcal2 = str(varcal2)
            print("The awnser is: ( " + finalcal2 + ", " + finalcal1 + ")")
        elif xory == "3":
            print("Input X cordnet")
            xcor = float(input())
            print("Input Y cordnet")
            ycor = float(input())
            finalcal1 = str(ycor)
            finalcal2 = str(xcor)
            print("The awnser is: ( " + finalcal1 + ", " + finalcal2 + ")")
        elif xcor == "4":
            print("Rotations")
            print("Input X cordnate")
            xcor = float(input())
            print("Input Y cordnate")
            ycor = float(input())
            print("Input CLOCKWISE rotation (90, 180, 270)")
            rot = input()
            if rot == "90":
                cal1 = xcor * -1
                calstrx = str(cal1)
                calstry = str(ycor)
                print("The answer is: (" + calstry + ", " + calstrx + ")")
            elif rot == "180":
                cal1 = xcor * -1
                cal2 = ycor * -1
                calstrx = str(cal1)
                calstry = str(cal2)
                print("The answer is: (" + calstrx + ", " + calstry + ")")
            elif rot == "270":
                cal2 = ycor * -1
                calstrx = str(xcor)
                calstry = str(cal2)
                print("The answer is: (" + calstry + ", " + calstrx + ")")
    def fraction_to_decimal():
        print('Fracton to decimal converter')
        print('Input the numerator in interger form (Top part of the fraction)')
        varnumfractodec = int(input())
        print('input demonimator in Intager form (Bottom of the fraction)')
        vardemfractonecdem = int(input())
        varcal1 = varnumfractodec / vardemfractonecdem
        varprint = str(varcal1)
        if varcal1 < 1:
            varprint = str(varcal1) + '0'
        print('Your awnswer is ' + varprint)
    def square_roots():
        print('Input number you want to square')
        varnumtosquare = float(input())
        varsquarerootcal1 = varnumtosquare ** 2
        print('your awnswer is ' + str(varsquarerootcal1))
    def cube_roots():
        print('Input number you want to cube')
        varnumtocube = float(input())
        varcuberootcal1 = varnumtocube ** 3
        print('your awnswer is ' + str(varcuberootcal1))
    def exponents():
        print('Input base number')
        varbasenumber = float(input())
        print('Input what woy would like to multiply it by a power to')
        vartoapower = float(input())
        varcaltoapower1 = varbasenumber ** vartoapower
        print('your awnswer is ' + str(varcaltoapower1))
    def volume_of_cones():
        print('Input unit')
        varconevoluni = input()
        print('Input radius')
        varinradcone = float(input())
        print('Input hight')
        varnhighcon = float(input())
        varcal1 = (((varinradcone ** 2) * pi) * varnhighcon) * 1/3
        print('Your awnswer is ' + str(varcal1) + ' Cubic ' + varconevoluni)
    def volume_of_cylienders():
        print('Input unit')
        var_ciluninit = input()
        print('Input radius')
        var_radcil = float(input())
        print('Input hight')
        var_highcil = float(input())
        varcalcil1 = ((((var_radcil ** 2) * pi)) * var_highcil)
        print('Your awnswer is ' + str(varcalcil1) + ' Cubic ' + str(var_ciluninit))
    def volume_of_cubes():
        print('Input unit')
        varcubeunit = input()
        print('Input legth of side 1')
        varcubeside1leg = float(input())
        print('Input legth of side 2')
        varcubeside2leg = float(input())
        print('Input hight')
        varcubehight = float(input())
        varcalcubevol1 = (varcubeside1leg* varcubeside2leg) * varcubehight
        print('Your awnswer is ' + str(varcalcubevol1) + ' Cubic ' + str(varcubeunit))
    def volume_of_triangular_prism():
        print('Input unit')
        var_unitri = input()
        print('Input legth')
        var_trilegth = float(input())
        print('Input hight of triangle')
        var_tritrihigh = float(input())
        print('Input Triangle base')
        var_tritribase = float(input())
        var_caltrivol1 = ((var_tritrihigh * var_tritribase) * var_trilegth) * 1/2
        print('Your answer is ' + str(var_caltrivol1) + ' cubic ' + var_unitri)
    def area_of_square():
        print('Input unit')
        var_areasquareuni = input()
        print('Input Hight of square')
        var_highsquarearea = float(input())
        print('Input Width of square')
        var_squarewidth = float(input())
        var_squareareacal1 = var_highsquarearea * var_squarewidth
        print('Your awnswer is ' + str(var_squareareacal1) + ' ' + var_areasquareuni + ' Squared')
    def area_of_triangle():
        print('Input unit')
        var_unitareatri = input()
        print('Input triangle hight')
        var_triareahigh = float(input())
        print('Input triangle base')
        var_tribasearea = float(input())
        var_caltriarea1 = (var_triareahigh * var_tribasearea) * 1/2
        print('Your answer is ' + str(var_caltriarea1) +  ' ' + var_unitareatri + ' squared')
    def area_of_a_circle():
        print('Input unit')
        var_unicirin = input()
        print('Input Radius')
        var_radcirin = float(input())
        var_calcirc1 = (var_radcirin ** 2) * pi
        print('The answer is ' + str(var_calcirc1) + ' ' + var_unicirin + ' squared')
    def pythagorean_theorem():
        print('Input A')
        var_apainput = float(input())
        print('Input B')
        var_bpainput = float(input())
        var_calpa1 = (var_apainput ** 2) + (var_bpainput ** 2)
        var_rootpa = math.sqrt(var_calpa1)
        print('Your awnswer is ' + str(var_rootpa))

