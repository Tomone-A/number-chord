from flask import Flask, render_template, request

app = Flask(__name__)

# 数字をコード進行に変換する関数
def generate_chord_progression(input_number):

    chord_map = {
        '1': 'C',
        '2': 'Dm',
        '3': 'Em',
        '4': 'F',
        '5': 'G',
        '6': 'Am',
        '7': 'Bm(b5)',
        '8': 'C (High)',  
        '9': 'Cadd9',     
        '0': 'N.C.'       
    }
    
    result_progression = []
    
    for i in input_number:
        if i in chord_map:
            code_name = chord_map[i]
            result_progression.append(code_name)
            
    return result_progression

@app.route('/' , methods=['GET', 'POST'])
def index():
    chords = generate_chord_progression(input_number='')

    if request.method == 'POST':
        input_number = request.form['input_number']
        chords = generate_chord_progression(input_number)
    
    return render_template('index.html', chords=chords)


if __name__ == "__main__":
    app.run(debug=True, port=8000)