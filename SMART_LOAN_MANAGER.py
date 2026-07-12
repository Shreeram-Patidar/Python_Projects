print("=" * 55)
print("        WELCOME TO SMART LOAN MANAGER")
print("=" * 55)

input("\nPress Enter to Continue...")
name = ""
age = 0
gender = ""
occupation = ""
mobile = ""
city = ""
income = 0
cibil = 0
loan = 0
amount = 0
duration = 0
status = ""
reason = ""
while True:

    print("\n" + "=" * 55)
    print("              MAIN MENU")
    print("=" * 55)
    print("1. Loan Information")
    print("2. Apply for Loan")
    print("3. Check Eligibility")
    print("4. EMI Calculator")
    print("5. View Loan Report")
    print("6. Exit")
    print("=" * 55)

    choice = int(input("Enter your choice : "))

    match choice:
          case 1:
               print("\n" + "="*55)
               print("            LOAN INFORMATION")
               print("="*55)
             
               print("1. Home Loan")
               print("2. Personal Loan")
               print("3. Education Loan")
               print("4. Vehicle Loan")
               print("5. Gold Loan")
               print("6. Business Loan")
               print("7. MSME Loan")
               print("8. Mudra Loan")
               print("9. Kisan Credit Card (KCC) Loan")

               loan = int(input("\nSelect Loan Type : "))
               
               match loan:
                     case 1:
                          print("\n" + "=" * 55)
                          print("                  HOME LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 8.5% per year")
                          print("Maximum Loan Amount   : ₹1 Crore")
                          print("Maximum Tenure        : 30 Years")
                          print("Minimum Age           : 21 Years")
                          print("Maximum Age           : 65 Years")
                          print("Minimum Income        : ₹50,000/month")
                          print("Minimum CIBIL Score   : 700")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- Property Documents")
                          print("- Income Proof")
                          print("- Bank Statement")

                          print("\nEligibility:")
                          print("- Age between 21 and 65 years")
                          print("- Monthly income ₹50,000 or above")
                          print("- CIBIL score 700 or above")
                          print("- Valid property documents")

                          print("\nBenefits:")
                          print("- Low Interest Rate")
                          print("- Long Repayment Period")
                          print("- High Loan Amount")
                          print("- Tax Benefits")
                          print("- Easy EMI Options")

                          print("=" * 55)
        

                     case 2:
                          print("\n" + "=" * 55)
                          print("                PERSONAL LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 12% per year")
                          print("Maximum Loan Amount   : ₹20 Lakh")
                          print("Maximum Tenure        : 5 Years")
                          print("Minimum Age           : 21 Years")
                          print("Maximum Age           : 60 Years")
                          print("Minimum Income        : ₹25,000/month")
                          print("Minimum CIBIL Score   : 700")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- Salary Slip")
                          print("- Address Proof")
                          print("- Bank Statement")

                          print("\nEligibility:")
                          print("- Age between 21 and 60 years")
                          print("- Monthly income ₹25,000 or above")
                          print("- CIBIL score 700 or above")
                          print("- Valid identity proof")

                          print("\nBenefits:")
                          print("- No Collateral Required")
                          print("- Fast Approval")
                          print("- Instant Disbursement")
                          print("- Flexible Usage")
                          print("- Easy EMI Options")

                          print("=" * 55)

                     case 3:
                          print("\n" + "=" * 55)
                          print("               EDUCATION LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 7.5% per year")
                          print("Maximum Loan Amount   : ₹50 Lakh")
                          print("Maximum Tenure        : 15 Years")
                          print("Minimum Age           : 18 Years")
                          print("Maximum Age           : 35 Years")
                          print("Minimum Income        : Guardian Required")
                          print("Minimum CIBIL Score   : 650")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- Admission Letter")
                          print("- Fee Structure")
                          print("- Guardian Income Proof")

                          print("\nEligibility:")
                          print("- Indian citizen")
                          print("- Admission in recognized institute")
                          print("- Guardian with stable income")
                          print("- Required documents available")

                          print("\nBenefits:")
                          print("- Low Interest Rate")
                          print("- Moratorium Period")
                          print("- Covers Tuition Fees")
                          print("- Flexible Repayment")
                          print("- Supports Higher Education")

                          print("=" * 55)

                     case 4:
                          print("\n" + "=" * 55)
                          print("                VEHICLE LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 9% per year")
                          print("Maximum Loan Amount   : ₹50 Lakh")
                          print("Maximum Tenure        : 7 Years")
                          print("Minimum Age           : 21 Years")
                          print("Maximum Age           : 65 Years")
                          print("Minimum Income        : ₹30,000/month")
                          print("Minimum CIBIL Score   : 700")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- Driving Licence")
                          print("- Income Proof")
                          print("- Bank Statement")

                          print("\nEligibility:")
                          print("- Age between 21 and 65 years")
                          print("- Monthly income ₹30,000 or above")
                          print("- CIBIL score 700 or above")
                          print("- Valid driving licence")

                          print("\nBenefits:")
                          print("- Finance New & Used Vehicles")
                          print("- Flexible Repayment")
                          print("- Fast Processing")
                          print("- Affordable EMI")
                          print("- Quick Approval")

                          print("=" * 55)

                     case 5:
                          print("\n" + "=" * 55)
                          print("                  GOLD LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 8% per year")
                          print("Maximum Loan Amount   : Based on Gold Value")
                          print("Maximum Tenure        : 3 Years")
                          print("Minimum Age           : 18 Years")
                          print("Maximum Age           : 70 Years")
                          print("Minimum Income        : Not Mandatory")
                          print("Minimum CIBIL Score   : Not Required")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- Gold Jewellery")
                          print("- Address Proof")
                          print("- Passport Size Photo")

                          print("\nEligibility:")
                          print("- Applicant must own gold")
                          print("- Valid identity proof")
                          print("- Age above 18 years")
                          print("- Gold should meet purity standards")

                          print("\nBenefits:")
                          print("- Quick Approval")
                          print("- Low Documentation")
                          print("- Lower Interest Rate")
                          print("- No Income Proof Required")
                          print("- Safe Gold Storage")

                          print("=" * 55)

                     case 6:
                          print("\n" + "=" * 55)
                          print("               BUSINESS LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 11% per year")
                          print("Maximum Loan Amount   : ₹2 Crore")
                          print("Maximum Tenure        : 10 Years")
                          print("Minimum Age           : 21 Years")
                          print("Maximum Age           : 65 Years")
                          print("Minimum Income        : ₹50,000/month")
                          print("Minimum CIBIL Score   : 700")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- GST Certificate")
                          print("- Business Registration")
                          print("- Bank Statement")

                          print("\nEligibility:")
                          print("- Existing business")
                          print("- Good credit score")
                          print("- Stable income")
                          print("- Valid business documents")

                          print("\nBenefits:")
                          print("- Business Expansion")
                          print("- Working Capital")
                          print("- Flexible Repayment")
                          print("- Higher Loan Amount")
                          print("- Quick Processing")

                          print("=" * 55)

                     case 7:
                          print("\n" + "=" * 55)
                          print("                 MSME LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 9.5% per year")
                          print("Maximum Loan Amount   : ₹5 Crore")
                          print("Maximum Tenure        : 15 Years")
                          print("Minimum Age           : 21 Years")
                          print("Maximum Age           : 65 Years")
                          print("Minimum Income        : Business Income")
                          print("Minimum CIBIL Score   : 700")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- UDYAM Registration")
                          print("- GST Certificate")
                          print("- Bank Statement")

                          print("\nEligibility:")
                          print("- Registered MSME")
                          print("- Good credit history")
                          print("- Business proof")
                          print("- Stable business income")

                          print("\nBenefits:")
                          print("- Government Support")
                          print("- Lower Interest")
                          print("- Business Growth")
                          print("- Flexible EMI")
                          print("- High Loan Amount")

                          print("=" * 55)

                     case 8:
                          print("\n" + "=" * 55)
                          print("                 MUDRA LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 8% per year")
                          print("Maximum Loan Amount   : ₹10 Lakh")
                          print("Maximum Tenure        : 5 Years")
                          print("Minimum Age           : 18 Years")
                          print("Maximum Age           : 65 Years")
                          print("Minimum Income        : Business Income")
                          print("Minimum CIBIL Score   : 650")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- Business Proof")
                          print("- Address Proof")
                          print("- Bank Statement")

                          print("\nEligibility:")
                          print("- Indian citizen")
                          print("- Small business owner")
                          print("- Valid business documents")
                          print("- Business plan")

                          print("\nBenefits:")
                          print("- Government Scheme")
                          print("- No Collateral")
                          print("- Easy Approval")
                          print("- Supports Startups")
                          print("- Affordable EMI")

                          print("=" * 55)

                     case 9:
                          print("\n" + "=" * 55)
                          print("      KISAN CREDIT CARD (KCC) LOAN")
                          print("=" * 55)
                          print("Interest Rate         : 4% - 7% per year")
                          print("Maximum Loan Amount   : Depends on Land Holding")
                          print("Maximum Tenure        : 5 Years")
                          print("Minimum Age           : 18 Years")
                          print("Maximum Age           : 75 Years")
                          print("Minimum Income        : Farming Income")
                          print("Minimum CIBIL Score   : Not Mandatory")

                          print("\nDocuments Required:")
                          print("- Aadhaar Card")
                          print("- PAN Card")
                          print("- Land Records")
                          print("- Passport Size Photo")
                          print("- Bank Passbook")

                          print("\nEligibility:")
                          print("- Indian farmer")
                          print("- Agricultural land ownership")
                          print("- Valid land records")
                          print("- Identity proof")

                          print("\nBenefits:")
                          print("- Low Interest Rate")
                          print("- Agricultural Support")
                          print("- Flexible Repayment")
                          print("- Easy Credit Access")
                          print("- Government Subsidy")

                          print("=" * 55)

                     case __:
                          print("Invalid Choice!")

          case 2:

               print("\n" + "=" * 55)
               print("               APPLY FOR LOAN")
               print("=" * 55)

               print("\nEnter Applicant Details\n")

               name = input("Applicant Name          : ")
               age = int(input("Age                     : "))
               gender = input("Gender (Male/Female)    : ")
               occupation = input("Occupation              : ")
               mobile = input("Mobile Number           : ")
               city = input("City                    : ")

               print("\nFinancial Details\n")

               income = int(input("Monthly Income (₹)      : "))
               cibil = int(input("CIBIL Score             : "))

               print("\nSelect Loan Type\n")

               print("1. Home Loan")
               print("2. Personal Loan")
               print("3. Education Loan")
               print("4. Vehicle Loan")
               print("5. Gold Loan")
               print("6. Business Loan")
               print("7. MSME Loan")
               print("8. Mudra Loan")
               print("9. Kisan Credit Card (KCC) Loan")

               loan = int(input("\nEnter Loan Type : "))

               amount = int(input("Required Loan Amount (₹): "))
               duration = int(input("Loan Duration (Years)   : "))

               print("\n" + "=" * 55)
               print("Application Submitted Successfully")
               print("=" * 55)

               print("Applicant Name  :", name)
               print("Selected Loan   :", loan)
               print("Loan Amount     : ₹", amount)
               print("Duration        :", duration, "Years")
 
               print("\nYour application has been recorded.")
               print("Please select 'Check Eligibility' from the Main Menu.")

               input("\nPress Enter to return to Main Menu...")

          case 3:
               if loan == 0:
                  print("\n====================================")
                  print("No Loan Application Found!")
                  print("Please select 'Apply for Loan' first.")
                  print("====================================")
                  input("\nPress Enter to return to Main Menu...")
                  continue

               print("\n" + "=" * 55)
               print("             ELIGIBILITY CHECKER")
               print("=" * 55)

               status = "Rejected"
               reason = ""

               match loan:

                    case 1:  # Home Loan
                         if age >= 21 and age <= 65:
                            if income >= 50000:
                               if cibil >= 700:
                                  if amount <= income * 50:
                                     status = "Approved"
                                  else:
                                     reason = "Loan amount exceeds limit."
                               else:
                                  reason = "CIBIL Score should be 700 or above."
                            else:
                               reason = "Monthly income should be at least ₹50,000."
                         else:
                            reason = "Age should be between 21 and 65."

                    case 2:  # Personal Loan
                         if age >= 21 and age <= 60:
                            if income >= 25000:
                               if cibil >= 700:
                                  if amount <= income * 20:
                                     status = "Approved"
                                  else:
                                     reason = "Loan amount exceeds limit."
                               else:
                                  reason = "CIBIL Score should be 700 or above."
                            else:
                               reason = "Monthly income should be at least ₹25,000."
                         else:
                            reason = "Age should be between 21 and 60."
                    case 3:  # Education Loan
                         if age >= 18 and age <= 35:
                            if cibil >= 650:
                               if amount <= 5000000:
                                  status = "Approved"
                               else:
                                  reason = "Requested amount exceeds maximum limit."
                            else:
                               reason = "CIBIL Score should be 650 or above."
                         else:
                            reason = "Age should be between 18 and 35."

                    case 4:  # Vehicle Loan
                         if age >= 21 and age <= 65:
                            if income >= 30000:
                               if cibil >= 700:
                                  status = "Approved"
                               else:
                                  reason = "CIBIL Score should be 700 or above."
                            else:
                               reason = "Monthly income should be at least ₹30,000."
                         else:
                            reason = "Age should be between 21 and 65."
                    case 5:  # Gold Loan
                         if age >= 18:
                            status = "Approved"
                         else:
                            reason = "Minimum age should be 18 years."

                    case 6:  # Business Loan
                         if age >= 21 and age <= 65:
                            if income >= 50000:
                               if cibil >= 700:
                                  status = "Approved"
                               else:
                                  reason = "CIBIL Score should be 700 or above."
                            else:
                               reason = "Monthly income should be at least ₹50,000."
                         else:
                            reason = "Age should be between 21 and 65."
                    case 7:  # MSME Loan
                         if age >= 21 and age <= 65:
                            if cibil >= 700:
                               status = "Approved"
                            else:
                               reason = "CIBIL Score should be 700 or above."
                         else:
                            reason = "Age should be between 21 and 65."
                    case 8:  # Mudra Loan
                         if age >= 18 and age <= 65:
                            if cibil >= 650:
                               status = "Approved"
                            else:
                               reason = "CIBIL Score should be 650 or above."
                         else:
                            reason = "Age should be between 18 and 65."
                    case 9:  # KCC Loan
                         if age >= 18 and age <= 75:
                            status = "Approved"
                         else:
                            reason = "Age should be between 18 and 75."

               print("\n" + "=" * 55)
               print("             ELIGIBILITY RESULT")
               print("=" * 55)

               print("Applicant Name :", name)

               if status == "Approved":
                  print("Status         : APPROVED")
                  print("Congratulations! Your loan is eligible.")
               else:
                  print("Status         : REJECTED")
                  print("Reason         :", reason)

               print("=" * 55)

               input("\nPress Enter to continue...")

          case 4:
               
               if loan == 0:
                  print("\nPlease apply for a loan first.")
                  input("Press Enter to continue...")
                  continue

               if status != "Approved":
                  print("\nLoan is not approved.")
                  print("EMI cannot be calculated.")
                  input("\nPress Enter to continue...")
                  continue

               print("\n" + "=" * 55)
               print("              EMI CALCULATOR")
               print("=" * 55)

               match loan:

                     case 1:
                          rate = 8.5
                     case 2:
                          rate = 12
                     case 3:
                          rate = 7.5
                     case 4:
                          rate = 9
                     case 5:
                          rate = 8
                     case 6:
                          rate = 11
                     case 7:
                          rate = 9.5
                     case 8:
                          rate = 8
                     case 9:
                          rate = 5

               interest = (amount * rate * duration) / 100
               total_payment = amount + interest
               emi = total_payment / (duration * 12)

               print("Loan Amount        : ₹", amount)
               print("Interest Rate      :", rate, "%")
               print("Loan Duration      :", duration, "Years")
               print("Total Interest     : ₹", round(interest, 2))
               print("Total Payment      : ₹", round(total_payment, 2))
               print("Monthly EMI        : ₹", round(emi, 2))

               input("\nPress Enter to continue...")

          case 5:

               if loan == 0:
                  print("\nPlease apply for a loan first.")
                  input("\nPress Enter to continue...")
                  continue

               print("\n" + "="*60)
               print("               Smart Loan Manger")
               print("                LOAN REPORT")
               print("="*60)

               print("\nApplicant Details")
               print("-"*60)
               print("Applicant Name      :", name)
               print("Age                 :", age)
               print("Gender              :", gender)
               print("Occupation          :", occupation)
               print("Mobile Number       :", mobile)
               print("City                :", city)

               print("\nLoan Details")
               print("-"*60)

               if loan == 1:
                  print("Loan Type           : Home Loan")
               elif loan == 2:
                  print("Loan Type           : Personal Loan")
               elif loan == 3:
                  print("Loan Type           : Education Loan")
               elif loan == 4:
                  print("Loan Type           : Vehicle Loan")
               elif loan == 5:
                  print("Loan Type           : Gold Loan")
               elif loan == 6:
                  print("Loan Type           : Business Loan")
               elif loan == 7:
                  print("Loan Type           : MSME Loan")
               elif loan == 8:
                  print("Loan Type           : Mudra Loan")
               elif loan == 9:
                  print("Loan Type           : KCC Loan")

               print("Loan Amount         : ₹", amount)
               print("Loan Duration       :", duration, "Years")
               print("Interest Rate       :", rate, "%")
               print("Monthly Income      : ₹", income)
               print("CIBIL Score         :", cibil)

               print("\nLoan Calculation")
               print("-"*60)
               print("Total Interest      : ₹", round(interest,2))
               print("Total Payment       : ₹", round(total_payment,2))
               print("Monthly EMI         : ₹", round(emi,2))

               print("\nApplication Status")
               print("-"*60)

               if status == "Approved":
                  print("Status              : APPROVED")
                  print("Congratulations!")
                  print("Your loan has been approved.")
               else:
                  print("Status              : REJECTED")
                  print("Reason              :", reason)

                  print("="*60)
                  print("      Thank You For Choosing Smart Loan Manger")
                  print("="*60)

               input("\nPress Enter to continue...")

          case 6:
               exit_choice = input("\nAre you sure you want to exit? (yes/no): ").lower()

               if exit_choice == "yes":
                  print("\nThank you for visiting Smart Loan Manger.")
                  print("Have a Great Day!")
                  break
               else:
                  print("\nReturning to Main Menu...")

          case __:
               print("\nInvalid Choice!")
               print("Please enter a number between 1 and 6.")
      