import sys
import random
import math
import os

from PySide6.QtGui import (
    QPixmap,
    QFontDatabase,
    QColor,
    QImage,
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
)

from PySide6.QtCore import (
    Qt,
    QPoint,
    QTimer,
    QEasingCurve,
    QVariantAnimation,
)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ==========================================
# Colour Presets
# ==========================================

COLOUR_PRESETS = {

    "1": {
        "#8FD77D": "#8FD77D", # Body
        "#FFE4C1": "#FFE4C1", # Tummy
        "#FF673C": "#FF673C", # Spikes
        "#FFE789": "#FFE789", # Toes
    },

    "2": {
        "#8FD77D": "#DB4A4A", # Body
        "#FFE4C1": "#3F70C4", # Tummy
        "#FF673C": "#A8EA78", # Spikes
        "#FFE789": "#EC9C70", # Toes
    },

    "3": {
        "#8FD77D": "#7D7ED7", # Body
        "#FFE4C1": "#7B58C4", # Tummy
        "#FF673C": "#FFDF6D", # Spikes
        "#FFE789": "#DCA3ED", # Toes
    },

    "4": {
        "#8FD77D": "#F0C736", # Body
        "#FFE4C1": "#C44B4B", # Tummy
        "#FF673C": "#84C6EF", # Spikes
        "#FFE789": "#FDF95C", # Toes
    },

    "5": {
        "#8FD77D": "#D060A8", # Body
        "#FFE4C1": "#D7D7D7", # Tummy
        "#FF673C": "#208080", # Spikes
        "#FFE789": "#E783C2", # Toes
    },

    "6": {
        "#8FD77D": "#D00020", # Body
        "#FFE4C1": "#515151", # Tummy
        "#FF673C": "#060660", # Spikes
        "#FFE789": "#FBA900", # Toes
    },

    "7": {
        "#8FD77D": "#F86020", # Body
        "#FFE4C1": "#FFC874", # Tummy 
        "#FF673C": "#208040", # Spikes
        "#FFE789": "#FF9A72", # Toes
    },
        
    "8": {
        "#8FD77D": "#6020A8", # Body
        "#FFE4C1": "#330232", # Tummy
        "#FF673C": "#F80040", # Spikes
        "#FFE789": "#9456DD", # Toes
    },
    
    "9": {
        "#8FD77D": "#F8A800", # Body
        "#FFE4C1": "#74B2B4", # Tummy
        "#FF673C": "#A84060", # Spikes
        "#FFE789": "#FFD372", # Toes
    },
    
    "10": {
        "#8FD77D": "#20A860", # Body
        "#FFE4C1": "#D6D964", # Tummy
        "#FF673C": "#D0A820", # Spikes
        "#FFE789": "#65E39F", # Toes
    },
    
    "11": {
        "#8FD77D": "#60D0A8", # Body
        "#FFE4C1": "#D7D7D7", # Tummy
        "#FF673C": "#206060", # Spikes
        "#FFE789": "#A2F3D7", # Toes
    },
    
    "12": {
        "#8FD77D": "#408080", # Body
        "#FFE4C1": "#A7C2C3", # Tummy
        "#FF673C": "#F82020", # Spikes
        "#FFE789": "#9CC9CA", # Toes
    },
    
    "13": {
        "#8FD77D": "#20A840", # Body
        "#FFE4C1": "#ADE0BD", # Tummy
        "#FF673C": "#F80000", # Spikes
        "#FFE789": "#A8F8A8", # Toes
    },
    
    "14": {
        "#8FD77D": "#80D020", # Body
        "#FFE4C1": "#A1B679", # Tummy
        "#FF673C": "#D04000", # Spikes
        "#FFE789": "#C2F881", # Toes
    },
    
    "15": {
        "#8FD77D": "#A82080", # Body
        "#FFE4C1": "#FDFF8E", # Tummy
        "#FF673C": "#60D060", # Spikes
        "#FFE789": "#7E2B66", # Toes
    },

    "16": {
        "#8FD77D": "#20A8D0", # Body
        "#FFE4C1": "#D7D980", # Tummy
        "#FF673C": "#F8A800", # Spikes
        "#FFE789": "#72D7F4", # Toes
    },
    
    "17": {
        "#8FD77D": "#DCD0FE", # Body
        "#FFE4C1": "#F5F5F5", # Tummy
        "#FF673C": "#4A1DC4", # Spikes
        "#FFE789": "#BDA5FF", # Toes
    },
    
    "18": {
        "#8FD77D": "#6E8EFF", # Body
        "#FFE4C1": "#D7D7D7", # Tummy
        "#FF673C": "#FEFFAF", # Spikes
        "#FFE789": "#9CDAFF", # Toes
    },
    
    "19": {
        "#8FD77D": "#779F63", # Body
        "#FFE4C1": "#E8F2CD", # Tummy
        "#FF673C": "#FFB100", # Spikes
        "#FFE789": "#ABCF99", # Toes
    },
    
    "20": {
        "#8FD77D": "#28C020", # Body
        "#FFE4C1": "#EE9A60", # Tummy
        "#FF673C": "#FF9C42", # Spikes
        "#FFE789": "#63ECB4", # Toes
    },
    
    "21": {
        "#8FD77D": "#346856", # Body
        "#FFE4C1": "#92BC77", # Tummy
        "#FF673C": "#081820", # Spikes
        "#FFE789": "#88C070", # Toes
    },
    
    "22": {
        "#8FD77D": "#84B468", # Body
        "#FFE4C1": "#B8B840", # Tummy
        "#FF673C": "#D0805C", # Spikes
        "#FFE789": "#C8FCA4", # Toes
    },
    
    "23": {
        "#8FD77D": "#BE8542", # Body
        "#FFE4C1": "#F5D69D", # Tummy
        "#FF673C": "#FF5FBE", # Spikes
        "#FFE789": "#E8B06F", # Toes
    },
    
    "24": {
        "#8FD77D": "#DD8A79", # Body
        "#FFE4C1": "#FFDCAC", # Tummy
        "#FF673C": "#5BBDF5", # Spikes
        "#FFE789": "#F27777", # Toes
    },
    
    "25": {
        "#8FD77D": "#7D7ED7", # Body
        "#FFE4C1": "#FFDCAC", # Tummy
        "#FF673C": "#FFD77A", # Spikes
        "#FFE789": "#87BEDE", # Toes
    },
    
    "26": {
        "#8FD77D": "#DBC260", # Body
        "#FFE4C1": "#FFDCAC", # Tummy
        "#FF673C": "#97D848", # Spikes
        "#FFE789": "#EDF086", # Toes
    },
    
    "27": {
        "#8FD77D": "#F5EAE8", # Body
        "#FFE4C1": "#2170AB", # Tummy
        "#FF673C": "#7A6546", # Spikes
        "#FFE789": "#FFFFFF", # Toes
    },
    
    "28": {
        "#8FD77D": "#0058D8", # Body
        "#FFE4C1": "#FFDF70", # Tummy
        "#FF673C": "#FC4383", # Spikes
        "#FFE789": "#54ECFC", # Toes
    },

    "29": {
        "#8FD77D": "#CB2113", # Body
        "#FFE4C1": "#D09C43", # Tummy
        "#FF673C": "#5D1810", # Spikes
        "#FFE789": "#E65C11", # Toes
    },
    
    "30": {
        "#8FD77D": "#F2B740", # Body
        "#FFE4C1": "#FFF7E7", # Tummy
        "#FF673C": "#E091EA", # Spikes
        "#FFE789": "#FFFBB2", # Toes
    },
    
    "31": {
        "#8FD77D": "#83B87E", # Body
        "#FFE4C1": "#F6E274", # Tummy
        "#FF673C": "#FFE75E", # Spikes
        "#FFE789": "#B6E498", # Toes
    },
    
    "32": {
        "#8FD77D": "#525252", # Body
        "#FFE4C1": "#F05D00", # Tummy
        "#FF673C": "#FE7800", # Spikes
        "#FFE789": "#8C8C8C", # Toes
    },
    
    "33": {
        "#8FD77D": "#EBF3F5", # Body
        "#FFE4C1": "#99AEEF", # Tummy
        "#FF673C": "#0074F2", # Spikes
        "#FFE789": "#FFFFFF", # Toes
    },
    
    "34": {
        "#8FD77D": "#2C2E31", # Body
        "#FFE4C1": "#FFDCAC", # Tummy
        "#FF673C": "#F21100", # Spikes
        "#FFE789": "#616568", # Toes
    },
    
    "35": {
        "#8FD77D": "#1C1C1C", # Body
        "#FFE4C1": "#D8D8D8", # Tummy
        "#FF673C": "#F9B746", # Spikes
        "#FFE789": "#6B6B6B", # Toes
    },
    
    "36": {
        "#8FD77D": "#EAEAEA", # Body
        "#FFE4C1": "#595959", # Tummy
        "#FF673C": "#F9B746", # Spikes
        "#FFE789": "#FFFFFF", # Toes
    },
    
    "37": {
        "#8FD77D": "#191A17", # Body
        "#FFE4C1": "#D4F0AF", # Tummy
        "#FF673C": "#AAFF38", # Spikes
        "#FFE789": "#4A553B", # Toes
    },
    
    "38": {
        "#8FD77D": "#DBDBDB", # Body
        "#FFE4C1": "#95DDEF", # Tummy
        "#FF673C": "#00FAFF", # Spikes
        "#FFE789": "#CCF0FB", # Toes
    },
    
    "39": {
        "#8FD77D": "#FF6C68", # Body
        "#FFE4C1": "#FFE5A8", # Tummy
        "#FF673C": "#FFE000", # Spikes
        "#FFE789": "#FFA631", # Toes
    },
    
    "40": {
        "#8FD77D": "#FF4590", # Body
        "#FFE4C1": "#FF8686", # Tummy
        "#FF673C": "#F5EAF0", # Spikes
        "#FFE789": "#FFC4DB", # Toes
    },
    
    "41": {
        "#8FD77D": "#875636", # Body
        "#FFE4C1": "#FFF0E7", # Tummy
        "#FF673C": "#437BBB", # Spikes
        "#FFE789": "#562E15", # Toes
    },
    
    "42": {
        "#8FD77D": "#6C2000", # Body
        "#FFE4C1": "#C0A69B", # Tummy
        "#FF673C": "#98CA41", # Spikes
        "#FFE789": "#AB4E26", # Toes
    },
    
    "43": {
        "#8FD77D": "#E38939", # Body
        "#FFE4C1": "#EDEDED", # Tummy
        "#FF673C": "#695D52", # Spikes
        "#FFE789": "#AE5200", # Toes
    },
    
    "44": {
        "#8FD77D": "#7D1815", # Body
        "#FFE4C1": "#817E7C", # Tummy
        "#FF673C": "#292420", # Spikes
        "#FFE789": "#350100", # Toes
    },
    
    "45": {
        "#8FD77D": "#FFBB31", # Body
        "#FFE4C1": "#E8E8E8", # Tummy
        "#FF673C": "#DE0000", # Spikes
        "#FFE789": "#FFD98C", # Toes
    },
    
    "46": {
        "#8FD77D": "#1F2F28", # Body
        "#FFE4C1": "#FFD465", # Tummy
        "#FF673C": "#FF3E00", # Spikes
        "#FFE789": "#466B5A", # Toes
    },
    
    "47": {
        "#8FD77D": "#D3F8FF", # Body
        "#FFE4C1": "#FFDCAC", # Tummy
        "#FF673C": "#FFD800", # Spikes
        "#FFE789": "#F7FDFF", # Toes
    },
    
    "48": {
        "#8FD77D": "#D52C00", # Body
        "#FFE4C1": "#A20262", # Tummy
        "#FF673C": "#F5EFEF", # Spikes
        "#FFE789": "#FF9A56", # Toes
    },
    
    "49": {
        "#8FD77D": "#D60270", # Body
        "#FFE4C1": "#0038A8", # Tummy
        "#FF673C": "#9B4F96", # Spikes
        "#FFE789": "#900049", # Toes
    },
    
    "50": {
        "#8FD77D": "#5BCEFA", # Body
        "#FFE4C1": "#F5A9B8", # Tummy
        "#FF673C": "#EFF2F5", # Spikes
        "#FFE789": "#B8EBFF", # Toes
    },
    
    "51": {
        "#8FD77D": "#FE218B", # Body
        "#FFE4C1": "#76D0FF", # Tummy
        "#FF673C": "#FED700", # Spikes
        "#FFE789": "#FFA4CF", # Toes
    },
    
    "52": {
        "#8FD77D": "#7E007E", # Body
        "#FFE4C1": "#373737", # Tummy
        "#FF673C": "#B5B9BF", # Spikes
        "#FFE789": "#B33FB1", # Toes
    },
    
    "53": {
        "#8FD77D": "#9C3BBC", # Body
        "#FFE4C1": "#FFEF63", # Tummy
        "#FF673C": "#211C1B", # Spikes
        "#FFE789": "#D8ADE7", # Toes
    },
    
    "54": {
        "#8FD77D": "#FF6460", # Body
        "#FFE4C1": "#A8FFD6", # Tummy
        "#FF673C": "#8A5549", # Spikes
        "#FFE789": "#FFED99", # Toes
    },
    
    "55": {
        "#8FD77D": "#E40303", # Body
        "#FFE4C1": "#88FF30", # Tummy
        "#FF673C": "#EBCDFF", # Spikes
        "#FFE789": "#F2FF3E", # Toes
    },
    
    "56": {
        "#8FD77D": "#EB5624", # Body
        "#FFE4C1": "#FDF2E3", # Tummy
        "#FF673C": "#2C140C", # Spikes
        "#FFE789": "#C0431A", # Toes
    },
    
    "57": {
        "#8FD77D": "#B1D283", # Body
        "#FFE4C1": "#F3F3F3", # Tummy
        "#FF673C": "#111111", # Spikes
        "#FFE789": "#5AA24E", # Toes
    },
    
    "58": {
        "#8FD77D": "#004DCF", # Body
        "#FFE4C1": "#FFDCAC", # Tummy
        "#FF673C": "#C51E15", # Spikes
        "#FFE789": "#276CE5", # Toes
    },
    
    "59": {
        "#8FD77D": "#936C54", # Body
        "#FFE4C1": "#A8A8A8", # Tummy
        "#FF673C": "#8B8778", # Spikes
        "#FFE789": "#B8AC8B", # Toes
    },
    
    "60": {
        "#8FD77D": "#6A7378", # Body
        "#FFE4C1": "#A6B498", # Tummy
        "#FF673C": "#85C293", # Spikes
        "#FFE789": "#88A095", # Toes
    },
    
    "61": {
        "#8FD77D": "#9F67CD", # Body
        "#FFE4C1": "#ABD2D1", # Tummy
        "#FF673C": "#4B80B0", # Spikes
        "#FFE789": "#76489D", # Toes
    },
    
    "62": {
        "#8FD77D": "#81FCFF", # Body
        "#FFE4C1": "#A4BFDA", # Tummy
        "#FF673C": "#E8FFFE", # Spikes
        "#FFE789": "#D8FEFF", # Toes
    },
    
    "63": {
        "#8FD77D": "#4069C6", # Body
        "#FFE4C1": "#F2CA8D", # Tummy
        "#FF673C": "#F3AA3B", # Spikes
        "#FFE789": "#43598B", # Toes
    },
    
    "64": {
        "#8FD77D": "#884533", # Body
        "#FFE4C1": "#B85E54", # Tummy
        "#FF673C": "#FF0900", # Spikes
        "#FFE789": "#371C16", # Toes
    },
    
    "65": {
        "#8FD77D": "#6E36AA", # Body
        "#FFE4C1": "#C3B2CA", # Tummy
        "#FF673C": "#9DC048", # Spikes
        "#FFE789": "#8C56C5", # Toes
    },
    
    "66": {
        "#8FD77D": "#73279D", # Body
        "#FFE4C1": "#FFB430", # Tummy
        "#FF673C": "#1C1C1C", # Spikes
        "#FFE789": "#461562", # Toes
    },
    
    "67": {
        "#8FD77D": "#1D7A67", # Body
        "#FFE4C1": "#B7CAF2", # Tummy
        "#FF673C": "#F1EFFC", # Spikes
        "#FFE789": "#6A9ED1", # Toes
    },
    
    "68": {
        "#8FD77D": "#139E7F", # Body
        "#FFE4C1": "#37139E", # Tummy
        "#FF673C": "#E9F6FF", # Spikes
        "#FFE789": "#99E8C2", # Toes
    },
    
    "69": {
        "#8FD77D": "#A73725", # Body
        "#FFE4C1": "#3B3632", # Tummy
        "#FF673C": "#D5E3E8", # Spikes
        "#FFE789": "#CB351D", # Toes
    },
    
    "70": {
        "#8FD77D": "#A840A8", # Body
        "#FFE4C1": "#F8840A", # Tummy
        "#FF673C": "#400020", # Spikes
        "#FFE789": "#D341D6", # Toes
    },
    
    "71": { # This is 21 Inverted :3
        "#8FD77D": "#CB97A9", # Body
        "#FFE4C1": "#6D4388", # Tummy
        "#FF673C": "#F7E7DF", # Spikes
        "#FFE789": "#773F8F", # Toes
    },

}

