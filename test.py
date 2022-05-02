from bokeh.plotting import figure, save
from bokeh.resources import CDN
from bokeh.embed import file_html, components

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title='Simple line chart', x_axis_label='x', y_axis_label='y')

p.line(x, y, legend_label='Temp', line_width=2)
html = file_html(p, CDN, "my plot")
print(html)
save(p)