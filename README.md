# Installation & running
Install the following python packages: ```ndspy, pyyaml``` 
using a python package manager.

Documentation for the NDSpy package is available [here](https://ndspy.readthedocs.io/en/latest/).


Run using the following command: 

```python main.py [rom file]``` where ```[rom file]``` is the path to a NTSC UtK2 rom (US locale)

Output is a file called ```utk2_rando.nds``` loadable in any ds emulator from the current millennial

DM any bug reports, questions or suggestions to me on Discord 

# Notes on the current progress
As seen in the associations file, not all operations are included in the randomiser, most notably any multi-patient operations or operations requiring the use of the healing touch at any point during gameplay, as that would either crash the game (in the first case, where the game will attempt to load the following patients and not find them) or potentially softlock the player out of the game (in the second case).
On top of that, stage time, starting vitals and backing tracks will be unchanged from the original operation, their values seemingly not actually being in what I believe to be the operation data files, but somewhere else entirely.

# Current TODO:
  - [ ] Fix the output file with the new operation associations
  - [ ] Add a more robust random seed generator
  - [ ] Find and add vitals, stage time & backing track values in the rom in order to fully randomise each currently considered operation
  - [ ] Figure out system to add multi-patient operations into the randomiser
