from flask import Flask, render_template

app = Flask(__name__)  # Gunakan __name__

@app.route("/")
def home():
   print("Halaman utama diakses")
   return render_template("index.html")  # Menampilkan file index.html

if __name__ == "__main__":  # Gunakan __name__ dan "__main__"
    app.run(debug=True)