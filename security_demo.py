from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Customer Management System</h1>
    <h2>INTERNAL SYSTEM - CONFIDENTIAL</h2>
    <hr>
    <p><b>Name:</b> Budi Santoso</p>
    <p><b>Email:</b> budi@example.com</p>
    <p><b>Balance:</b> Rp25,000,000</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
