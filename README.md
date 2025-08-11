# 💳 Cerberus CC Pro

Cerberus CC Pro is a **professional BIN testing and credit card generator tool** for **security researchers, payment system developers, and fraud prevention testers**.  
It is designed to **simulate** BIN checking, Luhn validation, and SK (Secret Key) method integrations for **educational and legal testing purposes only**.

<img width="1258" height="1012" alt="Screenshot_2025-08-11_15-55-58" src="https://github.com/user-attachments/assets/50706fd9-6b6c-4707-8a54-8661581356e1" />


⚠️ **Disclaimer**  
This tool is **strictly for authorized testing** on systems you own or have explicit permission to test.  
The author is **not responsible** for any illegal use.

---

## ✨ Features

- 🔍 **BIN Checker** — Validate BIN patterns and detect issuer.
- ✅ **Luhn Validator** — Verify card numbers using the Luhn algorithm.
- 🏦 **SK Methods Integration** — Simulated Stripe/Braintree-style validations.
- 🎲 **Random CC Generator** — Generate cards using BIN patterns.
- 🚀 **Multi-threaded Checking** — Fast validation simulations.
- 📂 **Result Filtering** — Separate valid & invalid cards.
- 📄 **File Output** — Save results to `.txt` file.
- 🎨 **Rich Terminal UI** — Beautiful, colored CLI output.

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/CerberusMrX/Cerberus-CC

# Navigate into the folder
cd Cerberus-CC-Pro

# Install required Python packages
pip install -r requirements.txt

# All set
python3 cerberus_cc.py
