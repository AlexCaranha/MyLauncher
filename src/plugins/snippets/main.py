
import pluggy

hookimpl = pluggy.HookimplMarker('mylauncher')

def get_class():
    return SnippetsPlugin()

class SnippetsPlugin:
    @hookimpl
    def setup(self):
        print("Setup ...")

    @hookimpl
    def get_alias(self):
        return "snippets"

    @hookimpl
    def execute(self, input:str):
        return None
