class Context(object):
    """The context in which a test or set of tests should execute.

    This class stores all context variables for a given test or set of tests. These variables can include anything from
    a reference to an excel workbook storing data sets to return values from test commands. This class behaves like a
    standard python dict.

    This class also supports nesting, such that all keys will first be attempted in this instance, and if not found,
    will be tried in the parent context. That parent context may also have its own parent.

    Args:
        parent: The parent context.
    """

    # noinspection PyDictCreation
    def __init__(self, parent: 'Context' = None):
        self._dict = {}
        self._dict['parent'] = parent

    def __setitem__(self, key, value):
        """Set a variable in the current context."""
        self._dict[key] = value

    def __getitem__(self, item):
        """Get a variable from the current context, or the parent if it does not exist in the current context."""
        if item in self._dict:
            return self._dict[item]
        elif self._dict['parent'] is not None and item in self._dict['parent']:
            return self._dict['parent'][item]
        else:
            raise KeyError(item)

    def __delitem__(self, key):
        """Delete a variable from the current context."""
        del self._dict[key]

    def __contains__(self, item):
        """Check if this context contains a variable."""
        if item in self._dict:
            return True
        elif self._dict['parent'] is not None and item in self._dict['parent']:
            return True
        else:
            return False

    def get(self, item, otherwise=None):
        """Get a variable from this context, or the parent if it does not exist in the current context. If it does not
        exist in either, then return otherwise."""
        if item in self._dict:
            return self._dict[item]
        elif self._dict['parent'] is not None and item not in self._dict['parent']:
            return self._dict
        else:
            return otherwise


_global_context = None


def get_global_context():
    global _global_context
    if _global_context is None:
        _global_context = Context()
    return _global_context
