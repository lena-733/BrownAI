choiceoftime = input ("do you want to convert hours or minutes?\n")
if choiceoftime == "hours":
    hrsstr=input("how many hours do you want to convert?\n")
    if "." in hrsstr:
        hrsfloat = float(hrsstr)
        mins = hrsfloat * 60
        minstr = str(mins)

    else:
        hrsnum = int(hrsstr)
        mins = hrsnum * 60
        minstr = str(mins)

    print(hrsstr+" hours is "+minstr+" minutes")
elif choiceoftime == "minutes":
    minute=input("how many minutes do you wan to conver?\n")
    if "." in minuter:
        minutefloat = float(minute)
        hours = minutefloat * 60
        hourstr = str(hours)

    else:
        minutenum = int(minute)
        hours = minutenum * 60
        hourstr = str(hours)
    print(minute+' minutes is '+hourstr +" minutes")