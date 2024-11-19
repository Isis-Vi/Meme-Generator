# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Asignación #2. Recepción del texto
        top_text = request.form.get("textTop")
        bottom_text = request.form.get("textBottom")
        # Assignment #3. Receiving the text's color
        color = request.form.get("color-selector")

        # Asignación #3. Recepción del posicionamiento del texto
        position = request.form.get("textTop_y")
        position2 = request.form.get("textBottom_y")

        return render_template('index.html', 
                            # Visualización de la imagen seleccionada
                            selected_image=selected_image, 

                            # Asignación #2. Visualización del texto
                            cambio_texto=top_text,

                            bottom_text=bottom_text, 

                            #  Asignación #3. Visualización del color
                            color=color,
                            
                            # Asignación #3. Visualización de la posición del texto
                            position=position,

                            position2=position2

                            )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
