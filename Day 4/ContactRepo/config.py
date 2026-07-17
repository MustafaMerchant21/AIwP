import re
COUNT = 0

FILE_NAME = "contact.xlsx"
NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z\s.'-]{1,48}[A-Za-z]$")
EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
COUNTRY_CODE_PATTERN = re.compile(r"^[1-9][0-9]{0,3}$")
PHONE_PATTERN = re.compile(r"^[0-9]{10,15}$")
RECORD_ID_PATTERN = re.compile(r"^[1-9][0-9]*$")


FILE_NAME = "contact.xlsx"
FONT = "Segoe UI"

BG            = "#EEF1F6"   # app bg
CARD          = "#FFFFFF"
BORDER        = "#E2E8F0"
BORDER_FOCUS  = "#6366F1"

HEADER_BG     = "#0F172A"
HEADER_FG     = "#F8FAFC"
HEADER_MUTED  = "#94A3B8"
HEADER_CHIP   = "#1E293B"

PRIMARY       = "#4F46E5"   # main accent, used sparingly
PRIMARY_DARK  = "#4338CA"
PRIMARY_TINT  = "#EEF2FF"
PRIMARY_DEEP  = "#3730A3"

TEXT          = "#0F172A"
TEXT_2        = "#475569"
MUTED         = "#94A3B8"

SUCCESS       = "#047857"
SUCCESS_TINT  = "#ECFDF5"
SUCCESS_HOVER = "#D1FAE5"

DANGER        = "#DC2626"
DANGER_DEEP   = "#B91C1C"
DANGER_TINT   = "#FEF2F2"
DANGER_HOVER  = "#FEE2E2"

NEUTRAL_TINT  = "#F1F5F9"
NEUTRAL_HOVER = "#E2E8F0"
NEUTRAL_TEXT  = "#334155"

ROW_EVEN      = "#FFFFFF"
ROW_ODD       = "#F8FAFC"
ROW_SELECTED  = "#E0E7FF"
ROW_SEL_FG    = "#1E1B4B"

HEAD_BG       = "#F8FAFC"   # table heading bg, deliberately not accent-colored
HEAD_FG       = "#475569"

SEARCH_PLACEHOLDER = "Search name, email, or phone…"