from typing import Union, ClassVar, Callable, List, Any, TypedDict, Optional


orientation_t = int
type_t = int
font_kerning_t = int
long_mode_t = int
text_align_t = int
align_t = int
opa_t = int
border_side_t = int
flag_t = int
grid_align_t = int
str_symbol_t = int
scrollbar_mode_t = int
draw_task_type_t = int
blur_quality_t = int
text_decor_t = int
palette_t = int
span_overflow_t = int
scroll_snap_t = int
gridnav_ctrl_t = int
dir_t = int
encoding_code128_t = int
state_t = int
indev_type_t = int
mode_t = int
grad_dir_t = int
base_dir_t = int
screen_load_anim_t = int
part_t = int
ctrl_t = int
indev_mode_t = int
fs_mode_t = int
color_format_t = int
display_render_mode_t = int
flags_t = int
group_refocus_policy_t = int
cover_res_t = int
span_mode_t = int
font_glyph_format_t = int
result_t = int
rb_color_t = int
flex_align_t = int
fs_res_t = int
indev_gesture_t = int
text_flag_t = int
style_state_cmp_t = int
flex_flow_t = int
display_rotation_t = int
indev_state_t = int
style_res_t = int
blend_mode_t = int
grad_extend_t = int
overflow_t = int
style_prop_t = int
grad_color_t = int
event_code_t = int
style_selector_t = int
anim_enable_t = int
event_list_t = int
ll_node_t = int
value_precise_t = float
fs_whence_t = int
screen_load_anim_t = int
_mp_int_wrapper = int

event_cb_t = Callable
group_edge_cb_t = Callable
group_focus_cb_t = Callable
indev_read_cb_t = Callable
anim_exec_xcb_t = Callable
cache_compare_cb_t = Callable
rb_compare_t = Callable
draw_buf_malloc_cb = Callable
draw_buf_free_cb = Callable
draw_buf_align_cb = Callable
draw_buf_invalidate_cache_cb = Callable
draw_buf_width_to_stride_cb = Callable
draw_glyph_cb_t = Callable
timer_handler_resume_cb_t = Callable
delay_cb_t = Callable
tick_get_cb_t = Callable


class _draw_sw_mask_radius_circle_dsc_t(object):
   ...


class _draw_sw_mask_common_dsc_t(object):
   ...


class mutex_t(object):
   ...


class thread_sync_t(object):
   ...


class thread_t(object):
   ... 
   

class mem_pool_t(object):
    ...


DPI_DEF: int = ...
DRAW_BUF_STRIDE_ALIGN: int = ...
DRAW_BUF_ALIGN: int = ...
ANIM_REPEAT_INFINITE: int = ...
ANIM_PLAYTIME_INFINITE: int = ...
SIZE_CONTENT: int = ...
COLOR_DEPTH: int = ...
IMAGE_HEADER_MAGIC: int = ...
STRIDE_AUTO: int = ...
GRID_CONTENT: int = ...
GRID_TEMPLATE_LAST: int = ...
SCALE_NONE: int = ...
RADIUS_CIRCLE: int = ...
LABEL_DOT_NUM: int = ...
LABEL_POS_LAST: int = ...
LABEL_TEXT_SELECTION_OFF: int = ...
BUTTONMATRIX_BUTTON_NONE: int = ...
CHART_POINT_NONE: int = ...
DROPDOWN_POS_LAST: int = ...
SCALE_TOTAL_TICK_COUNT_DEFAULT: int = ...
SCALE_MAJOR_TICK_EVERY_DEFAULT: int = ...
SCALE_LABEL_ENABLED_DEFAULT: int = ...
SCALE_LABEL_ROTATE_MATCH_TICKS: int = ...
SCALE_LABEL_ROTATE_KEEP_UPRIGHT: int = ...
SCALE_ROTATION_ANGLE_MASK: int = ...
TEXTAREA_CURSOR_LAST: int = ...
PART_TEXTAREA_PLACEHOLDER: int = ...
TABLE_CELL_NONE: int = ...


class LOG_LEVEL(object):
    """
    No Docstrings Yet
    """
    TRACE: ClassVar[int] = ...
    INFO: ClassVar[int] = ...
    WARN: ClassVar[int] = ...
    ERROR: ClassVar[int] = ...
    USER: ClassVar[int] = ...
    NONE: ClassVar[int] = ...


class COORD(object):
    """
    No Docstrings Yet
    """
    MAX: ClassVar[int] = ...
    MIN: ClassVar[int] = ...


class OPA(object):
    """
    No Docstrings Yet
    """
    TRANSP: ClassVar[int] = ...
    _0: ClassVar[int] = ...
    _10: ClassVar[int] = ...
    _20: ClassVar[int] = ...
    _30: ClassVar[int] = ...
    _40: ClassVar[int] = ...
    _50: ClassVar[int] = ...
    _60: ClassVar[int] = ...
    _70: ClassVar[int] = ...
    _80: ClassVar[int] = ...
    _90: ClassVar[int] = ...
    _100: ClassVar[int] = ...
    COVER: ClassVar[int] = ...


class TREE_WALK(object):
    """
    No Docstrings Yet
    """
    PRE_ORDER: ClassVar[int] = ...
    POST_ORDER: ClassVar[int] = ...


class STR_SYMBOL(object):
    """
    No Docstrings Yet
    """
    BULLET: ClassVar[int] = ...
    AUDIO: ClassVar[int] = ...
    VIDEO: ClassVar[int] = ...
    LIST: ClassVar[int] = ...
    OK: ClassVar[int] = ...
    CLOSE: ClassVar[int] = ...
    POWER: ClassVar[int] = ...
    SETTINGS: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    DOWNLOAD: ClassVar[int] = ...
    DRIVE: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    MUTE: ClassVar[int] = ...
    VOLUME_MID: ClassVar[int] = ...
    VOLUME_MAX: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    TINT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    PLAY: ClassVar[int] = ...
    PAUSE: ClassVar[int] = ...
    STOP: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    EJECT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    PLUS: ClassVar[int] = ...
    MINUS: ClassVar[int] = ...
    EYE_OPEN: ClassVar[int] = ...
    EYE_CLOSE: ClassVar[int] = ...
    WARNING: ClassVar[int] = ...
    SHUFFLE: ClassVar[int] = ...
    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    LOOP: ClassVar[int] = ...
    DIRECTORY: ClassVar[int] = ...
    UPLOAD: ClassVar[int] = ...
    CALL: ClassVar[int] = ...
    CUT: ClassVar[int] = ...
    COPY: ClassVar[int] = ...
    SAVE: ClassVar[int] = ...
    BARS: ClassVar[int] = ...
    ENVELOPE: ClassVar[int] = ...
    CHARGE: ClassVar[int] = ...
    PASTE: ClassVar[int] = ...
    BELL: ClassVar[int] = ...
    KEYBOARD: ClassVar[int] = ...
    GPS: ClassVar[int] = ...
    FILE: ClassVar[int] = ...
    WIFI: ClassVar[int] = ...
    BATTERY_FULL: ClassVar[int] = ...
    BATTERY_3: ClassVar[int] = ...
    BATTERY_2: ClassVar[int] = ...
    BATTERY_1: ClassVar[int] = ...
    BATTERY_EMPTY: ClassVar[int] = ...
    USB: ClassVar[int] = ...
    BLUETOOTH: ClassVar[int] = ...
    TRASH: ClassVar[int] = ...
    EDIT: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    SD_CARD: ClassVar[int] = ...
    NEW_LINE: ClassVar[int] = ...
    DUMMY: ClassVar[int] = ...


class STYLE(object):
    """
    No Docstrings Yet
    """
    PROP_INV: ClassVar[int] = ...
    WIDTH: ClassVar[int] = ...
    HEIGHT: ClassVar[int] = ...
    LENGTH: ClassVar[int] = ...
    TRANSFORM_WIDTH: ClassVar[int] = ...
    TRANSFORM_HEIGHT: ClassVar[int] = ...
    MIN_WIDTH: ClassVar[int] = ...
    MAX_WIDTH: ClassVar[int] = ...
    MIN_HEIGHT: ClassVar[int] = ...
    MAX_HEIGHT: ClassVar[int] = ...
    TRANSLATE_X: ClassVar[int] = ...
    TRANSLATE_Y: ClassVar[int] = ...
    RADIAL_OFFSET: ClassVar[int] = ...
    X: ClassVar[int] = ...
    Y: ClassVar[int] = ...
    ALIGN: ClassVar[int] = ...
    PAD_TOP: ClassVar[int] = ...
    PAD_BOTTOM: ClassVar[int] = ...
    PAD_LEFT: ClassVar[int] = ...
    PAD_RIGHT: ClassVar[int] = ...
    PAD_RADIAL: ClassVar[int] = ...
    PAD_ROW: ClassVar[int] = ...
    PAD_COLUMN: ClassVar[int] = ...
    MARGIN_TOP: ClassVar[int] = ...
    MARGIN_BOTTOM: ClassVar[int] = ...
    MARGIN_LEFT: ClassVar[int] = ...
    MARGIN_RIGHT: ClassVar[int] = ...
    BG_GRAD: ClassVar[int] = ...
    BG_GRAD_DIR: ClassVar[int] = ...
    BG_MAIN_OPA: ClassVar[int] = ...
    BG_GRAD_OPA: ClassVar[int] = ...
    BG_GRAD_COLOR: ClassVar[int] = ...
    BG_MAIN_STOP: ClassVar[int] = ...
    BG_GRAD_STOP: ClassVar[int] = ...
    BG_IMAGE_SRC: ClassVar[int] = ...
    BG_IMAGE_OPA: ClassVar[int] = ...
    BG_IMAGE_RECOLOR_OPA: ClassVar[int] = ...
    BG_IMAGE_TILED: ClassVar[int] = ...
    BG_IMAGE_RECOLOR: ClassVar[int] = ...
    BORDER_WIDTH: ClassVar[int] = ...
    BORDER_COLOR: ClassVar[int] = ...
    BORDER_OPA: ClassVar[int] = ...
    BORDER_POST: ClassVar[int] = ...
    BORDER_SIDE: ClassVar[int] = ...
    OUTLINE_WIDTH: ClassVar[int] = ...
    OUTLINE_COLOR: ClassVar[int] = ...
    OUTLINE_OPA: ClassVar[int] = ...
    OUTLINE_PAD: ClassVar[int] = ...
    BG_OPA: ClassVar[int] = ...
    BG_COLOR: ClassVar[int] = ...
    SHADOW_WIDTH: ClassVar[int] = ...
    LINE_WIDTH: ClassVar[int] = ...
    ARC_WIDTH: ClassVar[int] = ...
    TEXT_FONT: ClassVar[int] = ...
    IMAGE_RECOLOR_OPA: ClassVar[int] = ...
    IMAGE_OPA: ClassVar[int] = ...
    SHADOW_OPA: ClassVar[int] = ...
    LINE_OPA: ClassVar[int] = ...
    ARC_OPA: ClassVar[int] = ...
    TEXT_OPA: ClassVar[int] = ...
    SHADOW_COLOR: ClassVar[int] = ...
    IMAGE_RECOLOR: ClassVar[int] = ...
    LINE_COLOR: ClassVar[int] = ...
    ARC_COLOR: ClassVar[int] = ...
    TEXT_COLOR: ClassVar[int] = ...
    ARC_IMAGE_SRC: ClassVar[int] = ...
    SHADOW_OFFSET_X: ClassVar[int] = ...
    SHADOW_OFFSET_Y: ClassVar[int] = ...
    SHADOW_SPREAD: ClassVar[int] = ...
    LINE_DASH_WIDTH: ClassVar[int] = ...
    TEXT_ALIGN: ClassVar[int] = ...
    TEXT_LETTER_SPACE: ClassVar[int] = ...
    TEXT_LINE_SPACE: ClassVar[int] = ...
    LINE_DASH_GAP: ClassVar[int] = ...
    LINE_ROUNDED: ClassVar[int] = ...
    IMAGE_COLORKEY: ClassVar[int] = ...
    TEXT_OUTLINE_STROKE_WIDTH: ClassVar[int] = ...
    TEXT_OUTLINE_STROKE_OPA: ClassVar[int] = ...
    TEXT_OUTLINE_STROKE_COLOR: ClassVar[int] = ...
    TEXT_DECOR: ClassVar[int] = ...
    ARC_ROUNDED: ClassVar[int] = ...
    OPA: ClassVar[int] = ...
    OPA_LAYERED: ClassVar[int] = ...
    COLOR_FILTER_DSC: ClassVar[int] = ...
    COLOR_FILTER_OPA: ClassVar[int] = ...
    ANIM: ClassVar[int] = ...
    ANIM_DURATION: ClassVar[int] = ...
    TRANSITION: ClassVar[int] = ...
    RADIUS: ClassVar[int] = ...
    BITMAP_MASK_SRC: ClassVar[int] = ...
    BLEND_MODE: ClassVar[int] = ...
    ROTARY_SENSITIVITY: ClassVar[int] = ...
    TRANSLATE_RADIAL: ClassVar[int] = ...
    CLIP_CORNER: ClassVar[int] = ...
    BASE_DIR: ClassVar[int] = ...
    RECOLOR: ClassVar[int] = ...
    RECOLOR_OPA: ClassVar[int] = ...
    LAYOUT: ClassVar[int] = ...
    BLUR_RADIUS: ClassVar[int] = ...
    BLUR_BACKDROP: ClassVar[int] = ...
    BLUR_QUALITY: ClassVar[int] = ...
    DROP_SHADOW_RADIUS: ClassVar[int] = ...
    DROP_SHADOW_OFFSET_X: ClassVar[int] = ...
    DROP_SHADOW_OFFSET_Y: ClassVar[int] = ...
    DROP_SHADOW_COLOR: ClassVar[int] = ...
    DROP_SHADOW_OPA: ClassVar[int] = ...
    DROP_SHADOW_QUALITY: ClassVar[int] = ...
    TRANSFORM_SCALE_X: ClassVar[int] = ...
    TRANSFORM_SCALE_Y: ClassVar[int] = ...
    TRANSFORM_PIVOT_X: ClassVar[int] = ...
    TRANSFORM_PIVOT_Y: ClassVar[int] = ...
    TRANSFORM_ROTATION: ClassVar[int] = ...
    TRANSFORM_SKEW_X: ClassVar[int] = ...
    TRANSFORM_SKEW_Y: ClassVar[int] = ...
    FLEX_FLOW: ClassVar[int] = ...
    FLEX_MAIN_PLACE: ClassVar[int] = ...
    FLEX_CROSS_PLACE: ClassVar[int] = ...
    FLEX_TRACK_PLACE: ClassVar[int] = ...
    FLEX_GROW: ClassVar[int] = ...
    GRID_COLUMN_DSC_ARRAY: ClassVar[int] = ...
    GRID_ROW_DSC_ARRAY: ClassVar[int] = ...
    GRID_COLUMN_ALIGN: ClassVar[int] = ...
    GRID_ROW_ALIGN: ClassVar[int] = ...
    GRID_CELL_COLUMN_POS: ClassVar[int] = ...
    GRID_CELL_COLUMN_SPAN: ClassVar[int] = ...
    GRID_CELL_X_ALIGN: ClassVar[int] = ...
    GRID_CELL_ROW_POS: ClassVar[int] = ...
    GRID_CELL_ROW_SPAN: ClassVar[int] = ...
    GRID_CELL_Y_ALIGN: ClassVar[int] = ...
    LAST_BUILT_IN_PROP: ClassVar[int] = ...
    NUM_BUILT_IN_PROPS: ClassVar[int] = ...
    PROP_ANY: ClassVar[int] = ...
    PROP_CONST: ClassVar[int] = ...


class RESULT(object):
    """
    No Docstrings Yet
    """
    INVALID: ClassVar[int] = ...
    OK: ClassVar[int] = ...


class RB_COLOR(object):
    """
    No Docstrings Yet
    """
    RED: ClassVar[int] = ...
    BLACK: ClassVar[int] = ...


class ALIGN(object):
    """
    No Docstrings Yet
    """
    DEFAULT: ClassVar[int] = ...
    TOP_LEFT: ClassVar[int] = ...
    TOP_MID: ClassVar[int] = ...
    TOP_RIGHT: ClassVar[int] = ...
    BOTTOM_LEFT: ClassVar[int] = ...
    BOTTOM_MID: ClassVar[int] = ...
    BOTTOM_RIGHT: ClassVar[int] = ...
    LEFT_MID: ClassVar[int] = ...
    RIGHT_MID: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    OUT_TOP_LEFT: ClassVar[int] = ...
    OUT_TOP_MID: ClassVar[int] = ...
    OUT_TOP_RIGHT: ClassVar[int] = ...
    OUT_BOTTOM_LEFT: ClassVar[int] = ...
    OUT_BOTTOM_MID: ClassVar[int] = ...
    OUT_BOTTOM_RIGHT: ClassVar[int] = ...
    OUT_LEFT_TOP: ClassVar[int] = ...
    OUT_LEFT_MID: ClassVar[int] = ...
    OUT_LEFT_BOTTOM: ClassVar[int] = ...
    OUT_RIGHT_TOP: ClassVar[int] = ...
    OUT_RIGHT_MID: ClassVar[int] = ...
    OUT_RIGHT_BOTTOM: ClassVar[int] = ...


