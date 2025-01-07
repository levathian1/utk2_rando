import ndspy.rom
import ndspy.fnt as fnt
from yaml_parsing import load_ops_rando, load_ops
import random
import sys

rom_file = None

if (len(sys.argv) > 1):
    rom_file = sys.argv[1]
else:
    rom_file = "utk2.nds"

operation_list = "operations.txt"

# To fully switch operation stuff need:
#   - corresponding data file
#   - area A, B, C files
#   - pos file
#   - operation text 

# Loading files to swap around
# Can probably just have a loadable file with relevant filenames and load stuff around that

# set randomiser flags in association file

def get_files(rom):
    """
        Returns files from rom
    """
    return rom.files

def load_op_list(op_list = operation_list):
    op = list()
    with open(op_list, "r") as f:
        op = f.read().splitlines()

    print(op)

def switch_operation_data(rom, op1, op2):
    op1_content = rom.files[op1]
    op2_content = rom.files[op2]

    rom.setFileByName(rom.filenames.filenameOf(op1), op2_content)
    rom.setFileByName(rom.filenames.filenameOf(op2), op1_content)

def operation_list_rando(operations):
    rando = sorted(operations, key=lambda x: random.random())
    return rando

def op_randomiser(rando, operations, associations, rom):
    for op in rando:
        # print(op, operations[0])
        swap_operations(rom, op, operations[0], associations)
        rando.pop(0)
        operations.pop(0)

def get_key(associations, op):
    for i in range(0, len(associations['operations'])):
        # print(associations['operations'][i]['name'], op)
        if associations['operations'][i]['name'] == op:
            return i

def swap_operations(rom, op1, op2, associations):
    header_data = "operation/data/"
    header_area = "operation/hit/"
    header_text = "operation/msg/"
    op1_key = get_key(associations, op1)
    op2_key = get_key(associations, op2)
    print(associations['operations'][op1_key]['area_a'])
    op1_id = rom.filenames.idOf(header_data + op1)
    op2_id = rom.filenames.idOf(header_data + op2)
    # print(op1_id, op2_id)
    # swap data file
    old_op1 = rom.files[op1_id]
    rom.setFileByName(header_data + op1, rom.files[op2_id])
    rom.setFileByName(header_data + op2, old_op1)
    # swap area A
    old_area_a = rom.files[associations['operations'][op1_key]['area_a']]
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op1_key]['area_a']), rom.files[associations['operations'][op2_key]['area_a']])
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op2_key]['area_a']), old_area_a)
    # swap area B
    old_area_b = rom.files[associations['operations'][op1_key]['area_b']]
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op1_key]['area_b']), rom.files[associations['operations'][op2_key]['area_b']])
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op2_key]['area_b']), old_area_b)
    # swap area C
    old_area_c = rom.files[associations['operations'][op1_key]['area_c']]
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op1_key]['area_c']), rom.files[associations['operations'][op2_key]['area_c']])
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op2_key]['area_c']), old_area_c)
    # swap pos 
    old_pos = rom.files[associations['operations'][op1_key]['pos']]
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op1_key]['pos']), rom.files[associations['operations'][op2_key]['pos']])
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op2_key]['pos']), old_pos)
    # swap op text
    old_text = rom.files[associations['operations'][op1_key]['text']]
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op1_key]['text']), rom.files[associations['operations'][op2_key]['text']])
    rom.setFileByName(rom.filenames.filenameOf(associations['operations'][op2_key]['text']), old_text)

def save_rando_list(operations, rando):
    with open("rando.txt", "w") as f:
        for i in range(0, len(rando)):
            f.write(f"original: {operations[i]} | new: {rando[i]} \n")

rom = ndspy.rom.NintendoDSRom.fromFile(rom_file)

# print(rom.filenames.filenameOf(766))
# print(rom.filenames.idOf('operation/msg/ope_scn807.bin'))


# replace final op msg content by 7-7 content

# switch_operation_data(rom, 1668, 1674)
# swap_operations(rom, 1, 1)
associations = load_ops()
operations = load_ops_rando()
rando = operation_list_rando(operations)
print(len(operations) == len(rando))
save_rando_list(operations, rando)
op_randomiser(rando, operations, associations, rom)
fnt.save(rom.filenames)

# load_op_list()

rom.saveToFile('utk2_rando.nds')
