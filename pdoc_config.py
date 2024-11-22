import pdoc

def configure_pdoc():
    # Customize pdoc settings here
    # For example, exclude the __init__ method from all classes
    def exclude_init_method(cls):
        if '__init__' in cls.__dict__:
            cls.__init__.__doc__ = None  # Remove the docstring for __init__
        return cls

    # Exclude methods globally or for specific classes
    pdoc.renderers._DEFAULT_RENDERER.options.exclude = ['__init__']

    # You can also exclude entire classes or specific methods
    # Add logic for other configurations, like output format or template settings
    return pdoc.Module(pdoc.import_module('pycomptox'), exclude=exclude_init_method)
