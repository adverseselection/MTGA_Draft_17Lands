import os
import getpass
# Global Constants
## The different types of draft.

LOG_TYPE_DEBUG = "mtgaTool"
LOG_TYPE_DRAFT = "draftLog"

BASIC_LANDS = ["Island","Mountain","Swamp","Plains","Forest"]

LIMITED_TYPE_UNKNOWN            = 0
LIMITED_TYPE_DRAFT_PREMIER_V1   = 1
LIMITED_TYPE_DRAFT_PREMIER_V2   = 2
LIMITED_TYPE_DRAFT_QUICK        = 3
LIMITED_TYPE_DRAFT_TRADITIONAL  = 4
LIMITED_TYPE_SEALED             = 5
LIMITED_TYPE_SEALED_TRADITIONAL = 6

URL_17LANDS = "https://www.17lands.com"

IMAGE_17LANDS_SITE_PREFIX = "/static/images/"

DATA_FIELD_17LANDS_OHWR       = "opening_hand_win_rate"
DATA_FIELD_17LANDS_NGOH       = "opening_hand_game_count"
DATA_FIELD_17LANDS_GPWR       = "win_rate"
DATA_FIELD_17LANDS_NGP        = "game_count"
DATA_FIELD_17LANDS_GIHWR      = "ever_drawn_win_rate"
DATA_FIELD_17LANDS_IWD        = "drawn_improvement_win_rate"
DATA_FIELD_17LANDS_ALSA       = "avg_seen"
DATA_FIELD_17LANDS_GIH        = "ever_drawn_game_count"
DATA_FIELD_17LANDS_ATA        = "avg_pick"
DATA_FIELD_17LANDS_NGND       = "never_drawn_game_count"
DATA_FIELD_17LANDS_GNDWR      = "never_drawn_win_rate"
DATA_FIELD_17LANDS_IMAGE      = "url"
DATA_FIELD_17LANDS_IMAGE_BACK = "url_back"


DATA_FIELD_GIHWR = "gihwr"
DATA_FIELD_OHWR = "ohwr"
DATA_FIELD_GPWR = "gpwr"
DATA_FIELD_ALSA = "alsa"
DATA_FIELD_IWD = "iwd"
DATA_FIELD_ATA = "ata"
DATA_FIELD_NGP = "ngp"
DATA_FIELD_NGOH = "ngoh"
DATA_FIELD_GIH = "gih"
DATA_FIELD_GNDWR = "gndwr"
DATA_FIELD_NGND = "ngnd"

DATA_SECTION_IMAGES = "image"
DATA_SECTION_RATINGS = "ratings"

DATA_FIELD_CMC = "cmc"
DATA_FIELD_COLORS = "colors"
DATA_FIELD_NAME = "name"
DATA_FIELD_TYPES = "types"
DATA_FIELD_DECK_COLORS = "deck_colors"
DATA_FIELD_COUNT = "count"
DATA_FIELD_DISABLED = "disabled"

DATA_FIELDS_LIST = [DATA_FIELD_GIHWR, 
                    DATA_FIELD_OHWR, 
                    DATA_FIELD_GPWR, 
                    DATA_FIELD_GNDWR,
                    DATA_FIELD_ALSA,
                    DATA_FIELD_ATA, 
                    DATA_FIELD_IWD,
                    DATA_FIELD_NGP,
                    DATA_FIELD_NGOH,
                    DATA_FIELD_GIH,
                    DATA_FIELD_NGND]

DATA_SET_FIELDS = [DATA_FIELD_GIHWR, 
                   DATA_FIELD_OHWR, 
                   DATA_FIELD_GPWR, 
                   DATA_FIELD_ALSA, 
                   DATA_FIELD_IWD, 
                   DATA_FIELD_CMC, 
                   DATA_FIELD_COLORS, 
                   DATA_FIELD_NAME, 
                   DATA_FIELD_TYPES,
                   DATA_SECTION_IMAGES,
                   DATA_FIELD_DECK_COLORS]

FILTER_OPTION_ALL_DECKS = "All Decks"
FILTER_OPTION_AUTO = "Auto"
FILTER_OPTION_TIER = "Tier"

