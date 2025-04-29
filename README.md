# CareEco-Company-Assignment
# 📈 One Big Exchange

A mini project to simulate a consolidated live order book by merging multiple exchange feeds.

---

## 📂 Project Structure

- `order_book.py` → Backend logic for order book handling
- `test_order_book.py` → Unit tests for validation
- `app.py` → Frontend UI with live market simulation using Streamlit
- `requirements.txt` → Python packages list

---

## 🚀 How to Run

### 1. Clone / Download Project

```bash
git clone <repo_link>  # or download ZIP
cd one-big-exchange
```
## Install Requirements
```bash
pip install -r requirements.txt

```
## Run Streamlit App
```bash
streamlit run app.py

```
## How to Run Tests
```bash
python test_order_book.py

```
Features

    Consolidated Order Book for multiple symbols (AAPL, GOOG, MSFT, TSLA, AMZN)

    Supports both "Top of Book" and "Order Based Book" updates

    Live random exchange feed simulation

    Top 5 levels shown for bids/asks

    Real-time refreshing UI and price charts

    Manual order insertion, cancellation, and modification
