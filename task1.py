#password checker task
import string 

class PasswordChecker:
    def __init__(self, pwd):
        self.pwd = pwd
        self.score = 0
        self.feedback = []

    def analyze(self):
        self.score = 0
        self.feedback = []

        if len(self.pwd) >= 6:
            self.score += 1
        else:
            self.feedback.append("Password should be at least 6 characters long")
        
        if any(char.isupper() for char in self.pwd):
            self.score += 1
        else:
            self.feedback.append("Missing an uppercase letter")

        
        if any(char.islower() for char in self.pwd):
            self.score += 1
        else:
            self.feedback.append("Missing a lowercase letter")

        
        if any(char.isdigit() for char in self.pwd):
            self.score += 1
        else:
            self.feedback.append("Missing a digit")
        
        
        if any(char in string.punctuation for char in self.pwd):
            self.score += 1
        else:
            self.feedback.append("Missing a special character")

    def get_report(self):
        if self.score >= 5:
            return "Strong"
        elif self.score >= 3:
            return "Medium"
        else:
            return "Weak"


user_input = input("Enter the password: ")
checker = PasswordChecker(user_input)
checker.analyze()

print(f"--- Results for: {user_input} ---")
print(f"Strength: {checker.get_report()}")

if checker.feedback:
    print("Improvements needed:")
    for tip in checker.feedback:
        print(f" - {tip}")