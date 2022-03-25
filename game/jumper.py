class Jumper:
    """The responsibility of Jumper is to
        print itself to the screen.
        
        Attributes:
        layers: A list containing the layers for each stage
                of the jumpers parachute."""

    def __init__(self):
        self._layers = []
        self.make_jumper()

    def make_jumper(self):
        self._layers.append(" ___")
        self._layers.append("/   \\")
        self._layers.append(" ___")
        self._layers.append("\\   /")
        self._layers.append(" \\ /")
        self._layers.append("  0")
        self._layers.append(" /|\\")
        self._layers.append(" / \\")

    def print_self(self):
        for layer in self._layers:
            print(layer)

    def lose_life(self):
        if self._layers[0] != "  0":
            self._layers.pop(0)
        else:
            self._layers[0] = "  x"

    def is_dead(self):
        if self._layers[0] == "  x":
            return True
        return False
