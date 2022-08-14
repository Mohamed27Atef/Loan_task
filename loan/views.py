from django.shortcuts import render
from .models import loan

import numpy_financial as np 

def loan_details(request):

    x=loan.objects.all().last()

#Summary of Results
    Number_of_Payments=x.Term_of_Loan*x.Payments_Per_Year

    Rate_Period=x.Annual_Interest_Rate/x.Compound_Periods
    
    Monthly_Payment=(x.amount*(Rate_Period/100))/(1-(1+(Rate_Period/100))**-Number_of_Payments)

    Total_Payment=Monthly_Payment*x.Term_of_Loan*x.Payments_Per_Year

    Total_Interest=Total_Payment-x.amount


    Summary_of_Results={
           "Number_of_Payments" :Number_of_Payments,
           "Rate_Period" :round(Rate_Period,3),
           "Total_Payment" :round(Total_Payment,2),
           "Total_Interest" :round(Total_Interest,2),
           "Monthly_Payment" :round(Monthly_Payment,2),
                      }
########################

# Yearly Amortization Schedule
    Cumulative_Interest=[0]
    Cumulative_Principal=[0]
    Balance=[0]
    Cumulative_Payments=[0]
    Yearly_Payments=[0]
    Yearly_Interest=[0]



    Balance[0]=x.amount

    for i in range(x.Term_of_Loan+1):

         if i==0:
                continue
         else:
# center element

          Balance.append(np.fv(Rate_Period/100,x.Payments_Per_Year,Monthly_Payment, -Balance[i-1]))

#left elements

          Cumulative_Payments.append(i*Monthly_Payment*x.Payments_Per_Year)   

          Yearly_Payments.append(Balance[i-1]-Balance[i])

          Yearly_Interest.append((Cumulative_Payments[i]-Cumulative_Payments[i-1])-Yearly_Payments[i])
# right elements

          Cumulative_Principal.append(x.amount-Balance[i])

          Cumulative_Interest.append(Cumulative_Payments[i]-Cumulative_Principal[i])

    

# rounding the variable to 2 decimal point
    Balance=[round(value, 2) for value in Balance]
    Cumulative_Payments=[round(value, 2) for value in Cumulative_Payments]
    Yearly_Payments=[round(value, 2) for value in Yearly_Payments]
    Yearly_Interest=[round(value, 2) for value in Yearly_Interest]
    Cumulative_Principal=[round(value, 2) for value in Cumulative_Principal]
    Cumulative_Interest=[round(value, 2) for value in Cumulative_Interest]
    
    Yearly_Amortization=zip(Balance, Cumulative_Payments, Yearly_Payments, Yearly_Interest, Cumulative_Principal, Cumulative_Interest)
    
    
    
    return render(request,'loan/loan.html',{"Summary_of_Results":Summary_of_Results,"Yearly_Amortization":Yearly_Amortization})
#Create your views here.
