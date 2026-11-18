from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    error = None

    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        notas_validas = all(10 <= n <= 70 for n in (nota1, nota2, nota3))
        asistencia_valida = 0 <= asistencia <= 100

        if not notas_validas or not asistencia_valida:
            error = "Las notas deben estar entre 10 y 70 y la asistencia entre 0 y 100."
        else:
            promedio = round((nota1 + nota2 + nota3) / 3, 1)
            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

    return render_template("ejercicio1.html", promedio=promedio, estado=estado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_mayor = None
    cantidad = None
    error = None

    if request.method == "POST":
        nombres = [
            request.form["nombre1"].strip(),
            request.form["nombre2"].strip(),
            request.form["nombre3"].strip(),
        ]

        nombres_en_minuscula = [n.lower() for n in nombres]

        if len(set(nombres_en_minuscula)) < 3:
            error = "Los 3 nombres deben ser diferentes."
        else:
            nombre_mayor = max(nombres, key=len)
            cantidad = len(nombre_mayor)

    return render_template("ejercicio2.html", nombre_mayor=nombre_mayor, cantidad=cantidad, error=error)


if __name__ == "__main__":
    app.run(debug=True)