from textblob import TextBlob
y=input("Identify sentiment: ")
z=TextBlob(y)
x=z.sentiment.polarity

if x<0:
	print("Negative")
elif x==0:
	print("Neutral")
elif x>0 and x<=1:
	print("Positive")