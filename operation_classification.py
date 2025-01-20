from enum import Enum

# Randomiser flag pool: 
#   - 1: does not have active ht flag or flag only becomes available later in the op
#   - 2: ht is available at start of op
#   - 3: op is muliop (ht distinction not done for now)

class OpClassification(Enum):
    NO_HT  = 1
    HT     = 2
    MULTI  = 3
    FORGET = 4