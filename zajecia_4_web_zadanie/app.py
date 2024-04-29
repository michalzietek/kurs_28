from flask import Flask, render_template, request
from file_handler import FileHandler

app = Flask(__name__)

# file_handler = FileHandler("historia.json", "ksiegozbior_i_saldo.json")
#
# saldo_dane, ksiegozbior_dane = file_handler.odczyt_danych_z_pliku_z_ksiegozbiorem_i_saldem()
# historia = file_handler.odczyt_danych_z_pliku_z_historia()

@app.route("/", methods=["GET", "POST"])
def main_view():
    if request.method == "GET":
        return render_template("home_page.html", **{
            "ksiegozbior": ksiegozbior_dane,
            "saldo": saldo_dane
        })
    else:
        try:
            request_type = request.form.get("request_type")
            if request_type == "sales_form":
                handle_sales_form(request.form)
            else:
                amount_to_substract = float(request.form.get("amount")) * 10
                ksiegozbior_dane.append({
                    "tytul": request.form.get("title"),
                    "autor": request.form.get("author"),
                    "wydawnictwo": request.form.get("publisher"),
                    "gatunek": request.form.get("genre"),
                    "ilosc_sztuk": request.form.get("amount"),
                    "ilosc_dostepnych_sztuk": request.form.get("amount"),
                })
            file_handler.zapis_do_pliku_z_ksiegozbiorem_i_saldem(saldo_dane, ksiegozbior_dane)
            return render_template("home_page.html", **{
                "ksiegozbior": ksiegozbior_dane,
                "saldo": saldo_dane
            })
        except ValueError:
             print("Ilość musi być liczbą")

def handle_sales_form(form):
    #logika do sprzedaży książki
    pass


with app.app_context():
    file_handler = FileHandler("historia.json", "ksiegozbior_i_saldo.json")

    saldo_dane, ksiegozbior_dane = file_handler.odczyt_danych_z_pliku_z_ksiegozbiorem_i_saldem()
    historia = file_handler.odczyt_danych_z_pliku_z_historia()

@app.route("/history")
def history():
    return render_template("history.html")

if __name__ == "__main__":
    app.run(debug=True)