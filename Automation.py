import random
import time

character = ['the hero', 'the villain', 'the sidekick', 'the antihero', 'the mentor', 'the love interest', 'that one random character', 'the dog', 'a fool', 'a chosen one', 'a normal girl', 'an alien', 'an eldritch being of unimaginable darkness']
characterdet = ['who wants love', 'who wants acceptance', 'who is angry', 'who is not as bad as they seem', 'who has a great and terrible secret', 'who really wants a hamburger', 'who has three friends', 'whose friends would follow them to hell with eyes wide open']
verb = ['dies', 'wins', 'loses', 'survives', 'yodels', 'talks some sense into the idiot', 'dooms themself', 'hacks into a top-secret thing', 'is an idiot', 'chases a kangaroo', 'summons the devil', 'summons a devil (no, not the one youre thinking of)']
details = ['stupidly', 'to save the world', 'with a hairbrush', 'with extreme prejudice', 'in the name of a lord, though not neccessarily a good one', 'violently', 'and dies', 'with time-travel', 'for their one true love', 'because they are human', 'tragically']
ran = random.randint(0, 12)
rand = random.randint(0, 10)
r = random.randint(0, 10)
ra = random.randint(0, 7)
t = time.time()
if time.time() - t > 86400:
  print("Write a story where", character[ran], characterdet[ra], verb[rand], details[r])
  t = time.time()