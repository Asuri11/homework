def palindrome(s): 
    return s[::-1] == s 

while True: 
    s = input("введите слово: ") 
    print(f"{s} - слово являющееся палиндромом" if palindrome(s) else f"{s} - слово не являющееся палиндромом")
