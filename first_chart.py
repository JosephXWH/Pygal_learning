import pygal                                                       # First import pygal
bar_chart = pygal.HorizontalStackedBar()                                            # Then create a bar graph object
bar_chart.title = "Remarquable sequences"
bar_chart.x_labels = map(str, range(11))
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
bar_chart.add('China', [0, 3, 3, 4, 6, 10, 16, 26, 42, 68, 110])
bar_chart.render_to_file('bar_chart.svg')                          # Save the svg to a file
