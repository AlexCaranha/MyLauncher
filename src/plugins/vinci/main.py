
import pluggy

hookimpl = pluggy.HookimplMarker('mylauncher')

def get_class():
    return VinciPlugin()

class VinciPlugin:
    @hookimpl
    def setup(self):
        print(f"plugin {self.get_alias()} - setup ...")

    @hookimpl
    def get_alias(self):
        return "vinci"

    @hookimpl
    def execute(self, input:str):
        return None
