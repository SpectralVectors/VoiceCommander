import bpy
import subprocess, sys

def initialsetup():
    string = bpy.app.version_string
    blenderversion = string.rstrip(string[-2:])

    packages = ["pipwin", "SpeechRecognition", "word2number"]

    subprocess.check_call([
        sys.executable, 
        "-m", "ensurepip"])

    subprocess.check_call([
        sys.executable, 
        "-m", "pip", "install", "--upgrade", "pip"])

    for package in packages:
        subprocess.check_call([
            sys.executable, 
            "-m", "pip", "install",
            f"--target=C:\\Program Files\\Blender Foundation\\Blender {blenderversion}\\{blenderversion}\\python\\lib", 
            package])

    subprocess.check_call([
        sys.executable, 
        "-m", "pipwin", "install", "pyaudio"])
