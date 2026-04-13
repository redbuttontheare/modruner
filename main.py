import os
import importlib.util

PLUGINS_DIR = "mods"

def load_plugins():
    plugins = []
    for filename in os.listdir(PLUGINS_DIR):
        if filename.endswith(".py") or filename.endswith(".pyw"):
            path = os.path.join(PLUGINS_DIR, filename)
            name = filename[:-3]

            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "on_load"):
                module.on_load()
            plugins.append(module)

    return plugins


if __name__ == "__main__":
    plugins = load_plugins()
