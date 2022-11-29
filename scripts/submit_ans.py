import requests
from request_data import USER_AGENT, SESSION_ID

# may use this some day lmao
URL_DAY_MAIN = f'https://adventofcode.com/2015/day/13/answer'

day_res = requests.post(URL_DAY_MAIN, data={"level":1, "answer":"answer"}, cookies={'session': SESSION_ID, 'User-Agent': USER_AGENT})

print(day_res.text)