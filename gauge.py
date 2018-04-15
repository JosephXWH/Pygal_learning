import pygal
gauge_chart = pygal.Gauge(human_readable=False)
gauge_chart.title = 'DeltaBlue V8 benchmark results'
gauge_chart.range = [0, 10000]
gauge_chart.add('Chrome', 8212)
gauge_chart.add('Firefox', 8099)
gauge_chart.add('Opera', 2933)
gauge_chart.add('IE', 41)
gauge_chart.render_to_file('gauge.svg')