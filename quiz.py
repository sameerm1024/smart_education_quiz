import random

states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

def quiz():
    score = 0
    num_questions = 5
    states = list(states_and_capitals.keys())
    random.shuffle(states)

    for i in range(num_questions):
        state = states[i]
        capital = states_and_capitals[state]
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The capital of {state} is {capital}.")

    print(f"\nYour final score is {score}/{num_questions}")

quiz()
