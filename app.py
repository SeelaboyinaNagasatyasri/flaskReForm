from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        gender = request.form.get("gender")

        # Validate password match
        if password != confirm_password:
            return "Error: Passwords do not match!"

        # You can save the data in a database or process it further here.
        print(f"Registered User: {fullname}, {username}, {email}, {phone}, {gender}")

        return redirect(url_for("success"))

    return render_template("register.html")

@app.route("/success")
def success():
    return "Registration successful! 🎉"

if __name__ == "__main__":
    app.run(debug=True)
