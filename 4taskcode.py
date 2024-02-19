from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd 
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

app = Dash(__name__)
df = pd.read_csv("C:/.csv")
df = df.sort_values(by = "date")
fig = px.line(df, x = "date", y = "sales", title = "Pink Morsel Sales")
fig.update_traces(line_color = 'purple')
pio.templates['custom'] = go.layout.Template(
    layout_paper_bgcolor = '#E3D912',
    layout_plot_bgcolor = '#7CE2DB',
    layout_font_color = '#9E0D20',
    layout_font_size = 20
    )
pio.templates.default = 'plotly+custom'

@app.callback(
    Output(dcc.Graph(id = "all_draw",figure = fig),"figure"),
    Input(dcc.RadioItems(["north", "east", "south", "west", "all"],"all",id = "select_location",inline = True), "value")
)
def newgraph(location):
    if location == "all":
        new_drawing = df
    else:
        new_drawing = df[df["region"] == location]
    figure = px.line(new_drawing, x = "date", y = "sales", title = "Pink Morsel Sales") 
    return figure
app.layout = html.Div( style={'backgroundColor': "#983418", "border-radius": "20px"},  
      children = [
      html.H1( "Pink Morsel Visualization", style = {"color": "#0A1A09", "textAlign":"center", "background-color":"#983418", "border-radius": "20px"}),
      dcc.Graph(id = "all_draw", figure = fig),
      dcc.RadioItems(["north", "east", "south", "west", "all"],"all",id = "select_location", inline = True, style = {"font-size": "200%", "textAlign": "center", "color": "#173814", "font-weight": "bold"})
      ])
if __name__ == "__main__":
     app.run(debug = True)