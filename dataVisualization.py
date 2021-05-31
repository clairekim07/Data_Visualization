import pandas as panda
import plotly.express as plots

#we can use plotly to make data visualizations
#can also make other graphs too

#this is the line graph
# reads thae csv file and stores it in df
df = panda.read_csv("line_chart.csv")


#you can add by (file,x,y,color,title) to parameters
#the color is where you diffrenciate by different colums
#the x and y have to match from the dataframe/panda
lineGraph = plots.line(df,x="Year",y="Per capita income",color="Country",title="Per Capita Income")
lineGraph.show()

#this is bar chart
bc = panda.read_csv("data.csv")
barChart = plots.bar(bc,x="Country",y="InternetUsers",title="Internet Users per Country")
barChart.show()

#this is scatter chart
sc = panda.read_csv("data.csv")

scatterChart = plots.scatter(sc,x="Population" ,y="Per capita" ,size= "Percentage",color= "Country",size_max= 60)
scatterChart.show()

#this is pie chart
pc = panda.read_csv("data.csv")
#instead of x and y, it only has values
#this is the only one that doesn't have x,y
pieChart = plots.pie(pc,values="Population",color="Country",title="Population by Country")
pieChart.show()