"""
Author: Rayhan Biju
Version: October 28, 2021
Description: File contains functionality to run the web app and contains necessary components to initialize
a Flask app.
"""

from website import create_app

app = create_app()
# Debug is set to false because this app will be pushed to production
if __name__ == '__main__':
    app.run(debug=True)
