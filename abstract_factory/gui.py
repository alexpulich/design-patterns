from .abstracts import Button, InputField


class MacButton(Button):
    def render(self):
        return 'I am a MacButton'


class WinButton(Button):
    def render(self):
        return 'I am a WinButton'


class GnomeButton(Button):
    def render(self):
        return 'I am a GnomeButton'


class MacInputField(InputField):
    def render(self):
        return 'I am a MacInputField'


class WinInputField(InputField):
    def render(self):
        return 'I am a WinInputField'


class GnomeInputField(InputField):
    def render(self):
        return 'I am a GnomeInputField'