def recolour_pixmap(pixmap, colour_map):

    image = pixmap.toImage()

    for y in range(image.height()):
        for x in range(image.width()):

            pixel = image.pixelColor(x, y)

            current = pixel.name().upper()

            if current in colour_map:

                image.setPixelColor(
                    x,
                    y,
                    QColor(
                        colour_map[current]
                    )
                )

    return QPixmap.fromImage(image)

# ==========================================
# Speech Bubble
# ==========================================

class SpeechBubble(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
            | Qt.WindowDoesNotAcceptFocus
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        font_id = QFontDatabase.addApplicationFont(
            resource_path("Fonts/PixelOperator.ttf")
        )

        if font_id != -1:
            font_family = (
                QFontDatabase.applicationFontFamilies(
                    font_id
                )[0]
            )
        else:
            font_family = "Arial"

        self.outer_label = QLabel(self)

        self.outer_label.setStyleSheet("""
            QLabel {
                background-color: white;
                border: none;
            }
        """)

        self.label = QLabel(self)

        self.label.setStyleSheet(f"""
            QLabel {{
                background-color: #ffedd6;
                color: black;

                border: 1px solid black;
                padding: 6px;

                font-family: "{font_family}";
                font-size: 16px;
            }}
        """)

        self.hide()

    def set_message(self, text):

        self.label.setText(text)
        self.label.adjustSize()

        outline = 2

        self.outer_label.resize(
            self.label.width() + outline * 2,
            self.label.height() + outline * 2
        )

        self.label.move(
            outline,
            outline
        )

        self.resize(
            self.outer_label.width(),
            self.outer_label.height()
        )


# ==========================================
# Pico
# ==========================================

class Pico(QWidget):

    def __init__(self):
        super().__init__()

        # ----------------------
        # State
        # ----------------------

        self.is_talking = False
        self.is_crying = False
        self.playing_animation = False

        # ----------------------
        # Window
        # ----------------------

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
            | Qt.WindowDoesNotAcceptFocus
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )

        self.resize(64, 64)

        # ----------------------
        # Sprite Display
        # ----------------------

        self.label = QLabel(self)
        self.label.resize(64, 64)

        self.setCursor(Qt.OpenHandCursor)

        # Random colour selection

        self.colour_name = random.choice(
            list(COLOUR_PRESETS.keys())
        )

        print(
            f"Pico: {self.colour_name}"
        )

        colour_map = COLOUR_PRESETS[
            self.colour_name
        ]

        # Load base sprites

        base_idle = QPixmap(
            resource_path("Assets/MelonIdle.png")
        )

        base_hop = QPixmap(
            resource_path("Assets/MelonTipToe.png")
)

        base_happy = QPixmap(
            resource_path("Assets/MelonHappy.png")
        )

        base_cry = QPixmap(
            resource_path("Assets/MelonCry.png")
        )
        
        base_dizzy = QPixmap(
            resource_path("Assets/MelonDizzy.png")
        )
        
        base_speak = QPixmap(
            resource_path("Assets/MelonSpeak.png")
        )

        # Recolour sprites

        self.melon_idle_sprite = recolour_pixmap(
            base_idle,
            colour_map
        )

        self.melon_hop_sprite = recolour_pixmap(
            base_hop,
            colour_map
        )

        self.melon_happy_sprite = recolour_pixmap(
            base_happy,
            colour_map
        )

        self.melon_cry_sprite = recolour_pixmap(
            base_cry,
            colour_map
        )
        
        self.melon_dizzy_sprite = recolour_pixmap(
            base_dizzy,
            colour_map
        )
        
        self.melon_speak_sprite = recolour_pixmap(
            base_speak,
            colour_map
        )

        self.label.setPixmap(
            self.melon_idle_sprite
        )

        # ----------------------
        # Animation Registry
        # ----------------------

        self.animations = [

            {
                "name": "hop",
                "sprite": self.melon_hop_sprite,
                "duration": 1000,
                "weight": 500
            },
            
            {
                "name": "happy",
                "sprite": self.melon_happy_sprite,
                "duration": 1000,
                "weight": 500
            },


            {
                "name": "dizzy",
                "sprite": self.melon_dizzy_sprite,
                "duration": 1200,
                "weight": 100
            },
            
            {
                "name": "speak",
                "sprite": self.melon_speak_sprite,
                "duration": 5000,
                "weight": 10
            },

        ]

        # ----------------------
        # Dialogue
        # ----------------------

        self.random_messages = [
            "Drink some water!",
            "Stretch!",
            "Stretch time?",
            "I need a drink!",
            "Yaya",
            "Keep going!",
            "How's it going?",
            "Don't forget to stretch!",
            "You're doing great!",
            "Need a snack?",
            "Are we there yet?",
            "I believe in you!",
            "Hydration check!",
            "You got this!",
            "Don't forget breaks!",
            ":D",
            ":o",
            ":)",
            ";D",
            "<3",
        ]

        self.click_messages = [
            "Zzz...",
            "You can do this!",
            "I believe in you!",
            "Mmm snacks...",
            "Don't give up!",
            "Goooo Pico!!!",
            "Yaya!",
            "I'm sleepy... Zzz",
            "Need some help?",
            "You're doing great!",
        ]



        # ----------------------
        # Speech Bubble
        # ----------------------

        self.bubble = SpeechBubble()

        # ----------------------
        # Dragging
        # ----------------------

        self.drag_position = QPoint()

        # ----------------------
        # Rapid Click Counter
        # ----------------------

        self.click_count = 0

        self.click_timer = QTimer()

        self.click_timer.setSingleShot(True)

        self.click_timer.timeout.connect(
            self.reset_click_count
        )

        # ----------------------
        # Animation Timer
        # ----------------------

        self.animation_timer = QTimer()

        self.animation_timer.timeout.connect(
            self.check_animation
        )

        self.animation_timer.start(100)

        self.schedule_next_animation()

        # ----------------------
        # Message Timer
        # ----------------------

        self.message_timer = QTimer()

        self.message_timer.setSingleShot(True)

        self.message_timer.timeout.connect(
            self.random_message
        )

        self.message_timer.start(
            random.randint(
                600000,
                900000
            )
        )

    # ======================================
    # Dialogue
    # ======================================

    def speak(self, message):

        if self.is_crying:
            return

        self.is_talking = True

        self.label.setPixmap(
            self.melon_speak_sprite
        )

        self.bubble.set_message(message)

        self.update_bubble_position()

        self.bubble.show()

        QTimer.singleShot(
            5000,
            self.hide_speech
        )

    def hide_speech(self):

        self.bubble.hide()

        self.is_talking = False

        if not self.playing_animation:
            self.label.setPixmap(
                self.melon_idle_sprite
            )

    def random_message(self):

        self.speak(
            random.choice(
                self.random_messages
            )
        )

        self.message_timer.start(
            random.randint(
                600000,
                900000
            )
        )
        

    # ======================================
    # Bubble Position
    # ======================================

    def update_bubble_position(self):

        self.bubble.move(
            self.x()
            + self.width() // 2
            - self.bubble.width() // 2,
            self.y()
            - self.bubble.height()
            - 10
        )

    # ======================================
    # Animation System
    # ======================================

    def schedule_next_animation(self):

        self.next_animation_time = random.randint(
            10000,
            20000
        )

        self.elapsed_time = 0

    def check_animation(self):

        self.elapsed_time += 100

        if (
            not self.playing_animation
            and self.elapsed_time >= self.next_animation_time
        ):
            self.play_random_animation()

    def play_random_animation(self):

        if self.is_talking:
            return

        if self.is_crying:
            return

        animation = random.choices(
            self.animations,
            weights=[
                a["weight"]
                for a in self.animations
            ],
            k=1
        )[0]

        self.current_animation = animation

        self.playing_animation = True

        self.label.setPixmap(
            animation["sprite"]
        )

        QTimer.singleShot(
            animation["duration"],
            self.finish_animation
        )

    def finish_animation(self):

        self.playing_animation = False

        if self.is_crying:
            return

        if self.is_talking:
            self.label.setPixmap(
                self.melon_speak_sprite
            )
        else:
            self.label.setPixmap(
                self.melon_idle_sprite
            )

        self.schedule_next_animation()

    # ======================================
    # Cry Mode
    # ======================================

    def reset_click_count(self):

        self.click_count = 0

    def start_crying(self):

        self.is_crying = True

        self.click_count = 0

        self.bubble.set_message(
            "My head hurts..."
        )

        self.update_bubble_position()

        self.bubble.show()

        self.label.setPixmap(
            self.melon_cry_sprite
        )

        QTimer.singleShot(
            5000,
            self.stop_crying
        )

    def stop_crying(self):

        self.is_crying = False

        self.bubble.hide()

        self.label.setPixmap(
            self.melon_idle_sprite
        )

    # ======================================
    # Dragging
    # ======================================

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.drag_position = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() & Qt.LeftButton:

            self.move(
                event.globalPosition().toPoint()
                - self.drag_position
            )

            self.update_bubble_position()

            event.accept()

    # ======================================
    # Clicking
    # ======================================

    def mouseReleaseEvent(self, event):

        if event.button() != Qt.LeftButton:
            return

        if self.is_crying:
            return

        self.click_count += 1

        self.click_timer.start(
            2000
        )

        if self.click_count >= 5:
            self.start_crying()
            return

        self.speak(
            random.choice(
                self.click_messages
            )
        )

    # ======================================
    # Escape Exit
    # ======================================

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            QApplication.quit()


# ==========================================
# Launch
# ==========================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    pico = Pico()

    pico.show()

    QTimer.singleShot(
        1000,
        lambda: pico.speak(
            "Hi! I'm your little desktop Pico Buddy!"
        )
    )

    QTimer.singleShot(
        8000,
        lambda: pico.speak(
            "Drag 'n drop me to where I should sit."
        )
    )

    sys.exit(app.exec())