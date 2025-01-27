import ndspy.rom
import ndspy.fnt as fnt
import random, secrets
from operation_classification import OpClassification
from yaml_parsing import load_ops, rando_levels
from info_writer import InfoWriter

# To fully switch operation stuff need:
#   - corresponding data file
#   - area A, B, C files
#   - pos file
#   - operation text 

# TODO: Remove multiple key seeking 
# TODO: remove loop in loop iterations somehow

class Randomiser():
    """_summary_: Class handling randomising operations
    """
    def __init__(self, rom, seed = None):
        """_summary_: Initialises Randomiser class

        Args:
            rom (_type_): the rom to randomise
            seed (_type_, optional): Custom seed to use when swapping operations. Defaults to None.
        """
        self.seed = random.seed(seed or secrets.choice(range(0, 100000)))
        self.rom = rom
        self.associations = load_ops()
        self.NO_HT_ori, self.HT_ori, self.MULTI_ori = rando_levels()
        self.NO_HT_list, self.HT_list, self.MULTI_list = self.operation_list_rando()

        self.infoWriter = InfoWriter()

    def operation_list_rando(self):
        """_summary_: Generates randomised list

        Returns:
            _type_: List: Returns 3 randomised sorted by criteria defined in operation_classification.py
        """
        no_ht_op_list = sorted(self.NO_HT_ori, key=lambda x: random.random())
        ht_op_list = sorted(self.HT_ori, key=lambda x: random.random())
        multiop_op_list = sorted(self.MULTI_ori, key=lambda x: random.random())
        return no_ht_op_list, ht_op_list, multiop_op_list

    def op_randomiser(self):
        """_summary_: Main randomiser function, reads and iterates over randomised lists.
        """
    # TODO: cleaner implementation when sure this is properly working (no more millions of loops and checks)
        for op in self.NO_HT_list.copy():
            if op in (self.NO_HT_list):
                # print(op, operations[0])
                # print(self.NO_HT_ori[0], op)
                self.swap_operations(op, self.NO_HT_ori[0])
                rando_pop = self.NO_HT_list.pop(0)
                op_pop = self.NO_HT_ori.pop(0)
                # Removes the instance in the other list (either the ordered, or rando'd one) and removes it if it was not the head
                if(rando_pop != op_pop):
                    self.NO_HT_ori.remove(rando_pop)
                    self.NO_HT_list.remove(op_pop)

        for op in self.HT_list.copy():
            if op in (self.HT_list):
                # print(op, operations[0])
                self.swap_operations(op, self.HT_ori[0])
                rando_pop = self.HT_list.pop(0)
                op_pop = self.HT_ori.pop(0)
                # Removes the instance in the other list (either the ordered, or rando'd one) and removes it if it was not the head
                if(rando_pop != op_pop):
                    self.HT_ori.remove(rando_pop)
                    self.HT_list.remove(op_pop)

    def get_key(self, op):
        """_summary_: Temporary function to retrieve indices of specified operation

        Args:
            op (_type_): The operation to retrieve in associations.yaml

        Returns:
            _type_: int: The value of the index in associations.yaml
        """
        # TODO: this really shouldn't exist here, pass off to reader 
        for i in range(0, len(self.associations['operations'])):
            if self.associations['operations'][i]['name'] == op:
                return i

    def swap_operations(self, op1, op2):
        """_summary_: Operation swapping function, logs result to log file defined in info_writer.py

        Args:
            op1 (_type_): First operation to be swapped
            op2 (_type_): Second operation to be swapped
        """

        header_data = "operation/data/"

        op1_key = self.get_key(op1)
        op2_key = self.get_key(op2)


        op1_id = self.rom.filenames.idOf(header_data + op1)
        op2_id = self.rom.filenames.idOf(header_data + op2)
        # print(op1_id, op2_id)
        # swap data file
        op1_old = header_data + op1
        op2_old = header_data + op2
        self.rom.setFileByName(op1_old, op2_old)
        self.rom.setFileByName(op2_old, op1_old)
        # swap area A
        area_a_op1 = self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['area_a'])
        area_a_op2 = self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['area_a'])
        self.rom.setFileByName(area_a_op1, area_a_op2)
        self.rom.setFileByName(area_a_op2, area_a_op1)
        # swap area B
        area_b_op1 = self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['area_b'])
        area_b_op2 = self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['area_b'])
        self.rom.setFileByName(area_b_op1, area_b_op2)
        self.rom.setFileByName(area_b_op2, area_b_op1)
        # swap area C
        area_c_op1 = self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['area_c'])
        area_c_op2 = self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['area_c'])
        self.rom.setFileByName(area_c_op1, area_c_op2)
        self.rom.setFileByName(area_c_op2, area_c_op1)
        # swap pos 
        pos_op1 = self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['pos'])
        pos_op2 = self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['pos'])
        self.rom.setFileByName(pos_op1, pos_op2)
        self.rom.setFileByName(pos_op2, pos_op1)
        # swap op text
        text_op1 = self.rom.filenames.filenameOf(self.associations['operations'][op1_key]['text'])
        text_op2 = self.rom.filenames.filenameOf(self.associations['operations'][op2_key]['text'])
        self.rom.setFileByName(text_op1, text_op2)
        self.rom.setFileByName(text_op2, text_op1)
        
        self.infoWriter.append_order(op1, op2)

if __name__ == "__main__":
    print("ran the randomiser class but there are no functions to run, please run main.py to use the programme")