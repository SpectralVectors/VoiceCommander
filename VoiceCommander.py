import bpy, re
import speech_recognition

recognizer = speech_recognition.Recognizer()

commands = {
    "delete object":"bpy.ops.object.delete()",
    "delete objects":"bpy.ops.object.delete()",
    "add cube": "bpy.ops.mesh.primitive_cube_add()",
    "add monkey": "bpy.ops.mesh.primitive_monkey_add()",
    "shade smooth": "bpy.ops.object.shade_smooth()",
    "subdivide": "bpy.ops.object.modifier_add(type='SUBSURF')",
    "edit mode": "bpy.ops.object.editmode_toggle()",
    "object mode": "bpy.ops.object.editmode_toggle()",
    "select all": "bpy.ops.object.select_all(action='SELECT')",
    "deselect": "bpy.ops.object.select_all(action='DESELECT')",
}

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

