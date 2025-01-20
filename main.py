import ndspy.rom

from randomiser import Randomiser
import sys
from pathlib import Path

# Loading files to swap around
# Can probably just have a loadable file with relevant filenames and load stuff around that
# TODO: pydoc 

# TODO: flag usage in argv to allow inclusion of only seed without rom name

def main():
    if (len(sys.argv) > 1 and isinstance(sys.argv, str)):
        rom_file = sys.argv[1]
    else:   
        rom_file = "utk2.nds"

    if(len(sys.argv) > 2 and isinstance(sys.argv, (int or str))):
        rom = ndspy.rom.NintendoDSRom.fromFile(rom_file, sys.argv[2]) 
    else:
        rom = ndspy.rom.NintendoDSRom.fromFile(rom_file)
    
    randomiser = Randomiser(rom)

    randomiser.op_randomiser()

    print("randomised operations, check output file for new ordering")


if __name__ == "__main__":
    main()