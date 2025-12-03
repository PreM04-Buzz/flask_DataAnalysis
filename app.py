from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

DB_NAME = "immigration.db"

def init_db():
    if not os.path.exists(DB_NAME):
        df = pd.read_csv("immigration.csv")
        df.columns = [
            "year",
            "immigrants",
            "refugee_arrivals",
            "apprehensions",
            "removals",
            "returns"
        ]
        num_cols = ["immigrants", "refugee_arrivals", "apprehensions", "removals", "returns"]
        for col in num_cols:
            df[col] = df[col].astype(str).str.replace(",", "").astype(int)
        df["year"] = df["year"].astype(int)
        conn = sqlite3.connect(DB_NAME)
        df.to_sql("immigration", conn, index=False, if_exists="replace")
        conn.close()

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM immigration ORDER BY year")
    rows = cur.fetchall()
    return render_template("index.html", rows=rows)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        year = request.form["year"]
        immigrants = request.form["immigrants"]
        refugee = request.form["refugee_arrivals"]
        appre = request.form["apprehensions"]
        removals = request.form["removals"]
        returns = request.form["returns"]
        conn = get_db()
        conn.execute("""
            INSERT INTO immigration(year, immigrants, refugee_arrivals, apprehensions, removals, returns)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (year, immigrants, refugee, appre, removals, returns))
        conn.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:year>", methods=["GET", "POST"])
def edit(year):
    conn = get_db()
    cur = conn.cursor()
    if request.method == "POST":
        immigrants = request.form["immigrants"]
        refugee = request.form["refugee_arrivals"]
        appre = request.form["apprehensions"]
        removals = request.form["removals"]
        returns = request.form["returns"]
        cur.execute("""
            UPDATE immigration
            SET immigrants=?, refugee_arrivals=?, apprehensions=?, removals=?, returns=?
            WHERE year=?
        """, (immigrants, refugee, appre, removals, returns, year))
        conn.commit()
        return redirect("/")
    cur.execute("SELECT * FROM immigration WHERE year=?", (year,))
    row = cur.fetchone()
    return render_template("edit.html", row=row)

@app.route("/delete/<int:year>")
def delete(year):
    conn = get_db()
    conn.execute("DELETE FROM immigration WHERE year=?", (year,))
    conn.commit()
    return redirect("/")

@app.route("/charts")
def charts():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT year, immigrants, refugee_arrivals, apprehensions FROM immigration ORDER BY year")
    rows = cur.fetchall()
    years = [row["year"] for row in rows]
    immigrants = [row["immigrants"] for row in rows]
    refugees = [row["refugee_arrivals"] for row in rows]
    apprehensions = [row["apprehensions"] for row in rows]
    return render_template("charts.html",
                           years=years,
                           immigrants=immigrants,
                           refugees=refugees,
                           apprehensions=apprehensions)

@app.route("/filter", methods=["GET", "POST"])
def filter_years():
    conn = get_db()
    cur = conn.cursor()
    if request.method == "POST":
        start = request.form["start"]
        end = request.form["end"]
        cur.execute("SELECT * FROM immigration WHERE year BETWEEN ? AND ? ORDER BY year", (start, end))
        rows = cur.fetchall()
        return render_template("filter.html", rows=rows, start=start, end=end)
    cur.execute("SELECT MIN(year) as min_year, MAX(year) as max_year FROM immigration")
    row = cur.fetchone()
    return render_template("filter.html", rows=None, start=row["min_year"], end=row["max_year"])

@app.route("/dashboard")
def dashboard():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM immigration ORDER BY year")
    rows = cur.fetchall()
    years = [row["year"] for row in rows]
    immigrants = [row["immigrants"] for row in rows]
    refugees = [row["refugee_arrivals"] for row in rows]
    apprehensions = [row["apprehensions"] for row in rows]
    removals = [row["removals"] for row in rows]
    returns_data = [row["returns"] for row in rows]
    return render_template("dashboard.html",
                           years=years,
                           immigrants=immigrants,
                           refugees=refugees,
                           apprehensions=apprehensions,
                           removals=removals,
                           returns=returns_data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

