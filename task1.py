def corrector(question):
  num = input(question)

  if num.isdigit() or float(num):
     return num
  else:
      print('put in a number!')
      return corrector(question)

hrs = corrector("how many hours do you want to convert\n")
if "." in hrs:
    hrsfloat = float(hrs)
    mins = hrsfloat * 60
else:
    hrsnum = int(hrs)
    mins = hrsnum * 60

minsstr=str(mins)
print(hrs + " hours is "+ minsstr + " minutes")