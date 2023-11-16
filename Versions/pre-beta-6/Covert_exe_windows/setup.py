from setuptools import setup
import sys
import os

# Find the main script file
main_script = '../Script/v_pre-beta_6.py'  # Replace with the name of your main script file

# Create shortcuts directory paths
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
start_menu_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')

# Setup script options
options = {
    'script': main_script,
    'icon_resources': [(1, '../../Icon/Icon.ico')],  # Replace with the path to your icon file
    'shortcuts': [
        ('DesktopShortcut', desktop_path, 'Your Program Name', 'Your Program Description'),
        ('StartMenuShortcut', start_menu_path, 'Your Program Name', 'Your Program Description')
    ]
}

# Create the setup configuration
setup(
    name='Comet Waves',
    version='pre-beta-6',
    description='A Browser for Comet Operating System [KG-OS], Developed by Krishna Goel',
    options={'py2exe': options},
    windows=[{'script': main_script}],
    zipfile=None,
)
