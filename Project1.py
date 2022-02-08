"""
CAP4630: Project1 - Python Basics

Description: This project was designed to parse a csv file containing records of each state including 
a 2022 report for each state's population size, median household income, and covid cases & casualties. 
These records are then placed into a state list with various fields

The program will search for a csv file to which it will then prompt the user to choose amongst serval actions.
If any input does not meet the program's requirements, an error message will appear. The actions include: 
printing a state report, sort the states by name, sort the states by full vaccination rates, find and print 
a particular state's records, display a Spearman's Rho correlation, for {Case Rate, Death Rate} 
x {Median Household Income, Violent Crime Rates, Full Vaccination Rates}. If any of these actions are no longer 
requested, the user will have the option to quit from the program.

Author: Eyob Tekle
Version: February 4, 2022
Email: N01239628@unf.edu
"""
import csv
from State import *

"""
Description: prints out each states' name, median household income, violent crime rate, covid fatality rate, 
            case rate, death rate, and full vaccination rate
:param state name
:return N/A
"""
def stateReport(states):
    space = " "
    print("\nName %15s MHI %8s VCR %8s CFR %10s Case Rate %5s Death Rate %2s FVR\n" 
            "------------------------------------------------"
            "---------------------------------------------------" 
            %(space, space, space, space, space, space))
    for x in states:
        poprate = psample / int(x.get_pop())
        print("%-20s %s %12.1f %15.6f %14.2f %13.2f %13.4f"
			    %(x.get_name(), x.get_income(), float(x.get_violent()),
                int(x.get_deaths())/int(x.get_cases()), int(x.get_cases()) * poprate, 
                int(x.get_deaths()) * poprate, float(x.get_vaccine())/100))
    #End For Loop

"""
Description: Sorts state list based on state fatality rate using mergesort
:param state object
:return N/A
"""
def fatalitySorter(states):

    if(len(states) <= 1):
        return
    else:
        mid = len(states) >> 1
        left = states[:mid]
        right = states[mid:]     

        fatalitySorter(left)
        fatalitySorter(right)   

        l_dex = r_dex = s_dex = 0

        while(l_dex < len(left) and r_dex < len(right)):
            if(int(left[l_dex].get_deaths())/int(left[l_dex].get_cases()) < int(right[r_dex].get_deaths())/int(right[r_dex].get_cases())):
                states[s_dex] = left[l_dex]
                l_dex += 1
            else:
                states[s_dex] = right[r_dex]
                r_dex += 1
            s_dex += 1
        #Enf While Loop
        while(l_dex) < len(left):
            states[s_dex] = left[l_dex]
            l_dex += 1
            s_dex += 1
        #End While Loop
        while(r_dex < len(right)):
            states[s_dex] = right[r_dex]
            r_dex += 1
            s_dex += 1
        #End While Loop

"""
Description: partitions a list during quicksort
:param state list
:param lower bound limit
:param upper bound limit
:return  new upper binding limit
"""
def partition(states, low_bound, up_bound):
    left_part = low_bound
    right_part = up_bound - 1
    pivot = states[up_bound].get_name()
    
    while True:
        while(states[left_part].get_name() < pivot):
            left_part += 1
        
        while(right_part + 1 > 0 and states[right_part].get_name() > pivot):
            right_part -= 1

        if(left_part >= right_part):
            break
        else:
            (states[left_part],states[right_part]) = (states[right_part],states[left_part])
    
    (states[left_part],states[up_bound]) = (states[up_bound],states[left_part])
    return left_part

"""
Description: sorts state list based on state name using quicksort
:param state object
:param list lower bound
:param list upper bound
:return N/A
"""
def nameSorter(states, low_bound, up_bound):
    if(up_bound - low_bound <= 0 or len(states) == 1):
        return
    else:
        part = partition(states, low_bound, up_bound)

        nameSorter(states, low_bound, part - 1)
        nameSorter(states, part + 1, up_bound)

