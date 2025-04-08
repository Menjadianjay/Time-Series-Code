import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np


abc = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i+1)
											for i in range(7)]), 
					'classes': [5, 6, 8, 2, 3, 7, 4]})



xyz = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i+1)
											for i in range(7)]), 
					'classes': [2, 3, 7, 3, 4, 1, 2]})


plt.figure(figsize=(12, 6))
plt.plot(abc.date_of_week, abc.classes)
plt.plot(xyz.date_of_week, xyz.classes, color='green')
plt.title('Classes by Date')
plt.xticks(rotation=30, ha='right')
plt.xlabel('Date')
plt.ylabel('Classes')
plt.show()