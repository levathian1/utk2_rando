import ndspy.rom
import ndspy.fnt as fnt
import random, secrets
from operation_classification import OpClassification
from yaml_parsing import load_ops_rando, load_ops, rando_levels
from info_writer import InfoWriter

# To fully switch operation stuff need:
#   - corresponding data file
#   - area A, B, C files
#   - pos file
#   - operation text 

# TODO: Remove multiple key seeking 
# TODO: remove loop in loop iterations somehow

class Randomiser():
    def __init__(self, rom, seed = None):
        self.seed = random.seed(seed or secrets.choice(range(0, 100000)))
        self.rom = rom
        self.associations = load_ops()
        self.NO_HT_ori, self.HT_ori, self.MULTI_ori = rando_levels()
        self.NO_HT_list, self.HT_list, self.MULTI_list = self.operation_list_rando()

        self.infoWriter = InfoWriter()

    def operation_list_rando(self):
        no_ht_op_list = sorted(self.NO_HT_ori, key=lambda x: random.random())
        ht_op_list = sorted(self.HT_ori, key=lambda x: random.random())
        multiop_op_list = sorted(self.MULTI_ori, key=lambda x: random.random())
        return no_ht_op_list, ht_op_list, multiop_op_list
    
    def switch_operation_data(self, op1, op2):
        op1_content = self.rom.files[op1]
        op2_content = self.rom.files[op2]

        self.rom.setFileByName(self.rom.filenames.filenameOf(op1), op2_content)
        self.rom.setFileByName(self.rom.filenames.filenameOf(op2), op1_content)

    def op_randomiser(self):
    # TODO: cleaner implementation when sure this is properly working (no more millions of loops)
        for op in self.NO_HT_list.copy():
            if op in (self.NO_HT_list and self.NO_HT_ori):
                # print(op, operations[0])
                print(self.NO_HT_ori[0], op)
                print(self.NO_HT_ori, self.NO_HT_list)
                self.swap_operations(op, self.NO_HT_ori[0])
                rando_pop = self.NO_HT_list.pop(0)
                op_pop = self.NO_HT_ori.pop(0)
                if(rando_pop != op_pop):
                    self.NO_HT_ori.remove(rando_pop)
                    self.NO_HT_list.remove(op_pop)

        for op in self.HT_list.copy():
            if op in (self.HT_list and self.HT_ori):
                # print(op, operations[0])
                print(self.HT_ori[0], op)
                self.swap_operations(op, self.HT_ori[0])
                rando_pop = self.HT_list.pop(0)
                op_pop = self.HT_ori.pop(0)
                if(rando_pop != op_pop):
                    self.HT_ori.remove(rando_pop)
                    self.HT_list.remove(op_pop)

    def get_key(self, op):
        # TODO: this really shouldn't exist here, pass off to reader 
        for i in range(0, len(self.associations['operations'])):
            # print(associations['operations'][i]['name'], op)
            if self.associations['operations'][i]['name'] == op:
                return i

    def swap_operations(self, op1, op2):
        header_data = "operation/data/"
        header_area = "operation/hit/"
        header_text = "operation/msg/"
        op1_key = self.get_key(op1)
        op2_key = self.get_key(op2)

        self.infoWriter.append_order(op1, op2)

        print(op1)
        print(self.associations['operations'][op1_key]['area_a'])
        op1_id = self.rom.filenames.idOf(header_data + op1)
        op2_id = self.rom.filenames.idOf(header_data + op2)
        # print(op1_id, op2_id)
        # swap data file
        old_op1 = self.rom.files[op1_id]
        self.rom.setFileByName(header_data + op1, self.rom.files[op2_id])
        self.rom.setFileByName(header_data + op2, old_op1)
        # swap area A
        old_area_a = self.rom.files[self.associations['operations'][op1_key]['area_a']]
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['area_a']), self.rom.files[self.associations['operations'][op2_key]['area_a']])
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['area_a']), old_area_a)
        # swap area B
        old_area_b = self.rom.files[self.associations['operations'][op1_key]['area_b']]
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['area_b']), self.rom.files[self.associations['operations'][op2_key]['area_b']])
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['area_b']), old_area_b)
        # swap area C
        old_area_c = self.rom.files[self.associations['operations'][op1_key]['area_c']]
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['area_c']), self.rom.files[self.associations['operations'][op2_key]['area_c']])
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['area_c']), old_area_c)
        # swap pos 
        old_pos = self.rom.files[self.associations['operations'][op1_key]['pos']]
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['pos']), self.rom.files[self.associations['operations'][op2_key]['pos']])
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['pos']), old_pos)
        # swap op text
        old_text = self.rom.files[self.associations['operations'][op1_key]['text']]
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['text']), self.rom.files[self.associations['operations'][op2_key]['text']])
        self.rom.setFileByName(self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['text']), old_text)

if __name__ == "__main__":
    print("ran the randomiser class but there are no functions to run, please run main.py to use the programme")