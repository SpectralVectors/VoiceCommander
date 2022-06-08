bl_info = {
    "name": "Voice Commander",
    "author": "Spectral Vectors",
    "version": (0, 0, 3),
    "blender": (2, 80, 0),
    "location": "View 3D > Properties Panel",
    "description": "Control Blender with your voice",
    "warning": "Experimental",
    "doc_url": "https://github.com/SpectralVectors/VoiceCommander",
    "category": "Object",
}

import bpy, re
import speech_recognition

from .Commands import commands
from .Setup import initialsetup

def single_command():
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        
        audio = recognizer.listen(mic, timeout=1, phrase_time_limit=1)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        command = commands[text]
        print(f"{text}")

    exec(command)
        
        
# To remove all letters from a string, leaving only
# numbers and special characters
# value = re.sub("[A-Za-z]", "", text).strip()

# print(value)

class SingleCommand(bpy.types.Operator):
    """Issue a single voice command"""
    bl_idname = "object.single_command"
    bl_label = "Single Command"   

    def execute(self, context):
        single_command()
        return {'FINISHED'}

class VoiceCommanderPanel(bpy.types.Panel):
    bl_label = "Voice Commander"
    bl_category = "Voice Commander"
    bl_idname = "VIEW3D_PT_VoiceCommanderPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        layout = self.layout
        column = layout.column()
        box = column.box()
        box.label(text='Available Commands:')
        box.label(text='- Add Cube')
        box.label(text='- Add Monkey')
        box.label(text='- Delete Object')
        box.label(text='- Shade Smooth')
        box.label(text='- Subdivide')
        box.label(text='- Edit Mode')
        box.label(text='- Object Mode')
        box.label(text='- Select All')
        box.label(text='- Deselect')
        column.label(text='')
        column.operator(SingleCommand.bl_idname, text='Command!')


classes = [
    SingleCommand,
    VoiceCommanderPanel,
]

def register():
    initialsetup()
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__package__":
    register()