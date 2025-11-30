# Keep imports minimal — editing is done only by changing the code
from flask import Flask, render_template


app = Flask(__name__)


# You can modify this information about the dogs here
# Just change the text between the quotes to update the website
dogs = {
    'bella': {
        'name': 'Bella',
        'breed': 'Cavalier King Charles Spaniel',
        'age': '8 years old',
        'description': 'Bella loves to eat sleep and more!',
        'fun_fact': 'Bella can catch treats in the air sometimes',
        # Change this to the path of your image file for Bella
        'image_path': 'static/Bella.jpeg'
    },
    'jasper': {
        'name': 'Jasper',
        'breed': 'Cavalier King Charles Spaniel',
        'age': '3 years old',
        'description': 'Jasper likes to sunbathe eat pencils and more!',
        'fun_fact': 'Jasper knows that cookie means food!',
        # Change this to the path of your image file for Jasper
        'image_path': 'static/Jasper.jpeg'
    },
    'dexter': {
        'name': 'Dexter',
        'breed': 'Cavalier King Charles Spaniel',
        'age': 'a few months old',
        'description': 'Dexter loves running and licking people!',
        'fun_fact': 'Dexter loves to annoy Bella and Jasper!',
        # default placeholder image; you can upload a new one via the edit page
        'image_path': 'static/Dexter.jpeg'
    },
    'frankie': {
        'name': 'Frankie',
        'breed': 'Mini Dachshund',
        'age': '1000 years old also all knowing',
        'description': 'Frankie loves to attack people with kisses!',
        'fun_fact': 'Frankie can actually clean your lips by attacking you!',
        # Change this to the path of your image file for Frankie
        'image_path': 'static/Frankie.jpeg'
    },
    'lula': {
        'name': 'Lula',
        'breed': 'Labradoodle',
        'age': '7 years old',
        'description': 'Lula is a gentle giant and very chill',
        'fun_fact': 'Lula can sit when you give her a treat!',
        # Change this to the path of your image file for Lula
        'image_path': 'static/Lula.jpeg'
    }
}

@app.route('/')
def home():
    return render_template('index.html', dogs=dogs)

if __name__ == '__main__':
    # bind to 0.0.0.0 so external proxies/tunnels can connect
    app.run(host='0.0.0.0', port=5555, debug=True)