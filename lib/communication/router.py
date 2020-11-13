from importlib import import_module


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name, method_name = dotted_path.rsplit('.', 2)
    except ValueError:
        msg = "%s doesn't look like a module path" % dotted_path

    module = import_module(module_path)

    try:
        return getattr(getattr(module, class_name), method_name)
    except AttributeError:
        msg = 'Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)


class Router:
    def __init__(self):
        self.routes = {}

    def setRoute(self, name: str, method: str):
        self.routes[name] = import_string(str)

    def getRoute(self, name):
        return self.routes[name]
