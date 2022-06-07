# VoiceCommander
Blender Python - Control Blender with your Voice

This can be considered an experiment at this point, it is not yet in addon form and cannot be installed.

Rather, copy and paste the setup script into Blender's Text Editor and run it. It will take a little time to install all the Python packages and dependencies.

The issue here is that SpeechRecognition depends on PyAudio, which depends on PortAudio, which must be built to be run, and PyAudio is not compatible with Python 3.10 that ships with Blender. To get around this we install pipwin, which will install a compatible version of PyAudio with a pre-built PortAudio binary, making the install process a little easier for Windows users.

Next, copy the VoiceCommander text into the Text Editor and run it.

This will allow you to issue a single voice command, you can see what is currently available in the code itself, but for quick reference, you can use the following commands:

- "Delete Object"
- "Add Cube"
- "Add Monkey"
- "Shade Smooth"
- "Subdivide"
- "Edit Mode"
- "Object Mode"
- "Select All"
- "Deselect"

The script is currently designed to stop listening after 1 second, you can change that value in the code, and it will likely be exposed to adjustment when the script morphs into an addon.