"""
Description: finds a state based on user input and prints records
:param user input in the form of a state name
:param boolean variable, checks which sort method was used
:param state list
:return N/A
"""
def state_finder(key, nSort, states):
    num2 = 0
    if(nSort == True):
        low_bound = 0
        up_bound = len(states) - 1

        print("Using Binary Search...\n")

        while(low_bound <= up_bound):
            
            mid = (low_bound + up_bound) >> 1
            if(states[mid].get_name() == key):
                num2 = mid
                break
            elif(states[mid].get_name() > key):
                up_bound = mid - 1
            else:
                low_bound = mid + 1
    else:
        j = 0

        print("Using Sequential Search...\n")

        while(j < len(states)):
            if(states[j].get_name() == key):
                break
            j += 1
        
        num2 = 0 if j == 50 else j

    if(states[num2].get_name() != key):
        print("Sorry, but '" + key +"' was not found.\n")
    else:
        poprate = psample/int(states[num2].get_pop())
        space = " "
        print("State Search Succedsul\n"
             "Name: %10s%s\n"
             "MHI: %11s%s\n"
             "VCR: %11s%.1f\n"
             "CFR: %11s%.6f\n"
             "Case Rate: %5s%.2f\n"
             "Death Rate: %4s%.2f\n"
             "FV Rate: %7s%.3f\n"
             %(space, states[num2].get_name(), space, states[num2].get_income(), space, float(states[num2].get_violent()), space, 
             int(states[num2].get_deaths())/int(states[num2].get_cases()), space, int(states[num2].get_cases()) * poprate, space,
             int(states[num2].get_deaths()) * poprate, space, float(states[num2].get_vaccine())/100))
        
"""
Description: this method displays the Spearman's Rho correlation between the states'
            covid case rate & median household income,
            covid case rate & violent crime rate,
            covid case rate & full vaccination rate,
            covid death rate & median household income,
            covid death rate & violent crime rate, and
            covid death rate & full vaccination rate.
:param state list
:return N/A
"""
def spearman_rho(states):
    
    rho1 = rho2 = rho3 = rho4 = rho5 = rho6 = 0.0000
    tempMHI = []
    medHI = []
    tempVCR = []
    caseRank = []
    deathRank = []
    vRate = []
    tempFVR = []
    fullVR = []
    cRate = []
    dRate = []

    for x in states:
        tempMHI.append(int(x.get_income()))
        medHI.append(int(x.get_income()))
        tempVCR.append(float(x.get_violent()))
        vRate.append(float(x.get_violent()))
        tempFVR.append(float(x.get_vaccine()))
        fullVR.append(float(x.get_vaccine()))
        cRate.append(int(x.get_cases()) * psample / int(x.get_pop()))
        dRate.append(int(x.get_deaths()) * psample / int(x.get_pop()))
        caseRank.append(int(x.get_cases()) * psample / int(x.get_pop()))
        deathRank.append(int(x.get_deaths()) * psample / int(x.get_pop()))

    for x in range(1, len(states)):
        tempInc = medHI[x]
        tempCsRt = cRate[x]
        tempDthRt = dRate[x]
        tempCrime = vRate[x]
        tempFull = fullVR[x]

        in1 = in2 = in3 = in4 = in5 = x - 1

        while(in1 >= 0 and cRate[in1] > tempCsRt):
            cRate[in1 + 1] = cRate[in1]
            in1 -= 1
        while(in2 >= 0 and dRate[in2] > tempDthRt):
            dRate[in2 + 1] = dRate[in2]
            in2 -= 1
        while(in3 >= 0 and medHI[in3] > tempInc):
            medHI[in3 + 1] = medHI[in3]
            in3 -= 1
        while(in4 >= 0 and vRate[in4] > tempCrime):
            vRate[in4 + 1] = vRate[in4]
            in4 -= 1
        while(in5 >= 0 and fullVR[in5] > tempFull):
            fullVR[in5 + 1] = fullVR[in5]
            in5 -= 1

        cRate[in1 + 1] = tempCsRt
        dRate[in2 + 1] = tempDthRt
        medHI[in3 + 1] = tempInc
        vRate[in4 + 1] = tempCrime
        fullVR[in5 + 1] = tempFull
    #End For Loop    
    ranking(caseRank,cRate)
    ranking(deathRank,dRate)
    ranking(tempMHI,medHI)
    ranking(tempVCR,vRate)
    ranking(tempFVR,fullVR)

    for x in range(0, len(states)):
        rho1 += (caseRank[x] - tempMHI[x]) ** 2
        rho2 += (caseRank[x] - tempVCR[x]) ** 2
        rho3 += (caseRank[x] - tempFVR[x]) ** 2
        rho4 += (deathRank[x] - tempMHI[x]) ** 2
        rho5 += (deathRank[x] - tempVCR[x]) ** 2
        rho6 += (deathRank[x] - tempFVR[x]) ** 2

    p = len(states) * ((len(states) ** 2) - 1)

    rho1 = 1 - (6 * rho1 / p)
    rho2 = 1 - (6 * rho2 / p)
    rho3 = 1 - (6 * rho3 / p)
    rho4 = 1 - (6 * rho4 / p)
    rho5 = 1 - (6 * rho5 / p)
    rho6 = 1 - (6 * rho6 / p)

    print("\n------------------------------------------------------------------\n"
		  "|\t\t|\tMHI\t |\tVCR\t | \tFVR\t | \n"
		  "------------------------------------------------------------------\n"
		  "|   Case Rate   |      %.4f\t |      %.4f\t |     %.4f\t |\n"
		  "------------------------------------------------------------------\n"
		  "|   Death Rate  |      %.4f\t |      %.4f\t |     %.4f\t |\n"
		  "------------------------------------------------------------------\n" %(rho1, rho2, rho3, rho4, rho5, rho6))
    
