class ABError(Exception):
    pass


class ABValidationError(ABError):
    pass


class ABBuildUnsuccesful(ABError):
    """ Build was not successful """
    def __init__(self, msg, output):
        self.msg = msg
        self.output = output

    def __str__(self):
        return "%s" % self.msg
