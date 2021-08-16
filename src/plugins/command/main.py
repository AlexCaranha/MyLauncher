
import pluggy

hookimpl = pluggy.HookimplMarker('mylauncher')

def get_class():
    return CommandPlugin()

class CommandPlugin:
    @hookimpl
    def setup(self):
        print("Setup ...")

    @hookimpl
    def get_alias(self):
        return "command"

    @hookimpl
    def execute(self, input:str):
        return None
