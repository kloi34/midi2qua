# midi2qua v1.2 by kloi34
# Converts a MIDI file into a text file whose contents can be copied into a .qua file.
from mido import MidiFile
import math
import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def print_notes_to_file(key_mode, note_times, note_data_file):
  note_lanes = get_sorted_note_lanes(note_times, key_mode)
  for note_time in sorted(note_lanes.keys()):
    for note_lane in note_lanes[note_time]:
      print(f"- StartTime: {note_time}", file=note_data_file)
      print(f"  Lane: {note_lane}", file=note_data_file)
      print("  KeySounds: []", file=note_data_file)
  note_times.clear()

def convert_midi():
  file_path = midi_file_path.get() 
  if not os.path.isfile(file_path): 
    messagebox.showerror('Error', 'File not found. Please choose a valid MIDI file.')
    return
  key_mode = output_key_mode.get()
  output_file_name = f"{midi_file_name.get().split('.')[0]}-{key_mode}Key.txt"
  with open(output_file_name, "w") as note_data_file:
    max_chord_time_separation = 0.04
    current_time = 0 # seconds
    time_since_first_chord_note = 0 # seconds
    note_times = {}
    for msg in MidiFile(file_path, clip=True):
      if msg.is_meta and msg.type == 'end_of_track':
        print_notes_to_file(key_mode, note_times, note_data_file)
      current_time += msg.time
      time_since_first_chord_note += msg.time
      if msg.type == 'note_on' and msg.velocity > 0:
        if time_since_first_chord_note >= max_chord_time_separation:  
          time_since_first_chord_note = 0
          print_notes_to_file(key_mode , note_times, note_data_file)
        note_time = math.floor(current_time * 1000) # convert to milliseconds + round down
        if msg.note in note_times.keys():
          note_times[msg.note].append(note_time)
        else:
          note_times[msg.note] = [note_time]

def get_sorted_note_lanes(note_times, key_mode):
  lanes_of_note_time = {}
  current_note_lane = 1
  for note in sorted(note_times):
    for note_time in note_times[note]:
      new_note_lane = ((current_note_lane - 1) % key_mode) + 1
      if note_time in lanes_of_note_time.keys():
        lanes_of_note_time[note_time].append(new_note_lane)
      else:
        lanes_of_note_time[note_time] = [new_note_lane]
      current_note_lane += 1
  return lanes_of_note_time

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
midi_file_name = StringVar()
midi_file_path = StringVar()
output_key_mode = IntVar(value=7)
ttk.Button(mainframe, text="Choose MIDI file", command=select_midi_file).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="MIDI File:").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, textvariable=midi_file_name).grid(column=3, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Output Keymode:").grid(column=1, row=2, sticky=E)
ttk.Radiobutton(mainframe, text="7K", variable=output_key_mode, value=7).grid(column=2, row=2, sticky=W)
ttk.Radiobutton(mainframe, text="4K", variable=output_key_mode, value=4).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Convert selected MIDI file to .txt", command=convert_midi).grid(column=1, row=3, columnspan=3, sticky=W)
for child in mainframe.winfo_children(): 
  child.grid_configure(padx=5, pady=5)

root.mainloop()