from openai import OpenAI
from secret import my_sk
import time

client = OpenAI(
    api_key=my_sk,
)


# Function for just an API call
def cgpt_msg(msg):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msg,
            }
        ],
        model="gpt-4o",
    )
    return chat_completion.choices[0].message.content

# Well defined prompt
def prompt(co, rh, press, temp):
    tempp = f'''There are 4 parameters measuring air inside a room: CO2, relative humidity, athmospheric pressure and temeperature.
    I want you to compare every specific value with a good value after it, and if it don't fit, than air is bad quality.
    It does not need to fit perfectly.
    I want from you to write just short warning (must be less than 10 words) if air is bad quality and how practicly can be done to improve it. If it is not bad just say everything is good.

    Specific values (to be analized) are:
    CO2 is {co} ppm, less than 1000 is good;
    relative humidity is {rh} percent, good is between 40 and 60;
    athmospheric pressure is {press} hPa, good is between 850 and 1150 hPa;
    temperature is {temp} degress celsius, good is between 20 and 22, less than 20 is cold, more than 22 is to hot.
    
    response to be short as possible'''
    return cgpt_msg(tempp)