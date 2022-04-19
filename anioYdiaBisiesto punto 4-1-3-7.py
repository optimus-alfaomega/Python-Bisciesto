from calendar import month_abbr

#define primero si el año es bisiesto o no 
def isYearLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False 
#comprueba que el dia y el año ingresado corresponda al dia del calendario
#la funcion retorna los dias totales que corresponden al mes ingresado

def daysInMonth(year, month):
    meses=[31,28,31,30,31,30,31,31,30,31,30,31]
    mes=int(month)
    if (year > 1000) and  (mes > 0 and mes < 13) :
        anio=isYearLeap(year)
        for i in range(len(meses)):
            if mes == 2 and anio == True:
                return  29
            elif mes == 2 and anio == False:
                return  28
            elif meses[i]== meses[mes-1]:
                return meses[i]
    else:
        return None
#valida  que los datos del arreglo con los años predefinidos sean el correcto de lo contrario retornara error
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")