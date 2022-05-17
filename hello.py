class Hello(object):

    def __init__(self, hel):
        self._hel = hel

    def hello(self):
        print("say", self._hel)

    @property
    def hel(self):
        return self._hel

    def __str__(self):
        return 'Hello(%s)' % self._hel