#FIELD_LABEL_ATA = "Average Taken At (ATA)"
#FIELD_LABEL_ALSA = "Average Last Seen At (ALSA)"
#FIELD_LABEL_IWD = "Improvement When Drawn (IWD)"
#FIELD_LABEL_OHWR = "Opening Hand Win Rate (OHWR)"
#FIELD_LABEL_GPWR = "Games Played Win Rate (GPWR)"
#FIELD_LABEL_GIHWR = "Games In Hand Win Rate (GIHWR)"
FIELD_LABEL_ATA = "ATA"
FIELD_LABEL_ALSA = "ALSA"
FIELD_LABEL_IWD = "IWD"
FIELD_LABEL_OHWR = "OHWR"
FIELD_LABEL_GPWR = "GPWR"
FIELD_LABEL_GIHWR = "GIHWR"
FIELD_LABEL_DISABLED = "DISABLED"
FIELD_LABEL_COLORS = "COLORS"
FIELD_LABEL_GNDWR = "GNDWR"

DATA_SET_VERSION_3 = 3.0

WIN_RATE_OPTIONS = [DATA_FIELD_GIHWR, DATA_FIELD_OHWR, DATA_FIELD_GPWR, DATA_FIELD_GNDWR]
NON_COLORS_OPTIONS = WIN_RATE_OPTIONS + [DATA_FIELD_IWD, DATA_FIELD_ALSA, DATA_FIELD_ATA]
DECK_COLORS = [FILTER_OPTION_ALL_DECKS,"W","U","B","R","G","WU","WB","WR","WG","UB","UR","UG","BR","BG","RG","WUB","WUR","WUG","WBR","WBG","WRG","UBR","UBG","URG","BRG"]
COLUMN_OPTIONS = NON_COLORS_OPTIONS
DECK_FILTERS = [FILTER_OPTION_AUTO] + DECK_COLORS

COLUMN_2_DEFAULT = FIELD_LABEL_ALSA
COLUMN_3_DEFAULT = FIELD_LABEL_IWD
COLUMN_4_DEFAULT = FIELD_LABEL_GIHWR
COLUMN_5_DEFAULT = FIELD_LABEL_DISABLED
COLUMN_6_DEFAULT = FIELD_LABEL_DISABLED
COLUMN_7_DEFAULT = FIELD_LABEL_DISABLED

DECK_FILTER_DEFAULT = FILTER_OPTION_AUTO

DRAFT_LOG_FOLDER = os.path.join(os.getcwd(), "Logs")

TIER_FOLDER = os.path.join(os.getcwd(), FILTER_OPTION_TIER)
TIER_FILE_PREFIX = "Tier_"

DRAFT_DETECTION_CATCH_ALL = ["Draft", "draft"]

DRAFT_START_STRING_EVENT_JOIN = "[UnityCrossThreadLogger]==> Event_Join "
DRAFT_START_STRING_BOT_DRAFT = "[UnityCrossThreadLogger]==> BotDraft_DraftStatus "

DRAFT_START_STRINGS = [DRAFT_START_STRING_EVENT_JOIN, DRAFT_START_STRING_BOT_DRAFT]

DATA_SOURCES_NONE = {"None" : ""}

DECK_FILTER_FORMAT_NAMES = "Names"
DECK_FILTER_FORMAT_COLORS = "Colors"
DECK_FILTER_FORMAT_SET_NAMES = "Set Names"

DECK_FILTER_FORMAT_LIST = [DECK_FILTER_FORMAT_COLORS, DECK_FILTER_FORMAT_NAMES]

RESULT_FORMAT_WIN_RATE = "Percentage"
RESULT_FORMAT_RATING = "Rating (*/5)"

RESULT_FORMAT_LIST = [RESULT_FORMAT_WIN_RATE, RESULT_FORMAT_RATING]

LOCAL_DATA_FOLDER_PATH_WINDOWS = os.path.join("Wizards of the Coast","MTGA","MTGA_Data")
LOCAL_DATA_FOLDER_PATH_OSX = os.path.join("Library","Application Support","com.wizards.mtga")

LOCAL_DOWNLOADS_DATA = os.path.join("Downloads","Raw")

LOCAL_DATA_FILE_PREFIX_CARDS = "Raw_cards_"
LOCAL_DATA_FILE_PREFIX_DATABASE = "Raw_CardDatabase_"

