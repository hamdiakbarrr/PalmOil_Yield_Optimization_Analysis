import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load Data
df = pd.read_csv("datasetKS2.csv")
df['yield_kg_ha'] = df['produksi'] / df['luas_ha']
subset = df[[
    'populasi_ha',
    'sex_ratio',
    'yield_kg_ha'
]]

#Features & Target
X = df[['populasi_ha','sex_ratio']]
y = df['yield_kg_ha']

#Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

#Train Model
model = LinearRegression()
model.fit(X_train, y_train)

