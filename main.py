import ndspy.rom
import ndspy.fnt as fnt
from yaml_parsing import load_ops_rando, load_ops, rando_levels

import random
import sys
from pathlib import Path

rom_file = None
rando_log = 'rando.txt'

open('rando.txt', 'w').close()

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

# Randomiser flag pool: 
#   - 1: does not have active ht flag or flag only becomes available later in the op
#   - 2: ht is available at start of op
#   - 3: op is muliop (ht distinction not done for now)

def get_files(rom):
    """
        Returns files from rom
    """
    return rom.files

def append_order(file, op1, op2):
    with open("rando.txt", "a") as f:
        f.write(f"original: {op1} | new: {op2} \noriginal: {op2} | new: {op1} \n")


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

def operation_list_rando(no_ht, ht, multiop, seed = random.randint(0, 10000)):
    random.seed(seed)
    no_ht = sorted(no_ht, key=lambda x: random.random())
    ht = sorted(ht, key=lambda x: random.random())
    multiop = sorted(multiop, key=lambda x: random.random())
    return no_ht, ht, multiop

def op_randomiser(no_ht, ht, multiop, no_ht_ori, ht_ori, multiop_ori, associations, rom):
    # TODO: cleaner implementation when sure this is properly working (no more millions of loops)
    for op in no_ht.copy():
        if op in (no_ht and no_ht_ori):
            # print(op, operations[0])
            print(no_ht_ori[0], op)
            print(no_ht_ori, no_ht)
            swap_operations(rom, op, no_ht_ori[0], associations)
            rando_pop = no_ht.pop(0)
            op_pop = no_ht_ori.pop(0)
            if(rando_pop != op_pop):
                no_ht_ori.remove(rando_pop)
                no_ht.remove(op_pop)

    for op in ht.copy():
        if op in (ht and ht_ori):
            # print(op, operations[0])
            print(ht_ori[0], op)
            print(ht_ori, no_ht)
            swap_operations(rom, op, ht_ori[0], associations)
            rando_pop = ht.pop(0)
            op_pop = ht_ori.pop(0)
            if(rando_pop != op_pop):
                ht_ori.remove(rando_pop)
                ht.remove(op_pop)
    
    # for op in multiop.copy():
    #     if op in (multiop and multiop_ori):
    #         # print(op, operations[0])
    #         print(multiop_ori[0], op)
    #         print(multiop_ori, multiop)
    #         swap_operations(rom, op, multiop_ori[0], associations)
    #         rando_pop = multiop.pop(0)
    #         op_pop = multiop_ori.pop(0)
    #         if(rando_pop != op_pop):
    #             multiop_ori.remove(rando_pop)
    #             multiop.remove(op_pop)

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
    print(op1)
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

    append_order(rando_log, op1, op2)

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
# operations = load_ops_rando()
no_ht_ori, ht_ori, multiop_ori = rando_levels()
print(ht_ori)
no_ht, ht, multiop = operation_list_rando(no_ht_ori, ht_ori, multiop_ori)

op_randomiser(no_ht, ht, multiop, no_ht_ori, ht_ori, multiop_ori, associations, rom)

fnt.save(rom.filenames)
rom.saveToFile('utk2_rando.nds')
