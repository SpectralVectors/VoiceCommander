# VoiceCommander
Blender Python - Control Blender with your Voice

__Experimental__

It depends on a number of python packages that do not come pre-installed with Blender, SpeechRecognition depends on PyAudio, which depends on PortAudio, which must be built to be run, and PyAudio is not compatible with Python 3.10 that ships with Blender. 

To get around this we install pipwin, which will install a compatible version of PyAudio with a pre-built PortAudio binary, making the install process a little easier for Windows users.

It will take a little time to install all the Python packages and dependencies.

You can open the System Console to monitor the progress of the package downloads.

### YOU MUST RUN BLENDER AS ADMINISTRATOR TO BE ABLE TO REGISTER THE ADDON, OTHERWISE YOU WILL ONLY GET AN ERROR MESSAGE!

This will allow you to issue a single voice command, currently includes:

- "Delete Object"
- "Add Cube"
- "Add Monkey"
- "Shade Smooth"
- "Subdivide"
- "Edit Mode"
- "Object Mode"
- "Select All"
- "Deselect"
- "Undo"
- "Redo"
- "Render Image"
- "Render Animation"
- "Play"
- "Stop"
- "Go To Frame _"
- "Move X _"
- "Move Y _"
- "Move Z _"
- "Rotate X _"
- "Rotate Y _"
- "Rotate Z _"
- "Scale X _"
- "Scale Y _"
- "Scale Z _"

The script is currently designed to stop listening after 2 seconds, you can change that value in the code, but it is not yet exposed to user editing.
