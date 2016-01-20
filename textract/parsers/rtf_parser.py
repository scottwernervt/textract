import sys

if sys.version_info < (3,):
    import codecs


    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

from .utils import ShellParser


class Parser(ShellParser):
    """Extract text from rtf files using unrtf.
    """

    def extract(self, filename, **kwargs):
        # http://superuser.com/a/243089/126633
        stdout, stderr = self.run('unrtf --text "%(filename)s"' % locals())
        text_conversion = u(stdout).split('-' * 17 + '\n', 1)[-1]
        return text_conversion
