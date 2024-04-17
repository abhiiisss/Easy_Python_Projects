from random import randint
import time


sentences = [
    "Python is a low level language",
    "Javascript is used for web development",
    "C and C# is used for quantJavascript is ative finance",
    "How can i learn all of the languages in just 3 months",
    "dude this is crazy all this tongue twisters are weird"
]


def calculate_wpm(time, words):
    minutes = time / 60
    wpm = words / minutes
    return wpm

print("Get ready to type this sentence:")

sentence = sentences[randint(0, 4)]
print(sentence)
time.sleep(1)
print("In 3,", end=" ", flush= True )
time.sleep(1)
print("2,", end=" ", flush= True)
time.sleep(1)
print("1 go!", flush= True)

start_time = time.time()
user_input = input()
end_time = time.time()


if user_input == sentence:
    #calculate wpm
    words = len(sentence.split())
    wpm = calculate_wpm(end_time - start_time, words )
    print("Your typing speed is:", wpm)
else:
    print("Your sentence does not match the above sentence, Try again!")
