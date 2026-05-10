# This function will be tested by the evaluation system. Do not modify the function name or parameters.
def check_loan_eligibility(age: int, income: float) -> str:
   if age >= 21:
      if income >= 25000:
         return "Eligible for loan"
      else:
         return "Not eligible for loan: Income too low"
   else:
      return "Not eligible for loan: Age must be 21 or above"