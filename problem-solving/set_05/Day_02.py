import numpy as np
import pandas as pd

# Initialize the modern random number generator with a seed
rng = np.random.default_rng(42)

# Generate the uniform distribution using the generator
years = rng.uniform(0.5, 10, 100).round(2)

salaries = (30000 + years * 6000 + rng.normal(0, 4000, size=100)).round(2)

df = pd.DataFrame({
    "yearsOfExperience": years,
    "salary": salaries
})

df.to_csv("salary.csv", index=False)
print("Data Saved ✅")
