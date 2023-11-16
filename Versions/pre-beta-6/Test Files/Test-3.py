import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebEngineCore import QWebEngineSettings


class BrowserPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createWindow(self, windowType):
        # Open new windows in the same browser instance
        if windowType == QWebEnginePage.WebBrowserTab:
            new_page = BrowserPage(self)
            new_page.urlChanged.connect(self.handle_url_change)
            return new_page
        return super().createWindow(windowType)

    def handle_url_change(self, url):
        # Update the address bar with the new URL
        main_window = self.window()
        main_window.address_bar.setText(url.toString())


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Custom Browser")
        self.resize(1024, 768)

        # Create address bar and search button
        self.address_bar = QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_url)
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.load_url)

        # Create web view
        self.web_view = QWebEngineView(self)
        self.web_view.setPage(BrowserPage(self.web_view))

        # Enable camera and microphone access
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.ScreenCaptureEnabled, True)
        settings.setAttribute(QWebEngineSettings.MediaAudioCaptureEnabled, True)
        settings.setAttribute(QWebEngineSettings.MediaVideoCaptureEnabled, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        # Set up the layout
        self.setCentralWidget(self.web_view)
        self.addToolBar(self.create_toolbar())

    def create_toolbar(self):
        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(self.address_bar)
        toolbar.addWidget(self.search_button)
        return toolbar

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.web_view.load(QUrl(url))


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the browser window
    browser_window = BrowserWindow()
    browser_window.show()

    # Run the application
    sys.exit(app.exec_())
