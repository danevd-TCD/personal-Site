from flask import Flask, render_template, send_file, url_for, jsonify
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

@app.route('/about')
def aboutMe():
        return render_template('about.html')

@app.route('/projects')
def projects():
        return render_template('projects.html')

@app.route('/gallery')
def gallery():
        getImages()
        return render_template('gallery.html', imgList = imgArray)
        #return "<p>" + str(imgArray) + "</p>"

#initial hardcoded API response for debug/test
status = {'isUp':'Yes','memUse':750,'cpuUse':'15%','upSince':1621768538}

#basic API endpoint
@app.route('/status/all', methods=['GET'])
def status_all():
        return(jsonify(status)) #jsonify isn't strictly necessary anymore


if __name__ == "__main__":
        app.run()
