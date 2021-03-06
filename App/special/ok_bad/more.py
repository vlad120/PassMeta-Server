from App.special.ok_bad.more_type import *
from App.translate import OK_BAD_MORE_TYPES_TRANSLATE_PACK, get_package_text
from typing import Any, Union, Dict

__all__ = (
    'ResultMore',
    'MORE',
)


class ResultMore:
    __slots__ = ('type', 'value')

    def __init__(self, _type: int, _value):
        self.type = _type
        self.value = _value

    def to_dict(self, locale: str) -> Dict[str, Any]:
        if self.type == INFO:
            return {'info': self.value}
        return {'text': f"{get_package_text(OK_BAD_MORE_TYPES_TRANSLATE_PACK, self.type, locale, self.type)}: "
                        f"{self.value if type(self.value) is not list else ', '.join(map(str, self.value))}"}


class MORE:

    @staticmethod
    def text(val: str) -> ResultMore:
        return ResultMore(TEXT, val)

    @staticmethod
    def info(*values: Dict[str, Any]):
        return ResultMore(INFO, list(values))

    @staticmethod
    def required(*values: Any) -> ResultMore:
        return ResultMore(REQUIRED, list(values))

    @staticmethod
    def allowed(*values: Any) -> ResultMore:
        return ResultMore(ALLOWED, list(values))

    @staticmethod
    def disallowed(*values: Any) -> ResultMore:
        return ResultMore(DISALLOWED, list(values))

    @staticmethod
    def min_allowed(val: Union[int, float, str]) -> ResultMore:
        return ResultMore(MIN_ALLOWED, val)

    @staticmethod
    def max_allowed(val: Union[int, float, str]) -> ResultMore:
        return ResultMore(MAX_ALLOWED, val)

    @staticmethod
    def exception(ex: BaseException) -> ResultMore:
        return ResultMore(TEXT, str(ex))
