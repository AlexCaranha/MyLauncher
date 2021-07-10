# hookspec.py
import pluggy

hookspec = pluggy.HookspecMarker('mylauncher')

class PluginBase:
    @hookspec
    def setup(self):
        pass

    @hookspec
    def get_alias(self):
        pass

    @hookspec
    def execute(self, input:str):
        pass