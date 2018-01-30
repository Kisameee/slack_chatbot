class AbstractResponse(object):

    def run(self, command):
        raise SyntaxError('Cannot respond to command {command}. Should be implemented'.format(command=command))


