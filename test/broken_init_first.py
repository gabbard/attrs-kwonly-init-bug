from attr import attrs, attrib


@attrs
class BrokenInitFirst:
    _to_init: str  = attrib(init=False)
    kwarg: str = attrib(kw_only=True)

    @_to_init.default
    def _init_to_init(self) -> str:
        return self.kwarg + "foo"


BrokenInitFirst(kwarg="meep")
