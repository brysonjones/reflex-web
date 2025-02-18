from pcweb import flexdown
from pcweb.base_state import State


class FormState(State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def render_form():
    return flexdown.render_file("docs/library/forms/form.md")
