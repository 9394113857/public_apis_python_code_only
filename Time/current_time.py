from datetime import datetime
import pytz

newYorkTz = pytz.timezone("America/New_York")
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")

print("The current time in New York is:", currentTimeInNewYork)
# Output: The current time in New York is: 05:36:59

# https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#:~:text=You%20can%20get%20the%20current%20time%20in%20a%20particular%20timezone,with%20another%20module%20called%20pytz%20.&text=You%20can%20then%20check%20for,all%20timezones%20of%20the%20world.

