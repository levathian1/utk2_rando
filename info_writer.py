class InfoWriter:
    """_summary_: Logging Class
    """
    def __init__(self):
        """_summary_: Class initialisation, create a blank logging file to be used
        """
        self.log_file = 'rando.txt'

        open('rando.txt', 'w').close()

    def append_order(self, op1, op2):
        """_summary_: Logs exchanged operations

        Args:
            op1 (_type_): First operation used in swap
            op2 (_type_): Second operation used in swap
        """
        with open(self.log_file, "a") as f:
            f.write(f"original: {op1} | new: {op2}\n")


if __name__ == "__main__":
    print("ran the information handler class but there are no functions to run, please run main.py to use the programme")