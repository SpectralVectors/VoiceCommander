bl_info = {
    "name": "Voice Commander",
    "author": "Spectral Vectors",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "View 3D > Properties Panel",
    "description": "Control Blender with your voice",
    "warning": "Experimental",
    "doc_url": "https://github.com/SpectralVectors/VoiceCommander",
    "category": "Object",
}

import bpy, re, math
import speech_recognition

from .Commands import commands
from .Setup import initialsetup

def single_command():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        
        audio = recognizer.listen(mic, timeout=2, phrase_time_limit=2)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        
        letters = re.sub("\d+", '', text)
        value = re.sub("[A-Za-z]", "", text).strip()
        
        if value:
            command = commands[letters] + str(value)
        else:
            command = commands[text]
    try:
        exec(command)
    except SyntaxError:
        command = commands[letters] + str(value) + ")"
        exec(command)
        
        
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
        column.operator(SingleCommand.bl_idname, text='Command!')
        icon = 'TRIA_DOWN' if context.scene.commandlist_panel_open else 'TRIA_RIGHT'
        row = column.row()
        row.prop(context.scene, 'commandlist_panel_open', icon=icon, icon_only=True)
        row.label(text="Command List")
        
        shortlist = [
            "Delete Object",
            "Add Cube",
            "Add Monkey",
            "Shade Smooth",
            "Subdivide",
            "Edit Mode",
            "Object Mode",
            "Select All",
            "Deselect",
            "Undo",
            "Redo",
            "Render Image",
            "Render Animation",
            "Play",
            "Stop",
            "Go To Frame _",
            "Move X _",
            "Move Y _",
            "Move Z _",
            "Rotate X _",
            "Rotate Y _",
            "Rotate Z _",
            "Scale X _",
            "Scale Y _",
            "Scale Z _",
        ]
                        
        if context.scene.commandlist_panel_open:
            box = column.box()
            for item in shortlist:
                box.label(text=item)


classes = [
    SingleCommand,
    VoiceCommanderPanel,
]

def register():
    
    initialsetup()
    
    bpy.types.Scene.commandlist_panel_open = bpy.props.BoolProperty(
    default=False
    )
    
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__package__":
    register()