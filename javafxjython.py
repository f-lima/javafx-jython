#
# Fork of jythonfx (made by Jeremi Biernacki) in one file
# Made by Fernando Lima
#
# =========================
#    CHANGES
# =========================
#
# - requirement changed: now require JAVA 8
# - removed fix.py file and its code (unnecessary for the new requirement)
# - some lines removed: mainly print commands
# - imported classes renamed to be prefixed by JFX to make the code more readable:
#   new name of imported classes is JFX{className}
# - all classes are now together in just one file
# - all components at FXML are now correctly imported
#
# =========================
#    REQUIREMENTS
# =========================
#
# - JAVA 8 OR NEWER
# - JYTHON 2.7 OR NEWER
#
# ========================
#    HOW TO USE
# =========================
#
# Copy this file to your project folder and import it for your code, using:
#
# import javafxjython
#
#


# import java packages
from java.io import File
from javafx.application import Application as JFXApplication
from javafx.fxml import FXMLLoader as JFXFXMLLoader
from javafx.event import EventHandler as JFXEventHandler
from javafx.scene.image import (Image as JFXImage, ImageView as JFXImageView)

# import python packages
from collections import Iterable

class Application(JFXApplication):
   def __init__(self):
      # this override method self.launch using self.__launch__
      setattr(self, "launch", self.__launch__)

   def __launch__(self, app):
      JFXApplication.launch(app().getClass(), [])


class Image(JFXImageView):
   def __init__(self, path_to_img):
      f = File(path_to_img).toURI().toString()
      img = JFXImage(f)
      super(Image, self).__init__(img)


class EventHandler(JFXEventHandler):
   def __init__(self, method=None):
      super(EventHandler, self).__init__()

      if method != None:
         setattr(self, "handle", method)


# start: fully rewritten by Fernando Lima
class FXMLLoader(object):
   def __init__(self, fxmlfile):   # changed by Fernando Lima
      fxml = JFXFXMLLoader(File(fxmlfile).toURL())
      fxml.setController(self)

      self.body = fxml.load()
      self.getChildren().add(self.body)
      self.components = []
      self.components.append(self.body)
      self.getInnerComponents(self.body)
      self.setIds(self.components)

   # start: made by Fernando Lima
   def getInnerComponents(self, component):
      # print("component: " + str(component))
      if (hasattr(component, "columns")):   # component is a JavaFX TableView
         innerComponents = getattr(component, "columns", [])
         if isinstance(innerComponents, Iterable):
            for innerComponent in innerComponents:
               self.components.append(innerComponent)
               self.getInnerComponents(innerComponent)
         else:
            self.components.append(innerComponents)
            self.getInnerComponents(innerComponents)
      if (hasattr(component, "items")):   # component is a JavaFX Menu
         innerComponents = getattr(component, "items", [])
         if isinstance(innerComponents, Iterable):
            for innerComponent in innerComponents:
               self.components.append(innerComponent)
               self.getInnerComponents(innerComponent)
         else:
            self.components.append(innerComponents)
            self.getInnerComponents(innerComponents)
      elif (hasattr(component, "children")):   # component is a JavaFX Pane
         innerComponents = getattr(component, "children", [])
         if isinstance(innerComponents, Iterable):
            for innerComponent in innerComponents:
               self.components.append(innerComponent)
               self.getInnerComponents(innerComponent)
         else:
            self.components.append(innerComponents)
            self.getInnerComponents(innerComponents)
      elif (hasattr(component, "content")):  # component is a JavaFX Control
         innerComponents = getattr(component, "content", [])
         if isinstance(innerComponents, Iterable):
            for innerComponent in innerComponents:
               self.components.append(innerComponent)
               self.getInnerComponents(innerComponent)
         else:
            self.components.append(innerComponents)
            self.getInnerComponents(innerComponents)
      elif (hasattr(component, "tabs")):     # component is a JavaFX TabPane
         tabs = getattr(component, "tabs", [])
         if isinstance(tabs, Iterable):
            for tab in tabs:
               self.components.append(tab)
               self.getInnerComponents(tab)
         else:
            self.components.append(tabs)
            self.getInnerComponents(tabs)
      elif (hasattr(component, "columns")):     # component is a JavaFX TableView
         cols = getattr(component, "columns", [])
         if isinstance(cols, Iterable):
            for col in cols:
               self.components.append(col)
               self.getInnerComponents(col)
         else:
            self.components.append(cols)
            self.getInnerComponents(cols)

   def setIds(self, components):
      for component in components:
         componentId = getattr(component, "id", "")
         strId = str(componentId)
         if (not(componentId is None)) and (strId != ""):
            # print("JavaFX Id: " + strId)
            setattr(self, strId, component)
# end: completely rewritten by Fernando Lima
