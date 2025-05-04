# 🎓 Student Result Fetcher & Exporter

A Flask-based web application that allows users to:

* Enter a **BASE\_URL**
* Specify a **range of registration numbers**
* **Scrape student results**
* **Sort** results by Registration No., CGPA, or Last Semester SGPA
* **Export** results in TXT, CSV, XLSX, or PDF formats (PDF exports in landscape mode with proper formatting)

---

## 🚀 Features

✅ Input `BASE_URL` and registration number range
✅ View results sorted by:

* Registration Number
* CGPA (descending)
* Last Semester SGPA (descending)

✅ Download results in:

* `.txt`
* `.csv`
* `.xlsx`
* `.pdf` (landscape view, fixed column widths, includes student ranking)

✅ Sleek UI using Bootstrap
✅ Backend powered by Flask + Pandas
✅ HTML to PDF export using `xhtml2pdf`

---

## 📂 Project Structure

```
BEU_Result_Fetcher/
│
├── app.py                # Flask main app
├── scraper.py            # Scrapes student result data from given URL range
├── export_utils.py       # Handles exporting to PDF, Excel, TXT, and CSV
├── templates/
│   ├── index.html        # Main webpage UI
│
└── README.md             # This file
```

---

## 🛠️ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/aditya-kr86/beu-result-automation.git
cd beu-result-automation
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
Flask
pandas
xhtml2pdf
openpyxl
```

3. **Run the Flask app**

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

---

## 📌 Notes

* **PDF export** uses landscape mode for better readability.
* Column width for SGPA is reduced.
* A **Sl. No.** column is auto-inserted to reflect student rank based on selected sort order.
* For `.xlsx`, ensure you have the `openpyxl` engine installed.

---

## 📸 Screenshots

> *(You can add screenshots here later for UI and exports)*

---

## ✨ Future Improvements

* Authentication system
* Save previous fetches
* Graphical summary (Topper Chart, GPA Histograms, etc.)
* REST API for integration

---

## 🧑‍💻 Author

**Aditya Kumar**
*B.Tech CSE Student | Python Enthusiast*
📧 *[aditya_kumar_gupta@yahoo.com](mailto:aditya_kumar_gupta@yahoo.com)*

