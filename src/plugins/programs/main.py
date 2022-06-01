
import pluggy

hookimpl = pluggy.HookimplMarker('mylauncher')

def get_class():
    return ProgramsPlugin()

class ProgramsPlugin:
    @hookimpl
    def setup(self):
        print(f"plugin {self.get_alias()} - setup ...")

    @hookimpl
    def get_alias(self):
        return "programs"

    @hookimpl
    def execute(self, input:str):
        return None
