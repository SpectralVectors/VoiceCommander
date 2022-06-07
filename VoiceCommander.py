import bpy
import speech_recognition

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    
    audio = recognizer.listen(mic, timeout=1, phrase_time_limit=1)
    text = recognizer.recognize_google(audio)
    text = text.lower()
    print(f"{text}")

    if text == "delete object":
        bpy.ops.object.delete()
    if text == "add cube":
        bpy.ops.mesh.primitive_cube_add()
    if text == "add monkey":
        bpy.ops.mesh.primitive_monkey_add()
    if text == "shade smooth":
        bpy.ops.object.shade_smooth()
    if text == "subdivide":
        bpy.ops.object.modifier_add(type='SUBSURF')
    if text == "edit mode":
        bpy.ops.object.editmode_toggle()
    if text == "object mode":
        bpy.ops.object.editmode_toggle()
    if text == "select all":
        bpy.ops.object.select_all(action='SELECT')
    if text == "deselect":
        bpy.ops.object.select_all(action='DESELECT')
