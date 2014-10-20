from gutter.client.operators import Base
from gutter.client.registry import operators


class EqualsStripIgnoreCase(Base):

    name = 'strip_ignorecase_equals'
    group = 'string'
    preposition = 'strip ignore case equal to'
    arguments = ('value',)

    def _normalize(self, value):
        return value.lower().strip()

    def applies_to(self, argument):
        if not isinstance(argument, basestring):
            argument = str(argument)
        return self._normalize(argument) == self._normalize(self.value)

    def __str__(self):
        return '%s "%s"' % (self.preposition, self._normalize(self.value))

operators.register(EqualsStripIgnoreCase)
