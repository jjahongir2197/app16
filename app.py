from flask import Flask, render_template, request, redirect

app = Flask(__name__)

bookings = []

@app.route("/", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        bookings.append(f"{name} - {date}")
        return redirect("/")

    return render_template("book.html", bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)
