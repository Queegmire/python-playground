import cmd

class CalcShell(cmd.Cmd):
    intro = 'Brew time\n'
    state = 0
    prompt = f'{state}> '

    def do_add(self, arg):
        self.state += parse(arg)
        self.prompt = f'{self.state} :'

    def do_sub(self, arg):
        self.state -= parse(arg)
        self.prompt = f'{self.state} :'

    def do_mul(self, arg):
        self.state *= parse(arg)
        self.prompt = f'{self.state} :'

    def do_bye(self, arg):
        return True

    def close(self):
        pass

def parse(arg):
    return int(arg)

if __name__ == '__main__':
    CalcShell().cmdloop()
