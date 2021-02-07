"""A vaccination calculator."""

__author__ = "730394070"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

pop: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_pd: int = int (input("Doses per day: "))
target_per: int = int(input("Target percent vaccinated: "))
# User Inputs

target_vac: float = (target_per * pop) / 100
num_vac: float = (doses_admin / 2)
doses_rate: float = (doses_pd / 2)

days: int = round((target_vac - num_vac) / doses_rate)
# Calculations

today: datetime = datetime.today()
vac_day: timedelta = timedelta(days)
future: datetime = today + vac_day
# Calculations for Future Date

percent: str = str(target_per) + "%"
# Find way to print percent sign ?

print("We will reach " + percent + " vaccination in " + str(days) + " days, which falls on " + future.strftime("%B %d, %Y") + ".")