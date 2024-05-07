from trame.app import get_server
from trame.decorators import TrameApp, change
from trame.ui.html import DivLayout
from trame.widgets import html
from trame_bbox.widgets import bbox

BBOXES_0 = {
    "left": {
        "x": 10,
        "y": 10,
        "width": 100,
        "height": 200,
        "style": {
            "stroke": "blue",
            "stroke-width": 2,
        },
    },
    "right": {
        "x": 100,
        "y": 50,
        "width": 75,
        "height": 50,
        "style": {
            "stroke": "green",
            "stroke-width": 3,
        },
    },
    "hello": {
        "x": 150,
        "y": 150,
        "width": 50,
        "height": 75,
        "style": {
            "stroke": "yellow",
            "stroke-width": 5,
        },
    },
}

BBOXES_1 = {
    "left": {
        "x": 25,
        "y": 25,
        "width": 100,
        "height": 200,
        "style": {
            "stroke": "blue",
            "stroke-width": 5,
        },
    },
    "right": {
        "x": 150,
        "y": 250,
        "width": 75,
        "height": 50,
        "style": {
            "stroke": "green",
            "stroke-width": 5,
        },
    },
    "hello": {
        "x": 50,
        "y": 250,
        "width": 50,
        "height": 75,
        "style": {
            "stroke": "yellow",
            "stroke-width": 5,
        },
    },
}

TIMES = [
    BBOXES_0,
    BBOXES_1,
    BBOXES_0,
    BBOXES_1,
]


@TrameApp()
class App:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.ui = self._build_ui()

    @property
    def state(self):
        return self.server.state

    @change("t_idx")
    def on_time_change(self, t_idx, **kwargs):
        self.state.boxes = TIMES[t_idx]

    def _build_ui(self):
        with DivLayout(self.server) as layout:
            html.Input(
                v_model_number=("t_idx", 0),
                min=0,
                max=len(TIMES) - 1,
                step=1,
                type="range",
                style="position: absolute; top: 1rem; right: 1rem;",
            )
            bbox.BBox(style="border: solid 1px #333;", v_model=("boxes", {}))

            return layout


def main():
    app = App()
    app.server.start()


if __name__ == "__main__":
    main()
