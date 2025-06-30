# 📧 Email Alias Finder

Easily extract and analyze **email aliases** from a list of email addresses.  
Supports detection of both **plus-addressing aliases** (e.g., `john+promo@gmail.com`) and **role-based aliases** (e.g., `info@domain.com`).  
Groups all related addresses by their “root” mailbox for deeper analysis.

---

## ✨ Features

- 🔎 Detects **plus-addressing aliases** (e.g., `user+label@domain.com`)
- 📧 Detects **role-based aliases** (`info@`, `admin@`, `support@`, etc.)
- 🗂 Groups all addresses by their root mailbox (`user@domain.com`)
- 🚀 Bulk processing of large lists—fast and efficient!
- 📝 Outputs results to CSV files for easy further use

---

## 📦 Files Included

| File                     | Description                                   |
|--------------------------|-----------------------------------------------|
| `email_alias_finder.py`  | Main Python script                            |
| `emails.txt`             | Input file — list of email addresses (sample) |
| `plus_aliases.csv`       | Output: plus-addressing aliases               |
| `role_aliases.csv`       | Output: role-based aliases                    |
| `grouped_mailboxes.csv`  | Output: grouped mailboxes and variants        |

---

## 🏃 Usage

### 1. Prepare your email list

Add one email address per line in `emails.txt`:

info@domain.com
john.doe@gmail.com
john.doe+promo@gmail.com
support@domain.com
jane@another.com
jane+test@another.com

yaml
Copy
Edit

---

### 2. Run the Script

```bash
python email_alias_finder.py

```


3. View the Results
plus_aliases.csv — all plus-addressing alias emails

role_aliases.csv — all role-based alias emails

grouped_mailboxes.csv — all emails grouped by their root mailbox

🧠 How it Works
Plus-addressing detection: Finds emails using the + symbol in the username.

Role-based detection: Matches emails with common aliases like info@, admin@, etc.

Mailbox grouping: All variants (with or without alias) are grouped under the main mailbox.

🛠️ Customization
Add more role-based names to the ROLE_BASED set in the script for your organization’s needs.

Adjust input/output file paths as necessary.

🛡️ License
Open source — use, modify, and share as you like!

Made with ❤️ to simplify email list management.