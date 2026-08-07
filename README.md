# desktop-pico

**RIGHT CLICK TO CLOSE THE APPLICATION**

<img width="850" height="200" alt="PicoBanner" src="https://github.com/user-attachments/assets/6afbbe72-f474-4e1d-addf-7647200a1093" />

Hey, Static here! :D

Still learning how to use this github thingy, so DM me at **@xavinat0rmax** on Discord for any advice or issues! Follow the guide below, and you will become the owner of your very own pet Pico Dragon!!!

## Download

If you want download it through:

1. Navigate to releases
2. Download 'Desktop_Pico.exe'
3. Double click to run

That's it! No PyInstaller required. (The .exe is also in Pico-Chat)

## PyInstaller

If you would rather build Pico yourself:

1. Download the Desktop_Pico .zip folder.
2. Extract the files
3. Double click the python file to make sure it runs (If you have python, alternatively, the program can be used like this)
4. In the Desktop_Pico folder type cmd into the address bar
5. Paste this: _python -m pip install pyinstaller_
6. Paste this: _python -m pip install PySide6_
7. Wait until it's done, and then paste this: _python -m PyInstaller --onefile --windowed --icon=Melon.ico --add-data "Assets;Assets" --add-data "Fonts;Fonts" Pico_Python.py_
8. Wait until that's done (May take a while) and then open _dist_ folder
9. Your .exe file should be in there! (It is now safe to remove it from the _dist_ folder and rename it!)

## Customisation Notes

Note 1: If you want, the animation images are attached in the .zip file. Using a pixel art software, you can change the Pico's colour and use a PNG - ICO converter to make a custom app icon, by replacing the --icon=Melon.ico with your own .ico file.

Note 2: You can go into the source code and add your very own dialogue, or add and remove colour variants. For dialogue, I recommend asking a friend to do that, so you don't know everything Pico is going to say.
