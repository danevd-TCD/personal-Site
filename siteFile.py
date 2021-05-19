from flask import Flask, render_template, send_file, url_for
import os

app = Flask(__name__, static_url_path='')

imgArray = None
def getImages():
        global imgArray
        imgArray = []
        for fileName in os.listdir(app.static_folder + '/gallery'):
                imgArray.append(os.path.join('static/gallery/', fileName))

@app.route('/')
def root():
        return render_template('index.html')

#endpoint for gallery images; send file if present, 404 if not
@app.route('/static/gallery/<image>')
def returnImage(image):
        return send_file(app.static_folder + '/gallery/' + image)

@app.route('/gallery')
def gallery():
        getImages()
        return render_template('gallery.html', imgList = imgArray)
        #return "<p>" + str(imgArray) + "</p>"

if __name__ == "__main__":
        app.run(debug=True)
