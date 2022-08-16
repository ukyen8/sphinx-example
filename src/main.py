"""This is a Sphinx example module."""


class SimpleClass:
    """Class level docstring.

    .. todo:: This is a TODO.
    """

    def method_1(self) -> None:
        """Public method will be documented.

        - Bullet list 1
        - Bullet list 2

        1. This is a numbered list.
        2. It has two items too.

        #. This is also a numbered list.
        #. It has two items too.

        Sample code block::

            >>> 1 + 1
            2

        `Link to Httpbins <https://httpbin.org/>`_
        """

    def method_2(self, arg1: str, arg2: int) -> str:
        """Public method will be documented.

        :param arg1: first argument.
        :param arg2: second argument.
        """
        return f"{arg1}-{arg2}"

    def _method_3(self) -> None:
        """Private method will not be documented."""


def module_level_function(val1: int, val2) -> int:
    """Module level function.

    =====  =====  =======
    Item1  Item2  Summary
    =====  =====  =======
    1      4      5
    2      3      5
    3      2      5
    4      1      5
    =====  =====  =======

    :param val1: first value.
    :param val2: second value.
    """
    return val1 + val2