class DIR(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    ALL: ClassVar[int] = ...


class COLOR_FORMAT(object):
    """
    No Docstrings Yet
    """
    UNKNOWN: ClassVar[int] = ...
    RAW: ClassVar[int] = ...
    RAW_ALPHA: ClassVar[int] = ...
    L8: ClassVar[int] = ...
    I1: ClassVar[int] = ...
    I2: ClassVar[int] = ...
    I4: ClassVar[int] = ...
    I8: ClassVar[int] = ...
    A8: ClassVar[int] = ...
    RGB565: ClassVar[int] = ...
    ARGB8565: ClassVar[int] = ...
    RGB565A8: ClassVar[int] = ...
    AL88: ClassVar[int] = ...
    RGB565_SWAPPED: ClassVar[int] = ...
    RGB888: ClassVar[int] = ...
    ARGB8888: ClassVar[int] = ...
    XRGB8888: ClassVar[int] = ...
    ARGB8888_PREMULTIPLIED: ClassVar[int] = ...
    A1: ClassVar[int] = ...
    A2: ClassVar[int] = ...
    A4: ClassVar[int] = ...
    ARGB1555: ClassVar[int] = ...
    ARGB4444: ClassVar[int] = ...
    ARGB2222: ClassVar[int] = ...
    YUV_START: ClassVar[int] = ...
    I420: ClassVar[int] = ...
    I422: ClassVar[int] = ...
    I444: ClassVar[int] = ...
    I400: ClassVar[int] = ...
    NV21: ClassVar[int] = ...
    NV12: ClassVar[int] = ...
    YUY2: ClassVar[int] = ...
    UYVY: ClassVar[int] = ...
    YUV_END: ClassVar[int] = ...
    PROPRIETARY_START: ClassVar[int] = ...
    NEMA_TSC_START: ClassVar[int] = ...
    NEMA_TSC4: ClassVar[int] = ...
    NEMA_TSC6: ClassVar[int] = ...
    NEMA_TSC6A: ClassVar[int] = ...
    NEMA_TSC6AP: ClassVar[int] = ...
    NEMA_TSC12: ClassVar[int] = ...
    NEMA_TSC12A: ClassVar[int] = ...
    NEMA_TSC_END: ClassVar[int] = ...
    NATIVE: ClassVar[int] = ...
    NATIVE_WITH_ALPHA: ClassVar[int] = ...


class PALETTE(object):
    """
    No Docstrings Yet
    """
    RED: ClassVar[int] = ...
    PINK: ClassVar[int] = ...
    PURPLE: ClassVar[int] = ...
    DEEP_PURPLE: ClassVar[int] = ...
    INDIGO: ClassVar[int] = ...
    BLUE: ClassVar[int] = ...
    LIGHT_BLUE: ClassVar[int] = ...
    CYAN: ClassVar[int] = ...
    TEAL: ClassVar[int] = ...
    GREEN: ClassVar[int] = ...
    LIGHT_GREEN: ClassVar[int] = ...
    LIME: ClassVar[int] = ...
    YELLOW: ClassVar[int] = ...
    AMBER: ClassVar[int] = ...
    ORANGE: ClassVar[int] = ...
    DEEP_ORANGE: ClassVar[int] = ...
    BROWN: ClassVar[int] = ...
    BLUE_GREY: ClassVar[int] = ...
    GREY: ClassVar[int] = ...
    LAST: ClassVar[int] = ...
    NONE: ClassVar[int] = ...


class FONT_GLYPH_FORMAT(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    A1: ClassVar[int] = ...
    A2: ClassVar[int] = ...
    A3: ClassVar[int] = ...
    A4: ClassVar[int] = ...
    A8: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    VECTOR: ClassVar[int] = ...
    SVG: ClassVar[int] = ...
    CUSTOM: ClassVar[int] = ...


class FONT_SUBPX(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    BOTH: ClassVar[int] = ...


class FONT_KERNING(object):
    """
    No Docstrings Yet
    """
    NORMAL: ClassVar[int] = ...
    NONE: ClassVar[int] = ...


class TEXT_FLAG(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    EXPAND: ClassVar[int] = ...
    FIT: ClassVar[int] = ...
    BREAK_ALL: ClassVar[int] = ...
    RECOLOR: ClassVar[int] = ...


class TEXT_ALIGN(object):
    """
    No Docstrings Yet
    """
    AUTO: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...


class BASE_DIR(object):
    """
    No Docstrings Yet
    """
    LTR: ClassVar[int] = ...
    RTL: ClassVar[int] = ...
    AUTO: ClassVar[int] = ...
    NEUTRAL: ClassVar[int] = ...
    WEAK: ClassVar[int] = ...


class GRAD_DIR(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    LINEAR: ClassVar[int] = ...
    RADIAL: ClassVar[int] = ...
    CONICAL: ClassVar[int] = ...


class GRAD_EXTEND(object):
    """
    No Docstrings Yet
    """
    PAD: ClassVar[int] = ...
    REPEAT: ClassVar[int] = ...
    REFLECT: ClassVar[int] = ...


class LAYOUT(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    FLEX: ClassVar[int] = ...
    GRID: ClassVar[int] = ...
    LAST: ClassVar[int] = ...


class FLEX_ALIGN(object):
    """
    No Docstrings Yet
    """
    START: ClassVar[int] = ...
    END: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    SPACE_EVENLY: ClassVar[int] = ...
    SPACE_AROUND: ClassVar[int] = ...
    SPACE_BETWEEN: ClassVar[int] = ...


class FLEX_FLOW(object):
    """
    No Docstrings Yet
    """
    ROW: ClassVar[int] = ...
    COLUMN: ClassVar[int] = ...
    ROW_WRAP: ClassVar[int] = ...
    ROW_REVERSE: ClassVar[int] = ...
    ROW_WRAP_REVERSE: ClassVar[int] = ...
    COLUMN_WRAP: ClassVar[int] = ...
    COLUMN_REVERSE: ClassVar[int] = ...
    COLUMN_WRAP_REVERSE: ClassVar[int] = ...


class GRID_ALIGN(object):
    """
    No Docstrings Yet
    """
    START: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    END: ClassVar[int] = ...
    STRETCH: ClassVar[int] = ...
    SPACE_EVENLY: ClassVar[int] = ...
    SPACE_AROUND: ClassVar[int] = ...
    SPACE_BETWEEN: ClassVar[int] = ...


class BLEND_MODE(object):
    """
    No Docstrings Yet
    """
    NORMAL: ClassVar[int] = ...
    ADDITIVE: ClassVar[int] = ...
    SUBTRACTIVE: ClassVar[int] = ...
    MULTIPLY: ClassVar[int] = ...
    DIFFERENCE: ClassVar[int] = ...


class TEXT_DECOR(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    UNDERLINE: ClassVar[int] = ...
    STRIKETHROUGH: ClassVar[int] = ...


class BORDER_SIDE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    FULL: ClassVar[int] = ...
    INTERNAL: ClassVar[int] = ...


class BLUR_QUALITY(object):
    """
    No Docstrings Yet
    """
    AUTO: ClassVar[int] = ...
    SPEED: ClassVar[int] = ...
    PRECISION: ClassVar[int] = ...


class STYLE_RES(object):
    """
    No Docstrings Yet
    """
    NOT_FOUND: ClassVar[int] = ...
    FOUND: ClassVar[int] = ...


class EVENT(object):
    """
    No Docstrings Yet
    """
    ALL: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...
    PRESSING: ClassVar[int] = ...
    PRESS_LOST: ClassVar[int] = ...
    SHORT_CLICKED: ClassVar[int] = ...
    SINGLE_CLICKED: ClassVar[int] = ...
    DOUBLE_CLICKED: ClassVar[int] = ...
    TRIPLE_CLICKED: ClassVar[int] = ...
    LONG_PRESSED: ClassVar[int] = ...
    LONG_PRESSED_REPEAT: ClassVar[int] = ...
    CLICKED: ClassVar[int] = ...
    RELEASED: ClassVar[int] = ...
    SCROLL_BEGIN: ClassVar[int] = ...
    SCROLL_THROW_BEGIN: ClassVar[int] = ...
    SCROLL_END: ClassVar[int] = ...
    SCROLL: ClassVar[int] = ...
    GESTURE: ClassVar[int] = ...
    KEY: ClassVar[int] = ...
    ROTARY: ClassVar[int] = ...
    FOCUSED: ClassVar[int] = ...
    DEFOCUSED: ClassVar[int] = ...
    LEAVE: ClassVar[int] = ...
    HIT_TEST: ClassVar[int] = ...
    INDEV_RESET: ClassVar[int] = ...
    HOVER_OVER: ClassVar[int] = ...
    HOVER_LEAVE: ClassVar[int] = ...
    COVER_CHECK: ClassVar[int] = ...
    REFR_EXT_DRAW_SIZE: ClassVar[int] = ...
    DRAW_MAIN_BEGIN: ClassVar[int] = ...
    DRAW_MAIN: ClassVar[int] = ...
    DRAW_MAIN_END: ClassVar[int] = ...
    DRAW_POST_BEGIN: ClassVar[int] = ...
    DRAW_POST: ClassVar[int] = ...
    DRAW_POST_END: ClassVar[int] = ...
    DRAW_TASK_ADDED: ClassVar[int] = ...
    VALUE_CHANGED: ClassVar[int] = ...
    INSERT: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    READY: ClassVar[int] = ...
    CANCEL: ClassVar[int] = ...
    STATE_CHANGED: ClassVar[int] = ...
    CREATE: ClassVar[int] = ...
    DELETE: ClassVar[int] = ...
    CHILD_CHANGED: ClassVar[int] = ...
    CHILD_CREATED: ClassVar[int] = ...
    CHILD_DELETED: ClassVar[int] = ...
    SCREEN_UNLOAD_START: ClassVar[int] = ...
    SCREEN_LOAD_START: ClassVar[int] = ...
    SCREEN_LOADED: ClassVar[int] = ...
    SCREEN_UNLOADED: ClassVar[int] = ...
    SIZE_CHANGED: ClassVar[int] = ...
    STYLE_CHANGED: ClassVar[int] = ...
    LAYOUT_CHANGED: ClassVar[int] = ...
    GET_SELF_SIZE: ClassVar[int] = ...
    INVALIDATE_AREA: ClassVar[int] = ...
    RESOLUTION_CHANGED: ClassVar[int] = ...
    COLOR_FORMAT_CHANGED: ClassVar[int] = ...
    REFR_REQUEST: ClassVar[int] = ...
    REFR_START: ClassVar[int] = ...
    REFR_READY: ClassVar[int] = ...
    RENDER_START: ClassVar[int] = ...
    RENDER_READY: ClassVar[int] = ...
    FLUSH_START: ClassVar[int] = ...
    FLUSH_FINISH: ClassVar[int] = ...
    FLUSH_WAIT_START: ClassVar[int] = ...
    FLUSH_WAIT_FINISH: ClassVar[int] = ...
    UPDATE_LAYOUT_COMPLETED: ClassVar[int] = ...
    VSYNC: ClassVar[int] = ...
    VSYNC_REQUEST: ClassVar[int] = ...
    LAST: ClassVar[int] = ...
    PREPROCESS: ClassVar[int] = ...
    MARKED_DELETING: ClassVar[int] = ...


class DISPLAY_ROTATION(object):
    """
    No Docstrings Yet
    """
    _0: ClassVar[int] = ...
    _90: ClassVar[int] = ...
    _180: ClassVar[int] = ...
    _270: ClassVar[int] = ...


class DISPLAY_RENDER_MODE(object):
    """
    No Docstrings Yet
    """
    PARTIAL: ClassVar[int] = ...
    DIRECT: ClassVar[int] = ...
    FULL: ClassVar[int] = ...


class SCREEN_LOAD_ANIM(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    OVER_LEFT: ClassVar[int] = ...
    OVER_RIGHT: ClassVar[int] = ...
    OVER_TOP: ClassVar[int] = ...
    OVER_BOTTOM: ClassVar[int] = ...
    MOVE_LEFT: ClassVar[int] = ...
    MOVE_RIGHT: ClassVar[int] = ...
    MOVE_TOP: ClassVar[int] = ...
    MOVE_BOTTOM: ClassVar[int] = ...
    FADE_IN: ClassVar[int] = ...
    FADE_ON: ClassVar[int] = ...
    FADE_OUT: ClassVar[int] = ...
    OUT_LEFT: ClassVar[int] = ...
    OUT_RIGHT: ClassVar[int] = ...
    OUT_TOP: ClassVar[int] = ...
    OUT_BOTTOM: ClassVar[int] = ...


class SCROLLBAR_MODE(object):
    """
    No Docstrings Yet
    """
    OFF: ClassVar[int] = ...
    ON: ClassVar[int] = ...
    ACTIVE: ClassVar[int] = ...
    AUTO: ClassVar[int] = ...


class SCROLL_SNAP(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    START: ClassVar[int] = ...
    END: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...


class STATE(object):
    """
    No Docstrings Yet
    """
    DEFAULT: ClassVar[int] = ...
    ALT: ClassVar[int] = ...
    CHECKED: ClassVar[int] = ...
    FOCUSED: ClassVar[int] = ...
    FOCUS_KEY: ClassVar[int] = ...
    EDITED: ClassVar[int] = ...
    HOVERED: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...
    SCROLLED: ClassVar[int] = ...
    DISABLED: ClassVar[int] = ...
    USER_1: ClassVar[int] = ...
    USER_2: ClassVar[int] = ...
    USER_3: ClassVar[int] = ...
    USER_4: ClassVar[int] = ...
    ANY: ClassVar[int] = ...


class PART(object):
    """
    No Docstrings Yet
    """
    MAIN: ClassVar[int] = ...
    SCROLLBAR: ClassVar[int] = ...
    INDICATOR: ClassVar[int] = ...
    KNOB: ClassVar[int] = ...
    SELECTED: ClassVar[int] = ...
    ITEMS: ClassVar[int] = ...
    CURSOR: ClassVar[int] = ...
    CUSTOM_FIRST: ClassVar[int] = ...
    ANY: ClassVar[int] = ...


class STYLE_STATE_CMP(object):
    """
    No Docstrings Yet
    """
    SAME: ClassVar[int] = ...
    DIFF_REDRAW: ClassVar[int] = ...
    DIFF_DRAW_PAD: ClassVar[int] = ...
    DIFF_LAYOUT: ClassVar[int] = ...


class FS_RES(object):
    """
    No Docstrings Yet
    """
    OK: ClassVar[int] = ...
    HW_ERR: ClassVar[int] = ...
    FS_ERR: ClassVar[int] = ...
    NOT_EX: ClassVar[int] = ...
    FULL: ClassVar[int] = ...
    LOCKED: ClassVar[int] = ...
    DENIED: ClassVar[int] = ...
    BUSY: ClassVar[int] = ...
    TOUT: ClassVar[int] = ...
    NOT_IMP: ClassVar[int] = ...
    OUT_OF_MEM: ClassVar[int] = ...
    INV_PARAM: ClassVar[int] = ...
    DRIVE_LETTER_ALREADY_USED: ClassVar[int] = ...
    UNKNOWN: ClassVar[int] = ...


class FS_MODE(object):
    """
    No Docstrings Yet
    """
    WR: ClassVar[int] = ...
    RD: ClassVar[int] = ...


class FS_SEEK(object):
    """
    No Docstrings Yet
    """
    SET: ClassVar[int] = ...
    CUR: ClassVar[int] = ...
    END: ClassVar[int] = ...


class DRAW_TASK_TYPE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    FILL: ClassVar[int] = ...
    BORDER: ClassVar[int] = ...
    BOX_SHADOW: ClassVar[int] = ...
    LETTER: ClassVar[int] = ...
    LABEL: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    LAYER: ClassVar[int] = ...
    LINE: ClassVar[int] = ...
    ARC: ClassVar[int] = ...
    TRIANGLE: ClassVar[int] = ...
    MASK_RECTANGLE: ClassVar[int] = ...
    MASK_BITMAP: ClassVar[int] = ...
    BLUR: ClassVar[int] = ...


class DRAW_TASK_STATE(object):
    """
    No Docstrings Yet
    """
    BLOCKED: ClassVar[int] = ...
    WAITING: ClassVar[int] = ...
    QUEUED: ClassVar[int] = ...
    IN_PROGRESS: ClassVar[int] = ...
    FINISHED: ClassVar[int] = ...


class LAYER_TYPE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    SIMPLE: ClassVar[int] = ...
    TRANSFORM: ClassVar[int] = ...


class KEY(object):
    """
    No Docstrings Yet
    """
    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    ESC: ClassVar[int] = ...
    DEL: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    ENTER: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    END: ClassVar[int] = ...


class GROUP_REFOCUS_POLICY(object):
    """
    No Docstrings Yet
    """
    NEXT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...


class INDEV_TYPE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    POINTER: ClassVar[int] = ...
    KEYPAD: ClassVar[int] = ...
    BUTTON: ClassVar[int] = ...
    ENCODER: ClassVar[int] = ...


class INDEV_STATE(object):
    """
    No Docstrings Yet
    """
    RELEASED: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...


class INDEV_MODE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    TIMER: ClassVar[int] = ...
    EVENT: ClassVar[int] = ...


class INDEV_GESTURE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    PINCH: ClassVar[int] = ...
    SWIPE: ClassVar[int] = ...
    ROTATE: ClassVar[int] = ...
    TWO_FINGERS_SWIPE: ClassVar[int] = ...
    SCROLL: ClassVar[int] = ...
    CNT: ClassVar[int] = ...


class COVER_RES(object):
    """
    No Docstrings Yet
    """
    COVER: ClassVar[int] = ...
    NOT_COVER: ClassVar[int] = ...
    MASKED: ClassVar[int] = ...


class SUBJECT_TYPE(object):
    """
    No Docstrings Yet
    """
    INVALID: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    INT: ClassVar[int] = ...
    FLOAT: ClassVar[int] = ...
    POINTER: ClassVar[int] = ...
    COLOR: ClassVar[int] = ...
    GROUP: ClassVar[int] = ...
    STRING: ClassVar[int] = ...


class GRIDNAV_CTRL(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    ROLLOVER: ClassVar[int] = ...
    SCROLL_FIRST: ClassVar[int] = ...
    HORIZONTAL_MOVE_ONLY: ClassVar[int] = ...
    VERTICAL_MOVE_ONLY: ClassVar[int] = ...


class FONT_FMT_TXT_CMAP(object):
    """
    No Docstrings Yet
    """
    FORMAT0_FULL: ClassVar[int] = ...
    SPARSE_FULL: ClassVar[int] = ...
    FORMAT0_TINY: ClassVar[int] = ...
    SPARSE_TINY: ClassVar[int] = ...


class FONT_FMT_TXT(object):
    """
    No Docstrings Yet
    """
    PLAIN: ClassVar[int] = ...
    COMPRESSED: ClassVar[int] = ...
    COMPRESSED_NO_PREFILTER: ClassVar[int] = ...


class ANIM_IMAGE_PART(object):
    """
    No Docstrings Yet
    """
    MAIN: ClassVar[int] = ...


class SPAN_OVERFLOW(object):
    """
    No Docstrings Yet
    """
    CLIP: ClassVar[int] = ...
    ELLIPSIS: ClassVar[int] = ...
    LAST: ClassVar[int] = ...


class SPAN_MODE(object):
    """
    No Docstrings Yet
    """
    FIXED: ClassVar[int] = ...
    EXPAND: ClassVar[int] = ...
    BREAK: ClassVar[int] = ...
    LAST: ClassVar[int] = ...


class SYMBOL(object):
    """
    No Docstrings Yet
    """
    BULLET: ClassVar[int] = ...
    AUDIO: ClassVar[int] = ...
    VIDEO: ClassVar[int] = ...
    LIST: ClassVar[int] = ...
    OK: ClassVar[int] = ...
    CLOSE: ClassVar[int] = ...
    POWER: ClassVar[int] = ...
    SETTINGS: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    DOWNLOAD: ClassVar[int] = ...
    DRIVE: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    MUTE: ClassVar[int] = ...
    VOLUME_MID: ClassVar[int] = ...
    VOLUME_MAX: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    TINT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    PLAY: ClassVar[int] = ...
    PAUSE: ClassVar[int] = ...
    STOP: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    EJECT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    PLUS: ClassVar[int] = ...
    MINUS: ClassVar[int] = ...
    EYE_OPEN: ClassVar[int] = ...
    EYE_CLOSE: ClassVar[int] = ...
    WARNING: ClassVar[int] = ...
    SHUFFLE: ClassVar[int] = ...
    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    LOOP: ClassVar[int] = ...
    DIRECTORY: ClassVar[int] = ...
    UPLOAD: ClassVar[int] = ...
    CALL: ClassVar[int] = ...
    CUT: ClassVar[int] = ...
    COPY: ClassVar[int] = ...
    SAVE: ClassVar[int] = ...
    BARS: ClassVar[int] = ...
    ENVELOPE: ClassVar[int] = ...
    CHARGE: ClassVar[int] = ...
    PASTE: ClassVar[int] = ...
    BELL: ClassVar[int] = ...
    KEYBOARD: ClassVar[int] = ...
    GPS: ClassVar[int] = ...
    FILE: ClassVar[int] = ...
    WIFI: ClassVar[int] = ...
    BATTERY_FULL: ClassVar[int] = ...
    BATTERY_3: ClassVar[int] = ...
    BATTERY_2: ClassVar[int] = ...
    BATTERY_1: ClassVar[int] = ...
    BATTERY_EMPTY: ClassVar[int] = ...
    USB: ClassVar[int] = ...
    BLUETOOTH: ClassVar[int] = ...
    TRASH: ClassVar[int] = ...
    EDIT: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    SD_CARD: ClassVar[int] = ...
    NEW_LINE: ClassVar[int] = ...
    DUMMY: ClassVar[int] = ...




class _C_Pointer_type(TypedDict, total=False):
    ptr_val: Any = ...
    str_val: str = ...
    int_val: int = ...
    uint_val: int = ...



class C_Pointer(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_C_Pointer_type] = dict(), /) -> "C_Pointer":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def ptr_val(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @ptr_val.setter
    def ptr_val(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def str_val(self) -> str:
       """
       No Docstrings Yet
       """ 
       ...

    @str_val.setter
    def str_val(self, value: str) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def int_val(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @int_val.setter
    def int_val(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def uint_val(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @uint_val.setter
    def uint_val(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _color_t_type(TypedDict, total=False):
    blue: int = ...
    green: int = ...
    red: int = ...



class color_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_color_t_type] = dict(), /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def is_in_range(self, l_color: "color_t", h_color: "color_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def to_32(self, opa: "opa_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...
    
    def to_int(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def eq(self, c2: "color_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def to_u16(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def to_u32(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def lighten(self, lvl: "opa_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def darken(self, lvl: "opa_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def to_hsv(self, /) -> "color_hsv_t":
        """
        No Docstrings Yet
        """
        ...
    
    def luminance(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def mix(self, c2: "color_t", mix: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def brightness(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def blue(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @blue.setter
    def blue(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def green(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @green.setter
    def green(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def red(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @red.setter
    def red(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _grad_dsc_t_type(TypedDict, total=False):
    stops: List["grad_stop_t"] = ...
    stops_count: int = ...
    dir: "grad_dir_t" = ...
    extend: "grad_extend_t" = ...
    params: "grad_dsc_params_t" = ...
    state: Any = ...



class grad_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_grad_dsc_t_type] = dict(), /) -> "grad_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init_stops(self, colors: List["color_t"], opa: List["opa_t"], fracs: List[int], num_stops: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def horizontal_init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def vertical_init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def linear_init(self, from_x: int, from_y: int, to_x: int, to_y: int, extend: "grad_extend_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def radial_init(self, from_x: int, from_y: int, to_x: int, to_y: int, extend: "grad_extend_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def radial_set_focal(self, center_x: int, center_y: int, radius: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def conical_init(self, from_x: int, from_y: int, to_x: int, to_y: int, extend: "grad_extend_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def stops(self) -> List["grad_stop_t"]:
       """
       No Docstrings Yet
       """ 
       ...

    @stops.setter
    def stops(self, value: List["grad_stop_t"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def stops_count(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @stops_count.setter
    def stops_count(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dir(self) -> "grad_dir_t":
       """
       No Docstrings Yet
       """ 
       ...

    @dir.setter
    def dir(self, value: "grad_dir_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def extend(self) -> "grad_extend_t":
       """
       No Docstrings Yet
       """ 
       ...

    @extend.setter
    def extend(self, value: "grad_extend_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def params(self) -> "grad_dsc_params_t":
       """
       No Docstrings Yet
       """ 
       ...

    @params.setter
    def params(self, value: "grad_dsc_params_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def state(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @state.setter
    def state(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...




class _grad_stop_t_type(TypedDict, total=False):
    color: "color_t" = ...
    opa: "opa_t" = ...
    frac: int = ...



class grad_stop_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_grad_stop_t_type] = dict(), /) -> "grad_stop_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def frac(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @frac.setter
    def frac(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _grad_dsc_params_t_type(TypedDict, total=False):
    linear: "grad_dsc_params_linear_t" = ...
    radial: "grad_dsc_params_radial_t" = ...
    conical: "grad_dsc_params_conical_t" = ...



class grad_dsc_params_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_grad_dsc_params_t_type] = dict(), /) -> "grad_dsc_params_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def linear(self) -> "grad_dsc_params_linear_t":
       """
       No Docstrings Yet
       """ 
       ...

    @linear.setter
    def linear(self, value: "grad_dsc_params_linear_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radial(self) -> "grad_dsc_params_radial_t":
       """
       No Docstrings Yet
       """ 
       ...

    @radial.setter
    def radial(self, value: "grad_dsc_params_radial_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def conical(self) -> "grad_dsc_params_conical_t":
       """
       No Docstrings Yet
       """ 
       ...

    @conical.setter
    def conical(self, value: "grad_dsc_params_conical_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _grad_dsc_params_linear_t_type(TypedDict, total=False):
    start: "point_t" = ...
    end: "point_t" = ...



class grad_dsc_params_linear_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_grad_dsc_params_linear_t_type] = dict(), /) -> "grad_dsc_params_linear_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def start(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @start.setter
    def start(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @end.setter
    def end(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _point_t_type(TypedDict, total=False):
    x: int = ...
    y: int = ...



class point_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_point_t_type] = dict(), /) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def transform(self, angle: int, scale_x: int, scale_y: int, pivot: "point_t", zoom_first: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def array_transform(self, count: int, angle: int, scale_x: int, scale_y: int, pivot: "point_t", zoom_first: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def to_precise(self, /) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def swap(self, p2: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @x.setter
    def x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @y.setter
    def y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _grad_dsc_params_radial_t_type(TypedDict, total=False):
    focal: "point_t" = ...
    focal_extent: "point_t" = ...
    end: "point_t" = ...
    end_extent: "point_t" = ...



class grad_dsc_params_radial_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_grad_dsc_params_radial_t_type] = dict(), /) -> "grad_dsc_params_radial_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def focal(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @focal.setter
    def focal(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def focal_extent(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @focal_extent.setter
    def focal_extent(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @end.setter
    def end(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_extent(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @end_extent.setter
    def end_extent(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _grad_dsc_params_conical_t_type(TypedDict, total=False):
    center: "point_t" = ...
    start_angle: int = ...
    end_angle: int = ...



class grad_dsc_params_conical_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_grad_dsc_params_conical_t_type] = dict(), /) -> "grad_dsc_params_conical_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def center(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @center.setter
    def center(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_angle(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @start_angle.setter
    def start_angle(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_angle(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @end_angle.setter
    def end_angle(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _font_t_type(TypedDict, total=False):
    line_height: int = ...
    base_line: int = ...
    subpx: int = ...
    kerning: int = ...
    static_bitmap: int = ...
    underline_position: int = ...
    underline_thickness: int = ...
    dsc: Any = ...
    fallback: "font_t" = ...
    user_data: Any = ...



class font_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_font_t_type] = dict(), /) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_glyph_dsc(self, arg0: "font_glyph_dsc_t", letter: int, letter_next: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_glyph_width(self, letter: int, letter_next: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_line_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_kerning(self, kerning: "font_kerning_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def has_static_bitmap(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_glyph_dsc_fmt_txt(self, arg0: "font_glyph_dsc_t", letter: int, letter_next: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def line_height(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @line_height.setter
    def line_height(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base_line(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @base_line.setter
    def base_line(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def subpx(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @subpx.setter
    def subpx(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def kerning(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @kerning.setter
    def kerning(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def static_bitmap(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @static_bitmap.setter
    def static_bitmap(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def underline_position(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @underline_position.setter
    def underline_position(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def underline_thickness(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @underline_thickness.setter
    def underline_thickness(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @dsc.setter
    def dsc(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def fallback(self) -> "font_t":
       """
       No Docstrings Yet
       """ 
       ...

    @fallback.setter
    def fallback(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...




class _font_glyph_dsc_t_type(TypedDict, total=False):
    resolved_font: "font_t" = ...
    adv_w: int = ...
    box_w: int = ...
    box_h: int = ...
    ofs_x: int = ...
    ofs_y: int = ...
    stride: int = ...
    format: "font_glyph_format_t" = ...
    is_placeholder: int = ...
    req_raw_bitmap: int = ...
    outline_stroke_width: int = ...
    gid: "font_glyph_dsc_gid_t" = ...
    entry: "cache_entry_t" = ...



class font_glyph_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_font_glyph_dsc_t_type] = dict(), /) -> "font_glyph_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_glyph_bitmap(self, arg0: "draw_buf_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_glyph_static_bitmap(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def release_draw_data(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_bitmap_fmt_txt(self, arg0: "draw_buf_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def resolved_font(self) -> "font_t":
       """
       No Docstrings Yet
       """ 
       ...

    @resolved_font.setter
    def resolved_font(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def adv_w(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @adv_w.setter
    def adv_w(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def box_w(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @box_w.setter
    def box_w(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def box_h(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @box_h.setter
    def box_h(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @ofs_x.setter
    def ofs_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @ofs_y.setter
    def ofs_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def stride(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @stride.setter
    def stride(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def format(self) -> "font_glyph_format_t":
       """
       No Docstrings Yet
       """ 
       ...

    @format.setter
    def format(self, value: "font_glyph_format_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def is_placeholder(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @is_placeholder.setter
    def is_placeholder(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def req_raw_bitmap(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @req_raw_bitmap.setter
    def req_raw_bitmap(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_stroke_width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @outline_stroke_width.setter
    def outline_stroke_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gid(self) -> "font_glyph_dsc_gid_t":
       """
       No Docstrings Yet
       """ 
       ...

    @gid.setter
    def gid(self, value: "font_glyph_dsc_gid_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def entry(self) -> "cache_entry_t":
       """
       No Docstrings Yet
       """ 
       ...

    @entry.setter
    def entry(self, value: "cache_entry_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _font_glyph_dsc_gid_t_type(TypedDict, total=False):
    index: int = ...
    src: Any = ...



class font_glyph_dsc_gid_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_font_glyph_dsc_gid_t_type] = dict(), /) -> "font_glyph_dsc_gid_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def index(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @index.setter
    def index(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def src(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @src.setter
    def src(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...




class _cache_entry_t_type(TypedDict, total=False):
    ...



class cache_entry_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_cache_entry_t_type] = dict(), /) -> "cache_entry_t":
        """
        No Docstrings Yet
        """
        ...





class _draw_buf_t_type(TypedDict, total=False):
    header: "image" = ...
    data_size: int = ...
    data: Union[str, List[int]] = ...
    unaligned_data: Any = ...
    handlers: "draw_buf_handlers_t" = ...



class draw_buf_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_buf_t_type] = dict(), /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def has_flag(self, flag: "image", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flag(self, flag: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear_flag(self, flag: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def invalidate_cache(self, area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def flush_cache(self, area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear(self, a: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def dup(self, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...
    
    def init(self, w: int, h: int, cf: "color_format_t", stride: int, data: Any, data_size: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def reshape(self, cf: "color_format_t", w: int, h: int, stride: int, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...
    
    def destroy(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def copy(self, dest_area: "area_t", src: "draw_buf_t", src_area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def goto_xy(self, x: int, y: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def adjust_stride(self, stride: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def premultiply(self, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def from_image(self, img: "image", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def to_image(self, img: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_palette(self, index: int, color: "color32_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def save_to_file(self, path: str, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def header(self) -> "image":
       """
       No Docstrings Yet
       """ 
       ...

    @header.setter
    def header(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def data_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @data_size.setter
    def data_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def data(self) -> Union[str, List[int]]:
       """
       No Docstrings Yet
       """ 
       ...

    @data.setter
    def data(self, value: Union[str, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def unaligned_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @unaligned_data.setter
    def unaligned_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def handlers(self) -> "draw_buf_handlers_t":
       """
       No Docstrings Yet
       """ 
       ...

    @handlers.setter
    def handlers(self, value: "draw_buf_handlers_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_buf_handlers_t_type(TypedDict, total=False):
    ...



class draw_buf_handlers_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_buf_handlers_t_type] = dict(), /) -> "draw_buf_handlers_t":
        """
        No Docstrings Yet
        """
        ...

    def init_with_default_handlers(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init(self, buf_malloc_cb: "draw_buf_malloc_cb_t", buf_free_cb: "draw_buf_free_cb_t", buf_copy_cb: "draw_buf_copy_cb_t", align_pointer_cb: "draw_buf_align_cb_t", invalidate_cache_cb: "draw_buf_cache_operation_cb_t", flush_cache_cb: "draw_buf_cache_operation_cb_t", width_to_stride_cb: "draw_buf_width_to_stride_cb_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def align_ex(self, buf: Any, color_format: "color_format_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def width_to_stride_ex(self, w: int, color_format: "color_format_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def create_ex(self, w: int, h: int, cf: "color_format_t", stride: int, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...
    
    def dup_ex(self, draw_buf: "draw_buf_t", /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...
    



class _color_filter_dsc_t_type(TypedDict, total=False):
    user_data: Any = ...



class color_filter_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_color_filter_dsc_t_type] = dict(), /) -> "color_filter_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...




class _anim_t_type(TypedDict, total=False):
    var: Any = ...
    user_data: Any = ...
    start_value: int = ...
    current_value: int = ...
    end_value: int = ...
    duration: int = ...
    act_time: int = ...
    reverse_delay: int = ...
    reverse_duration: int = ...
    repeat_delay: int = ...
    repeat_cnt: int = ...
    parameter: "anim_parameter_t" = ...
    last_timer_run: int = ...
    pause_time: int = ...
    pause_duration: int = ...
    is_paused: int = ...
    reverse_play_in_progress: int = ...
    run_round: int = ...
    start_cb_called: int = ...
    early_apply: int = ...



class anim_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_anim_t_type] = dict(), /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_var(self, var: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_exec_cb(self, exec_cb: "anim_exec_xcb_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_duration(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_delay(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def resume(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def pause(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def pause_for(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_paused(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_values(self, start: int, end: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_custom_exec_cb(self, exec_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_path_cb(self, path_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_start_cb(self, start_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_get_value_cb(self, get_value_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_completed_cb(self, completed_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_deleted_cb(self, deleted_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_reverse_duration(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_reverse_time(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_reverse_delay(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_repeat_count(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_repeat_delay(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_early_apply(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_user_data(self, var: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bezier3_param(self, x1: int, y1: int, x2: int, y2: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def start(self, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_delay(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_playtime(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_time(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_repeat_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def custom_delete(self, exec_cb: Callable, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def custom_get(self, exec_cb: Callable, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...
    
    def path_linear(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def path_ease_in(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def path_ease_out(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def path_ease_in_out(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def path_overshoot(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def path_bounce(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def path_step(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def path_custom_bezier3(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def var(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @var.setter
    def var(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_value(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @start_value.setter
    def start_value(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def current_value(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @current_value.setter
    def current_value(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_value(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @end_value.setter
    def end_value(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def duration(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @duration.setter
    def duration(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def act_time(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @act_time.setter
    def act_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def reverse_delay(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @reverse_delay.setter
    def reverse_delay(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def reverse_duration(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @reverse_duration.setter
    def reverse_duration(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def repeat_delay(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @repeat_delay.setter
    def repeat_delay(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def repeat_cnt(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @repeat_cnt.setter
    def repeat_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def parameter(self) -> "anim_parameter_t":
       """
       No Docstrings Yet
       """ 
       ...

    @parameter.setter
    def parameter(self, value: "anim_parameter_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_timer_run(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @last_timer_run.setter
    def last_timer_run(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pause_time(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @pause_time.setter
    def pause_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pause_duration(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @pause_duration.setter
    def pause_duration(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def is_paused(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @is_paused.setter
    def is_paused(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def reverse_play_in_progress(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @reverse_play_in_progress.setter
    def reverse_play_in_progress(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def run_round(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @run_round.setter
    def run_round(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_cb_called(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @start_cb_called.setter
    def start_cb_called(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def early_apply(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @early_apply.setter
    def early_apply(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _anim_parameter_t_type(TypedDict, total=False):
    bezier3: "anim_bezier3_para_t" = ...



class anim_parameter_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_anim_parameter_t_type] = dict(), /) -> "anim_parameter_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def bezier3(self) -> "anim_bezier3_para_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bezier3.setter
    def bezier3(self, value: "anim_bezier3_para_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _anim_bezier3_para_t_type(TypedDict, total=False):
    x1: int = ...
    y1: int = ...
    x2: int = ...
    y2: int = ...



class anim_bezier3_para_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_anim_bezier3_para_t_type] = dict(), /) -> "anim_bezier3_para_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def x1(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @x1.setter
    def x1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y1(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @y1.setter
    def y1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def x2(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @x2.setter
    def x2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y2(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @y2.setter
    def y2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _style_transition_dsc_t_type(TypedDict, total=False):
    props: "style_prop_t" = ...
    user_data: Any = ...
    time: int = ...
    delay: int = ...



class style_transition_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_style_transition_dsc_t_type] = dict(), /) -> "style_transition_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, props: List["style_prop_t"], path_cb: Callable, time: int, delay: int, tr: "style_transition_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def props(self) -> "style_prop_t":
       """
       No Docstrings Yet
       """ 
       ...

    @props.setter
    def props(self, value: "style_prop_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def time(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @time.setter
    def time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def delay(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @delay.setter
    def delay(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _display_t_type(TypedDict, total=False):
    ...



class display_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_display_t_type] = dict(), /) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_default(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_next(self, /) -> "display_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_resolution(self, hor_res: int, ver_res: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_physical_resolution(self, hor_res: int, ver_res: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_offset(self, hor_res: int, ver_res: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_rotation(self, rotation: "display_rotation_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_matrix_rotation(self, enable: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_dpi(self, dpi: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_horizontal_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_vertical_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_original_horizontal_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_original_vertical_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_physical_horizontal_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_physical_vertical_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_offset_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_offset_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_rotation(self, /) -> "display_rotation_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_matrix_rotation(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_dpi(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_buffers(self, buf1: Any, buf2: Any, buf_size: int, render_mode: "display_render_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_buffers_with_stride(self, buf1: Any, buf2: Any, buf_size: int, stride: int, render_mode: "display_render_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_draw_buffers(self, buf1: "draw_buf_t", buf2: "draw_buf_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_3rd_draw_buffer(self, buf3: "draw_buf_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_render_mode(self, render_mode: "display_render_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flush_cb(self, flush_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flush_wait_cb(self, wait_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_color_format(self, color_format: "color_format_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_color_format(self, /) -> "color_format_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_tile_cnt(self, tile_cnt: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_tile_cnt(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_antialiasing(self, enable: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_antialiasing(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def flush_ready(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def flush_is_last(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_double_buffered(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_render_mode(self, /) -> "display_render_mode_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_screen_active(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_screen_prev(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_screen_loading(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_layer_top(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_layer_sys(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_layer_bottom(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_event_cb(self, event_cb: Callable, filter: "event_code_t", disp: "display_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_event_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_event_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def delete_event(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_event_cb_with_user_data(self, event_cb: Callable, disp: "display_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def send_event(self, code: "event_code_t", param: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_theme(self, th: "theme_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_theme(self, /) -> "theme_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_inactive_time(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def trigger_activity(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def enable_invalidation(self, enable: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_invalidation_enabled(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_refr_timer(self, /) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def delete_refr_timer(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def register_vsync_event(self, event_cb: Callable, disp: "display_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def unregister_vsync_event(self, event_cb: Callable, disp: "display_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def send_vsync_event(self, param: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_user_data(self, disp: "display_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_driver_data(self, disp: "display_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_driver_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_buf_active(self, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...
    
    def rotate_area(self, area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def rotate_point(self, point: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_draw_buf_size(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_invalidated_draw_buf_size(self, width: int, height: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def dpx(self, n: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def draw_dispatch_layer(self, layer: "layer_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    



class _matrix_t_type(TypedDict, total=False):
    ...



class matrix_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_matrix_t_type] = dict(), /) -> "matrix_t":
        """
        No Docstrings Yet
        """
        ...





class _area_t_type(TypedDict, total=False):
    x1: int = ...
    y1: int = ...
    x2: int = ...
    y2: int = ...



class area_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_area_t_type] = dict(), /) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def copy(self, src: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set(self, x1: int, y1: int, x2: int, y2: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_width(self, w: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_height(self, w: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_size(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def increase(self, w_extra: int, h_extra: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def move(self, w_extra: int, h_extra: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def align(self, to_align: "area_t", align: "align_t", ofs_x: int, ofs_y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def x1(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @x1.setter
    def x1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y1(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @y1.setter
    def y1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def x2(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @x2.setter
    def x2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y2(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @y2.setter
    def y2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _style_t_type(TypedDict, total=False):
    values_and_props: Any = ...
    has_group: int = ...
    prop_cnt: int = ...



class style_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_style_t_type] = dict(), /) -> "style_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def is_const(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_prop_inlined(self, prop: "style_prop_t", value: "style_value_t", /) -> "style_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_size(self, width: int, height: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_all(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_hor(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_ver(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_gap(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_margin_hor(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_margin_ver(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_margin_all(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_scale(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def reset(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def copy(self, src: "style_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def merge(self, src: "style_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_prop(self, prop: "style_prop_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_prop(self, prop: "style_prop_t", value: "style_value_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_prop(self, prop: "style_prop_t", value: "style_value_t", /) -> "style_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def is_empty(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_length(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_align(self, value: "align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_translate_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_translate_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_translate_radial(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_scale_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_scale_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_rotation(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_pivot_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_pivot_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_skew_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform_skew_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_top(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_bottom(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_left(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_right(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_row(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_column(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pad_radial(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_margin_top(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_margin_bottom(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_margin_left(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_margin_right(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_grad_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_grad_dir(self, value: "grad_dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_main_stop(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_grad_stop(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_main_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_grad_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_grad(self, value: "grad_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_image_src(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_image_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_image_recolor(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_image_recolor_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_image_tiled(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_border_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_border_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_border_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_border_side(self, value: "border_side_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_border_post(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_outline_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_outline_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_outline_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_outline_pad(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shadow_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shadow_offset_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shadow_offset_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shadow_spread(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shadow_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shadow_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_image_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_image_recolor(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_image_recolor_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_image_colorkey(self, value: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_line_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_line_dash_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_line_dash_gap(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_line_rounded(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_line_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_line_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_arc_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_arc_rounded(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_arc_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_arc_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_arc_image_src(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_font(self, value: "font_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_letter_space(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_line_space(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_decor(self, value: "text_decor_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_align(self, value: "text_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_outline_stroke_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_outline_stroke_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_outline_stroke_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_blur_radius(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_blur_backdrop(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_blur_quality(self, value: "blur_quality_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_drop_shadow_radius(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_drop_shadow_offset_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_drop_shadow_offset_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_drop_shadow_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_drop_shadow_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_drop_shadow_quality(self, value: "blur_quality_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_radius(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_radial_offset(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_clip_corner(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_opa_layered(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_color_filter_dsc(self, value: "color_filter_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_color_filter_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_recolor(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_recolor_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_anim(self, value: "anim_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_anim_duration(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transition(self, value: "style_transition_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_blend_mode(self, value: "blend_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_layout(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_base_dir(self, value: "base_dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bitmap_mask_src(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_rotary_sensitivity(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_flow(self, value: "flex_flow_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_main_place(self, value: "flex_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_cross_place(self, value: "flex_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_track_place(self, value: "flex_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_grow(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_column_dsc_array(self, value: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_column_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_row_dsc_array(self, value: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_row_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_cell_column_pos(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_cell_x_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_cell_column_span(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_cell_row_pos(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_cell_y_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_cell_row_span(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def values_and_props(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @values_and_props.setter
    def values_and_props(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def has_group(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @has_group.setter
    def has_group(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def prop_cnt(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @prop_cnt.setter
    def prop_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _style_value_t_type(TypedDict, total=False):
    num: int = ...
    ptr: Any = ...
    color: "color_t" = ...



class style_value_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_style_value_t_type] = dict(), /) -> "style_value_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def num(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @num.setter
    def num(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ptr(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @ptr.setter
    def ptr(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _color32_t_type(TypedDict, total=False):
    blue: int = ...
    green: int = ...
    red: int = ...
    alpha: int = ...



class color32_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_color32_t_type] = dict(), /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def eq(self, c2: "color32_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def color_premultiply(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def luminance(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def color_mix32(self, bg: "color32_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...
    
    def color_mix32_premultiplied(self, bg: "color32_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...
    
    def color_over32(self, bg: "color32_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def blue(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @blue.setter
    def blue(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def green(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @green.setter
    def green(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def red(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @red.setter
    def red(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def alpha(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @alpha.setter
    def alpha(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _observer_t_type(TypedDict, total=False):
    ...



class observer_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_observer_t_type] = dict(), /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    def remove(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_target(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_target_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    



class _subject_t_type(TypedDict, total=False):
    subs_ll: "ll_t" = ...
    value: "subject_value_t" = ...
    prev_value: "subject_value_t" = ...
    min_value: "subject_value_t" = ...
    max_value: "subject_value_t" = ...
    user_data: Any = ...
    type: int = ...
    size: int = ...
    notify_restart_query: int = ...



class subject_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_subject_t_type] = dict(), /) -> "subject_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init_int(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_int(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_int(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_previous_int(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_value_int(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_value_int(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_float(self, value: float, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_float(self, value: float, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_float(self, /) -> float:
        """
        No Docstrings Yet
        """
        ...
    
    def get_previous_float(self, /) -> float:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_value_float(self, value: float, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_value_float(self, value: float, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_string(self, buf: str, prev_buf: str, size: int, value: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def copy_string(self, buf: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_string(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_previous_string(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def init_pointer(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pointer(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_pointer(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_previous_pointer(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def init_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_previous_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def init_group(self, list: "subject_t", list_len: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def deinit(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_group_element(self, index: int, /) -> "subject_t":
        """
        No Docstrings Yet
        """
        ...
    
    def add_observer(self, observer_cb: Callable, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def add_observer_obj(self, observer_cb: Callable, obj: "obj", subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def add_observer_with_target(self, observer_cb: Callable, target: Any, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def notify(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def subs_ll(self) -> "ll_t":
       """
       No Docstrings Yet
       """ 
       ...

    @subs_ll.setter
    def subs_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def value(self) -> "subject_value_t":
       """
       No Docstrings Yet
       """ 
       ...

    @value.setter
    def value(self, value: "subject_value_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def prev_value(self) -> "subject_value_t":
       """
       No Docstrings Yet
       """ 
       ...

    @prev_value.setter
    def prev_value(self, value: "subject_value_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def min_value(self) -> "subject_value_t":
       """
       No Docstrings Yet
       """ 
       ...

    @min_value.setter
    def min_value(self, value: "subject_value_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def max_value(self) -> "subject_value_t":
       """
       No Docstrings Yet
       """ 
       ...

    @max_value.setter
    def max_value(self, value: "subject_value_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def type(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @type.setter
    def type(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def notify_restart_query(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @notify_restart_query.setter
    def notify_restart_query(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _ll_t_type(TypedDict, total=False):
    n_size: int = ...
    head: "ll_node_t" = ...
    tail: "ll_node_t" = ...



class ll_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_ll_t_type] = dict(), /) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, node_size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def ins_head(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def ins_prev(self, n_act: Any, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def ins_tail(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def remove(self, node_p: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear_custom(self, cleanup: List[void (], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def chg_list(self, ll_new_p: "ll_t", node: Any, head: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_head(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_tail(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_next(self, n_act: Any, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_prev(self, n_act: Any, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_len(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def move_before(self, n_act: Any, n_after: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_empty(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def n_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @n_size.setter
    def n_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def head(self) -> "ll_node_t":
       """
       No Docstrings Yet
       """ 
       ...

    @head.setter
    def head(self, value: "ll_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tail(self) -> "ll_node_t":
       """
       No Docstrings Yet
       """ 
       ...

    @tail.setter
    def tail(self, value: "ll_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _subject_value_t_type(TypedDict, total=False):
    num: int = ...
    pointer: Any = ...
    color: "color_t" = ...
    float_v: float = ...



class subject_value_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_subject_value_t_type] = dict(), /) -> "subject_value_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def num(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @num.setter
    def num(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pointer(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @pointer.setter
    def pointer(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def float_v(self) -> float:
       """
       No Docstrings Yet
       """ 
       ...

    @float_v.setter
    def float_v(self, value: float) -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_rect_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    bg_image_src: Any = ...
    bg_image_symbol_font: Any = ...
    bg_image_recolor: "color_t" = ...
    bg_image_opa: "opa_t" = ...
    bg_image_recolor_opa: "opa_t" = ...
    bg_image_tiled: int = ...
    bg_opa: "opa_t" = ...
    border_opa: "opa_t" = ...
    outline_opa: "opa_t" = ...
    shadow_opa: "opa_t" = ...
    bg_color: "color_t" = ...
    bg_grad: "grad_dsc_t" = ...
    bg_image_colorkey: "image" = ...
    border_color: "color_t" = ...
    border_width: int = ...
    border_side: "border_side_t" = ...
    border_post: int = ...
    outline_color: "color_t" = ...
    outline_width: int = ...
    outline_pad: int = ...
    shadow_color: "color_t" = ...
    shadow_width: int = ...
    shadow_offset_x: int = ...
    shadow_offset_y: int = ...
    shadow_spread: int = ...



class draw_rect_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_rect_dsc_t_type] = dict(), /) -> "draw_rect_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_src(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @bg_image_src.setter
    def bg_image_src(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_symbol_font(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @bg_image_symbol_font.setter
    def bg_image_symbol_font(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_recolor(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bg_image_recolor.setter
    def bg_image_recolor(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bg_image_opa.setter
    def bg_image_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_recolor_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bg_image_recolor_opa.setter
    def bg_image_recolor_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_tiled(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @bg_image_tiled.setter
    def bg_image_tiled(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bg_opa.setter
    def bg_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @border_opa.setter
    def border_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @outline_opa.setter
    def outline_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @shadow_opa.setter
    def shadow_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bg_color.setter
    def bg_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_grad(self) -> "grad_dsc_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bg_grad.setter
    def bg_grad(self, value: "grad_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_colorkey(self) -> "image":
       """
       No Docstrings Yet
       """ 
       ...

    @bg_image_colorkey.setter
    def bg_image_colorkey(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @border_color.setter
    def border_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @border_width.setter
    def border_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_side(self) -> "border_side_t":
       """
       No Docstrings Yet
       """ 
       ...

    @border_side.setter
    def border_side(self, value: "border_side_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_post(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @border_post.setter
    def border_post(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @outline_color.setter
    def outline_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @outline_width.setter
    def outline_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_pad(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @outline_pad.setter
    def outline_pad(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @shadow_color.setter
    def shadow_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @shadow_width.setter
    def shadow_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_offset_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @shadow_offset_x.setter
    def shadow_offset_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_offset_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @shadow_offset_y.setter
    def shadow_offset_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_spread(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @shadow_spread.setter
    def shadow_spread(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_dsc_base_t_type(TypedDict, total=False):
    obj: "obj" = ...
    part: int = ...
    id1: int = ...
    id2: int = ...
    layer: "layer_t" = ...
    drop_shadow_ofs_x: int = ...
    drop_shadow_ofs_y: int = ...
    drop_shadow_color: "color_t" = ...
    drop_shadow_opa: "opa_t" = ...
    drop_shadow_blur_radius: int = ...
    drop_shadow_quality: "blur_quality_t" = ...
    dsc_size: int = ...
    user_data: Any = ...



class draw_dsc_base_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_dsc_base_t_type] = dict(), /) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def obj(self) -> "obj":
       """
       No Docstrings Yet
       """ 
       ...

    @obj.setter
    def obj(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def part(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @part.setter
    def part(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def id1(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @id1.setter
    def id1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def id2(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @id2.setter
    def id2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layer(self) -> "layer_t":
       """
       No Docstrings Yet
       """ 
       ...

    @layer.setter
    def layer(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_shadow_ofs_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @drop_shadow_ofs_x.setter
    def drop_shadow_ofs_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_shadow_ofs_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @drop_shadow_ofs_y.setter
    def drop_shadow_ofs_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_shadow_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @drop_shadow_color.setter
    def drop_shadow_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_shadow_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @drop_shadow_opa.setter
    def drop_shadow_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_shadow_blur_radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @drop_shadow_blur_radius.setter
    def drop_shadow_blur_radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_shadow_quality(self) -> "blur_quality_t":
       """
       No Docstrings Yet
       """ 
       ...

    @drop_shadow_quality.setter
    def drop_shadow_quality(self, value: "blur_quality_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @dsc_size.setter
    def dsc_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...




class _layer_t_type(TypedDict, total=False):
    draw_buf: "draw_buf_t" = ...
    draw_task_head: "draw_task_t" = ...
    parent: "layer_t" = ...
    next: "layer_t" = ...
    user_data: Any = ...
    buf_area: "area_t" = ...
    phy_clip_area: "area_t" = ...
    _clip_area: "area_t" = ...
    partial_y_offset: int = ...
    recolor: "color32_t" = ...
    color_format: "color_format_t" = ...
    all_tasks_added: bool = ...
    opa: "opa_t" = ...



class layer_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_layer_t_type] = dict(), /) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def reset(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def draw_buf(self) -> "draw_buf_t":
       """
       No Docstrings Yet
       """ 
       ...

    @draw_buf.setter
    def draw_buf(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def draw_task_head(self) -> "draw_task_t":
       """
       No Docstrings Yet
       """ 
       ...

    @draw_task_head.setter
    def draw_task_head(self, value: "draw_task_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def parent(self) -> "layer_t":
       """
       No Docstrings Yet
       """ 
       ...

    @parent.setter
    def parent(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def next(self) -> "layer_t":
       """
       No Docstrings Yet
       """ 
       ...

    @next.setter
    def next(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buf_area(self) -> "area_t":
       """
       No Docstrings Yet
       """ 
       ...

    @buf_area.setter
    def buf_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def phy_clip_area(self) -> "area_t":
       """
       No Docstrings Yet
       """ 
       ...

    @phy_clip_area.setter
    def phy_clip_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def _clip_area(self) -> "area_t":
       """
       No Docstrings Yet
       """ 
       ...

    @_clip_area.setter
    def _clip_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def partial_y_offset(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @partial_y_offset.setter
    def partial_y_offset(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def recolor(self) -> "color32_t":
       """
       No Docstrings Yet
       """ 
       ...

    @recolor.setter
    def recolor(self, value: "color32_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color_format(self) -> "color_format_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color_format.setter
    def color_format(self, value: "color_format_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def all_tasks_added(self) -> bool:
       """
       No Docstrings Yet
       """ 
       ...

    @all_tasks_added.setter
    def all_tasks_added(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_task_t_type(TypedDict, total=False):
    ...



class draw_task_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_task_t_type] = dict(), /) -> "draw_task_t":
        """
        No Docstrings Yet
        """
        ...

    def get_dependent_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_type(self, /) -> "draw_task_type_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_draw_dsc(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_area(self, area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_fill_dsc(self, /) -> "draw_fill_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_border_dsc(self, /) -> "draw_border_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_box_shadow_dsc(self, /) -> "draw_box_shadow_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_label_dsc(self, /) -> "draw_label_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def label_iterate_characters(self, dsc: "draw_label_dsc_t", coords: "area_t", cb: "draw_glyph_cb_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def unit_draw_letter(self, dsc: "draw_glyph_dsc_t", pos: "point_t", font: "font_t", letter: int, cb: "draw_glyph_cb_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_image_dsc(self, /) -> "draw_image_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_line_dsc(self, /) -> "draw_line_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def line_iterate(self, dsc: "draw_line_dsc_t", draw_line_cb: List[void (], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_arc_dsc(self, /) -> "draw_arc_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_triangle_dsc(self, /) -> "draw_triangle_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_blur_dsc(self, /) -> "draw_blur_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    



class _draw_label_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    text: str = ...
    text_size: "point_t" = ...
    font: "font_t" = ...
    color: "color_t" = ...
    line_space: int = ...
    letter_space: int = ...
    ofs_x: int = ...
    ofs_y: int = ...
    rotation: int = ...
    sel_start: int = ...
    sel_end: int = ...
    sel_color: "color_t" = ...
    sel_bg_color: "color_t" = ...
    text_length: int = ...
    align: "text_align_t" = ...
    bidi_dir: "base_dir_t" = ...
    opa: "opa_t" = ...
    outline_stroke_opa: "opa_t" = ...
    decor: "text_decor_t" = ...
    flag: "text_flag_t" = ...
    text_local: int = ...
    text_static: int = ...
    has_bided: int = ...
    hint: "draw_label_hint_t" = ...
    outline_stroke_color: "color_t" = ...
    outline_stroke_width: int = ...



class draw_label_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_label_dsc_t_type] = dict(), /) -> "draw_label_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def text(self) -> str:
       """
       No Docstrings Yet
       """ 
       ...

    @text.setter
    def text(self, value: str) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def text_size(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @text_size.setter
    def text_size(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def font(self) -> "font_t":
       """
       No Docstrings Yet
       """ 
       ...

    @font.setter
    def font(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def line_space(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @line_space.setter
    def line_space(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def letter_space(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @letter_space.setter
    def letter_space(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @ofs_x.setter
    def ofs_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @ofs_y.setter
    def ofs_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rotation(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @rotation.setter
    def rotation(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_start(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @sel_start.setter
    def sel_start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_end(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @sel_end.setter
    def sel_end(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @sel_color.setter
    def sel_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_bg_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @sel_bg_color.setter
    def sel_bg_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def text_length(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @text_length.setter
    def text_length(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def align(self) -> "text_align_t":
       """
       No Docstrings Yet
       """ 
       ...

    @align.setter
    def align(self, value: "text_align_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bidi_dir(self) -> "base_dir_t":
       """
       No Docstrings Yet
       """ 
       ...

    @bidi_dir.setter
    def bidi_dir(self, value: "base_dir_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_stroke_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @outline_stroke_opa.setter
    def outline_stroke_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def decor(self) -> "text_decor_t":
       """
       No Docstrings Yet
       """ 
       ...

    @decor.setter
    def decor(self, value: "text_decor_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flag(self) -> "text_flag_t":
       """
       No Docstrings Yet
       """ 
       ...

    @flag.setter
    def flag(self, value: "text_flag_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def text_local(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @text_local.setter
    def text_local(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def text_static(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @text_static.setter
    def text_static(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def has_bided(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @has_bided.setter
    def has_bided(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def hint(self) -> "draw_label_hint_t":
       """
       No Docstrings Yet
       """ 
       ...

    @hint.setter
    def hint(self, value: "draw_label_hint_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_stroke_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @outline_stroke_color.setter
    def outline_stroke_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_stroke_width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @outline_stroke_width.setter
    def outline_stroke_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_label_hint_t_type(TypedDict, total=False):
    ...



class draw_label_hint_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_label_hint_t_type] = dict(), /) -> "draw_label_hint_t":
        """
        No Docstrings Yet
        """
        ...





class _draw_image_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    src: Any = ...
    header: "image" = ...
    clip_radius: int = ...
    rotation: int = ...
    scale_x: int = ...
    scale_y: int = ...
    skew_x: int = ...
    skew_y: int = ...
    pivot: "point_t" = ...
    recolor: "color_t" = ...
    recolor_opa: "opa_t" = ...
    opa: "opa_t" = ...
    blend_mode: "blend_mode_t" = ...
    antialias: int = ...
    tile: int = ...
    colorkey: "image" = ...
    sup: "draw_image_sup_t" = ...
    image_area: "area_t" = ...
    bitmap_mask_src: "image" = ...



class draw_image_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_image_dsc_t_type] = dict(), /) -> "draw_image_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def src(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @src.setter
    def src(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def header(self) -> "image":
       """
       No Docstrings Yet
       """ 
       ...

    @header.setter
    def header(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def clip_radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @clip_radius.setter
    def clip_radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rotation(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @rotation.setter
    def rotation(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scale_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @scale_x.setter
    def scale_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scale_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @scale_y.setter
    def scale_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def skew_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @skew_x.setter
    def skew_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def skew_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @skew_y.setter
    def skew_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pivot(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @pivot.setter
    def pivot(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def recolor(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @recolor.setter
    def recolor(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def recolor_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @recolor_opa.setter
    def recolor_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blend_mode(self) -> "blend_mode_t":
       """
       No Docstrings Yet
       """ 
       ...

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def antialias(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @antialias.setter
    def antialias(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tile(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @tile.setter
    def tile(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def colorkey(self) -> "image":
       """
       No Docstrings Yet
       """ 
       ...

    @colorkey.setter
    def colorkey(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sup(self) -> "draw_image_sup_t":
       """
       No Docstrings Yet
       """ 
       ...

    @sup.setter
    def sup(self, value: "draw_image_sup_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def image_area(self) -> "area_t":
       """
       No Docstrings Yet
       """ 
       ...

    @image_area.setter
    def image_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bitmap_mask_src(self) -> "image":
       """
       No Docstrings Yet
       """ 
       ...

    @bitmap_mask_src.setter
    def bitmap_mask_src(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_image_sup_t_type(TypedDict, total=False):
    ...



class draw_image_sup_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_image_sup_t_type] = dict(), /) -> "draw_image_sup_t":
        """
        No Docstrings Yet
        """
        ...





class _draw_line_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    p1: "point_precise_t" = ...
    p2: "point_precise_t" = ...
    points: "point_precise_t" = ...
    point_cnt: int = ...
    color: "color_t" = ...
    width: int = ...
    dash_width: int = ...
    dash_gap: int = ...
    opa: "opa_t" = ...
    round_start: int = ...
    round_end: int = ...
    raw_end: int = ...



class draw_line_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_line_dsc_t_type] = dict(), /) -> "draw_line_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def p1(self) -> "point_precise_t":
       """
       No Docstrings Yet
       """ 
       ...

    @p1.setter
    def p1(self, value: "point_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def p2(self) -> "point_precise_t":
       """
       No Docstrings Yet
       """ 
       ...

    @p2.setter
    def p2(self, value: "point_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def points(self) -> "point_precise_t":
       """
       No Docstrings Yet
       """ 
       ...

    @points.setter
    def points(self, value: "point_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def point_cnt(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @point_cnt.setter
    def point_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dash_width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @dash_width.setter
    def dash_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dash_gap(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @dash_gap.setter
    def dash_gap(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def round_start(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @round_start.setter
    def round_start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def round_end(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @round_end.setter
    def round_end(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def raw_end(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @raw_end.setter
    def raw_end(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _point_precise_t_type(TypedDict, total=False):
    x: "value_precise_t" = ...
    y: "value_precise_t" = ...



class point_precise_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_point_precise_t_type] = dict(), /) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def from_precise(self, /) -> "point_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set(self, x: "value_precise_t", y: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def swap(self, p2: "point_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def x(self) -> "value_precise_t":
       """
       No Docstrings Yet
       """ 
       ...

    @x.setter
    def x(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y(self) -> "value_precise_t":
       """
       No Docstrings Yet
       """ 
       ...

    @y.setter
    def y(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_arc_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    color: "color_t" = ...
    width: int = ...
    start_angle: "value_precise_t" = ...
    end_angle: "value_precise_t" = ...
    center: "point_t" = ...
    img_src: Any = ...
    radius: int = ...
    opa: "opa_t" = ...
    rounded: int = ...



class draw_arc_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_arc_dsc_t_type] = dict(), /) -> "draw_arc_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_angle(self) -> "value_precise_t":
       """
       No Docstrings Yet
       """ 
       ...

    @start_angle.setter
    def start_angle(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_angle(self) -> "value_precise_t":
       """
       No Docstrings Yet
       """ 
       ...

    @end_angle.setter
    def end_angle(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def center(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @center.setter
    def center(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def img_src(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @img_src.setter
    def img_src(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rounded(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @rounded.setter
    def rounded(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_blur_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    blur_radius: int = ...
    corner_radius: int = ...
    quality: "blur_quality_t" = ...



class draw_blur_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_blur_dsc_t_type] = dict(), /) -> "draw_blur_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blur_radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @blur_radius.setter
    def blur_radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def corner_radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @corner_radius.setter
    def corner_radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def quality(self) -> "blur_quality_t":
       """
       No Docstrings Yet
       """ 
       ...

    @quality.setter
    def quality(self, value: "blur_quality_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _event_t_type(TypedDict, total=False):
    ...



class event_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_event_t_type] = dict(), /) -> "event_t":
        """
        No Docstrings Yet
        """
        ...

    def get_target(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_current_target(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_code(self, /) -> "event_code_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_param(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def stop_bubbling(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def stop_trickling(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def stop_processing(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def free_user_data_cb(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_invalidated_area(self, /) -> "area_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_current_target_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_target_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_indev(self, /) -> "indev_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_layer(self, /) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_old_size(self, /) -> "area_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_key(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_rotary_diff(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_anim(self, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_ext_draw_size(self, size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_self_size_info(self, /) -> "point_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_hit_test_info(self, /) -> "hit_test_info_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_cover_area(self, /) -> "area_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_cover_res(self, res: "cover_res_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_draw_task(self, /) -> "draw_task_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_prev_state(self, /) -> "state_t":
        """
        No Docstrings Yet
        """
        ...
    



class _event_dsc_t_type(TypedDict, total=False):
    ...



class event_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_event_dsc_t_type] = dict(), /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_cb(self, /) -> "event_cb_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    



class _group_t_type(TypedDict, total=False):
    ...



class group_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_group_t_type] = dict(), /) -> "group_t":
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_default(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_obj(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_all_objs(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def focus_next(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def focus_prev(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def focus_freeze(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def send_data(self, c: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_focus_cb(self, focus_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_edge_cb(self, edge_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_refocus_policy(self, policy: "group_refocus_policy_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_editing(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_wrap(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_focused(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_focus_cb(self, /) -> "group_focus_cb_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_edge_cb(self, /) -> "group_edge_cb_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_editing(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_wrap(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_obj_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_obj_by_index(self, index: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def set_user_data(self, group: "group_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    



class _anim_timeline_t_type(TypedDict, total=False):
    ...



class anim_timeline_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_anim_timeline_t_type] = dict(), /) -> "anim_timeline_t":
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add(self, start_time: int, a: "anim_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def start(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def pause(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_reverse(self, reverse: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_delay(self, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_repeat_count(self, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_repeat_delay(self, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_progress(self, progress: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_user_data(self, at: "anim_timeline_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_playtime(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_reverse(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_delay(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_progress(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_repeat_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_repeat_delay(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def merge(self, src: "anim_timeline_t", delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    



class _subject_increment_dsc_t_type(TypedDict, total=False):
    ...



class subject_increment_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_subject_increment_dsc_t_type] = dict(), /) -> "subject_increment_dsc_t":
        """
        No Docstrings Yet
        """
        ...





class _span_t_type(TypedDict, total=False):
    ...



class span_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_span_t_type] = dict(), /) -> "span_t":
        """
        No Docstrings Yet
        """
        ...

    def set_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_static(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style(self, /) -> "style_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_text(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    



class _span_coords_t_type(TypedDict, total=False):
    heading: "area_t" = ...
    middle: "area_t" = ...
    trailing: "area_t" = ...



class span_coords_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_span_coords_t_type] = dict(), /) -> "span_coords_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def heading(self) -> "area_t":
       """
       No Docstrings Yet
       """ 
       ...

    @heading.setter
    def heading(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def middle(self) -> "area_t":
       """
       No Docstrings Yet
       """ 
       ...

    @middle.setter
    def middle(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def trailing(self) -> "area_t":
       """
       No Docstrings Yet
       """ 
       ...

    @trailing.setter
    def trailing(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _pinyin_dict_t_type(TypedDict, total=False):
    py: str = ...
    py_mb: str = ...



class pinyin_dict_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_pinyin_dict_t_type] = dict(), /) -> "pinyin_dict_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def py(self, value: str) -> None:
        """
        No Docstrings Yet
        """
        ...

    py = property(fset=py)

    def py_mb(self, value: str) -> None:
        """
        No Docstrings Yet
        """
        ...

    py_mb = property(fset=py_mb)




class _tree_class_t_type(TypedDict, total=False):
    base_class: "tree_class_t" = ...
    instance_size: int = ...



class tree_class_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_tree_class_t_type] = dict(), /) -> "tree_class_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def node_create(self, parent: "tree_node_t", /) -> "tree_node_t":
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base_class(self) -> "tree_class_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base_class.setter
    def base_class(self, value: "tree_class_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def instance_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @instance_size.setter
    def instance_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _tree_node_t_type(TypedDict, total=False):
    parent: "tree_node_t" = ...
    children: List["tree_node_t"] = ...
    child_cnt: int = ...
    child_cap: int = ...
    class_p: "tree_class_t" = ...



class tree_node_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_tree_node_t_type] = dict(), /) -> "tree_node_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def walk(self, mode: "tree_walk_mode_t", cb: Callable, bcb: Callable, acb: Callable, node: "tree_node_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def parent(self) -> "tree_node_t":
       """
       No Docstrings Yet
       """ 
       ...

    @parent.setter
    def parent(self, value: "tree_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def children(self) -> List["tree_node_t"]:
       """
       No Docstrings Yet
       """ 
       ...

    @children.setter
    def children(self, value: List["tree_node_t"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def child_cnt(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @child_cnt.setter
    def child_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def child_cap(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @child_cap.setter
    def child_cap(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def class_p(self) -> "tree_class_t":
       """
       No Docstrings Yet
       """ 
       ...

    @class_p.setter
    def class_p(self, value: "tree_class_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _font_class_t_type(TypedDict, total=False):
    ...



class font_class_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_font_class_t_type] = dict(), /) -> "font_class_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...



class _font_info_t_type(TypedDict, total=False):
    name: str = ...
    class_p: "font_class_t" = ...
    size: int = ...
    render_mode: int = ...
    style: int = ...
    kerning: "font_kerning_t" = ...



class font_info_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_font_info_t_type] = dict(), /) -> "font_info_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def is_equal(self, ft_info_2: "font_info_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def name(self) -> str:
       """
       No Docstrings Yet
       """ 
       ...

    @name.setter
    def name(self, value: str) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def class_p(self) -> "font_class_t":
       """
       No Docstrings Yet
       """ 
       ...

    @class_p.setter
    def class_p(self, value: "font_class_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def render_mode(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @render_mode.setter
    def render_mode(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def style(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @style.setter
    def style(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def kerning(self) -> "font_kerning_t":
       """
       No Docstrings Yet
       """ 
       ...

    @kerning.setter
    def kerning(self, value: "font_kerning_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _array_t_type(TypedDict, total=False):
    data: Union[str, List[int]] = ...
    size: int = ...
    capacity: int = ...
    element_size: int = ...
    inner_alloc: bool = ...



class array_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_array_t_type] = dict(), /) -> "array_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def size(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def capacity(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def is_empty(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_full(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def clear(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def front(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def back(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def init(self, capacity: int, element_size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_from_buf(self, buf: Any, capacity: int, element_size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def resize(self, new_capacity: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def deinit(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def copy(self, source: "array_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def shrink(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove(self, index: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_unordered(self, index: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def erase(self, start: int, end: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def concat(self, other: "array_t", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def push_back(self, element: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def assign(self, index: int, value: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def at(self, index: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def data(self) -> Union[str, List[int]]:
       """
       No Docstrings Yet
       """ 
       ...

    @data.setter
    def data(self, value: Union[str, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def capacity(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def element_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @element_size.setter
    def element_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def inner_alloc(self) -> bool:
       """
       No Docstrings Yet
       """ 
       ...

    @inner_alloc.setter
    def inner_alloc(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...




class _color16_t_type(TypedDict, total=False):
    blue: int = ...
    green: int = ...
    red: int = ...



class color16_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_color16_t_type] = dict(), /) -> "color16_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def to_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def premultiply(self, a: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def luminance(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def blue(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @blue.setter
    def blue(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def green(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @green.setter
    def green(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def red(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @red.setter
    def red(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _mem_monitor_t_type(TypedDict, total=False):
    total_size: int = ...
    free_cnt: int = ...
    free_size: int = ...
    free_biggest_size: int = ...
    used_cnt: int = ...
    max_used: int = ...
    used_pct: int = ...
    frag_pct: int = ...



class mem_monitor_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_mem_monitor_t_type] = dict(), /) -> "mem_monitor_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def core(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def monitor(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def total_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @total_size.setter
    def total_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def free_cnt(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @free_cnt.setter
    def free_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def free_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @free_size.setter
    def free_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def free_biggest_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @free_biggest_size.setter
    def free_biggest_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def used_cnt(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @used_cnt.setter
    def used_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def max_used(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @max_used.setter
    def max_used(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def used_pct(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @used_pct.setter
    def used_pct(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def frag_pct(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @frag_pct.setter
    def frag_pct(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _timer_t_type(TypedDict, total=False):
    ...



class timer_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_timer_t_type] = dict(), /) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def pause(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def resume(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cb(self, timer_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_period(self, period: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def ready(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_repeat_count(self, repeat_count: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_auto_delete(self, auto_delete: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_user_data(self, timer: "timer_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def reset(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_next(self, /) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_paused(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    



class _rb_t_type(TypedDict, total=False):
    ...



class rb_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_rb_t_type] = dict(), /) -> "rb_t":
        """
        No Docstrings Yet
        """
        ...

    def init(self, compare: "rb_compare_t", node_size: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def insert(self, key: Any, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...
    
    def find(self, key: Any, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_node(self, node: "rb_node_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def remove(self, key: Any, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def drop_node(self, node: "rb_node_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def drop(self, key: Any, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def minimum(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...
    
    def maximum(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...
    
    def destroy(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    



class _rb_node_t_type(TypedDict, total=False):
    ...



class rb_node_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_rb_node_t_type] = dict(), /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    def minimum_from(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...
    
    def maximum_from(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...
    



class _iter_t_type(TypedDict, total=False):
    ...



class iter_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_iter_t_type] = dict(), /) -> "iter_t":
        """
        No Docstrings Yet
        """
        ...

    def get_context(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def destroy(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def next(self, elem: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def make_peekable(self, capacity: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def peek(self, elem: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def peek_advance(self, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def peek_reset(self, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def inspect(self, inspect_cb: "iter_inspect_cb", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    



class _circle_buf_t_type(TypedDict, total=False):
    ...



class circle_buf_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_circle_buf_t_type] = dict(), /) -> "circle_buf_t":
        """
        No Docstrings Yet
        """
        ...

    def resize(self, capacity: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def destroy(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def size(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def capacity(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def remain(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def is_empty(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_full(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def reset(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def head(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def tail(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def read(self, data: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def write(self, data: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def fill(self, count: int, fill_cb: Callable, circle_buf: "circle_buf_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def skip(self, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def peek(self, data: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def peek_at(self, index: int, data: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    



class _layout_callbacks_t_type(TypedDict, total=False):
    ...



class layout_callbacks_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_layout_callbacks_t_type] = dict(), /) -> "layout_callbacks_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def create(self, callbacks: "layout_callbacks_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    



class _event_list_t_type(TypedDict, total=False):
    array: "array_t" = ...
    is_traversing: int = ...
    has_marked_deleting: int = ...



class event_list_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_event_list_t_type] = dict(), /) -> "event_list_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def send(self, e: "event_t", preprocess: bool, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def add(self, cb: Callable, filter: "event_code_t", list: "event_list_t", /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_dsc(self, dsc: "event_dsc_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def remove(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_all(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def array(self) -> "array_t":
       """
       No Docstrings Yet
       """ 
       ...

    @array.setter
    def array(self, value: "array_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def is_traversing(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @is_traversing.setter
    def is_traversing(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def has_marked_deleting(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @has_marked_deleting.setter
    def has_marked_deleting(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _fs_drv_t_type(TypedDict, total=False):
    letter: str = ...
    cache_size: int = ...
    user_data: Any = ...



class fs_drv_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_fs_drv_t_type] = dict(), /) -> "fs_drv_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def register(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def letter(self) -> str:
       """
       No Docstrings Yet
       """ 
       ...

    @letter.setter
    def letter(self, value: str) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cache_size(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @cache_size.setter
    def cache_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...




class _fs_file_t_type(TypedDict, total=False):
    file_d: Any = ...
    drv: "fs_drv_t" = ...
    cache: "fs_file_cache_t" = ...



class fs_file_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_fs_file_t_type] = dict(), /) -> "fs_file_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def open(self, path: str, mode: "fs_mode_t", /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def close(self, /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def read(self, buf: Any, btr: int, br: List[int], /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def write(self, buf: Any, btw: int, bw: List[int], /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def seek(self, pos: int, whence: "fs_whence_t", /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def tell(self, pos: List[int], /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_size(self, pos: List[int], /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def file_d(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @file_d.setter
    def file_d(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drv(self) -> "fs_drv_t":
       """
       No Docstrings Yet
       """ 
       ...

    @drv.setter
    def drv(self, value: "fs_drv_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cache(self) -> "fs_file_cache_t":
       """
       No Docstrings Yet
       """ 
       ...

    @cache.setter
    def cache(self, value: "fs_file_cache_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _fs_file_cache_t_type(TypedDict, total=False):
    ...



class fs_file_cache_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_fs_file_cache_t_type] = dict(), /) -> "fs_file_cache_t":
        """
        No Docstrings Yet
        """
        ...





class _fs_path_ex_t_type(TypedDict, total=False):
    path: List[str] = ...



class fs_path_ex_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_fs_path_ex_t_type] = dict(), /) -> "fs_path_ex_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def make_path_from_buffer(self, letter: str, buf: Any, size: int, ext: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_buffer_from_path(self, buffer: List[None], size: List[int], /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def path(self) -> List[str]:
       """
       No Docstrings Yet
       """ 
       ...

    @path.setter
    def path(self, value: List[str]) -> None:
        """
        No Docstrings Yet
        """
        ...




class _fs_dir_t_type(TypedDict, total=False):
    dir_d: Any = ...
    drv: "fs_drv_t" = ...



class fs_dir_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_fs_dir_t_type] = dict(), /) -> "fs_dir_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def open(self, path: str, /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def read(self, fn: str, fn_len: int, /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def close(self, /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def dir_d(self) -> Any:
       """
       No Docstrings Yet
       """ 
       ...

    @dir_d.setter
    def dir_d(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drv(self) -> "fs_drv_t":
       """
       No Docstrings Yet
       """ 
       ...

    @drv.setter
    def drv(self, value: "fs_drv_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_fill_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    opa: "opa_t" = ...
    color: "color_t" = ...
    grad: "grad_dsc_t" = ...



class draw_fill_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_fill_dsc_t_type] = dict(), /) -> "draw_fill_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def grad(self) -> "grad_dsc_t":
       """
       No Docstrings Yet
       """ 
       ...

    @grad.setter
    def grad(self, value: "grad_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_border_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    color: "color_t" = ...
    width: int = ...
    opa: "opa_t" = ...
    side: "border_side_t" = ...



class draw_border_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_border_dsc_t_type] = dict(), /) -> "draw_border_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def side(self) -> "border_side_t":
       """
       No Docstrings Yet
       """ 
       ...

    @side.setter
    def side(self, value: "border_side_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_box_shadow_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    color: "color_t" = ...
    width: int = ...
    spread: int = ...
    ofs_x: int = ...
    ofs_y: int = ...
    opa: "opa_t" = ...
    bg_cover: int = ...



class draw_box_shadow_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_box_shadow_dsc_t_type] = dict(), /) -> "draw_box_shadow_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def spread(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @spread.setter
    def spread(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @ofs_x.setter
    def ofs_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @ofs_y.setter
    def ofs_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_cover(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @bg_cover.setter
    def bg_cover(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_letter_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    unicode: int = ...
    font: "font_t" = ...
    color: "color_t" = ...
    rotation: int = ...
    scale_x: int = ...
    scale_y: int = ...
    skew_x: int = ...
    skew_y: int = ...
    pivot: "point_t" = ...
    opa: "opa_t" = ...
    decor: "text_decor_t" = ...
    blend_mode: "blend_mode_t" = ...
    outline_stroke_opa: "opa_t" = ...
    outline_stroke_width: int = ...
    outline_stroke_color: "color_t" = ...



class draw_letter_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_letter_dsc_t_type] = dict(), /) -> "draw_letter_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def unicode(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @unicode.setter
    def unicode(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def font(self) -> "font_t":
       """
       No Docstrings Yet
       """ 
       ...

    @font.setter
    def font(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rotation(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @rotation.setter
    def rotation(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scale_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @scale_x.setter
    def scale_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scale_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @scale_y.setter
    def scale_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def skew_x(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @skew_x.setter
    def skew_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def skew_y(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @skew_y.setter
    def skew_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pivot(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @pivot.setter
    def pivot(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def decor(self) -> "text_decor_t":
       """
       No Docstrings Yet
       """ 
       ...

    @decor.setter
    def decor(self, value: "text_decor_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blend_mode(self) -> "blend_mode_t":
       """
       No Docstrings Yet
       """ 
       ...

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_stroke_opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @outline_stroke_opa.setter
    def outline_stroke_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_stroke_width(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @outline_stroke_width.setter
    def outline_stroke_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_stroke_color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @outline_stroke_color.setter
    def outline_stroke_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _draw_glyph_dsc_t_type(TypedDict, total=False):
    ...



class draw_glyph_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_glyph_dsc_t_type] = dict(), /) -> "draw_glyph_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    



class _draw_triangle_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    p: List["point_precise_t"] = ...
    color: "color_t" = ...
    opa: "opa_t" = ...
    grad: "grad_dsc_t" = ...



class draw_triangle_dsc_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_draw_triangle_dsc_t_type] = dict(), /) -> "draw_triangle_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    @property
    def base(self) -> "draw_dsc_base_t":
       """
       No Docstrings Yet
       """ 
       ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def p(self) -> List["point_precise_t"]:
       """
       No Docstrings Yet
       """ 
       ...

    @p.setter
    def p(self, value: List["point_precise_t"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
       """
       No Docstrings Yet
       """ 
       ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
       """
       No Docstrings Yet
       """ 
       ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def grad(self) -> "grad_dsc_t":
       """
       No Docstrings Yet
       """ 
       ...

    @grad.setter
    def grad(self, value: "grad_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...




class _indev_t_type(TypedDict, total=False):
    ...



class indev_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_indev_t_type] = dict(), /) -> "indev_t":
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_next(self, /) -> "indev_t":
        """
        No Docstrings Yet
        """
        ...
    
    def read(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def enable(self, enable: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_type(self, indev_type: "indev_type_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_read_cb(self, read_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_user_data(self, indev: "indev_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_driver_data(self, indev: "indev_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_display(self, disp: "display_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_long_press_time(self, long_press_time: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_long_press_repeat_time(self, long_press_time: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scroll_limit(self, scroll_limit: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scroll_throw(self, scroll_limit: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_gesture_min_velocity(self, scroll_limit: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_gesture_min_distance(self, scroll_limit: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_type(self, /) -> "indev_type_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_read_cb(self, /) -> "indev_read_cb_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_state(self, /) -> "indev_state_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_group(self, /) -> "group_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_display(self, /) -> "display_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_driver_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_press_moved(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def reset(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def stop_processing(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def reset_long_press(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_group(self, group: "group_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_button_points(self, points: List["point_t"], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_point(self, point: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_gesture_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_key(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_short_click_streak(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_vect(self, point: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_cursor(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def wait_release(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_read_timer(self, /) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode(self, mode: "indev_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode(self, /) -> "indev_mode_t":
        """
        No Docstrings Yet
        """
        ...
    
    def add_event_cb(self, event_cb: Callable, filter: "event_code_t", indev: "indev_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_event_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_event_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_event(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_event_cb_with_user_data(self, event_cb: Callable, indev: "indev_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def send_event(self, code: "event_code_t", param: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_key_remap_cb(self, remap_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    



class _theme_t_type(TypedDict, total=False):
    ...



class theme_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_theme_t_type] = dict(), /) -> "theme_t":
        """
        No Docstrings Yet
        """
        ...

    def copy(self, src: "theme_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_parent(self, parent: "theme_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_apply_cb(self, apply_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    



class _color_hsv_t_type(TypedDict, total=False):
    h: int = ...
    s: int = ...
    v: int = ...



class color_hsv_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_color_hsv_t_type] = dict(), /) -> "color_hsv_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def h(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @h.setter
    def h(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def s(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @s.setter
    def s(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def v(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @v.setter
    def v(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class _hit_test_info_t_type(TypedDict, total=False):
    ...



class hit_test_info_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_hit_test_info_t_type] = dict(), /) -> "hit_test_info_t":
        """
        No Docstrings Yet
        """
        ...





class _indev_data_t_type(TypedDict, total=False):
    gesture_type: List["indev_gesture_type_t"] = ...
    gesture_data: None = ...
    state: "indev_state_t" = ...
    point: "point_t" = ...
    key: int = ...
    btn_id: int = ...
    enc_diff: int = ...
    timestamp: int = ...
    continue_reading: bool = ...



class indev_data_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_indev_data_t_type] = dict(), /) -> "indev_data_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def gesture_type(self) -> List["indev_gesture_type_t"]:
       """
       No Docstrings Yet
       """ 
       ...

    @gesture_type.setter
    def gesture_type(self, value: List["indev_gesture_type_t"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gesture_data(self) -> None:
       """
       No Docstrings Yet
       """ 
       ...

    @gesture_data.setter
    def gesture_data(self, value: None) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def state(self) -> "indev_state_t":
       """
       No Docstrings Yet
       """ 
       ...

    @state.setter
    def state(self, value: "indev_state_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def point(self) -> "point_t":
       """
       No Docstrings Yet
       """ 
       ...

    @point.setter
    def point(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def key(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @key.setter
    def key(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def btn_id(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @btn_id.setter
    def btn_id(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def enc_diff(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @enc_diff.setter
    def enc_diff(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def timestamp(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @timestamp.setter
    def timestamp(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def continue_reading(self) -> bool:
       """
       No Docstrings Yet
       """ 
       ...

    @continue_reading.setter
    def continue_reading(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...




class _sqrt_res_t_type(TypedDict, total=False):
    i: int = ...
    f: int = ...



class sqrt_res_t(object):
    """
    No Docstrings Yet
    """
    def __init__(self, args: Optional[_sqrt_res_t_type] = dict(), /) -> "sqrt_res_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def i(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @i.setter
    def i(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def f(self) -> int:
       """
       No Docstrings Yet
       """ 
       ...

    @f.setter
    def f(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...




class obj(object):
    """
    No Docstrings Yet
    """
    class TREE_WALK(object):
        """
        No Docstrings Yet
        """
        NEXT: ClassVar[int] = ...
        SKIP_CHILDREN: ClassVar[int] = ...
        END: ClassVar[int] = ...
    
    class POINT_TRANSFORM_FLAG(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        RECURSIVE: ClassVar[int] = ...
        INVERSE: ClassVar[int] = ...
        INVERSE_RECURSIVE: ClassVar[int] = ...
    
    class CLASS_EDITABLE(object):
        """
        No Docstrings Yet
        """
        INHERIT: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
        FALSE: ClassVar[int] = ...
    
    class CLASS_GROUP_DEF(object):
        """
        No Docstrings Yet
        """
        INHERIT: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
        FALSE: ClassVar[int] = ...
    
    class CLASS_THEME_INHERITABLE(object):
        """
        No Docstrings Yet
        """
        FALSE: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
    
    class FLAG(object):
        """
        No Docstrings Yet
        """
        HIDDEN: ClassVar[int] = ...
        CLICKABLE: ClassVar[int] = ...
        CLICK_FOCUSABLE: ClassVar[int] = ...
        CHECKABLE: ClassVar[int] = ...
        SCROLLABLE: ClassVar[int] = ...
        SCROLL_ELASTIC: ClassVar[int] = ...
        SCROLL_MOMENTUM: ClassVar[int] = ...
        SCROLL_ONE: ClassVar[int] = ...
        SCROLL_CHAIN_HOR: ClassVar[int] = ...
        SCROLL_CHAIN_VER: ClassVar[int] = ...
        SCROLL_CHAIN: ClassVar[int] = ...
        SCROLL_ON_FOCUS: ClassVar[int] = ...
        SCROLL_WITH_ARROW: ClassVar[int] = ...
        SNAPPABLE: ClassVar[int] = ...
        PRESS_LOCK: ClassVar[int] = ...
        EVENT_BUBBLE: ClassVar[int] = ...
        GESTURE_BUBBLE: ClassVar[int] = ...
        ADV_HITTEST: ClassVar[int] = ...
        IGNORE_LAYOUT: ClassVar[int] = ...
        FLOATING: ClassVar[int] = ...
        SEND_DRAW_TASK_EVENTS: ClassVar[int] = ...
        OVERFLOW_VISIBLE: ClassVar[int] = ...
        EVENT_TRICKLE: ClassVar[int] = ...
        STATE_TRICKLE: ClassVar[int] = ...
        LAYOUT_1: ClassVar[int] = ...
        LAYOUT_2: ClassVar[int] = ...
        FLEX_IN_NEW_TRACK: ClassVar[int] = ...
        WIDGET_1: ClassVar[int] = ...
        WIDGET_2: ClassVar[int] = ...
        USER_1: ClassVar[int] = ...
        USER_2: ClassVar[int] = ...
        USER_3: ClassVar[int] = ...
        USER_4: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def style_get_selector_state(self, /) -> "state_t":
        """
        No Docstrings Yet
        """
        ...
    
    def style_get_selector_part(self, /) -> "part_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_min_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_max_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_height(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_min_height(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_max_height(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_length(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_x(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_y(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_align(self, part: "part_t", /) -> "align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_height(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_translate_x(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_translate_y(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_translate_radial(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_scale_x(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_scale_y(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_rotation(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_pivot_x(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_pivot_y(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_skew_x(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_skew_y(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_pad_top(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_pad_bottom(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_pad_left(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_pad_right(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_pad_row(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_pad_column(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_pad_radial(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_margin_top(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_margin_bottom(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_margin_left(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_margin_right(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_grad_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_grad_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_grad_dir(self, part: "part_t", /) -> "grad_dir_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_main_stop(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_grad_stop(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_main_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_grad_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_grad(self, part: "part_t", /) -> "grad_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_image_src(self, part: "part_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_image_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_image_recolor(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_image_recolor_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_image_recolor_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bg_image_tiled(self, part: "part_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_border_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_border_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_border_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_border_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_border_side(self, part: "part_t", /) -> "border_side_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_border_post(self, part: "part_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_outline_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_outline_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_outline_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_outline_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_outline_pad(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_shadow_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_shadow_offset_x(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_shadow_offset_y(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_shadow_spread(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_shadow_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_shadow_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_shadow_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_image_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_image_recolor(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_image_recolor_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_image_recolor_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_image_colorkey(self, part: "part_t", /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_line_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_line_dash_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_line_dash_gap(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_line_rounded(self, part: "part_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_line_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_line_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_line_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_arc_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_arc_rounded(self, part: "part_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_arc_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_arc_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_arc_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_arc_image_src(self, part: "part_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_font(self, part: "part_t", /) -> "font_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_letter_space(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_line_space(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_decor(self, part: "part_t", /) -> "text_decor_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_align(self, part: "part_t", /) -> "text_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_outline_stroke_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_outline_stroke_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_outline_stroke_width(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_text_outline_stroke_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_blur_radius(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_blur_backdrop(self, part: "part_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_blur_quality(self, part: "part_t", /) -> "blur_quality_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_drop_shadow_radius(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_drop_shadow_offset_x(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_drop_shadow_offset_y(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_drop_shadow_color(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_drop_shadow_color_filtered(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_drop_shadow_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_drop_shadow_quality(self, part: "part_t", /) -> "blur_quality_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_radius(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_radial_offset(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_clip_corner(self, part: "part_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_opa_layered(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_color_filter_dsc(self, part: "part_t", /) -> "color_filter_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_color_filter_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_recolor(self, part: "part_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_recolor_opa(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_anim(self, part: "part_t", /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_anim_duration(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transition(self, part: "part_t", /) -> "style_transition_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_blend_mode(self, part: "part_t", /) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_layout(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_base_dir(self, part: "part_t", /) -> "base_dir_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_bitmap_mask_src(self, part: "part_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_rotary_sensitivity(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_flex_flow(self, part: "part_t", /) -> "flex_flow_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_flex_main_place(self, part: "part_t", /) -> "flex_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_flex_cross_place(self, part: "part_t", /) -> "flex_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_flex_track_place(self, part: "part_t", /) -> "flex_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_flex_grow(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_column_dsc_array(self, part: "part_t", /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_column_align(self, part: "part_t", /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_row_dsc_array(self, part: "part_t", /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_row_align(self, part: "part_t", /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_cell_column_pos(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_cell_x_align(self, part: "part_t", /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_cell_column_span(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_cell_row_pos(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_cell_y_align(self, part: "part_t", /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_grid_cell_row_span(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_all(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_hor(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_ver(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_margin_all(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_margin_hor(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_margin_ver(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_gap(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_size(self, width: int, height: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_scale(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_space_left(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_space_right(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_space_top(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_space_bottom(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_scale_x_safe(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_transform_scale_y_safe(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def move_foreground(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def move_background(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_flow(self, flow: "flex_flow_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_align(self, main_place: "flex_align_t", cross_place: "flex_align_t", track_cross_place: "flex_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flex_grow(self, grow: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_dsc_array(self, col_dsc: List[int], row_dsc: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_align(self, column_align: "grid_align_t", row_align: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_grid_cell(self, column_align: "grid_align_t", col_pos: int, col_span: int, row_align: "grid_align_t", row_pos: int, row_span: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clean(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def delete_delayed(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def delete_anim_completed_cb(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def delete_async(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_parent(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def swap(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def move_to_index(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_screen(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_display(self, /) -> "display_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_parent(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_child(self, idx: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_child_by_type(self, idx: int, class_p: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_sibling(self, idx: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_sibling_by_type(self, idx: int, class_p: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_child_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_child_count_by_type(self, class_p: "obj", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_index(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_index_by_type(self, class_p: "obj", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def tree_walk(self, cb: Callable, start_obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def dump_tree(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pos(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_x(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_y(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_size(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def refr_size(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_width(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_height(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_content_width(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_content_height(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_layout(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_layout_positioned(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def mark_layout_as_dirty(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def update_layout(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_align(self, align: "align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def align(self, align: "align_t", x_ofs: int, y_ofs: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def align_to(self, base: "obj", align: "align_t", x_ofs: int, y_ofs: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def center(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_transform(self, matrix: "matrix_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def reset_transform(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_coords(self, coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_x2(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_y2(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_x_aligned(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_y_aligned(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_content_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_content_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_content_coords(self, coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_self_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_self_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_clamped_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_clamped_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def is_width_min(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_height_min(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_width_max(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_height_max(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def refresh_self_size(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def refr_pos(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def move_to(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def move_children_by(self, x_diff: int, y_diff: int, ignore_floating: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_transform(self, /) -> "matrix_t":
        """
        No Docstrings Yet
        """
        ...
    
    def transform_point(self, p: "point_t", flags: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def transform_point_array(self, points: List["point_t"], count: int, flags: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_transformed_area(self, area: "area_t", flags: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def invalidate_area(self, area: "area_t", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def invalidate(self, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def area_is_visible(self, area: "area_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_visible(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_ext_click_area(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_click_area(self, coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def hit_test(self, point: "point_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def calc_dynamic_width(self, prop: "style_prop_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def calc_dynamic_height(self, prop: "style_prop_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scrollbar_mode(self, mode: "scrollbar_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scroll_dir(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scroll_snap_x(self, align: "scroll_snap_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scroll_snap_y(self, align: "scroll_snap_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scrollbar_mode(self, /) -> "scrollbar_mode_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_snap_x(self, /) -> "scroll_snap_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_snap_y(self, /) -> "scroll_snap_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_top(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_bottom(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_left(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_right(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scroll_end(self, end: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scroll_by(self, dx: int, dy: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scroll_by_bounded(self, dx: int, dy: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scroll_to(self, dx: int, dy: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scroll_to_x(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scroll_to_y(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scroll_to_view(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scroll_to_view_recursive(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_scrolling(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def stop_scroll_anim(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def update_snap(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scrollbar_area(self, hor: "area_t", ver: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def scrollbar_invalidate(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def readjust_scroll(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_style(self, style: "style_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def replace_style(self, old_style: "style_t", new_style: "style_t", selector: "style_selector_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_style(self, style: "style_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_theme(self, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_style_all(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def report_style_change(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def refresh_style(self, part: "part_t", prop: "style_prop_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def style_set_disabled(self, style: "style_t", selector: "style_selector_t", dis: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def style_get_disabled(self, style: "style_t", selector: "style_selector_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def enable_style_refresh(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_prop(self, part: "part_t", prop: "style_prop_t", /) -> "style_value_t":
        """
        No Docstrings Yet
        """
        ...
    
    def has_style_prop(self, selector: "style_selector_t", prop: "style_prop_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_local_style_prop(self, prop: "style_prop_t", value: "style_value_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_local_style_prop(self, prop: "style_prop_t", value: "style_value_t", selector: "style_selector_t", /) -> "style_res_t":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_local_style_prop(self, prop: "style_prop_t", selector: "style_selector_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def style_apply_color_filter(self, part: "part_t", v: "style_value_t", /) -> "style_value_t":
        """
        No Docstrings Yet
        """
        ...
    
    def fade_in(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def fade_out(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_min_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_max_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_height(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_min_height(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_max_height(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_length(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_align(self, value: "align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_height(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_translate_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_translate_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_translate_radial(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_scale_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_scale_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_rotation(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_pivot_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_pivot_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_skew_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transform_skew_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_top(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_bottom(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_left(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_right(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_row(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_column(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_pad_radial(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_margin_top(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_margin_bottom(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_margin_left(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_margin_right(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_grad_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_grad_dir(self, value: "grad_dir_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_main_stop(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_grad_stop(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_main_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_grad_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_grad(self, value: "grad_dsc_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_image_src(self, value: Any, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_image_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_image_recolor(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_image_recolor_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bg_image_tiled(self, value: bool, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_border_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_border_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_border_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_border_side(self, value: "border_side_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_border_post(self, value: bool, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_outline_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_outline_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_outline_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_outline_pad(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_shadow_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_shadow_offset_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_shadow_offset_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_shadow_spread(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_shadow_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_shadow_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_image_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_image_recolor(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_image_recolor_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_image_colorkey(self, value: "image", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_line_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_line_dash_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_line_dash_gap(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_line_rounded(self, value: bool, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_line_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_line_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_arc_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_arc_rounded(self, value: bool, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_arc_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_arc_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_arc_image_src(self, value: Any, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_font(self, value: "font_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_letter_space(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_line_space(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_decor(self, value: "text_decor_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_align(self, value: "text_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_outline_stroke_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_outline_stroke_width(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_text_outline_stroke_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_blur_radius(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_blur_backdrop(self, value: bool, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_blur_quality(self, value: "blur_quality_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_drop_shadow_radius(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_drop_shadow_offset_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_drop_shadow_offset_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_drop_shadow_color(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_drop_shadow_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_drop_shadow_quality(self, value: "blur_quality_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_radius(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_radial_offset(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_clip_corner(self, value: bool, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_opa_layered(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_color_filter_dsc(self, value: "color_filter_dsc_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_color_filter_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_recolor(self, value: "color_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_recolor_opa(self, value: "opa_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_anim(self, value: "anim_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_anim_duration(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_transition(self, value: "style_transition_dsc_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_blend_mode(self, value: "blend_mode_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_layout(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_base_dir(self, value: "base_dir_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_bitmap_mask_src(self, value: Any, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_rotary_sensitivity(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_flex_flow(self, value: "flex_flow_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_flex_main_place(self, value: "flex_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_flex_cross_place(self, value: "flex_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_flex_track_place(self, value: "flex_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_flex_grow(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_column_dsc_array(self, value: List[int], selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_column_align(self, value: "grid_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_row_dsc_array(self, value: List[int], selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_row_align(self, value: "grid_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_cell_column_pos(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_cell_x_align(self, value: "grid_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_cell_column_span(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_cell_row_pos(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_cell_y_align(self, value: "grid_align_t", selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_style_grid_cell_row_span(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def calculate_style_text_align(self, part: "part_t", txt: str, /) -> "text_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_opa_recursive(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...
    
    def style_apply_recolor(self, part: "part_t", color: "color32_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_style_recolor_recursive(self, part: "part_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_style(self, style: "style_t", selector: "style_selector_t", subject: "subject_t", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_style_prop(self, prop: "style_prop_t", selector: "style_selector_t", subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def init_draw_rect_dsc(self, part: "part_t", draw_dsc: "draw_rect_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_draw_label_dsc(self, part: "part_t", draw_dsc: "draw_label_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_draw_image_dsc(self, part: "part_t", draw_dsc: "draw_image_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_draw_line_dsc(self, part: "part_t", draw_dsc: "draw_line_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_draw_arc_dsc(self, part: "part_t", draw_dsc: "draw_arc_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_draw_blur_dsc(self, part: "part_t", draw_dsc: "draw_blur_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def calculate_ext_draw_size(self, part: "part_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def refresh_ext_draw_size(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def class_create_obj(self, parent: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def class_init_obj(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_editable(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_group_def(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def send_event(self, event_code: "event_code_t", param: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def event_base(self, e: "event_t", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def add_event_cb(self, event_cb: Callable, filter: "event_code_t", obj: "obj", /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_event_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_event_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_event(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_event_dsc(self, dsc: "event_dsc_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_event_cb(self, event_cb: Callable, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_event_cb_with_user_data(self, event_cb: Callable, obj: "obj", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def add_flag(self, f: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_flag(self, f: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_flag(self, f: "obj", v: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_state(self, state: "state_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_state(self, state: "state_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_state(self, state: "state_t", v: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_user_data(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_radio_button(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def has_flag(self, f: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def has_flag_any(self, f: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_state(self, /) -> "state_t":
        """
        No Docstrings Yet
        """
        ...
    
    def has_state(self, state: "state_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def is_radio_button(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_group(self, /) -> "group_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def allocate_spec_attr(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def check_type(self, class_p: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def has_class(self, class_p: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_class(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def is_valid(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def null_on_delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_screen_load_event(self, trigger: "event_code_t", screen: "obj", anim_type: "screen_load_anim_t", duration: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_screen_create_event(self, trigger: "event_code_t", screen_create_cb: "screen_create_cb_t", anim_type: "screen_load_anim_t", duration: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_play_timeline_event(self, trigger: "event_code_t", at: "anim_timeline_t", delay: int, reverse: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_id(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_id(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def find_by_id(self, id: Any, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def assign_id(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def free_id(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def id_compare(self, id2: Any, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def stringify_id(self, buf: str, len: int, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def redraw(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def remove_from_subject(self, subject: "subject_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_subject_increment_event(self, subject: "subject_t", trigger: "event_code_t", step: int, /) -> "subject_increment_dsc_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_subject_increment_event_min_value(self, dsc: "subject_increment_dsc_t", min_value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_subject_increment_event_max_value(self, dsc: "subject_increment_dsc_t", min_value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_subject_increment_event_rollover(self, dsc: "subject_increment_dsc_t", rollover: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_subject_toggle_event(self, subject: "subject_t", trigger: "event_code_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_subject_set_int_event(self, subject: "subject_t", trigger: "event_code_t", value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_subject_set_float_event(self, subject: "subject_t", trigger: "event_code_t", value: float, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_subject_set_string_event(self, subject: "subject_t", trigger: "event_code_t", value: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_flag_if_eq(self, subject: "subject_t", flag: "obj", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_flag_if_not_eq(self, subject: "subject_t", flag: "obj", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_flag_if_gt(self, subject: "subject_t", flag: "obj", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_flag_if_ge(self, subject: "subject_t", flag: "obj", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_flag_if_lt(self, subject: "subject_t", flag: "obj", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_flag_if_le(self, subject: "subject_t", flag: "obj", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_state_if_eq(self, subject: "subject_t", state: "state_t", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_state_if_not_eq(self, subject: "subject_t", state: "state_t", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_state_if_gt(self, subject: "subject_t", state: "state_t", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_state_if_ge(self, subject: "subject_t", state: "state_t", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_state_if_lt(self, subject: "subject_t", state: "state_t", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_state_if_le(self, subject: "subject_t", state: "state_t", ref_value: int, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_checked(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class image(obj):
    """
    No Docstrings Yet
    """
    class FLAGS(object):
        """
        No Docstrings Yet
        """
        PREMULTIPLIED: ClassVar[int] = ...
        COMPRESSED: ClassVar[int] = ...
        ALLOCATED: ClassVar[int] = ...
        MODIFIABLE: ClassVar[int] = ...
        CUSTOM_DRAW: ClassVar[int] = ...
        USER1: ClassVar[int] = ...
        USER2: ClassVar[int] = ...
        USER3: ClassVar[int] = ...
        USER4: ClassVar[int] = ...
        USER5: ClassVar[int] = ...
        USER6: ClassVar[int] = ...
        USER7: ClassVar[int] = ...
        USER8: ClassVar[int] = ...
    
    class COMPRESS(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        RLE: ClassVar[int] = ...
        LZ4: ClassVar[int] = ...
    
    class SRC(object):
        """
        No Docstrings Yet
        """
        VARIABLE: ClassVar[int] = ...
        FILE: ClassVar[int] = ...
        SYMBOL: ClassVar[int] = ...
        UNKNOWN: ClassVar[int] = ...
    
    class ALIGN(object):
        """
        No Docstrings Yet
        """
        DEFAULT: ClassVar[int] = ...
        TOP_LEFT: ClassVar[int] = ...
        TOP_MID: ClassVar[int] = ...
        TOP_RIGHT: ClassVar[int] = ...
        BOTTOM_LEFT: ClassVar[int] = ...
        BOTTOM_MID: ClassVar[int] = ...
        BOTTOM_RIGHT: ClassVar[int] = ...
        LEFT_MID: ClassVar[int] = ...
        RIGHT_MID: ClassVar[int] = ...
        CENTER: ClassVar[int] = ...
        STRETCH: ClassVar[int] = ...
        TILE: ClassVar[int] = ...
        CONTAIN: ClassVar[int] = ...
        COVER: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def buf_set_palette(self, id: int, c: "color32_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def buf_free(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_get_info(self, header: "image", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_open(self, src: Any, args: "image", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_get_area(self, full_area: "area_t", decoded_area: "area_t", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_close(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_create(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_get_next(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_set_info_cb(self, info_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_set_open_cb(self, open_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_set_get_area_cb(self, read_line_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_set_close_cb(self, close_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_add_to_cache(self, search_key: "image", decoded: "draw_buf_t", decoder: "image", /) -> "cache_entry_t":
        """
        No Docstrings Yet
        """
        ...
    
    def decoder_post_process(self, decoded: "draw_buf_t", /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...
    
    def src_get_type(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def set_src(self, src: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_offset_x(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_offset_y(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_rotation(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pivot(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pivot_x(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_pivot_y(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scale(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scale_x(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scale_y(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_blend_mode(self, blend_mode: "blend_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_antialias(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_inner_align(self, align: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bitmap_map_src(self, src: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_src(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_offset_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_offset_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_rotation(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_pivot(self, end: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scale(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scale_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_scale_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_src_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_src_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_transformed_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_transformed_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_blend_mode(self, /) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_antialias(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_inner_align(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def get_bitmap_map_src(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_src(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class animimg(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "animimg":
        """
        No Docstrings Yet
        """
        ...
    
    def set_src(self, dsc: Any, num: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_src_reverse(self, dsc: Any, num: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def start(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_duration(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_repeat_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_reverse_duration(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_reverse_delay(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_start_cb(self, start_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_completed_cb(self, completed_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_src_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_duration(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_repeat_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_anim(self, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...
    

class arc(obj):
    """
    No Docstrings Yet
    """
    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        REVERSE: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "arc":
        """
        No Docstrings Yet
        """
        ...
    
    def set_start_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_end_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_angles(self, start: "value_precise_t", end: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_start_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_end_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_bg_angles(self, start: "value_precise_t", end: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_rotation(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode(self, type: "arc", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_change_rate(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_knob_offset(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_angle_start(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_angle_end(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_bg_angle_start(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_bg_angle_end(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode(self, /) -> "arc":
        """
        No Docstrings Yet
        """
        ...
    
    def get_rotation(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_knob_offset(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_change_rate(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def align_obj_to_angle(self, obj_to_align: "obj", r_offset: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def rotate_obj_to_angle(self, obj_to_align: "obj", r_offset: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class arclabel(obj):
    """
    No Docstrings Yet
    """
    class DIR(object):
        """
        No Docstrings Yet
        """
        CLOCKWISE: ClassVar[int] = ...
        COUNTER_CLOCKWISE: ClassVar[int] = ...
    
    class TEXT_ALIGN(object):
        """
        No Docstrings Yet
        """
        DEFAULT: ClassVar[int] = ...
        LEADING: ClassVar[int] = ...
        CENTER: ClassVar[int] = ...
        TRAILING: ClassVar[int] = ...
    
    class OVERFLOW(object):
        """
        No Docstrings Yet
        """
        VISIBLE: ClassVar[int] = ...
        ELLIPSIS: ClassVar[int] = ...
        CLIP: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "arclabel":
        """
        No Docstrings Yet
        """
        ...
    
    def set_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_static(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_angle_start(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_angle_size(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_offset(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_dir(self, dir: "arclabel", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_recolor(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_radius(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_center_offset_x(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_center_offset_y(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_vertical_align(self, align: "arclabel", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_horizontal_align(self, align: "arclabel", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_overflow(self, overflow: "arclabel", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_end_overlap(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_angle_start(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_angle_size(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_dir(self, /) -> "arclabel":
        """
        No Docstrings Yet
        """
        ...
    
    def get_recolor(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_radius(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_center_offset_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_center_offset_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text_vertical_align(self, /) -> "arclabel":
        """
        No Docstrings Yet
        """
        ...
    
    def get_text_horizontal_align(self, /) -> "arclabel":
        """
        No Docstrings Yet
        """
        ...
    
    def get_overflow(self, /) -> "arclabel":
        """
        No Docstrings Yet
        """
        ...
    
    def get_end_overlap(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text_angle(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...
    

class label(obj):
    """
    No Docstrings Yet
    """
    class LONG_MODE(object):
        """
        No Docstrings Yet
        """
        WRAP: ClassVar[int] = ...
        DOTS: ClassVar[int] = ...
        SCROLL: ClassVar[int] = ...
        SCROLL_CIRCULAR: ClassVar[int] = ...
        CLIP: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "label":
        """
        No Docstrings Yet
        """
        ...
    
    def set_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_static(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_long_mode(self, long_mode: "label", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_selection_start(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_selection_end(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_recolor(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_long_mode(self, /) -> "label":
        """
        No Docstrings Yet
        """
        ...
    
    def get_letter_pos(self, char_id: int, pos: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_letter_on(self, pos_in: "point_t", bidi: bool, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def is_char_under_pos(self, pos: "point_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text_selection_start(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text_selection_end(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_recolor(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_text(self, subject: "subject_t", fmt: str, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def ins_text(self, pos: int, txt: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def cut_text(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class bar(obj):
    """
    No Docstrings Yet
    """
    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        RANGE: ClassVar[int] = ...
    
    class ORIENTATION(object):
        """
        No Docstrings Yet
        """
        AUTO: ClassVar[int] = ...
        HORIZONTAL: ClassVar[int] = ...
        VERTICAL: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "bar":
        """
        No Docstrings Yet
        """
        ...
    
    def set_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_start_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode(self, mode: "bar", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_orientation(self, orientation: "bar", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_start_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode(self, /) -> "bar":
        """
        No Docstrings Yet
        """
        ...
    
    def get_orientation(self, /) -> "bar":
        """
        No Docstrings Yet
        """
        ...
    
    def is_symmetrical(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class button(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "button":
        """
        No Docstrings Yet
        """
        ...
    

class buttonmatrix(obj):
    """
    No Docstrings Yet
    """
    class CTRL(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        WIDTH_1: ClassVar[int] = ...
        WIDTH_2: ClassVar[int] = ...
        WIDTH_3: ClassVar[int] = ...
        WIDTH_4: ClassVar[int] = ...
        WIDTH_5: ClassVar[int] = ...
        WIDTH_6: ClassVar[int] = ...
        WIDTH_7: ClassVar[int] = ...
        WIDTH_8: ClassVar[int] = ...
        WIDTH_9: ClassVar[int] = ...
        WIDTH_10: ClassVar[int] = ...
        WIDTH_11: ClassVar[int] = ...
        WIDTH_12: ClassVar[int] = ...
        WIDTH_13: ClassVar[int] = ...
        WIDTH_14: ClassVar[int] = ...
        WIDTH_15: ClassVar[int] = ...
        HIDDEN: ClassVar[int] = ...
        NO_REPEAT: ClassVar[int] = ...
        DISABLED: ClassVar[int] = ...
        CHECKABLE: ClassVar[int] = ...
        CHECKED: ClassVar[int] = ...
        CLICK_TRIG: ClassVar[int] = ...
        POPOVER: ClassVar[int] = ...
        RECOLOR: ClassVar[int] = ...
        RESERVED_1: ClassVar[int] = ...
        RESERVED_2: ClassVar[int] = ...
        CUSTOM_1: ClassVar[int] = ...
        CUSTOM_2: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "buttonmatrix":
        """
        No Docstrings Yet
        """
        ...
    
    def set_map(self, map: List[str], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_ctrl_map(self, ctrl_map: List["buttonmatrix"], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_selected_button(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_button_ctrl_all(self, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear_button_ctrl_all(self, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_button_width(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_one_checked(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected_button(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_button_text(self, btn_id: int, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def has_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_one_checked(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    

class calendar(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...
    
    def set_today_date(self, year: int, month: int, day: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_today_year(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_today_month(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_today_day(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_month_shown(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shown_year(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_shown_month(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_highlighted_dates(self, highlighted: List["calendar"], date_num: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_day_names(self, day_names: List[str], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_btnmatrix(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_today_date(self, /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...
    
    def get_showed_date(self, /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...
    
    def get_highlighted_dates(self, /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...
    
    def get_highlighted_dates_num(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_pressed_date(self, date: "calendar", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def add_header_arrow(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_header_dropdown(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def header_dropdown_set_year_list(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class canvas(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "canvas":
        """
        No Docstrings Yet
        """
        ...
    
    def set_buffer(self, buf: Any, w: int, h: int, cf: "color_format_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_draw_buf(self, draw_buf: "draw_buf_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_px(self, x: int, y: int, color: "color_t", opa: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_palette(self, index: int, color: "color32_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_draw_buf(self, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_px(self, x: int, y: int, /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_image(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...
    
    def get_buf(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def copy_buf(self, canvas_area: "area_t", src_buf: "draw_buf_t", src_area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def fill_bg(self, color: "color_t", opa: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def init_layer(self, layer: "layer_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def finish_layer(self, layer: "layer_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def buf_size(self, h: int, bpp: int, stride: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    

class chart(obj):
    """
    No Docstrings Yet
    """
    class TYPE(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        LINE: ClassVar[int] = ...
        CURVE: ClassVar[int] = ...
        BAR: ClassVar[int] = ...
        STACKED: ClassVar[int] = ...
        SCATTER: ClassVar[int] = ...
    
    class UPDATE_MODE(object):
        """
        No Docstrings Yet
        """
        SHIFT: ClassVar[int] = ...
        CIRCULAR: ClassVar[int] = ...
    
    class AXIS(object):
        """
        No Docstrings Yet
        """
        PRIMARY_Y: ClassVar[int] = ...
        SECONDARY_Y: ClassVar[int] = ...
        PRIMARY_X: ClassVar[int] = ...
        SECONDARY_X: ClassVar[int] = ...
        LAST: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...
    
    def set_type(self, type: "chart", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_point_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_axis_range(self, axis: "chart", min: int, max: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_axis_min_value(self, axis: "chart", min: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_axis_max_value(self, axis: "chart", min: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_update_mode(self, update_mode: "chart", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_div_line_count(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_hor_div_line_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_ver_div_line_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_type(self, /) -> "chart":
        """
        No Docstrings Yet
        """
        ...
    
    def get_point_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_update_mode(self, /) -> "chart":
        """
        No Docstrings Yet
        """
        ...
    
    def get_hor_div_line_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_ver_div_line_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_x_start_point(self, ser: "chart", /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_point_pos_by_id(self, ser: "chart", id: int, p_out: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def refresh(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_series(self, color: "color_t", axis: "chart", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_series(self, series: "chart", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def hide_series(self, series: "chart", hide: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_series_color(self, series: "chart", color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_series_color(self, series: "chart", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_x_start_point(self, ser: "chart", id: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_series_next(self, ser: "chart", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...
    
    def add_cursor(self, color: "color_t", dir: "dir_t", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...
    
    def remove_cursor(self, cursor: "chart", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor_pos(self, cursor: "chart", pos: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor_pos_x(self, cursor: "chart", x: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor_pos_y(self, cursor: "chart", x: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor_point(self, cursor: "chart", ser: "chart", point_id: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_cursor_point(self, cursor: "chart", /) -> "point_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_all_values(self, ser: "chart", value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_next_value(self, ser: "chart", value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_next_value2(self, ser: "chart", x_value: int, y_value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_series_values(self, ser: "chart", values: List[int], values_cnt: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_series_values2(self, ser: "chart", x_values: List[int], y_values: List[int], values_cnt: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_series_value_by_id(self, ser: "chart", id: int, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_series_value_by_id2(self, ser: "chart", id: int, x_value: int, y_value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_series_ext_y_array(self, ser: "chart", array: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_series_ext_x_array(self, ser: "chart", array: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_series_y_array(self, ser: "chart", /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...
    
    def get_series_x_array(self, ser: "chart", /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...
    
    def get_pressed_point(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_first_point_center_offset(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    

class checkbox(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "checkbox":
        """
        No Docstrings Yet
        """
        ...
    
    def set_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_static(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    

class dropdown(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "dropdown":
        """
        No Docstrings Yet
        """
        ...
    
    def set_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_static(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_options(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_options_static(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_option(self, option: str, pos: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear_options(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_selected(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_dir(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_symbol(self, src: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_selected_highlight(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_list(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_text(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_options(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_option_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected_str(self, buf: str, buf_size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_option_index(self, option: str, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_symbol(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected_highlight(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...
    
    def open(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def close(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_open(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class gif(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "gif":
        """
        No Docstrings Yet
        """
        ...
    
    def set_color_format(self, color_format: "color_format_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_src(self, src: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def restart(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def pause(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def resume(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def is_loaded(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_loop_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def set_loop_count(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_auto_pause_invisible(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_size(self, w: List[int], h: List[int], /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_frame_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_current_frame_index(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    

class imagebutton(obj):
    """
    No Docstrings Yet
    """
    class STATE(object):
        """
        No Docstrings Yet
        """
        RELEASED: ClassVar[int] = ...
        PRESSED: ClassVar[int] = ...
        DISABLED: ClassVar[int] = ...
        CHECKED_RELEASED: ClassVar[int] = ...
        CHECKED_PRESSED: ClassVar[int] = ...
        CHECKED_DISABLED: ClassVar[int] = ...
        NUM: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "imagebutton":
        """
        No Docstrings Yet
        """
        ...
    
    def set_src(self, state: "imagebutton", src_left: Any, src_mid: Any, src_right: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_src_left(self, state: "imagebutton", src_left: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_src_right(self, state: "imagebutton", src_left: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_src_mid(self, state: "imagebutton", src_left: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_src_left(self, state: "imagebutton", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_src_middle(self, state: "imagebutton", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    
    def get_src_right(self, state: "imagebutton", /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    

class keyboard(obj):
    """
    No Docstrings Yet
    """
    class MODE(object):
        """
        No Docstrings Yet
        """
        TEXT_LOWER: ClassVar[int] = ...
        TEXT_UPPER: ClassVar[int] = ...
        SPECIAL: ClassVar[int] = ...
        NUMBER: ClassVar[int] = ...
        USER_1: ClassVar[int] = ...
        USER_2: ClassVar[int] = ...
        USER_3: ClassVar[int] = ...
        USER_4: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "keyboard":
        """
        No Docstrings Yet
        """
        ...
    
    def set_textarea(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode(self, mode: "keyboard", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_popovers(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_map(self, mode: "keyboard", map: List[str], ctrl_map: List["buttonmatrix"], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_textarea(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode(self, /) -> "keyboard":
        """
        No Docstrings Yet
        """
        ...
    
    def get_popovers(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected_button(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_button_text(self, btn_id: int, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def def_event_cb(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class led(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "led":
        """
        No Docstrings Yet
        """
        ...
    
    def set_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_brightness(self, grow: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def on(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def off(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def toggle(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_brightness(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    

class line(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "line":
        """
        No Docstrings Yet
        """
        ...
    
    def set_points(self, points: List["point_precise_t"], point_num: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_points_mutable(self, points: List["point_precise_t"], point_num: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_y_invert(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_points(self, /) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_point_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def is_point_array_mutable(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_points_mutable(self, /) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_y_invert(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    

class list(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "list":
        """
        No Docstrings Yet
        """
        ...
    
    def add_text(self, txt: str, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_button(self, icon: Any, txt: str, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_button_text(self, btn: "obj", /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def set_button_text(self, btn: "obj", txt: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class menu(obj):
    """
    No Docstrings Yet
    """
    class HEADER(object):
        """
        No Docstrings Yet
        """
        TOP_FIXED: ClassVar[int] = ...
        TOP_UNFIXED: ClassVar[int] = ...
        BOTTOM_FIXED: ClassVar[int] = ...
    
    class ROOT_BACK_BUTTON(object):
        """
        No Docstrings Yet
        """
        DISABLED: ClassVar[int] = ...
        ENABLED: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "menu":
        """
        No Docstrings Yet
        """
        ...
    
    def set_page(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_page_title(self, title: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_page_title_static(self, title: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_sidebar_page(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode_header(self, mode: "menu", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode_root_back_button(self, mode: "menu", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_load_page_event(self, obj: "obj", page: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_cur_main_page(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_cur_sidebar_page(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_main_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_main_header_back_button(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_sidebar_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_sidebar_header_back_button(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def back_button_is_root(self, obj: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode_header(self, /) -> "menu":
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode_root_back_button(self, /) -> "menu":
        """
        No Docstrings Yet
        """
        ...
    
    def clear_history(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class menu_page(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "menu_page":
        """
        No Docstrings Yet
        """
        ...
    

class menu_cont(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "menu_cont":
        """
        No Docstrings Yet
        """
        ...
    

class menu_section(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "menu_section":
        """
        No Docstrings Yet
        """
        ...
    

class menu_separator(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "menu_separator":
        """
        No Docstrings Yet
        """
        ...
    

class msgbox(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "msgbox":
        """
        No Docstrings Yet
        """
        ...
    
    def add_title(self, txt: str, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_header_button(self, icon: Any, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_text(self, txt: str, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_footer_button(self, txt: str, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_close_button(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_footer(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_content(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_title(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def close(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def close_async(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class roller(obj):
    """
    No Docstrings Yet
    """
    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        INFINITE: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "roller":
        """
        No Docstrings Yet
        """
        ...
    
    def set_options(self, options: str, mode: "roller", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_selected(self, sel_opt: int, anim: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_selected_str(self, sel_opt: str, anim: "anim_enable_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def set_visible_row_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected_str(self, buf: str, buf_size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_options(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_option_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_option_str(self, option: int, buf: str, buf_size: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class scale(obj):
    """
    No Docstrings Yet
    """
    class MODE(object):
        """
        No Docstrings Yet
        """
        HORIZONTAL_TOP: ClassVar[int] = ...
        HORIZONTAL_BOTTOM: ClassVar[int] = ...
        VERTICAL_LEFT: ClassVar[int] = ...
        VERTICAL_RIGHT: ClassVar[int] = ...
        ROUND_INNER: ClassVar[int] = ...
        ROUND_OUTER: ClassVar[int] = ...
        LAST: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "scale":
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode(self, mode: "scale", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_total_tick_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_major_tick_every(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_label_show(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_angle_range(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_rotation(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_line_needle_value(self, needle_line: "obj", needle_length: int, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_image_needle_value(self, needle_img: "obj", value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_src(self, txt_src: List[str], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_post_draw(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_draw_ticks_on_top(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_section(self, /) -> "scale":
        """
        No Docstrings Yet
        """
        ...
    
    def section_set_range(self, min: int, max: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_section_range(self, section: "scale", min: int, max: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_section_min_value(self, section: "scale", min: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_section_max_value(self, section: "scale", min: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def section_set_style(self, part: "part_t", section_part_style: "style_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_section_style_main(self, section: "scale", style: "style_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_section_style_indicator(self, section: "scale", style: "style_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_section_style_items(self, section: "scale", style: "style_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode(self, /) -> "scale":
        """
        No Docstrings Yet
        """
        ...
    
    def get_total_tick_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_major_tick_every(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_rotation(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_label_show(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_angle_range(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_range_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_range_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_section_min_value(self, section: "scale", subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    
    def bind_section_max_value(self, section: "scale", subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class slider(obj):
    """
    No Docstrings Yet
    """
    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        RANGE: ClassVar[int] = ...
    
    class ORIENTATION(object):
        """
        No Docstrings Yet
        """
        AUTO: ClassVar[int] = ...
        HORIZONTAL: ClassVar[int] = ...
        VERTICAL: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "slider":
        """
        No Docstrings Yet
        """
        ...
    
    def set_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_start_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode(self, mode: "slider", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_orientation(self, orientation: "slider", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_left_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def is_dragged(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode(self, /) -> "slider":
        """
        No Docstrings Yet
        """
        ...
    
    def get_orientation(self, /) -> "slider":
        """
        No Docstrings Yet
        """
        ...
    
    def is_symmetrical(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class spangroup(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "spangroup":
        """
        No Docstrings Yet
        """
        ...
    
    def add_span(self, /) -> "span_t":
        """
        No Docstrings Yet
        """
        ...
    
    def delete_span(self, span: "span_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_span_text(self, span: "span_t", text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_span_text_static(self, span: "span_t", text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_span_style(self, span: "span_t", style: "style_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_overflow(self, overflow: "span_overflow_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_indent(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_mode(self, mode: "span_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_lines(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_span_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_align(self, /) -> "text_align_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_overflow(self, /) -> "span_overflow_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_indent(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_mode(self, /) -> "span_mode_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_max_lines(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_max_line_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_expand_width(self, max_width: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_expand_height(self, width: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_span_coords(self, span: "span_t", /) -> "span_coords_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_span_by_point(self, point: "point_t", /) -> "span_t":
        """
        No Docstrings Yet
        """
        ...
    
    def refresh(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_span_text(self, span: "span_t", subject: "subject_t", fmt: str, /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class textarea(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "textarea":
        """
        No Docstrings Yet
        """
        ...
    
    def add_char(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def add_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def delete_char(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def delete_char_forward(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_placeholder_text(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor_pos(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor_click_pos(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_password_mode(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_password_bullet(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_one_line(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_accepted_chars(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_accepted_chars_static(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_length(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_insert_replace(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_text_selection(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_password_show_time(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_placeholder_text(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_label(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_cursor_pos(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_cursor_click_pos(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_password_mode(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_password_bullet(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_one_line(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_accepted_chars(self, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_max_length(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def text_is_selected(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_text_selection(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_password_show_time(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_current_char(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def clear_selection(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def cursor_right(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def cursor_left(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def cursor_down(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def cursor_up(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class spinbox(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "spinbox":
        """
        No Docstrings Yet
        """
        ...
    
    def set_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_rollover(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_digit_format(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_digit_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_dec_point_pos(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_step(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_min_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_max_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cursor_pos(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_digit_step_direction(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_rollover(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_step(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_digit_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_dec_point_pos(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_digit_step_direction(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...
    
    def step_next(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def step_prev(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def increment(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def decrement(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...
    

class spinner(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "spinner":
        """
        No Docstrings Yet
        """
        ...
    
    def set_anim_params(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_anim_duration(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_arc_sweep(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_anim_duration(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_arc_sweep(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    

class switch(obj):
    """
    No Docstrings Yet
    """
    class ORIENTATION(object):
        """
        No Docstrings Yet
        """
        AUTO: ClassVar[int] = ...
        HORIZONTAL: ClassVar[int] = ...
        VERTICAL: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "switch":
        """
        No Docstrings Yet
        """
        ...
    
    def set_orientation(self, orientation: "switch", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_orientation(self, /) -> "switch":
        """
        No Docstrings Yet
        """
        ...
    

class table(obj):
    """
    No Docstrings Yet
    """
    class CELL_CTRL(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        MERGE_RIGHT: ClassVar[int] = ...
        TEXT_CROP: ClassVar[int] = ...
        CUSTOM_1: ClassVar[int] = ...
        CUSTOM_2: ClassVar[int] = ...
        CUSTOM_3: ClassVar[int] = ...
        CUSTOM_4: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "table":
        """
        No Docstrings Yet
        """
        ...
    
    def set_cell_value(self, row: int, col: int, txt: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_row_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_column_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_column_width(self, col_id: int, w: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cell_ctrl(self, row: int, col: int, ctrl: "table", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def clear_cell_ctrl(self, row: int, col: int, ctrl: "table", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_cell_user_data(self, row: int, col: int, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_selected_cell(self, row: int, col: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_cell_value(self, row: int, col: int, /) -> str:
        """
        No Docstrings Yet
        """
        ...
    
    def get_row_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_column_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_column_width(self, col: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def has_cell_ctrl(self, row: int, col: int, ctrl: "table", /) -> bool:
        """
        No Docstrings Yet
        """
        ...
    
    def get_selected_cell(self, row: List[int], col: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_cell_user_data(self, row: int, col: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...
    

class tabview(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "tabview":
        """
        No Docstrings Yet
        """
        ...
    
    def add_tab(self, txt: str, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def set_tab_text(self, pos: int, txt: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_active(self, sel_opt: int, anim: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_tab_bar_position(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_tab_bar_size(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_tab_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_tab_active(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_tab_button(self, idx: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_content(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_tab_bar(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_tab_bar_position(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...
    

class tileview(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "tileview":
        """
        No Docstrings Yet
        """
        ...
    
    def add_tile(self, col_id: int, row_id: int, dir: "dir_t", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def set_tile(self, tile_obj: "obj", anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_tile_by_index(self, col_id: int, row_id: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def get_tile_active(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    

class win(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "win":
        """
        No Docstrings Yet
        """
        ...
    
    def add_title(self, txt: str, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def add_button(self, icon: Any, btn_w: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def get_content(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    

class ime_pinyin(obj):
    """
    No Docstrings Yet
    """
    class PINYIN_MODE(object):
        """
        No Docstrings Yet
        """
        K26: ClassVar[int] = ...
        K9: ClassVar[int] = ...
        K9_NUMBER: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "ime_pinyin":
        """
        No Docstrings Yet
        """
        ...
    
    def pinyin_set_keyboard(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def pinyin_set_dict(self, dict: "pinyin_dict_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def pinyin_set_mode(self, mode: "ime_pinyin", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def pinyin_get_kb(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def pinyin_get_cand_panel(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...
    
    def pinyin_get_dict(self, /) -> "pinyin_dict_t":
        """
        No Docstrings Yet
        """
        ...
    

class barcode(obj):
    """
    No Docstrings Yet
    """
    class ENCODING_CODE128(object):
        """
        No Docstrings Yet
        """
        GS1: ClassVar[int] = ...
        RAW: ClassVar[int] = ...
    

    def __init__(self, parent: "obj", /) -> "barcode":
        """
        No Docstrings Yet
        """
        ...
    
    def set_dark_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_light_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_scale(self, scale: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_direction(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_tiled(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_encoding(self, encoding: "barcode", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def update(self, data: str, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_dark_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_light_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...
    
    def get_scale(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...
    
    def get_encoding(self, /) -> "barcode":
        """
        No Docstrings Yet
        """
        ...
    

class qrcode(obj):
    """
    No Docstrings Yet
    """
    def __init__(self, parent: "obj", /) -> "qrcode":
        """
        No Docstrings Yet
        """
        ...
    
    def set_dark_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_light_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def update(self, data: Any, data_len: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...
    
    def set_data(self, text: str, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    
    def set_quiet_zone(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...
    

class tree_node_class_class(object):
    """
    No Docstrings Yet
    """
    ...

class obj_class(object):
    """
    No Docstrings Yet
    """
    ...

class binfont_font_class_class(object):
    """
    No Docstrings Yet
    """
    ...

class builtin_font_class_class(object):
    """
    No Docstrings Yet
    """
    ...

class image_class(object):
    """
    No Docstrings Yet
    """
    ...

class animimg_class(object):
    """
    No Docstrings Yet
    """
    ...

class arc_class(object):
    """
    No Docstrings Yet
    """
    ...

class arclabel_class(object):
    """
    No Docstrings Yet
    """
    ...

class label_class(object):
    """
    No Docstrings Yet
    """
    ...

class bar_class(object):
    """
    No Docstrings Yet
    """
    ...

class button_class(object):
    """
    No Docstrings Yet
    """
    ...

class buttonmatrix_class(object):
    """
    No Docstrings Yet
    """
    ...

class calendar_class(object):
    """
    No Docstrings Yet
    """
    ...

class canvas_class(object):
    """
    No Docstrings Yet
    """
    ...

class chart_class(object):
    """
    No Docstrings Yet
    """
    ...

class checkbox_class(object):
    """
    No Docstrings Yet
    """
    ...

class dropdown_class(object):
    """
    No Docstrings Yet
    """
    ...

class gif_class(object):
    """
    No Docstrings Yet
    """
    ...

class imagebutton_class(object):
    """
    No Docstrings Yet
    """
    ...

class keyboard_class(object):
    """
    No Docstrings Yet
    """
    ...

class led_class(object):
    """
    No Docstrings Yet
    """
    ...

class line_class(object):
    """
    No Docstrings Yet
    """
    ...

class list_class(object):
    """
    No Docstrings Yet
    """
    ...

class menu_class(object):
    """
    No Docstrings Yet
    """
    ...

class menu_page_class(object):
    """
    No Docstrings Yet
    """
    ...

class menu_cont_class(object):
    """
    No Docstrings Yet
    """
    ...

class menu_section_class(object):
    """
    No Docstrings Yet
    """
    ...

class menu_separator_class(object):
    """
    No Docstrings Yet
    """
    ...

class msgbox_class(object):
    """
    No Docstrings Yet
    """
    ...

class roller_class(object):
    """
    No Docstrings Yet
    """
    ...

class scale_class(object):
    """
    No Docstrings Yet
    """
    ...

class slider_class(object):
    """
    No Docstrings Yet
    """
    ...

class spangroup_class(object):
    """
    No Docstrings Yet
    """
    ...

class textarea_class(object):
    """
    No Docstrings Yet
    """
    ...

class spinbox_class(object):
    """
    No Docstrings Yet
    """
    ...

class spinner_class(object):
    """
    No Docstrings Yet
    """
    ...

class switch_class(object):
    """
    No Docstrings Yet
    """
    ...

class table_class(object):
    """
    No Docstrings Yet
    """
    ...

class tabview_class(object):
    """
    No Docstrings Yet
    """
    ...

class tileview_class(object):
    """
    No Docstrings Yet
    """
    ...

class win_class(object):
    """
    No Docstrings Yet
    """
    ...

class ime_pinyin_class(object):
    """
    No Docstrings Yet
    """
    ...

class barcode_class(object):
    """
    No Docstrings Yet
    """
    ...

class qrcode_class(object):
    """
    No Docstrings Yet
    """
    ...


color_filter_shade: "color_filter_dsc_t" = ...
font_montserrat_8: "font_t" = ...
font_montserrat_10: "font_t" = ...
font_montserrat_12: "font_t" = ...
font_montserrat_14: "font_t" = ...
font_montserrat_16: "font_t" = ...
style_const_prop_id_inv: "_mp_int_wrapper" = ...
_nesting: "_mp_int_wrapper" = ...

def memzero(dst: Any, len: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def streq(s1: str, s2: str, /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def sqr(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_swap_16(c: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def swap_bytes_32(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def swap_bytes_16(c: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def bidi_calculate_align(align: "text_align_t", base_dir: "base_dir_t", txt: str, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def style_get_prop_group(prop: "style_prop_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def style_prop_has_flag(prop: "style_prop_t", flag: int, /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def task_handler() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_major() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_minor() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_patch() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_info() -> str:
    """
    No Docstrings Yet
    """
    ...


def mp_lv_init_gc() -> None:
    """
    No Docstrings Yet
    """
    ...


def init() -> None:
    """
    No Docstrings Yet
    """
    ...


def deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def is_initialized() -> bool:
    """
    No Docstrings Yet
    """
    ...


def memcpy(dst: Any, src: Any, len: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def memset(dst: Any, v: int, len: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def memmove(dst: Any, src: Any, len: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def memcmp(p1: Any, p2: Any, len: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def strlen(str: str, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def strnlen(str: str, max_len: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def strlcpy(dst: str, src: str, dst_size: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def strncpy(dst: str, src: str, dest_size: int, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def strcpy(dst: str, src: str, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def strcmp(s1: str, s2: str, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def strncmp(s1: str, s2: str, len: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def strdup(src: str, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def strndup(src: str, max_len: int, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def strcat(dst: str, src: str, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def strncat(dst: str, src: str, dest_size: int, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def strchr(str: str, c: int, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def mem_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def mem_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def mem_add_pool(mem: Any, bytes: int, /) -> "mem_pool_t":
    """
    No Docstrings Yet
    """
    ...


def mem_remove_pool(pool: "mem_pool_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def malloc(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def calloc(num: int, size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def zalloc(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def malloc_zeroed(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def free(src: Any, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def realloc(data_p: Any, new_size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def reallocf(data_p: Any, new_size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def malloc_core(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def free_core(src: Any, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def realloc_core(data_p: Any, new_size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def mem_test_core() -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def mem_test() -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def tick_inc(ms: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def tick_get() -> int:
    """
    No Docstrings Yet
    """
    ...


def tick_elaps(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def tick_diff(tick: int, prev_tick: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def delay_ms(ms: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def delay_set_cb(cb: "delay_cb_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def tick_set_cb(cb: "tick_get_cb_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def tick_get_cb() -> "tick_get_cb_t":
    """
    No Docstrings Yet
    """
    ...


def timer_handler() -> int:
    """
    No Docstrings Yet
    """
    ...


def timer_handler_run_in_period(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def timer_periodic_handler() -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_handler_set_resume_cb(cb: "timer_handler_resume_cb_t", data: Any, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_create_basic() -> "timer_t":
    """
    No Docstrings Yet
    """
    ...


def timer_create(timer_xcb: Callable, period: int, user_data: Any, /) -> "timer_t":
    """
    No Docstrings Yet
    """
    ...


def timer_enable(en: bool, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_get_idle() -> int:
    """
    No Docstrings Yet
    """
    ...


def timer_get_time_until_next() -> int:
    """
    No Docstrings Yet
    """
    ...


def trigo_sin(angle: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def trigo_cos(angle: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def cubic_bezier(x: int, x1: int, y1: int, x2: int, y2: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def bezier3(t: int, u0: int, u1: int, u2: int, u3: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def atan2(x: int, y: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def sqrt(x: int, q: "sqrt_res_t", mask: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def sqrt32(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def pow(base: int, exp: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def map(x: int, x1: int, y1: int, x2: int, y2: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def rand_set_seed(ms: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def rand(tick: int, prev_tick: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def async_call(async_xcb: Callable, user_data: Any, /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def async_call_cancel(async_xcb: Callable, user_data: Any, /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def anim_delete(var: Any, exec_cb: "anim_exec_xcb_t", /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def anim_delete_all() -> None:
    """
    No Docstrings Yet
    """
    ...


def anim_get(var: Any, exec_cb: "anim_exec_xcb_t", /) -> "anim_t":
    """
    No Docstrings Yet
    """
    ...


def anim_get_timer() -> "timer_t":
    """
    No Docstrings Yet
    """
    ...


def anim_count_running() -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_speed(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_speed_clamped(speed: int, min_time: int, max_time: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_resolve_speed(speed: int, start: int, end: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_speed_to_time(speed: int, start: int, end: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_refr_now() -> None:
    """
    No Docstrings Yet
    """
    ...


def anim_timeline_create() -> "anim_timeline_t":
    """
    No Docstrings Yet
    """
    ...


def pct(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def pct_to_px(v: int, base: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_format_get_bpp(cf: "color_format_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_format_get_size(cf: "color_format_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_format_has_alpha(src_cf: "color_format_t", /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def color_hex(c: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_make(r: int, g: int, b: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color32_make(r: int, g: int, b: int, a: int, /) -> "color32_t":
    """
    No Docstrings Yet
    """
    ...


def color_hex3(c: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_16_16_mix(c1: int, c2: int, mix: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_hsv_to_rgb(h: int, s: int, v: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_rgb_to_hsv(r8: int, g8: int, b8: int, /) -> "color_hsv_t":
    """
    No Docstrings Yet
    """
    ...


def color_white() -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_black() -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color24_luminance(c: Union[str, List[int]], /) -> int:
    """
    No Docstrings Yet
    """
    ...


def palette_main(p: "palette_t", /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def palette_lighten(p: "palette_t", lvl: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def palette_darken(p: "palette_t", lvl: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def draw_buf_get_handlers() -> "draw_buf_handlers_t":
    """
    No Docstrings Yet
    """
    ...


def draw_buf_get_font_handlers() -> "draw_buf_handlers_t":
    """
    No Docstrings Yet
    """
    ...


def draw_buf_get_image_handlers() -> "draw_buf_handlers_t":
    """
    No Docstrings Yet
    """
    ...


def draw_buf_align(buf: Any, color_format: "color_format_t", /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_buf_width_to_stride(w: int, color_format: "color_format_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def draw_buf_create(w: int, h: int, cf: "color_format_t", stride: int, /) -> "draw_buf_t":
    """
    No Docstrings Yet
    """
    ...


def utils_bsearch(key: Any, base: Any, n: int, size: int, cmp: List[int (], /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def iter_create(instance: Any, elem_size: int, context_size: int, next_cb: "iter_next_cb", /) -> "iter_t":
    """
    No Docstrings Yet
    """
    ...


def circle_buf_create(capacity: int, element_size: int, /) -> "circle_buf_t":
    """
    No Docstrings Yet
    """
    ...


def circle_buf_create_from_buf(buf: Any, capacity: int, element_size: int, /) -> "circle_buf_t":
    """
    No Docstrings Yet
    """
    ...


def circle_buf_create_from_array(array: "array_t", /) -> "circle_buf_t":
    """
    No Docstrings Yet
    """
    ...


def lock() -> None:
    """
    No Docstrings Yet
    """
    ...


def lock_isr() -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def unlock() -> None:
    """
    No Docstrings Yet
    """
    ...


def sleep_ms(ms: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def font_get_default() -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def text_get_size(size_res: "point_t", text: str, font: "font_t", letter_space: int, line_space: int, max_width: int, flag: "text_flag_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def layout_register(cb: Callable, user_data: Any, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def flex_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def grid_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def grid_fr(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def style_register_prop(flag: int, /) -> "style_prop_t":
    """
    No Docstrings Yet
    """
    ...


def style_get_num_custom_props() -> "style_prop_t":
    """
    No Docstrings Yet
    """
    ...


def style_prop_get_default(prop: "style_prop_t", /) -> "style_value_t":
    """
    No Docstrings Yet
    """
    ...


def style_prop_lookup_flags(prop: "style_prop_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def event_register_id() -> int:
    """
    No Docstrings Yet
    """
    ...


def event_code_get_name(code: "event_code_t", /) -> str:
    """
    No Docstrings Yet
    """
    ...


def display_create(hor_res: int, ver_res: int, /) -> "display_t":
    """
    No Docstrings Yet
    """
    ...


def display_get_default() -> "display_t":
    """
    No Docstrings Yet
    """
    ...


def screen_load(scr: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def screen_load_anim(scr: "obj", anim_type: "screen_load_anim_t", time: int, delay: int, auto_del: bool, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def screen_active() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def layer_top() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def layer_sys() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def layer_bottom() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def dpx(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def clamp_width(width: int, min_width: int, max_width: int, ref_width: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def clamp_height(width: int, min_width: int, max_width: int, ref_width: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def fs_get_drv(letter: str, /) -> "fs_drv_t":
    """
    No Docstrings Yet
    """
    ...


def fs_remove_drive(letter: str, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def fs_is_ready(letter: str, /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def fs_path_get_size(path: str, size_res: List[int], /) -> "fs_res_t":
    """
    No Docstrings Yet
    """
    ...


def fs_load_to_buf(buf: Any, buf_size: int, path: str, /) -> "fs_res_t":
    """
    No Docstrings Yet
    """
    ...


def fs_load_with_alloc(path: str, size: List[int], /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def fs_get_letters(buf: str, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def fs_get_ext(fn: str, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def fs_up(buf: str, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def fs_get_last(fn: str, /) -> str:
    """
    No Docstrings Yet
    """
    ...


def fs_path_join(buf: str, buf_sz: int, base: str, end: str, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def draw_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_create_unit(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_add_task(layer: "layer_t", coords: "area_t", type: "draw_task_type_t", /) -> "draw_task_t":
    """
    No Docstrings Yet
    """
    ...


def draw_finalize_task_creation(layer: "layer_t", t: "draw_task_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_dispatch() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_dispatch_wait_for_request() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_wait_for_finish() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_dispatch_request() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_get_unit_count() -> int:
    """
    No Docstrings Yet
    """
    ...


def draw_get_available_task(layer: "layer_t", t_prev: "draw_task_t", draw_unit_id: int, /) -> "draw_task_t":
    """
    No Docstrings Yet
    """
    ...


def draw_get_next_available_task(layer: "layer_t", t_prev: "draw_task_t", draw_unit_id: int, /) -> "draw_task_t":
    """
    No Docstrings Yet
    """
    ...


def draw_unit_send_event(name: str, code: "event_code_t", param: Any, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_layer_create(parent_layer: "layer_t", color_format: "color_format_t", area: "area_t", /) -> "layer_t":
    """
    No Docstrings Yet
    """
    ...


def draw_layer_init(layer: "layer_t", parent_layer: "layer_t", color_format: "color_format_t", area: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_layer_alloc_buf(layer: "layer_t", /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_layer_go_to_xy(layer: "layer_t", x: int, y: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_layer_create_drop_shadow(parent_layer: "layer_t", base: "draw_dsc_base_t", area: "area_t", /) -> "layer_t":
    """
    No Docstrings Yet
    """
    ...


def draw_layer_finish_drop_shadow(drop_shadow_layer: "layer_t", base: "draw_dsc_base_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_fill(layer: "layer_t", dsc: "draw_fill_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_border(layer: "layer_t", dsc: "draw_border_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_box_shadow(layer: "layer_t", dsc: "draw_box_shadow_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_rect(layer: "layer_t", dsc: "draw_rect_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_label(layer: "layer_t", dsc: "draw_label_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_character(layer: "layer_t", dsc: "draw_label_dsc_t", point: "point_t", unicode_letter: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_letter(layer: "layer_t", dsc: "draw_letter_dsc_t", point: "point_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_image(layer: "layer_t", dsc: "draw_image_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_layer(layer: "layer_t", dsc: "draw_image_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_line(layer: "layer_t", dsc: "draw_line_dsc_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_arc(layer: "layer_t", dsc: "draw_arc_dsc_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_arc_get_area(x: int, y: int, radius: int, start_angle: "value_precise_t", end_angle: "value_precise_t", w: int, rounded: bool, area: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_triangle(layer: "layer_t", draw_dsc: "draw_triangle_dsc_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_blur(layer: "layer_t", dsc: "draw_blur_dsc_t", coords: "area_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def group_create() -> "group_t":
    """
    No Docstrings Yet
    """
    ...


def group_get_default() -> "group_t":
    """
    No Docstrings Yet
    """
    ...


def group_swap_obj(obj: "obj", parent: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def group_remove_obj(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def group_focus_obj(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def group_get_count() -> int:
    """
    No Docstrings Yet
    """
    ...


def group_by_index(index: int, /) -> "group_t":
    """
    No Docstrings Yet
    """
    ...


def indev_create() -> "indev_t":
    """
    No Docstrings Yet
    """
    ...


def indev_read_timer_cb(arg0: "timer_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def indev_active() -> "indev_t":
    """
    No Docstrings Yet
    """
    ...


def indev_get_active_obj() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def indev_search_obj(obj: "obj", point: "point_t", /) -> "obj":
    """
    No Docstrings Yet
    """
    ...


def objid_builtin_destroy() -> None:
    """
    No Docstrings Yet
    """
    ...


def refr_now(disp: "display_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def display_refr_timer(arg0: "timer_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def gridnav_add(obj: "obj", ctrl: "gridnav_ctrl_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def gridnav_remove(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def gridnav_set_focused(tv: "obj", tile_obj: "obj", anim_en: "anim_enable_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def binfont_create(path: str, /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def binfont_destroy(font: "font_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def imgfont_create(height: int, path_cb: Callable, user_data: Any, /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def imgfont_destroy(font: "font_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def span_stack_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def span_stack_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def sysmon_create(disp: "display_t", /) -> "obj":
    """
    No Docstrings Yet
    """
    ...


def sysmon_show_performance(disp: "display_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def sysmon_hide_performance(disp: "display_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def sysmon_performance_dump(disp: "display_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def sysmon_performance_resume(disp: "display_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def sysmon_performance_pause(disp: "display_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_info(decoder: "image", dsc: "image", header: "image", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_get_area(decoder: "image", dsc: "image", full_area: "area_t", decoded_area: "area_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_open(decoder: "image", dsc: "image", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_close(decoder: "image", dsc: "image", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def bmp_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def bmp_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def lodepng_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def lodepng_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def tjpgd_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def tjpgd_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_i1_to_argb8888(buf_i1: Any, buf_argb8888: Any, width: int, height: int, buf_i1_stride: int, buf_argb8888_stride: int, index0_color: int, index1_color: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_rgb565_swap(buf: Any, buf_size_px: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_i1_invert(buf: Any, buf_size_px: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_i1_convert_to_vtiled(buf: Any, buf_size: int, width: int, height: int, out_buf: Any, out_buf_size: int, bit_order_lsb: bool, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_rotate(src: Any, dest: Any, src_width: int, src_height: int, src_stride: int, dest_stride: int, rotation: "display_rotation_t", color_format: "color_format_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def snapshot_take(obj: "obj", cf: "color_format_t", /) -> "draw_buf_t":
    """
    No Docstrings Yet
    """
    ...


def snapshot_create_draw_buf(obj: "obj", cf: "color_format_t", /) -> "draw_buf_t":
    """
    No Docstrings Yet
    """
    ...


def snapshot_reshape_draw_buf(obj: "obj", draw_buf: "draw_buf_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def snapshot_take_to_draw_buf(obj: "obj", cf: "color_format_t", draw_buf: "draw_buf_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def snapshot_free(dsc: "image", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def snapshot_take_to_buf(obj: "obj", cf: "color_format_t", dsc: "image", buf: Any, buf_size: int, /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def theme_create() -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_from_obj(obj: "obj", /) -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_apply(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def theme_get_font_small(obj: "obj", /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_font_normal(obj: "obj", /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_font_large(obj: "obj", /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_color_primary(obj: "obj", /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_color_secondary(obj: "obj", /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def theme_default_init(disp: "display_t", color_primary: "color_t", color_secondary: "color_t", dark: bool, font: "font_t", /) -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_default_is_inited() -> bool:
    """
    No Docstrings Yet
    """
    ...


def theme_default_get() -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_default_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def theme_simple_init(disp: "display_t", /) -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_simple_is_inited() -> bool:
    """
    No Docstrings Yet
    """
    ...


def theme_simple_get() -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_simple_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...

