import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTabWidget, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Comet Waves")
        self.setWindowIcon(QIcon("Icon/Icon.png"))  # Set the custom icon
        self.resize(1024, 768)

        # Create tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabBarAutoHide(False)  # Auto-hide the tab bar when only one tab is present
        self.tab_widget.setTabsClosable(True)  # Allow closing tabs
        # noinspection PyUnresolvedReferences
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tab_widget)

        # Create initial tab
        self.create_new_tab()

        # Create address bar and search button
        self.address_bar = QLineEdit()
        # noinspection PyUnresolvedReferences
        self.address_bar.returnPressed.connect(self.load_url)
        self.search_button = QPushButton("Connect")
        # noinspection PyUnresolvedReferences
        self.search_button.clicked.connect(self.load_url)

        # Create new tab button
        self.new_tab_button = QPushButton("+ New Signal")
        # noinspection PyUnresolvedReferences
        self.new_tab_button.clicked.connect(self.create_new_tab)

        # Add address bar, search button, and new tab button to a toolbar
        toolbar = QToolBar("Tool-Bar")
        toolbar.setMovable(False)  # Make the toolbar non-movable
        self.addToolBar(toolbar)
        toolbar.addWidget(self.address_bar)
        toolbar.addWidget(self.search_button)
        toolbar.addWidget(self.new_tab_button)

    def create_new_tab(self):
        # Create a new tab with a web view
        web_view = QWebEngineView()
        # noinspection PyUnresolvedReferences
        web_view.loadStarted.connect(self.update_address_bar)
        # noinspection PyUnresolvedReferences
        web_view.loadProgress.connect(self.update_load_progress)
        # noinspection PyUnresolvedReferences
        web_view.loadFinished.connect(self.update_window_title)
        self.tab_widget.addTab(web_view, "New Signal")
        self.tab_widget.setCurrentWidget(web_view)

    def update_address_bar(self):
        # Update the address bar with the current page's URL
        current_web_view = self.tab_widget.currentWidget()
        if current_web_view:
            self.address_bar.setText(current_web_view.url().toString())

    def update_load_progress(self, progress):
        # Update the tab's title with the page load progress
        current_web_view = self.tab_widget.currentWidget()
        if current_web_view:
            tab_index = self.tab_widget.indexOf(current_web_view)
            self.tab_widget.setTabText(tab_index, f"Loading... {progress}%")

    def update_window_title(self):
        # Update the tab's title with the current page's title
        current_web_view = self.tab_widget.currentWidget()
        if current_web_view:
            tab_index = self.tab_widget.indexOf(current_web_view)
            self.tab_widget.setTabText(tab_index, current_web_view.title())

    def load_url(self):
        # Load the entered URL in the current tab
        current_web_view = self.tab_widget.currentWidget()
        if current_web_view:
            url = self.address_bar.text()
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url
            current_web_view.load(QUrl(url))

    def close_tab(self, index):
        # Close the requested tab
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)
        else:
            self.close()

    def keyPressEvent(self, event):
        # Handle Alt + C key press to close the current tab
        if event.key() == Qt.Key_C and event.modifiers() == Qt.AltModifier:
            self.close_tab(self.tab_widget.currentIndex())

        # Handle Alt + Enter key press to open a new tab
        elif event.key() == Qt.Key_Return and event.modifiers() == Qt.AltModifier:
            self.create_new_tab()

        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the browser window
    browser_window = BrowserWindow()
    browser_window.show()

    # Run the application
    sys.exit(app.exec_())
