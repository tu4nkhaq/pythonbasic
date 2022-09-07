
import pandas as pd
songs={'Album':['Thriller','Back in Black','The Dark Side of the Moon',\
'The Bodyguard','Bat Out of Hell'],
'Released':[1982,1980,1973,1992,1977],
'Length':['00:42:19','00:42:11','00:42:49','00:57:44','00:46:33']}
song_dataframe=pd.DataFrame(songs)
print(song_dataframe)
