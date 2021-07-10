
import pluggy

hookimpl = pluggy.HookimplMarker('mylauncher')

def get_class():
    return EverythingPlugin()

class EverythingPlugin:
    @hookimpl
    def setup(self):
        print("Setup ...")

    @hookimpl
    def get_alias(self):
        return "everything"

    @hookimpl
    def execute(self, input:str):
        return None
