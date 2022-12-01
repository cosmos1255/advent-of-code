import requests
from request_data import USER_AGENT, SESSION_ID

# may use this some day lmao, deff need to work on it though
def submit(level, answer, year, day):
    URL_DAY_MAIN = f'https://adventofcode.com/{year}/day/{day}/answer'

    day_res = requests.post(URL_DAY_MAIN, data={"level":level, "answer":answer}, cookies={'session': SESSION_ID, 'User-Agent': USER_AGENT})
    
    message = day_res.content
    
    if b"That's the right answer" in message:
        print("You got the correct answer!!")
    elif b"Did you already complete it" in message:
        print("Already completed this challenge.")
    elif b"That's not the right answer" in message:
        print("Wrong answer, try again.")
    elif b"You gave an answer too recently" in message:
        print("Gave an answer too recently, try again later.")