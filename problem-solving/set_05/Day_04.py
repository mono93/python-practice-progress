import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# load data set
data = pd.read_csv("salary.csv")

x = data[["yearsOfExperience"]]
y = data["salary"]

model = LinearRegression()
model.fit(x, y)

st.title("Salary Predictor based on experience")
st.write("Enter your years of experience to predict your salary:")

year_input = st.number_input("Years of experience", min_value=0.0, max_value=50.0, value=0.0)

if year_input:
    print(year_input)

    predicted_salary = model.predict([[year_input]])[0]
    st.success(f"Estimated Salary: {predicted_salary:,.2f}")

st.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(x, y, color="blue", label="Actual Data")
ax.plot(x, model.predict(x), color="red", label="Regression line")
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()

st.pyplot(fig)


