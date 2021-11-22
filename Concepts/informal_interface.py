class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass


class PdfParserNew:
    """Extract text from a PDF."""

    def load_data_source(self) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_aa(self) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass


a = PdfParserNew()
print(issubclass(PdfParserNew, UpdatedInformalParserInterface))