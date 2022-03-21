from datetime import datetime

from peewee import TextField, AutoField


class BigAutoField(AutoField):
    field_type = "BIGAUTO"

    def adapt(self, value):
        return str(value)


class DateTimeField(TextField):
    __value: datetime = None

    def python_value(self, value):
        """
        sql => py
        """
        obj = DateTimeField()
        obj.__value = value
        return obj

    def toStr(self) -> str or None:
        if self.__value is None:
            return None
        elif isinstance(self.__value, datetime):
            return self.__value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return str(self.__value)

    def toInt(self) -> int or None:
        if self.__value is None:
            return None
        elif isinstance(self.__value, datetime):
            return int(self.__value.timestamp())
        else:
            return 0

    def getValue(self):
        return self.__value

    def setValue(self, a):
        self.__value = a
