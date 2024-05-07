from trame_client.widgets.core import AbstractElement

from trame_bbox import module


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


__all__ = [
    "BBox",
]


class BBox(HtmlElement):
    """Bounding Box component."""

    def __init__(self, **kwargs):
        """Create bounding box(es) component with the following parameters.

        Keyword Arguments:
        -----------------
        width -- width of the domain (default 300)
        height -- height of the domain (default 300)
        read_only -- if true, user won't be able to edit existing rectangles
        default_rect_style -- default SVG style to apply to the rectangles
        model_value -- Object providing the rectangles x, y, width, height and style

        """
        super().__init__(
            "trame-bbox",
            **kwargs,
        )
        self._attr_names += [
            "width",
            "height",
            ("model_value", "modelValue"),
            ("read_only", "readOnly"),
            ("default_rect_style", "defaultRectStyle"),
        ]
        self._event_names += [
            ("update_model_value", "update:modelValue"),
        ]
