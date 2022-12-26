from model import TASKS


class Controller():

    def handle_add(self, input, callback):
        TASKS.append(input)
        callback()
        print(TASKS)
