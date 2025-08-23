# 🧪 PrestaShop Automation Tests

This project contains automated UI tests for a PrestaShop storefront using **Selenium** + **Pytest**.  
The tests cover core checkout flows such as registration, adding products to cart, handling out-of-stock warnings, and placing orders.

---

## 📂 Project Structure

```
automation-prestashop/
├── pages/                 # Page Object Models (HomePage, AuthPage, CheckoutPage, etc.)
├── tests/                 # Test cases
├── utils/                 # Helper utilities (storefront, test data, etc.)
├── reports/               # Test reports (generated after test runs)
├── conftest.py            # Pytest fixtures (e.g., driver setup/teardown)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone "https://github.com/isubarnaL/automation-prestashop.git"
cd automation-prestashop
```

### 2. Create a virtual environment
```bash
python -m venv venv
# Activate:
# On Linux/macOS
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

### Run all tests
```bash
pytest
```

### Run tests with HTML report(RECOMMENDED)
Reports will be saved inside the `reports/` folder:
```bash
pytest -v --html=reports/report.html --self-contained-html --log-cli-level=INFO --capture=tee-sys
```

### Run a specific test file
```bash
pytest tests/test_checkout.py
```

---

## 🛠 Features Covered

- ✅ User registration & login  
- ✅ Selecting products  
- ✅ Setting large quantities (e.g., 1000) → Verify **Out of Stock** message (via `.js-product-availability`)  
- ✅ Resetting to valid quantity (e.g., 10) → Add to cart successfully → Cart modal appears  
- ✅ Proceeding to checkout (address, shipping, payment, place order)  

---


## ✅ Example Test Flow

1. Open storefront  
2. Register a new customer  
3. Select first product  
4. Set quantity to `1000` → Out-of-stock warning is displayed  
5. Set quantity to `10` → Add to cart successfully → Cart modal appears  
6. Proceed through checkout (address, shipping, payment, place order)  

---

## 📖 Notes
- Selenium waits are handled with `WebDriverWait` and `expected_conditions`.  
- Reports are automatically generated under `reports/`.  
- Logging is included for better debugging (`INFO` for steps, `ERROR` for failures`).  
