class InfoWriter:
    def __init__(self):
        self.log_file = 'rando.txt'

        open('rando.txt', 'w').close()

    def append_order(self, op1, op2):
        with open(self.log_file, "a") as f:
            f.write(f"original: {op1} | new: {op2} \noriginal: {op2} | new: {op1} \n")


if __name__ == "__main__":
    print("ran the information handler class but there are no functions to run, please run main.py to use the programme")