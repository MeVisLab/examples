# from mevis import *
import cv2
import OpenCVUtils

_interfaces = []
camera = None
face_cascade = cv2.CascadeClassifier("C:/tmp/haarcascade_frontalface_default.xml")


# Setup the interface for PythonImage module
def setupInterface():
    global _interfaces
    _interfaces = []
    interface = ctx.module("PythonImage").call("getInterface")
    _interfaces.append(interface)


# Grab image from camera and update
def grabImage():
    _, img = camera.read()
    updateImage(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow("img", img)


# Update image in interface
def updateImage(image):
    _interfaces[0].setImage(OpenCVUtils.convertImageToML(image), minMaxValues=[0, 255])


# Start capturing WebCam
def startCapture():
    global camera
    if not camera:
        camera = cv2.VideoCapture(0)
    ctx.callWithInterval(0.1, grabImage)


# Stop capturing WebCam
def stopCapture():
    ctx.removeTimers()


# Release camera in the end
def releaseCamera(_):
    global camera, _interfaces
    ctx.removeTimers()
    _interfaces = []
    if camera:
        camera.release()
        camera = None
    cv2.destroyAllWindows()
