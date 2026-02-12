import random
questions=[["I am able to regulate my emotions.  ",1],["I pick up on body language cues.  ",1],["When making a high-stakes decision, I try to factor in how I'm feeling now as well as how I might feel later.  ",1],["I can remain collected during conflict.  ",1],["I remain non-judgmental and accept the emotions of others.  ",1],["I’m easily overwhelmed by strong sensory input.  ",2],["I’m easily overwhelmed by things like bright lights, strong smells, coarse fabrics, or sirens.  ",2],["I notice when small things have changed in my environment.  ",2],["I enjoy violent films, TV shows, and movies.  ",2],["My nervous system sometimes feels so frazzled that I have to be alone.  ",2],["When a stranger talks to me, I consider it an opportunity to make a connection.  ",3],["Being out with a big group of friends all night can be exhausting.  ",3],["It’s not unusual for me to get lost in thought around other people.  ",3],["I think that being on a reality show would be a nightmare.  ",3],["I don’t mind talking about anything, even if I’m not that knowledgeable about it.  ",3],["I can usually stay calm during a crisis.  ",4],["I feel very embarrassed when I make small mistakes or commit a social faux pas.  ",4],["I believe I can handle almost anything that life throws at me.  ",4],["My unhappy moods never last too long.  ",4],["Mistakes that I made years ago often pop back into my mind and fill me with shame.  ",4]]
random.shuffle(questions)
marks=[0,0,0,0]
results=[["very low emotional intelligence","very few signs of high sensitivity","strongly introverted","no emotional stability"],["low emotional intelligence","few signs of high sensitivity","somewhat introverted","low emotional stability"],["neither low nor high emotional intelligence","some signs of high sensitivity","mixed by extroverted and introverted signs","middle emotional stability"],["high emotional intelligence","several signs of high sensitivity","somewhat extroverted","moderate emotional stability"],["very high emotional intelligence","strong signs of high sensitivity","strongly extroverted","high emotional stability"]]
print("""
The personality test about emotional intelligence,sensitivity,introversion/extroversion and emotional stability starts.
Using numbers from 1 to 5, answer the questions based on how strongly you agree or disagree with the statement.
1-5 represents from disagree to agree.
""")
for x in questions:
    y=int(input(x[0]))
    if x[1]==1:
        marks[0]+=y
    elif x[1]==2:
        marks[1]+=y
    elif x[1]==3:
        marks[2]+=y
    elif x[1]==4:
        marks[3]+=y
    if y<1 or y>5:
        print("Your choice is invalid, the test stops.")
        exit()
print(f"""
      Here are your scores:
      1.emotional intelligence: {marks[0]}/25
      2.sensitivity: {marks[1]}/25
      3.introversion/extroversion: {marks[2]}/25
      4.emotional stability: {marks[3]}/25 """)
for z in range(4):
    if 5<=marks[z]<=8:
        marks[z]=results[0][z]
    elif 9<=marks[z]<=12:
        marks[z]=results[1][z]
    elif 13<=marks[z]<=17:
        marks[z]=results[2][z]
    elif 18<=marks[z]<=21:
        marks[z]=results[3][z]
    elif 22<=marks[z]<=25:
        marks[z]=results[4][z]
print(f"""
You are a person with {marks[0]} and {marks[1]}.
In addition, you are {marks[2]} and you have {marks[3]}.
""",end="")
