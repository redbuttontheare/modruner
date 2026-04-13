class Block:
    def void(self):
        while True:
            print("This program is blocked for run!")
            print("Type 'quit' to exit")
            bcs = input()
            if bcs == "quit":
                import sys
                sys.exit()
    def run(self):
        Block.void()

def Blocker(runnable):
    if runnable == "1":
        Block.run()
    if runnable == "0":
        import sys
        sys.exit()