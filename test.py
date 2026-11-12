import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [2, 4, 6, 8]})
model = LinearRegression().fit(df[["x"]], df["y"])
print(model.predict(pd.DataFrame({"x": [5]})))