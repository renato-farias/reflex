"""Stub file for reflex/components/datadisplay/dataeditor.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from enum import Enum
from typing import Any, Callable, Dict, List, Literal, Optional, Union
from reflex.base import Base
from reflex.components.component import Component, NoSSRComponent
from reflex.components.literals import LiteralRowMarker
from reflex.utils import console, format, imports, types
from reflex.utils.serializers import serializer
from reflex.vars import ImportVar, Var, get_unique_variable_name

class GridColumnIcons(Enum):
    Array = "array"
    AudioUri = "audio_uri"
    Boolean = "boolean"
    HeaderCode = "code"
    Date = "date"
    Email = "email"
    Emoji = "emoji"
    GeoDistance = "geo_distance"
    IfThenElse = "if_then_else"
    Image = "image"
    JoinStrings = "join_strings"
    Lookup = "lookup"
    Markdown = "markdown"
    Math = "math"
    Number = "number"
    Phone = "phone"
    Reference = "reference"
    Rollup = "rollup"
    RowID = "row_id"
    SingleValue = "single_value"
    SplitString = "split_string"
    String = "string"
    TextTemplate = "text_template"
    Time = "time"
    Uri = "uri"
    VideoUri = "video_uri"

class DataEditorTheme(Base):
    accent_color: Optional[str]
    accent_fg: Optional[str]
    accent_light: Optional[str]
    base_font_style: Optional[str]
    bg_bubble: Optional[str]
    bg_bubble_selected: Optional[str]
    bg_cell: Optional[str]
    bg_cell_medium: Optional[str]
    bg_header: Optional[str]
    bg_header_has_focus: Optional[str]
    bg_header_hovered: Optional[str]
    bg_icon_header: Optional[str]
    bg_search_result: Optional[str]
    border_color: Optional[str]
    cell_horizontal_padding: Optional[int]
    cell_vertical_padding: Optional[int]
    drilldown_border: Optional[str]
    editor_font_size: Optional[str]
    fg_icon_header: Optional[str]
    font_family: Optional[str]
    header_bottom_border_color: Optional[str]
    header_font_style: Optional[str]
    horizontal_border_color: Optional[str]
    line_height: Optional[int]
    link_color: Optional[str]
    text_bubble: Optional[str]
    text_dark: Optional[str]
    text_group_header: Optional[str]
    text_header: Optional[str]
    text_header_selected: Optional[str]
    text_light: Optional[str]
    text_medium: Optional[str]

class DataEditor(NoSSRComponent):
    def get_event_triggers(self) -> Dict[str, Callable]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        rows: Optional[Union[Var[int], int]] = None,
        columns: Optional[
            Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]
        ] = None,
        data: Optional[Union[Var[List[List[Any]]], List[List[Any]]]] = None,
        get_cell_content: Optional[Union[Var[str], str]] = None,
        get_cell_for_selection: Optional[Union[Var[bool], bool]] = None,
        on_paste: Optional[Union[Var[bool], bool]] = None,
        draw_focus_ring: Optional[Union[Var[bool], bool]] = None,
        fixed_shadow_x: Optional[Union[Var[bool], bool]] = None,
        fixed_shadow_y: Optional[Union[Var[bool], bool]] = None,
        freeze_columns: Optional[Union[Var[int], int]] = None,
        group_header_height: Optional[Union[Var[int], int]] = None,
        header_height: Optional[Union[Var[int], int]] = None,
        max_column_auto_width: Optional[Union[Var[int], int]] = None,
        max_column_width: Optional[Union[Var[int], int]] = None,
        min_column_width: Optional[Union[Var[int], int]] = None,
        row_height: Optional[Union[Var[int], int]] = None,
        row_markers: Optional[
            Union[
                Var[Literal["none", "number", "checkbox", "both", "clickable-number"]],
                Literal["none", "number", "checkbox", "both", "clickable-number"],
            ]
        ] = None,
        row_marker_start_index: Optional[Union[Var[int], int]] = None,
        row_marker_width: Optional[Union[Var[int], int]] = None,
        smooth_scroll_x: Optional[Union[Var[bool], bool]] = None,
        smooth_scroll_y: Optional[Union[Var[bool], bool]] = None,
        vertical_border: Optional[Union[Var[bool], bool]] = None,
        column_select: Optional[
            Union[
                Var[Literal["none", "single", "multi"]],
                Literal["none", "single", "multi"],
            ]
        ] = None,
        prevent_diagonal_scrolling: Optional[Union[Var[bool], bool]] = None,
        overscroll_x: Optional[Union[Var[int], int]] = None,
        overscroll_y: Optional[Union[Var[int], int]] = None,
        scroll_offset_x: Optional[Union[Var[int], int]] = None,
        scroll_offset_y: Optional[Union[Var[int], int]] = None,
        theme: Optional[
            Union[Var[Union[DataEditorTheme, Dict]], Union[DataEditorTheme, Dict]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_cell_activated: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_cell_clicked: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_cell_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_cell_edited: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_column_resize: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_delete: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_finished_editing: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_group_header_clicked: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_group_header_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_group_header_renamed: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_header_clicked: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_header_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_header_menu_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_item_hovered: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_row_appended: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_selection_cleared: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "DataEditor":
        """Create the DataEditor component.

        Args:
            *children: The children of the data editor.
            rows: Number of rows.
            columns: Headers of the columns for the data grid.
            data: The data.
            get_cell_content: The name of the callback used to find the data to display.
            get_cell_for_selection: Allow selection for copying.
            on_paste: Allow paste.
            draw_focus_ring: Controls the drawing of the focus ring.
            fixed_shadow_x: Enables or disables the overlay shadow when scrolling horizontally.
            fixed_shadow_y: Enables or disables the overlay shadow when scrolling vertically.
            freeze_columns: The number of columns which should remain in place when scrolling horizontally. Doesn't include rowMarkers.
            group_header_height: Controls the header of the group header row.
            header_height: Controls the height of the header row.
            max_column_auto_width: Additional header icons:  header_icons: Var[Any] # (TODO: must be a map of name: svg)  The maximum width a column can be automatically sized to.
            max_column_width: The maximum width a column can be resized to.
            min_column_width: The minimum width a column can be resized to.
            row_height: Determins the height of each row.
            row_markers: Kind of row markers.
            row_marker_start_index: Changes the starting index for row markers.
            row_marker_width: Sets the width of row markers in pixels, if unset row markers will automatically size.
            smooth_scroll_x: Enable horizontal smooth scrolling.
            smooth_scroll_y: Enable vertical smooth scrolling.
            vertical_border: Controls the drawing of the left hand vertical border of a column. If set to a boolean value it controls all borders.
            column_select: Allow columns selections. ("none", "single", "multi")
            prevent_diagonal_scrolling: Prevent diagonal scrolling.
            overscroll_x: Allow to scroll past the limit of the actual content on the horizontal axis.
            overscroll_y: Allow to scroll past the limit of the actual content on the vertical axis.
            scroll_offset_x: Initial scroll offset on the horizontal axis.
            scroll_offset_y: Initial scroll offset on the vertical axis.
            theme: global theme
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the data editor.

        Raises:
            ValueError: invalid input.

        Returns:
            The DataEditor component.&
        """
        ...

@serializer
def serialize_dataeditortheme(theme: DataEditorTheme): ...
