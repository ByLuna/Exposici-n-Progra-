import pandas as pd
import random
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Tabs, TabPanel

output_file("pokemon_visualization.html")

df = pd.read_csv(r'C:\Users\Admin\Documents\python a3\ExpoProgra\pokemon_data.csv', delimiter=';')

types = ['Water', 'Fire', 'Electric', 'Grass', 'Psychic', 'Ice', 'Dragon', 
         'Dark', 'Fairy', 'Normal', 'Fighting', 'Flying', 'Poison', 
         'Ground', 'Rock', 'Bug', 'Ghost', 'Steel']

df['Type 1'] = [random.choice(types) for _ in range(len(df))]

type_colors = {
    'Water': 'blue', 'Fire': 'red', 'Electric': 'yellow', 'Grass': 'green',
    'Psychic': 'purple', 'Ice': 'lightblue', 'Dragon': 'orange', 'Dark': 'black',
    'Fairy': 'pink', 'Normal': 'gray', 'Fighting': 'brown', 'Flying': 'skyblue',
    'Poison': 'violet', 'Ground': 'saddlebrown', 'Rock': 'darkgray', 
    'Bug': 'olive', 'Ghost': 'indigo', 'Steel': 'slategray'
}

df['color'] = df['Type 1'].map(type_colors)

source1 = ColumnDataSource(df[df["Legendary"] == True])
source2 = ColumnDataSource(df[df["Legendary"] == False])

hover = HoverTool(
    tooltips=[
        ("Name", "@Name"),
        ("Type", "@{Type 1}"),  
        ("Attack", "@Attack"),
        ("Defense", "@Defense")
    ]
)

p1 = figure(width=500, height=500, title="Pokémons Legendarios",
            x_axis_label='Attack', y_axis_label='Defense',
            background_fill_color="#f0f0f0")

p1.scatter(x='Attack', y='Defense', source=source1, color='color', size=12, legend_field='Type 1')
p1.add_tools(hover)
p1.legend.location = "top_left"


p2 = figure(width=500, height=500, title="Pokémons No Legendarios",
            x_axis_label='Attack', y_axis_label='Defense',
            background_fill_color="#f0f0f0")

p2.scatter(x='Attack', y='Defense', source=source2, color='color', size=8, legend_field='Type 1')
p2.add_tools(hover)
p2.legend.location = "top_left"


tab1 = TabPanel(child=p1, title="Legendarios")
tab2 = TabPanel(child=p2, title="No Legendarios")

tabs = Tabs(tabs=[tab1, tab2])

show(tabs)
