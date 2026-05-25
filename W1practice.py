def is_palindrome(text):

    cleaned_text = "".join(text.lower().split())
    

    return cleaned_text == cleaned_text[::-1]


def generate_fibonacci(n):
    sequence = [0, 1]
    
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        
    return sequence[:n] if n > 0 else []


print("--- 1. Dynamic Palindrome Checker ---")
user_word = input("Enter a word or phrase to check: ")

if is_palindrome(user_word):
    print(f"✅ '{user_word}' is a palindrome!")
else:
    print(f"❌ '{user_word}' is NOT a palindrome.")


print("\n--- 2. Dynamic Fibonacci Sequence Generator ---")
try:
    # input() takes everything as a string, so we cast it to an integer
    user_terms = int(input("How many Fibonacci terms would you like to generate? "))
    
    fib_result = generate_fibonacci(user_terms)
    print(f"Generated sequence: {fib_result}")
except ValueError:
    print("❌ Please enter a valid whole number.")