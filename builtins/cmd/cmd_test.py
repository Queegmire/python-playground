import cmd

class MyCmd(cmd.Cmd):
    def __init__(self, prompt):
        self.line = 0
        self.prompt = prompt
        super().__init__()
    
def main():
    mc = MyCmd("hi")
    while True:
        mc.cmdloop()

if __name__ == "__main__":
    main()
