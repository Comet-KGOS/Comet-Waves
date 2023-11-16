import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Simple Browser")
        self.resize(1024, 768)

        # Load a webpage
        self.load(QUrl("https://www.google.com"))

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the browser window
    browser = Browser()
    browser.show()

    # Run the application
    sys.exit(app.exec_())
