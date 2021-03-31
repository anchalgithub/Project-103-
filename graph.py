#importing the visualizing library and creating graphs library.
import pandas as pd
import plotly.express as px

df=pd.read_csv("Covid.csv")

#Remember to make the x & y axis labels lowercase
#because otherwise it is going to show an error due it not being in a data frame.
fig=px.scatter(df, x="date", 
                   y="cases", 
                   color="country", 
                   title="Covid-19 Cases in Different Countries")
#calling the function
fig.show()