LOCAL_DATABASE_TABLE_LOCALIZATION = "Localizations"
LOCAL_DATABASE_TABLE_ENUMERATOR = "Enums"

LOCAL_DATABASE_LOCALIZATION_COLUMN_ID = "LocId"
LOCAL_DATABASE_LOCALIZATION_COLUMN_FORMAT = "Formatted"
LOCAL_DATABASE_LOCALIZATION_COLUMN_TEXT = "enUS"

LOCAL_DATABASE_ENUMERATOR_COLUMN_ID = "LocId"
LOCAL_DATABASE_ENUMERATOR_COLUMN_TYPE = "Type"
LOCAL_DATABASE_ENUMERATOR_COLUMN_VALUE = "Value"

LOCAL_DATABASE_ENUMERATOR_TYPE_COLOR = "Color"
LOCAL_DATABASE_ENUMERATOR_TYPE_CARD_TYPES = "CardType"

LOCAL_DATABASE_LOCALIZATION_QUERY = f"""SELECT 
                                            A.{LOCAL_DATABASE_LOCALIZATION_COLUMN_ID}, 
                                            A.{LOCAL_DATABASE_LOCALIZATION_COLUMN_FORMAT}, 
                                            A.{LOCAL_DATABASE_LOCALIZATION_COLUMN_TEXT}
                                        FROM {LOCAL_DATABASE_TABLE_LOCALIZATION} A INNER JOIN(
                                            SELECT 
                                                {LOCAL_DATABASE_LOCALIZATION_COLUMN_ID},
                                                min({LOCAL_DATABASE_LOCALIZATION_COLUMN_FORMAT}) AS MIN_FORMAT 
                                            FROM {LOCAL_DATABASE_TABLE_LOCALIZATION} 
                                            GROUP BY {LOCAL_DATABASE_LOCALIZATION_COLUMN_ID}) 
                                        B ON A.{LOCAL_DATABASE_LOCALIZATION_COLUMN_ID} = B.{LOCAL_DATABASE_LOCALIZATION_COLUMN_ID} 
                                        AND A.{LOCAL_DATABASE_LOCALIZATION_COLUMN_FORMAT} = B.MIN_FORMAT"""
                                        
LOCAL_DATABASE_ENUMERATOR_QUERY = f"""SELECT
                                        {LOCAL_DATABASE_ENUMERATOR_COLUMN_ID},
                                        {LOCAL_DATABASE_ENUMERATOR_COLUMN_TYPE},
                                        {LOCAL_DATABASE_ENUMERATOR_COLUMN_VALUE}
                                      FROM {LOCAL_DATABASE_TABLE_ENUMERATOR}
                                      WHERE {LOCAL_DATABASE_ENUMERATOR_COLUMN_TYPE} 
                                      IN ('{LOCAL_DATABASE_ENUMERATOR_TYPE_COLOR}', 
                                          '{LOCAL_DATABASE_ENUMERATOR_TYPE_CARD_TYPES}')"""

LOCAL_CARDS_KEY_SET = "set"
LOCAL_CARDS_KEY_DIGITAL_RELEASE_SET = "digitalreleaseset"
LOCAL_CARDS_KEY_GROUP_ID = "grpid"
LOCAL_CARDS_KEY_TOKEN = "istoken"
LOCAL_CARDS_KEY_LINKED_FACES = "linkedfaces"
LOCAL_CARDS_KEY_TYPES = "types"
LOCAL_CARDS_KEY_TITLE_ID = "titleid"
LOCAL_CARDS_KEY_CMC = "cmc"
LOCAL_CARDS_KEY_COLOR_ID = "coloridentity"
LOCAL_CARDS_KEY_CASTING_COST = "castingcost"


SETS_FOLDER = os.path.join(os.getcwd(), "Sets")
SET_FILE_SUFFIX = "Data.json"

CARD_RATINGS_BACKOFF_DELAY_SECONDS = 30
CARD_RATINGS_INTER_DELAY_SECONDS = 2

PLATFORM_ID_OSX = "darwin"
PLATFORM_ID_WINDOWS = "win32"

LOG_LOCATION_WINDOWS = os.path.join('Users', getpass.getuser(), "AppData", "LocalLow","Wizards Of The Coast","MTGA","Player.log")
LOG_LOCATION_OSX = os.path.join("Library","Logs","Wizards of the Coast","MTGA","Player.log")

