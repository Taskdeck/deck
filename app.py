
from flask import Flask, render_template

app = Flask(__name__)

domains = [
    {"domain": "example.com", "company_accounts": ["Google", "AWS", "GitHub"]},
    {"domain": "testsite.org", "company_accounts": ["Azure", "Slack"]}
]

@app.route("/")
def index():
    return render_template("index.html", domains=domains)

@app.route("/domain/<name>")
def domain(name):
    for d in domains:
        if d["domain"] == name:
            return render_template("domain.html", domain=d)
    return "Not found", 404

if __name__ == "__main__":
    app.run(debug=True)
