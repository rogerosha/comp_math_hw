"""
BS_1
Data
"""
#levij krai poiska (po OX)
a=2
#pravij krai poiska
b=3
#pogreshnost (tochnost)
eps=0.01
#kolichestvo tochek grafika
n_plot_dots=101
print("BS_1 started \n")
print("\n DATA \n")
print("a=", a)
print("b=", b)
print("eps=", eps)
print("n_plot_dots=", n_plot_dots)
"""
fun_BS_1
"""
def f(x): #korni f(x)=o poisk
    fx=x**2-5
    return fx
#end func f(x)
def fun_BS_1(a, b, eps):
    print("\n fun_BS_1 started")
    fa=f(a)
    for i in range(1, 100):
        x=(a+b)/2
        if fa*f(x) < 0:
            b=x
        else:
            a=x
        #end if
        if abs(b-a) < eps: #proverka uslovij prerivaniya cikla
            print("\n vipolneno iteracij i=", i)
            break #prerivanie cikla
        #end if
    #end for i
    x=(a+b)/2
    fx=f(x)
    return x, fx
#end fun_BS_1
(x, fx) = fun_BS_1(a,b, eps)
print("x=", x, "y=", fx)
"""
REPORT
"""
#oformlenie vivoda prilichnim obrazom
def REPORT(a, b, eps, n_plot_dots, x, fx)
    print("\n REPORT started")
    print('\n' + 'arguments' + '\n')
    print('levij krai poiska')
    print(f"a = {a:o.5f}")
    print('pravij krai poiska')
    print(f"b = {b:0.5f}")
    print('pogreshnosti')
    print(f"eps = {eps:0.5f}")
    print('\n' + 'results' + '\n')
    print('koren')
    print(f"x = {x:0.5f}")
    print('funciya')
    print(f"y = {fx:0.5f}")
    h=(b-a)/(int(n_plot_dots)-1)
    import numpy as np
    xmas=np.zeros(int(n_plot_dots))
    fmas=np.zeros(int(n_plot_dots))
    for i in range(0, int(n_plot_dots))
        if i == 0
            xmas[i] = a
        else:
            xmas[i] = xmas[i-1]+h
        #end if
        fmas[i] = f(xmas[i])
    #end for i
        print('   i    x     fx     ')
    for i in range(1, len(xmas))
        xx=xmas[i]
        ffx=fmas[i]
        print(f"{i:3d}\t{xx:0.3f}\t{ffx:0.3f}")
    #end for i
    import matplotlib.pyplot as plt
    plt.plot(xmas, fmas, 'r.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("grafik $y=x^2-5$")
    plt.grid(True)
#end REPORT
def REPORT(a, b, eps, n_plot_dots, x, fx)