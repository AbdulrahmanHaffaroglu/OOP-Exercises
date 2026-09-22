from abc import ABCMeta

def all_abstract(cls):
    """Automatically marks all user-defined methods in the class as abstract."""
    for name, value in list(cls.__dict__.items()):
        # Filter for functions, ignoring special dunder methods like __init__
        if callable(value) and not name.startswith("__"):
            value.__isabstractmethod__ = True
            
    # Force the ABC machinery to recalculate the abstract methods list
    if isinstance(cls, ABCMeta):
        import abc
        abc.update_abstractmethods(cls)
    return cls