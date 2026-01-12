# 🧾 Getting User Account Information (Octopus Energy API)

This guide explains how to configure and run the `Octopus_Request_API.py` script to retrieve your Octopus Energy account and consumption data.

---

## 📥 1. Import the Script

Download or copy the script **`Octopus_Request_API.py`** onto your Windows system (recommended platform).

Follow this link for further details 

If you are an Octopus Energy customer, log in to your account and obtain your personal API key.  
It will follow the format:

```
sk_live_<24 characters>
```
**https://octopus.energy/help-and-faqs/articles/how-do-i-access-the-octopus-api/**


Update the API key variable on **line 38** of the script.

Next, locate your **Octopus account number** and replace:

```
<account_number>
```

on **line 39**.

---

## ▶️ 2. First Run of the Script

After completing the steps above, you can run the script.  
At this stage, **only option 2** will work.

Selecting **option 2** will produce output similar to:

```
sample_octupus_json.txt
```

This file contains the meter and identifier values you need for the next step.

---

## 🔧 3. Update Meter & Identifier Values

From the output, locate the following values and update the corresponding lines in the script:

| Value Needed | Replace Placeholder | Script Line |
|--------------|---------------------|-------------|
| Electric serial number | `<electric serial id>` | Line 22 |
| Gas serial number | `<gas serial id>` | Line 23 |
| Electric MPAN ID | `<electric mpan id>` | Line 17 |
| Gas MPRN ID | `<gas mprn id>` | Line 18 |

Once these values are updated, the script is fully configured.

---

## ⚡ 4. Retrieve Consumption Data

You can now run the script to retrieve consumption data:

- **Option 0** → Electric consumption  
- **Option 1** → Gas consumption  

---

## 💾 5. (Optional) Save Output to a File

If you want to save the results to a file, un-comment the following lines and choose a valid file path:

```python
# df.to_csv(f'<filename_{url_number}.txt', index=False)  # Convert DataFrame to CSV (line 61)

# with open('<filename>.txt', 'w') as file:  # line 63
#     file.write(str(file_output_json))       # line 64
```

---
