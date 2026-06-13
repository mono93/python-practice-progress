import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load data set
data = pd.read_csv("salary.csv")

x = data[["yearsOfExperience"]]
y = data["salary"]

model = LinearRegression()
model.fit(x, y)

data["predictedSalary"] = model.predict(x)

print("Model Coefficient (slope)", round(float(model.coef_[0]), 2))
print("Model intercept (base salary)", round(float(model.intercept_), 2))

plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, data["predictedSalary"], color="red", label="Regression Line")

plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()