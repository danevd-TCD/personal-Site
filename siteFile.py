from flask import Flask

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
        return "<h1> Flask dev test v1.0.2 </h1>"

if __name__ == "__main__":
        app.run()
