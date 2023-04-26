import re

def is_valid_credit_card_number(c_num):
    consecutive_nums = r'(\d)\1{3}'  # matches when there are 4 consecutive digits
    pattern = r'^[4,5,6]\d{3}(?:-?\d{4}){3}$'
    
    if re.match(pattern,c_num) and not re.search(consecutive_nums,c_num):
        return print("The credit card number is valid")
    else:
        return print("The credit card number is invalid")
    


is_valid_credit_card_number("4567-4567-4567-4567")
is_valid_credit_card_number("aaa")
is_valid_credit_card_number("4567-4567-4567-456788")
is_valid_credit_card_number("4567-4567-0000-4567")
is_valid_credit_card_number("9567-4567-4567-4567")
is_valid_credit_card_number("9567-456777-4567-4567")

