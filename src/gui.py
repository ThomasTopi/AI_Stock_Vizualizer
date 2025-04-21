import streamlit as st
from src.data_loader import DataLoader

class MainPage:
    def __init__(self) -> None:
        st.title("AI Stock Analyzer")
        st.sidebar.title("Stock Picker")
        self.get_tickers()


    def get_tickers(self) -> None:
        predefined_examples = "TSLA, AAPL, NVDA"
        user_input = st.sidebar.text_input("Enter Ticker/Tickers that you want to analyse:", value=predefined_examples)
        if st.sidebar.button("Analyse"):
            self.analyse_data(user_input)

    def analyse_data(self, tickers:list[str]) -> None:
        tickers = [i.strip() for i in tickers.split(",")]
        for ticker in tickers:
            st.write(f"Analysing: {ticker} stock")
            try:
                data = DataLoader(ticker).get_info()
                if data:
                    st.write(data)
                else:
                    st.write(f"No data found for ticker: {ticker}. Please check if the ticker is correct!")
            except Exception as e:
                st.write(f"An error occurred while fetching data for {ticker}: Please check if the ticker is correct!")

    def data_formater(self):
        """ToDo:
            Prepare data formater to fetch data from DataLoader and update them.
        """