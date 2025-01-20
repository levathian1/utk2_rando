import ndspy.rom

from randomiser import Randomiser
import sys
from pathlib import Path

# Loading files to swap around
# Can probably just have a loadable file with relevant filenames and load stuff around that
# TODO: pydoc 

def main():
# TODO: this should check value in argv[1] not just assign to avoid problems down the road
    if (len(sys.argv) > 1):
        rom_file = sys.argv[1]
    else:   
        rom_file = "utk2.nds"

# TODO: this should check value in argv[2] not just assign to avoid problems down the road
    if(len(sys.argv) > 2):
        rom = ndspy.rom.NintendoDSRom.fromFile(rom_file, sys.argv[2])
    else:
        rom = ndspy.rom.NintendoDSRom.fromFile(rom_file)
    
    randomiser = Randomiser(rom)

    randomiser.op_randomiser()

    print("randomised operations, check output file for new ordering")


if __name__ == "__main__":
    main()