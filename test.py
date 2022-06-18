import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
d = {'Column 1': [i for i in range(10)],
      'Column 2': [i * i for i in range(10)]}
df = pd.DataFrame(d)
df.plot(style=['o', 'rx'])
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()