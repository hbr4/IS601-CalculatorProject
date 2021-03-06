from Calculator.Square import squaring
from Calculator.Division import division
from Calculator.Addition import addition
from Statistics.PopulationMean import populationmean


def proportion(num):
    try:
        p_list = list()
        x = sum(num)
        for i in num:
            y = division(i, x)
            p_list.append(y)
        return p_list
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
