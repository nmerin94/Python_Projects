from bokeh.plotting import figure, output_file, show
from motion_detection import df
from datetime import datetime
from motion_detection import assure_path_exists
import os
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y:%m:%d %H:%M:%s")
df["End_string"] = df["Stop"].dt.strftime("%Y:%m:%d %H:%M:%s")

cds = ColumnDataSource(df)

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])


p = figure(x_axis_type = 'datetime', height = 300, width = 500, sizing_mode = "scale_both", title = "Motion_Graph" )
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

p.add_tools(hover)


p.quad(left = "Start", right = "Stop", bottom = 0, top = 1, color = "Green",source=cds)


d = datetime.now().strftime("%Y_%m_%d_%H_%M")

assure_path_exists("html\\Graph%s.html" %(d))


output_file("html\\Graph%s.html" %(d))

show(p)
