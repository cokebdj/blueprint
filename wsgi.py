from ml_api.app import flask_app

if __name__ == "__main__":
    flask_app.run(port='8000',debug=True,host='0.0.0.0')