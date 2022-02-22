import functools
import inspect
import warnings

__string_types = (type(b''), type(u''))

def disuse(reason):
    """
    Adapted from: https://stackoverflow.com/a/40301488/6427171

    This is a decorator which can be used to mark functions
    as disuse. It will result in a warning being emitted
    when the function is used. 
    """

    if isinstance(reason, __string_types):

        # The @disuse is used with a 'reason'.
        #
        # .. code-block:: python
        #
        #    @disuse("please, use another function")
        #    def old_function(x, y):
        #      pass

        def decorator(func1):

            if inspect.isclass(func1):
                fmt1 = "Call to disuse class {name} ({reason})."
            else:
                fmt1 = "Call to disuse function {name} ({reason})."

            @functools.wraps(func1)
            def new_func1(*args, **kwargs):
                warnings.simplefilter('always', RuntimeWarning)
                warnings.warn(
                    fmt1.format(name=func1.__name__, reason=reason),
                    category=RuntimeWarning,
                    stacklevel=2
                )
                warnings.simplefilter('default', RuntimeWarning)
                return func1(*args, **kwargs)

            return new_func1

        return decorator

    elif inspect.isclass(reason) or inspect.isfunction(reason):

        # The @disuse is used without any 'reason'.
        #
        # .. code-block:: python
        #
        #    @disuse
        #    def old_function(x, y):
        #      pass

        func2 = reason

        if inspect.isclass(func2):
            fmt2 = "Call to disuse class {name}."
        else:
            fmt2 = "Call to disuse function {name}."

        @functools.wraps(func2)
        def new_func2(*args, **kwargs):
            warnings.simplefilter('always', RuntimeWarning)
            warnings.warn(
                fmt2.format(name=func2.__name__),
                category=RuntimeWarning,
                stacklevel=2
            )
            warnings.simplefilter('default', RuntimeWarning)
            return func2(*args, **kwargs)

        return new_func2

    else:
        raise TypeError(repr(type(reason)))