def weatherAnnouncer(temp, clearSkies, windy):
    #try to combine these two statements into one if statement!
    tempClass = temperatureClassification(temp)
    # HOT
    if(tempClass == 'HOT' and ((clearSkies and windy) or(clearSkies and not windy))):
        return 'Wear summer clothes today.'
    elif(tempClass == "HOT" and not clearSkies and windy):
        return 'Wear summer clothes today, but bring a rain jacket just in case.'
    elif(tempClass == "HOT" and not clearSkies and not windy):
        return 'Wear summer clothes today, but bring an umbrella just in case.'
    # FAIR
    elif(tempClass == "FAIR" and clearSkies and not windy):
        return 'Wear whatever you would like today.'
    elif(tempClass == "FAIR" and ((not clearSkies and not windy) or (not clearSkies and windy) or (clearSkies and windy))):
        return 'Wear a jacket today.'
    # COLD
    elif(tempClass == "COLD" and not windy and clearSkies):
        return 'Just stay inside today.'
    elif(tempClass == "COLD" and ((windy and clearSkies) or (clearSkies and not windy) or (not clearSkies and not windy))):
        return 'Wear winter gear today.'
    




def temperatureClassification(temp):
    if temp < 40:
        return "COLD"
    elif 40 <= temp < 75:
        return "FAIR"
    elif temp >= 75:
        return "HOT"
    else: 
        return "Enter a valid number"



#if hot and clear and not windy: 'Wear summer clothes today. 
print('TESTING', weatherAnnouncer(77, True, False))
# if hot and not clear and windy: 'Wear summer clothes today, but bring a rain jacket just in case.'
print('TESTING', weatherAnnouncer(95, False, True))
# if hot and not clear and not windy: 'Wear summer clothes today, but bring an umbrella just in case.'
print('TESTING', weatherAnnouncer(95, False, False))

# if fair AND clear AND not windy: 'Wear whatever you would like today.'
print('TESTING', weatherAnnouncer(56, True, False))
# if fair AND otherwise: 'Wear a jacket today.'
print('TESTING', weatherAnnouncer(56, False, False))

# if cold AND windy AND PC: 'Just stay inside today.'
print('TESTING', weatherAnnouncer(22, False, True))
# if cold AND otherwise: 'Wear winter gear today.'
print('TESTING', weatherAnnouncer(2, True, True)) 
