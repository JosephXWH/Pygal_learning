import pygal
hist = pygal.Histogram()
hist.add('Widen bars',[(5,0,10),(4,5,13),(2,4,12)])
hist.add('Narrow bars',[(9,2,4),(7,7,7.5),(10,11,12)])
hist.render_to_file('Histogram.svg')