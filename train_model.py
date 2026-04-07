from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Modeling
X = df[[
    'luas_ha',
    'umur_tanaman',
    'populasi_ha',
    'produksi',
    'pupuk_npk',
    'curah_hujan',
    'sex_ratio',
]]
y = df['yield_kg_ha']

# Split Training
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    shuffle=False
)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)