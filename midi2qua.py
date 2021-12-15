# midi2qua v1.1 by kloi34
# Converts MIDI into a text file whose contents can be copied into a .qua file.
from mido import MidiFile
import math
import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def print_notes_to_file(key_mode, start_times_of_note, lanes_of_start_time, note_data_file):
  current_note_lane = 1
  for note in sorted(start_times_of_note):
    for start_time in start_times_of_note[note]:
      new_note_lane = ((current_note_lane - 1) % key_mode) + 1
      if start_time in lanes_of_start_time.keys():
        lanes_of_start_time[start_time].append(new_note_lane)
      else:
        lanes_of_start_time[start_time] = [new_note_lane]
      current_note_lane += 1
  for start_time in sorted(lanes_of_start_time.keys()):
    for lane in lanes_of_start_time[start_time]:
      print("- StartTime: " + str(start_time), file=note_data_file)
      print("  Lane: " + str(lane), file=note_data_file)
      print("  KeySounds: []", file=note_data_file)
  start_times_of_note.clear()
  lanes_of_start_time.clear()

def convert_midi():
  try:
    key_mode = output_key_mode.get()
    note_output_file_name = midi_file_name.get().split(".")[0] + "-" + str(key_mode) + "Key.txt"
    note_data_file = open(note_output_file_name, "w")
    max_chord_second_separation = 0.04

    current_time = 0
    seconds_since_first_note_in_chord = 0
    start_times_of_note = {}
    lanes_of_start_time = {}
    for msg in MidiFile(midi_file_path.get(), clip=True):
      if msg.is_meta and msg.type == 'end_of_track':
        print_notes_to_file(key_mode, start_times_of_note, lanes_of_start_time, note_data_file)
        note_data_file.close()
        return
      current_time += msg.time
      seconds_since_first_note_in_chord += msg.time
      if msg.type == 'note_on' and msg.velocity > 0:
        if seconds_since_first_note_in_chord >= max_chord_second_separation:  
          seconds_since_first_note_in_chord = 0
          print_notes_to_file(key_mode, start_times_of_note, lanes_of_start_time, note_data_file)
        note_start_time = math.floor(current_time * 1000)
        if msg.note in start_times_of_note.keys():
          start_times_of_note[msg.note].append(note_start_time)
        else:
          start_times_of_note[msg.note] = [note_start_time]
    note_data_file.close()
  except FileNotFoundError:
    messagebox.showerror('Error', 'File not found. Please choose a valid MIDI file.')

def select_midi_file():
  midi_file_path.set(filedialog.askopenfilename(
     title='Select a MIDI file to convert',
     initialdir='./',
     filetypes=(('MIDI files', '*.mid'),)
  ))
  midi_file_name.set(os.path.basename(midi_file_path.get()))

root = Tk()
root.title("midi2qua")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#maxMidiNoteVelocity = StringVar()
#maxMidiNoteVelocity_entry = ttk.Entry(mainframe, width=7, textvariable=maxMidiNoteVelocity)
#maxMidiNoteVelocity_entry.grid(column=3, row=2, sticky=(W, E))
#maxMidiNoteVelocity_entry.focus()
midi_file_name = StringVar()
midi_file_path = StringVar()
output_key_mode = IntVar(value=7)
ttk.Button(mainframe, text="Choose MIDI file", command=select_midi_file).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="MIDI File:").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, textvariable=midi_file_name).grid(column=3, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Output Keymode:").grid(column=1, row=2, sticky=E)
ttk.Radiobutton(mainframe, text="7K", variable=output_key_mode, value=7).grid(column=2, row=2, sticky=W)
ttk.Radiobutton(mainframe, text="4K", variable=output_key_mode, value=4).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Convert selected MIDI file to .txt", command=convert_midi).grid(column=1, row=3, columnspan = 3, sticky=W)
for child in mainframe.winfo_children(): 
  child.grid_configure(padx=5, pady=5)

root.mainloop()