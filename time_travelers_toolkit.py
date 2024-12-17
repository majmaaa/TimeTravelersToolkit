import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# time_travelers_toolkit.py

# Importing necessary modules
import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# Step 5: Retrieve the current date and time
current_date = dt.date.today()
current_time = dt.datetime.now().time()

# Step 6: Print the current date and time
print(f"Current Date: {current_date}")
print(f"Current Time: {current_time:%H:%M:%S}")

# Step 7: Calculate the cost of time travel
base_cost = Decimal('1000.00')
current_year = current_date.year
random_year = randint(1800, 2500)
year_difference = abs(current_year - random_year)
cost_multiplier = Decimal('0.05')
final_cost = base_cost + (Decimal(year_difference) * cost_multiplier)

# Step 8: Format the final cost
final_cost = round(final_cost, 2)

# Step 9: Generate a random year
random_year = randint(1800, 2500)

# Step 10: Create a list of destinations and select one randomly
destinations = [
    "Ancient Rome",
    "Medieval Europe",
    "The Future Metropolis",
    "The Roaring Twenties",
    "Jurassic Era",
    "The Space Colonies"
]
selected_destination = choice(destinations)

# Step 11: Generate the time travel message
message = custom_module.generate_time_travel_message(random_year, selected_destination, final_cost)
print(message)
