# File: Unit Conversion Project.py
# Student: Tomas Chang
#
# Date: 3/7/2022
# Description of Program: This program aims to convert english length units to metric lengths
# and vice versa

ERRORMESSAGE = "\nERROR: Answer must be 1, 2 or 3. Try again."

print("Welcome to the English/Metric conversion utility.")

print("This utility allows you to convert between English units")
print("(miles, feet, inches) and metric units (kilometers, meters,")
print("centimeters).")

print("------------------------------------------------------------")

while True:
    print("Which direction would you like to convert:")
    print("   For English to Metric type: 1")
    print("   For Metric to English type: 2")
    print("   To Quit type:               3\n")
    answer = int(input("Input your answer (1, 2 or 3): "))

    if (answer ==3): #quit
        print("Thanks for using our converter. Goodbye!")
        break  
    if (answer==1): #english units to metric
        print ("Select English units to convert to metric equivalent:")
        print("    For miles type:  1")
        print("    For feet type:   2")
        print("    For inches type: 3\n")
        EnglishAnswer= int(input("Choose English units to convert (1, 2 or 3): "))
        
        if(answer != 1 or 2 or 3): #ERROR
            print(ERRORMESSAGE)
            continue

        if (EnglishAnswer==1): #miles to metric units
            print("Convert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3\n")
            EnglishMetricAnswer= int(input("Choose target metric units (1, 2 or 3):\n"))
        
            if (answer != 1 or 2 or 3):
                print(ERRORMESSAGE)  

            if (EnglishMetricAnswer ==1): #miles to km
                EngToMet = float(input("Enter the number of miles to conver to kilometers:\n"))
                MtoK = ((EngToMet * 1609.344)/1000)
                format(MtoK, "0.3f")
                print("Result:", EngToMet, "miles = ", MtoK, "kilometers\n")
                print("------------------------------------------------------------")
                continue
            if (EnglishMetricAnswer ==2): #miles to meters
                EngToMet = float(input("Enter the number of miles to convert to meters:\n"))
                MtoM= (EngToMet * 1609.344)
                format(MtoM, "0.3f")
                print("Result:", EngToMet, "miles = ", MtoM, "meters\n")
                print("------------------------------------------------------------")
                continue
            if (EnglishMetricAnswer ==3): #miles to cm
                EngToMet = float(input("Enter the number of miles to convert to centimeters:\n"))
                MtoCM = (EngToMet * 1609.344 * 100)
                format(MtoCM, "0.3f")
                print("Result:", EngToMet, "miles =", MtoCM,"centimeters\n")
                print("------------------------------------------------------------")
                continue
       
        if (EnglishAnswer==2): #feet to metric units 
            print("Convert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3\n")
            EnglishMetricAnswer= int(input("Choose target metric units (1, 2 or 3:\n"))
            
            if(answer != 1 or 2 or 3):
                ERRORMESSAGE

            if(EnglishMetricAnswer==1): #feet to km
                EngToMet = float(input("Enter the number of feet to convert to kilometers:\n"))
                FtoKm =((EngToMet * 0.3048)/1000)
                format(FtoKm, "0.3f")
                print("Result:", EngToMet, "feet =", FtoKm, "kilometers\n")
                print("------------------------------------------------------------")
                continue
            if(EnglishMetricAnswer==2): #feet to meters
                EngToMet = float(input("Enter the number of feet to convert to meters:\n"))
                FtoM = (EngToMet/3.82084)
                format(FtoM, "0.3f")
                print("Result:", EngToMet, "feet =", FtoM, "meters")
                print("------------------------------------------------------------")
                continue
            if(EnglishMetricAnswer==3): #feet to cm
                EngToMet = float(input("Enter the number of feet to convert to centimeters:\n"))
                FtoCm = ((EngToMet*3.82084)*1/100)
                format(FtoCm, "0.3f")
                print("Result:", EngToMet, "feet =", FtoCm, "centimeters\n")
                print("------------------------------------------------------------")
                continue
       
        if (EnglishAnswer==3): #inches to metric units
            print("Convert to which metric units:")
            print("   For kilometers type:  1")
            print("   For meters type:      2")
            print("   For centimeters type: 3\n")
            EnglishMetricAnswer= int(input("Choose target metric units (1, 2 or 3:\n"))
           
            if(answer != 1 or 2 or 3):
                ERRORMESSAGE
            if(EnglishMetricAnswer==1): #inches to km
                EngToMet = float(input("Enter the number of inches to conver to kilometers:\n"))
                ItoKm= (((EngToMet/12)*0.3048)/1000)
                format(ItoKm, "0.3f")
                print("Result:", EngToMet, "inches =", ItoKm, "kilometers\n")
                print("------------------------------------------------------------")
                continue
            if(EnglishMetricAnswer==2): #inches to meters
                EngToMet = float(input("Enter the number of inches to convert to meters:\n"))
                ItoM = ((EngToMet/12)*0.3048)
                format(ItoM, "0.3f")
                print("Result:", EngToMet, "inches=", ItoM, "meters\n")
                print("------------------------------------------------------------")
                continue
            if(EnglishMetricAnswer==3): #inches to cm
                EngToMet = float(input("Enter the number of inches to convert to centimeters:\n"))
                ItoCm =(EngToMet /12)*3.28084*1/100
                format(ItoCm, "0.3f")
                print("Result:", EngToMet, "inches =", ItoCm, "centimeters\n")
                print("------------------------------------------------------------")
                continue
    if(answer ==2): #metric to english
        print("Select metric units to convert to English equivalent:")
        print("   For kilometers type:  1")
        print("   For meters type:      2")
        print("   For centimeters type: 3")
        MetricAnswer= int(input("Choose metric units to convert (1, 2 or 3:\n"))
            
        if(MetricAnswer ==1): #km to english units
            print("Convert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            MetricEnglishAnswer = int(input("Choose target English units (1, 2 or 3:)\n"))

            if(answer != 1 or 2 or 3):
                ERRORMESSAGE

            if(MetricEnglishAnswer ==1): #km to miles
                MetToEng = float(input("Enter the number of kilometers to convert to miles:\n"))
                KmToM = ((MetToEng * 1000)/1609.344)
                format(KmToM, "0.3f")
                print("Result:", MetToEng, "kilometers =", KmToM, "miles")
                print("------------------------------------------------------------")
                continue
            if(MetricEnglishAnswer ==2): #km to feet
                MetToEng = float(input("Enter the number of kilometers to convert to feet:\n"))
                KmToF = ((MetToEng * 1000)/3.28084)
                format(KmToF, "0.3f")
                print ("Result:", MetToEng, "kilometers =", KmToF, "feet")
                print("------------------------------------------------------------")
                continue
            if(MetricEnglishAnswer ==3): #km to inches
                MetToEng = float(input("Enter the number of kilometers to convert to inches:\n"))
                KmToI = (MetToEng * 1000)/0.3048*12
                format(KmToI, "0.3f")
                print ("Result:", MetToEng, "kilometers =", KmToI, "inches")
                print("------------------------------------------------------------")
                continue
       
        if(MetricAnswer ==2): #meters to english units
            print("Convert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            MetricEnglishAnswer = int(input("Choose target English units (1, 2 or 3:)\n"))

            if(answer != 1 or 2 or 3):
                ERRORMESSAGE

            if(MetricEnglishAnswer ==1): #meters to miles
                 MetToEng = float(input("Enter the number of meters to convert to miles:\n"))
                 MetoM = (MetToEng/5280) 
                 format(MetoM, "0.3f")
                 print ("Result:", MetToEng, "meters =", MetoM, "miles")
                 print("------------------------------------------------------------")
                 continue
            if(MetricEnglishAnswer==2): #meters to feet
                MetToEng = float(input("Enter the number of meters to convert to feet:\n"))
                MtoF = (MetToEng * 3.28084)
                format(MtoF, "0.3f")
                print ("Result:", MetToEng, "meters =", MtoF, "feet")
                print("------------------------------------------------------------")
                continue
            if(MetricEnglishAnswer ==3): #meters to inches
                MetToEng = float(input("Enter the number of meters to convert to inches:\n"))
                MtoI= ((MetToEng/0.3048) * 12)
                format(MtoI)
                print ("Result:", MetToEng, "meters =", MtoI, "inches")
                print("------------------------------------------------------------")
                continue

        if(MetricAnswer ==3): # cm to english units
            print("Convert to which English units:")
            print("   For miles type:  1")
            print("   For feet type:   2")
            print("   For inches type: 3")
            MetricEnglishAnswer = int(input("Choose target English units (1, 2 or 3:)\n"))

            if(answer != 1 or 2 or 3):
                ERRORMESSAGE

            if(MetricEnglishAnswer ==1): #cm to miles
                MetToEng = float(input("Enter the number of centimeters to convert to miles:\n"))
                CmtoM= ((MetToEng/100)/1609.344)
                format(CmtoM, "0.3f")
                print ("Result:", MetToEng, "centimeters =", CmtoM, "miles")
                print("------------------------------------------------------------")
                continue
            if(MetricEnglishAnswer ==2): #cm to feet
                 MetToEng = float(input("Enter the number of centimeters to convert to feet:\n"))
                 CmtoF= (MetToEng/ 100)* 3.28084
                 format(CmtoF, "0.3f")
                 print ("Result:", MetToEng, "centimeters =", CmtoF, "feet")
                 print("------------------------------------------------------------")
                 continue
            if(MetricEnglishAnswer ==3): #cm to inches
                MetToEng = float(input("Enter the number of centimeters to convert to inches:\n"))
                CmtoI= (MetToEng/100)*3.28084*12
                format(CmtoI, "0.3f")
                print ("Result:", MetToEng, "centimeters =", CmtoI, "inches")
                print("------------------------------------------------------------")
                continue
   