DEFAULT_GIHWR_AVERAGE = 0.0

WINDOWS_DRIVES = ["C:/","D:/","E:/","F:/"]
WINDOWS_PROGRAM_FILES = ["Program Files","Program Files (x86)"]


SET_TYPE_EXPANSION = "expansion"
SET_TYPE_ALCHEMY = "alchemy"
SET_TYPE_MASTERS = "masters"

SET_LIST_ARENA = "arena"
SET_LIST_SCRYFALL = "scryfall"
SET_LIST_17LANDS = "17Lands"

SUPPORTED_SET_TYPES = [SET_TYPE_EXPANSION, SET_TYPE_ALCHEMY, SET_TYPE_MASTERS]

TABLE_STYLE = "Treeview"

DEBUG_LOG_FOLDER = os.path.join(os.getcwd(), "Debug")
DEBUG_LOG_FILE = os.path.join(DEBUG_LOG_FOLDER, "debug.log")

TEMP_FOLDER = os.path.join(os.getcwd(), "Temp")
TEMP_LOCALIZATION_FILE = os.path.join(TEMP_FOLDER, "temp_localization.json")

BW_ROW_COLOR_ODD_TAG = "bw_odd"
BW_ROW_COLOR_EVEN_TAG = "bw_even"
CARD_ROW_COLOR_WHITE_TAG = "white_card"
CARD_ROW_COLOR_RED_TAG = "red_card"
CARD_ROW_COLOR_BLUE_TAG = "blue_card"
CARD_ROW_COLOR_BLACK_TAG = "black_card"
CARD_ROW_COLOR_GREEN_TAG = "green_card"
CARD_ROW_COLOR_GOLD_TAG = "gold_card"

#Dictionaries
## Used to identify the limited type based on log string
LIMITED_TYPES_DICT = {
    "PremierDraft"     : LIMITED_TYPE_DRAFT_PREMIER_V1,
    "QuickDraft"       : LIMITED_TYPE_DRAFT_QUICK,
    "TradDraft"        : LIMITED_TYPE_DRAFT_TRADITIONAL,
    "BotDraft"         : LIMITED_TYPE_DRAFT_QUICK,
    "Sealed"           : LIMITED_TYPE_SEALED,
    "TradSealed"       : LIMITED_TYPE_SEALED_TRADITIONAL,
}

COLOR_NAMES_DICT = {
    "W"   : "White",
    "U"   : "Blue",
    "B"   : "Black",
    "R"   : "Red",
    "G"   : "Green",
    "WU"  : "Azorius",
    "UB"  : "Dimir",
    "BR"  : "Rakdos",
    "RG"  : "Gruul",
    "WG"  : "Selesnya",
    "WB"  : "Orzhov",
    "BG"  : "Golgari",
    "UG"  : "Simic",
    "UR"  : "Izzet",
    "WR"  : "Boros",
    "WUR" : "Jeskai",
    "UBG" : "Sultai",
    "WBR" : "Mardu",
    "URG" : "Temur",
    "WBG" : "Abzan",
    "WUB" : "Esper",
    "UBR" : "Grixis",
    "BRG" : "Jund",
    "WRG" : "Naya",
    "WUG" : "Bant",
}

CARD_COLORS_DICT = {
    "White" : "W",
    "Black" : "B",
    "Blue"  : "U",
    "Red"   : "R",
    "Green" : "G",
}

PLATFORM_LOG_DICT = {
    PLATFORM_ID_OSX     : LOG_LOCATION_OSX,
    PLATFORM_ID_WINDOWS : LOG_LOCATION_WINDOWS,
}

WIN_RATE_FIELDS_DICT = {
    DATA_FIELD_GIHWR : DATA_FIELD_GIH,
    DATA_FIELD_OHWR  : DATA_FIELD_NGOH,
    DATA_FIELD_GPWR  : DATA_FIELD_NGP,
    DATA_FIELD_GNDWR : DATA_FIELD_NGND,
}

