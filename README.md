# javafx-jython
Integration between JavaFX and Jython.

Fork of jythonfx (made by Jeremi Biernacki) in one file  
Made by Fernando Lima

# =========================
#    CHANGES
# =========================

- requirement changed: now require JAVA 8
- removed fix.py file and its code (unnecessary for the new requirement)
- some lines removed: mainly print commands
- imported classes renamed to be prefixed by JFX to make the code more readable:
  new name of imported classes is JFX{className}
- all classes are now together in just one file
- all components at FXML are now correctly imported

# =========================
#    REQUIREMENTS
# =========================

- JAVA 8 OR NEWER
- JYTHON 2.7 OR NEWER

# ========================
#    HOW TO USE
# =========================

Copy javafxjython.py to your project folder and import it for your code, using:

**import javafxjython**