"""
Description: This method searches a list contain a certain state field and rates it's rank
:param unsorted state list object
:param sorted state list object
:return N/A
"""
def ranking(rate, sortedRate):
    for x in range (0, len(rate)):
        low_bound = 0
        up_bound = len(rate) - 1

        while(low_bound <= up_bound):
            mid = (low_bound + up_bound) >> 1
            if(sortedRate[mid] == rate[x]):
                rate[x] = mid + 1
                break
            elif(sortedRate[mid] > rate[x]):
                up_bound = mid - 1
            else:
                low_bound = mid + 1
            #End If/Else
        #End While
    #End For
#End Method


num = 0
nameSorted = False
states = []
psample = 100000

try:
    f = open('States.csv', 'r') 
    next(f) #End Try
except IOError:
    print('cannot open file') #End Except

lines = csv.reader(f)

for s in lines:
    state = State(*s)
    states.append(state)

while True:
    try:
        print("\n Would you like to :\n"
                + "1. Print A State Report\n"
                + "2. Sort By State Name\n"
                + "3. Sort By Case Fatailty Rate\n"
                + "4. Find And Print A State For A Given Name\n"
                + "5. Print Spearman's \u03C1 Correlation Matrix\n"
                + "6. QUIT")

        num = int(input())
    #End Try
    except ValueError:
        while True:
            try:
                print("%s Is Not A Valid Input: Please Enter 1 - 6!" %num)
                num = int(input())
                break
            except ValueError:
                print("%s Is Not A Valid Input: Please Enter 1 - 6!" %num)
            #End Except
    if num == 1:
        stateReport(states)
    elif num == 2:
        nameSorter(states, 0, len(states) - 1)
        print("States Have Been Sorted By Name.\n")
        nameSorted = True
    elif num == 3:
        fatalitySorter(states)
        print("States Have Been Sorted By Fatality Rate\n")
        nameSorted = False
    elif num == 4:
        print("Which State Are You Searching: ")
        state_finder(input(), nameSorted, states)
    elif num == 5:
        spearman_rho(states)
    elif num == 6:
        print("Goodbye!\n")
        break
    else:
        print("%s Is Not A Valid Input: Please Enter 1 - 6!" % num)

f.close()