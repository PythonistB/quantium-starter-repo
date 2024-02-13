from dash import Dash, dcc, html
import plotly.express as px 
import pandas as pd 

app = Dash(__name__)

df = pd.read_csv("C:/Users/user/Desktop/final_output.csv")
df = df.sort_values(by = "date")

fig = px.line(df, x = "date", y = "sales", title = "Pink Morsel Sales", color = "region")

app.layout = html.Div([
                  html.H1(style = {'textAlign': 'center'}, children = "Pink Morsel Visualization" ),
                  dcc.Graph(
                       id = "Pink",
                       figure = fig )
                                ])                 
if __name__ == "__main__":
    app.run(debug = True)                 