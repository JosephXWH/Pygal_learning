import pygal
from datetime import timedelta
dateline = pygal.TimeDeltaLine(x_label_rotation=25)
dateline.add("Serie", [
  (timedelta(), 0),
  (timedelta(seconds=6), 5),
  (timedelta(minutes=11, seconds=59), 4),
  (timedelta(days=3, microseconds=30), 12),
  (timedelta(weeks=1), 10),
])
dateline.render_to_file('delta.svg')