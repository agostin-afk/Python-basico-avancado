import qdarktheme
from variables import *


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def setupTheme():
    qdarktheme.setup_theme(
        theme= 'dark',
        corner_shape= 'rounded',
        custom_colors= {
            '[dark]': {
                'primary': PRIMARY_COLOR
            },
            '[light]': {
                'primary': PRIMARY_COLOR
            }
        },
        additional_qss= qss
    )