#' if applicant has high income AND good credit
# Eligible for loan 'has
has_good_credit= True
has_high_income= True

if has_good_credit or has_high_income:
    print("Eligible for loan")

if has_good_credit and has_high_income:
    print("Eligible for loan")

#'if applicant has good credit and doesn't have a criminal record'
has_good_credit= True
has_criminal_record=True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
