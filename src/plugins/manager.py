
import pluggy, importlib

class Manager():
    def __init__(self):
        self.pm = pluggy.PluginManager('beth')   
        hookspec = importlib.import_module("plugins.hookspec")
        self.pm.add_hookspecs(hookspec.BethSpec)

    def load_plugins(self):
        plugins_names = \
        [
            "plugins.everything.main",
        ]

        for plugin_name in plugins_names:
            plugin = importlib.import_module(plugin_name)
            plugin_class = plugin.get_class()
            plugin_class.setup()

            self.pm.register(plugin_class)
            self.pm.check_pending()

        print("plugins loaded.")

    def get_plugin(self, alias:str):
        plugins = self.get_plugins()

        for plugin in plugins:
            if plugin.get_alias() == alias:
                return plugin

        return None

    def get_plugins(self):
        return self.pm.get_plugins()

    def get_qtd_plugins_loaded(self):
        plugins = self.get_plugins()
        output = len(plugins)
        return output

    def print_plugins_description(self):
        print(self.pm.list_name_plugin())
        
    def execute(self, plugin_alias: str, input: str):
        plugin = self.get_plugin(plugin_alias)
        output = plugin.execute(input)
        return output

    def execute_command(self, input: str):
        results = self.pm.hook.execute(input)

        if len(results) == 1:
            return results[0]
        
        return None
