import requests, streamlit as st

api_url = "https://stock-api-b1vq.onrender.com/"
symbol = st.text_input("Stock symbol", "TSLA")

if st.button("Predict_next_close"):
    r = requests.get(f"{api_url}/predict/live",
                     params={"symbol": symbol})
    data = r.json()
    st.metric("Predicted_next_close",
         data["Predicted_next_close"])
