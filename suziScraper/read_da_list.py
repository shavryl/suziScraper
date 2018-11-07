import io, csv


test_list = ['one', 'two', 'tree']


class ReadListInDaMemory:

    def __init__(self, args_list):
        self.args_list = args_list

    def return_value(self):
        _string = ", ".join(self.args_list)
        output = io.StringIO(_string, newline='\n')
        content = output.getvalue()
        return content
