print("How many kilometers did you run today?");
kms = input();
# miles = kms/1.60934;
miles = float(kms)/1.60934;
miles = round(miles, 2);
print(f"Okay, your {kms}km run was {miles}mi.");

# round(the thing to round, how many decimal points to round it to.);

userName = "Simi";
userAge = 26;
userEmail = "simi@gmail.com";
userBal = 100000000000;
userActiveStatus = "active";

print(f"{userName} is {userAge}, her email address is {userEmail} with an account balance of {userBal} and an {userActiveStatus} status.");

color = input("What is your favorite color to paint your house?: ");
if color == "Comeo":
    print("Excellent and amazing choice!");
elif color == "Pink":
    print("Beautiful!");
elif color == "Teal":
    print("Not a bad choice.");
elif color == "Black":
    print("Eww!");
else:
    print("LOL!");