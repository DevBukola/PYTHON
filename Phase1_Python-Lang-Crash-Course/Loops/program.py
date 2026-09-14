times = input("How many times do I have to tell you?: ");
time = int(times);

for t in range(time):
    print(f" time {t+1}: Clean up your room!")


for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky";
    elif num % 2 == 0:
        state = "even";
    else:
        state = "odd";
    print(f"{num} is {state}.");
