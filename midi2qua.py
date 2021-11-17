# midi2qua v1.0 by kloi34
# Converts a MIDI file to .qua format
# Noob program by noob Python programmer
from mido import MidiFile
import math
import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def selectMidiFile():
  filetypes = (
        ('MIDI files', '*.mid'),
    )
  midiFilePath.set(filedialog.askopenfilename(
     title='Select a MIDI file to convert',
     initialdir='./',
     filetypes=filetypes
  ))
  midiFileName.set(os.path.basename(midiFilePath.get()))
def converMidiToQua():
  outputFileName = "tset.txt"
  f = open(outputFileName, "w")
  maxSecondSeparation = 0.04
  keyMode = 7

  totalTime = 0
  timeBetweenNoteOn = 0
  noteToOffset = {}
  offsetToLane = {}
  for msg in MidiFile(midiFileName.get(), clip=True):
    if msg.is_meta:
      if msg.type == 'end_of_track':
        currentLane = 1
        for note in sorted(noteToOffset):
          for offset in noteToOffset[note]:
            newLane = ((currentLane - 1) % keyMode) + 1
            if offset in offsetToLane.keys():
              offsetToLane[offset].append(newLane)
            else:
              offsetToLane[offset] = [newLane]
            currentLane += 1
        for offset in sorted(offsetToLane.keys()):
          for lane in offsetToLane[offset]:
            print("- StartTime: " + str(offset), file=f)
            print("  Lane: " + str(lane), file=f)
            print("  KeySounds: []", file=f)
        noteToOffset.clear()
        offsetToLane.clear()
    else:
      totalTime += msg.time
      timeBetweenNoteOn += msg.time
      if msg.type == 'note_on' and msg.velocity > 0:
        if timeBetweenNoteOn >= maxSecondSeparation:  
          timeBetweenNoteOn = 0
          currentLane = 1
          for note in sorted(noteToOffset):
            for offset in noteToOffset[note]:
              newLane = ((currentLane - 1) % keyMode) + 1
              if offset in offsetToLane.keys():
                offsetToLane[offset].append(newLane)
              else:
                offsetToLane[offset] = [newLane]
              currentLane += 1
          for offset in sorted(offsetToLane.keys()):
            for lane in offsetToLane[offset]:
              print("- StartTime: " + str(offset), file=f)
              print("  Lane: " + str(lane), file=f)
              print("  KeySounds: []", file=f)
          noteToOffset.clear()
          offsetToLane.clear()
        if msg.note in noteToOffset.keys():
          noteToOffset[msg.note].append(math.floor(totalTime * 1000))
        else:
          noteToOffset[msg.note] = [math.floor(totalTime * 1000)]
  f.close()
  print('File Converted, .qua Hitobject text outputted to ' + outputFileName)
root = Tk()
root.title("midi2qua")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#maxMidiNoteVelocity = StringVar()
#maxMidiNoteVelocity_entry = ttk.Entry(mainframe, width=7, textvariable=maxMidiNoteVelocity)
#maxMidiNoteVelocity_entry.grid(column=3, row=2, sticky=(W, E))

midiFileName = StringVar()
midiFilePath = StringVar()
ttk.Label(mainframe, text="MIDI File:").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, textvariable=midiFileName).grid(column=3, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Choose MIDI File", command=selectMidiFile).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Convert MIDI to .qua Hitobject Text", command=converMidiToQua).grid(column=1, row=2, columnspan = 3, sticky=W)

for child in mainframe.winfo_children(): 
  child.grid_configure(padx=5, pady=5)

#maxMidiNoteVelocity_entry.focus()

root.mainloop()