DATA_FIELD_17LANDS_DICT = {
    DATA_FIELD_GIHWR    : DATA_FIELD_17LANDS_GIHWR,
    DATA_FIELD_OHWR     : DATA_FIELD_17LANDS_OHWR,
    DATA_FIELD_GPWR     : DATA_FIELD_17LANDS_GPWR,
    DATA_FIELD_ALSA     : DATA_FIELD_17LANDS_ALSA,
    DATA_FIELD_IWD      : DATA_FIELD_17LANDS_IWD,
    DATA_FIELD_ATA      : DATA_FIELD_17LANDS_ATA,
    DATA_FIELD_NGP      : DATA_FIELD_17LANDS_NGP,
    DATA_FIELD_NGOH     : DATA_FIELD_17LANDS_NGOH,
    DATA_FIELD_GIH      : DATA_FIELD_17LANDS_GIH,
    DATA_FIELD_GNDWR    : DATA_FIELD_17LANDS_GNDWR,
    DATA_FIELD_NGND     : DATA_FIELD_17LANDS_NGND,
    DATA_SECTION_IMAGES : [DATA_FIELD_17LANDS_IMAGE, DATA_FIELD_17LANDS_IMAGE_BACK]
}

COLUMNS_OPTIONS_MAIN_DICT = {
    FIELD_LABEL_ATA      : DATA_FIELD_ATA,
    FIELD_LABEL_ALSA     : DATA_FIELD_ALSA,
    FIELD_LABEL_IWD      : DATA_FIELD_IWD,
    FIELD_LABEL_OHWR     : DATA_FIELD_OHWR,
    FIELD_LABEL_GPWR     : DATA_FIELD_GPWR,
    FIELD_LABEL_GIHWR    : DATA_FIELD_GIHWR,
    FIELD_LABEL_GNDWR    : DATA_FIELD_GNDWR,
    FIELD_LABEL_COLORS   : DATA_FIELD_COLORS,
}

COLUMNS_OPTIONS_EXTRA_DICT = {
    FIELD_LABEL_DISABLED : DATA_FIELD_DISABLED,
    FIELD_LABEL_ATA      : DATA_FIELD_ATA,
    FIELD_LABEL_ALSA     : DATA_FIELD_ALSA,
    FIELD_LABEL_IWD      : DATA_FIELD_IWD,
    FIELD_LABEL_OHWR     : DATA_FIELD_OHWR,
    FIELD_LABEL_GPWR     : DATA_FIELD_GPWR,
    FIELD_LABEL_GIHWR    : DATA_FIELD_GIHWR,
    FIELD_LABEL_GNDWR    : DATA_FIELD_GNDWR,
    FIELD_LABEL_COLORS   : DATA_FIELD_COLORS,
}

STATS_HEADER_CONFIG = {"Colors"   : {"width" : .19, "anchor" : "w"},
                       "1"        : {"width" : .11, "anchor" : "c"},
                       "2"        : {"width" : .11, "anchor" : "c"},
                       "3"        : {"width" : .11, "anchor" : "c"},
                       "4"        : {"width" : .11, "anchor" : "c"},
                       "5"        : {"width" : .11, "anchor" : "c"},
                       "6+"       : {"width" : .11, "anchor" : "c"},
                       "Total"    : {"width" : .15, "anchor" : "c"}}
                       
ROW_TAGS_BW_DICT = {
    BW_ROW_COLOR_ODD_TAG      : ("Helvetica Neue", "#3d3d3d", "#e6ecec"),
    BW_ROW_COLOR_EVEN_TAG     : ("Helvetica Neue", "#333333", "#e6ecec"),
}

ROW_TAGS_COLORS_DICT = {
    CARD_ROW_COLOR_WHITE_TAG  : ("Helvetica Neue", "#E9E9E9", "#000000"),
    CARD_ROW_COLOR_RED_TAG    : ("Helvetica Neue", "#FF6C6C", "#000000"),
    CARD_ROW_COLOR_BLUE_TAG   : ("Helvetica Neue", "#6078F3", "#000000"),
    CARD_ROW_COLOR_BLACK_TAG  : ("Helvetica Neue", "#BFBFBF", "#000000"),
    CARD_ROW_COLOR_GREEN_TAG  : ("Helvetica Neue", "#60DC68", "#000000"),
    CARD_ROW_COLOR_GOLD_TAG   : ("Helvetica Neue", "#F0E657", "#000000"),
}
                       