import streamlit as st
import joblib
model = joblib.load('gold_price_model.pkl')
st.title('Gold Price Predictor')
spx = st.number_input('S&P 500 Index (SPX)', 0.0, 6000.0, 2500.0)
uso = st.number_input('Oil ETF Price (USO)', 0.0, 200.0, 12.0)
slv = st.number_input('Silver ETF Price (SLV)', 0.0, 100.0, 16.0)
eur_usd = st.number_input('EUR/USD Exchange Rate', 0.5, 2.0, 1.15)
if st.button('Predict Gold Price'):
    row = [spx, uso, slv, eur_usd]
    price = model.predict([row])[0]
    st.success(f'Predicted GLD Price: ${price:.2f}')
