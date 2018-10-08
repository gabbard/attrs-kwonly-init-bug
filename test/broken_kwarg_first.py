from attr import attrs, attrib


@attrs
class BrokenKwArgFirst:
    kwarg: str = attrib(kw_only=True)
    _to_init: str = attrib(init=False)

    @_to_init.default
    def _init_to_init(self) -> str:
        return self.kwarg + "foo"


BrokenKwArgFirst(kwarg="meep")
