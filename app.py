from flask import Flask, render_template, request, send_file
import os
import pandas as pd
from scraper import fetch_all_results, sort_by_current_cgpa, sort_by_latest_semester_grade
from export_utils import export_to_pdf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        base_url = request.form["base_url"].strip()
        start_reg = int(request.form["start_reg"])
        end_reg = int(request.form["end_reg"])
        view_mode = request.form["view_mode"]
        export_format = request.form["export_format"]

        # Fetch data
        results = fetch_all_results(base_url, start_reg, end_reg)
        df = pd.DataFrame(results)

        # Sort according to selected view mode
        if view_mode == "cgpa":
            df = sort_by_current_cgpa(df)
        elif view_mode == "semester":
            df = sort_by_latest_semester_grade(df)

        # Create results directory
        os.makedirs("results", exist_ok=True)
        filename = f"results.{export_format}"
        filepath = os.path.join("results", filename)

        # Export
        if export_format == "csv":
            df.to_csv(filepath, index=False)
        elif export_format == "xls":
            df.to_excel(filepath, index=False, engine='openpyxl')
        elif export_format == "txt":
            df.to_csv(filepath, sep="\t", index=False)
        elif export_format == "pdf":
            export_to_pdf(df, filepath)

        return send_file(filepath, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
