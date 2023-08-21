class BaseValidator:
    def validate(self, identifier):
        raise NotImplementedError("This method should be overridden in child classes.")
