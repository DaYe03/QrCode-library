MODE_NUMBER = 1
MODE_ALPHANUMERIC = 2
MODE_BYTE = 4
MODE_KANJI = 8
MODE_ECI = 7
MODE_MIXED = 0

ERROR_CORRECTION_LEVEL_L = 1
ERROR_CORRECTION_LEVEL_M = 2
ERROR_CORRECTION_LEVEL_Q = 3
ERROR_CORRECTION_LEVEL_H = 4

FONT_SIZE_SMALL = 1
FONT_SIZE_MEDIUM = 2
FONT_SIZE_LARGE = 3
FONT_SIZE_LARGE_LARGE = 4

POSITION_TOP_LEFT = 1
POSITION_TOP_RIGHT = 2
POSITION_BOTTOM_LEFT = 3
POSITION_BOTTOM_RIGHT = 4
POSITION_MIDDLE = 5

EC_CODEWORDS = {
    1: {
        # total data codewords, ec codewords per block, number of blocks in group 1, data codewords of group 1s blocks, number of blocks in group 2, data codewords of group 2s blocks 
        ERROR_CORRECTION_LEVEL_L: [19, 7, 1, 19, 0, 0], 
        ERROR_CORRECTION_LEVEL_M: [16, 10, 1, 16, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [13, 13, 1, 13, 0, 0],
        ERROR_CORRECTION_LEVEL_H: [9, 17, 1, 9, 0, 0]
    },
    2: {
        ERROR_CORRECTION_LEVEL_L: [34, 10, 1, 34, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [28, 16, 1, 28, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [22, 22, 1, 22, 0, 0],
        ERROR_CORRECTION_LEVEL_H: [16, 28, 1, 16, 0, 0]
    },
    3: {
        ERROR_CORRECTION_LEVEL_L: [55, 15, 1, 55, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [44, 26, 1, 44, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [34, 18, 2, 17, 0, 0],
        ERROR_CORRECTION_LEVEL_H: [26, 22, 2, 13, 0, 0]
    },
    4: {
        ERROR_CORRECTION_LEVEL_L: [80, 20, 1, 80, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [64, 18, 2, 32, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [48, 26, 2, 24, 0, 0],
        ERROR_CORRECTION_LEVEL_H: [36, 16, 4, 9, 0, 0]
    },
    5: {
        ERROR_CORRECTION_LEVEL_L: [108, 26, 1, 108, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [86, 24, 2, 43, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [62, 18, 2, 15, 2, 16],
        ERROR_CORRECTION_LEVEL_H: [46, 22, 2, 11, 2, 12]
    },
    6: {
        ERROR_CORRECTION_LEVEL_L: [136, 18, 2, 68, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [108, 16, 4, 27, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [76, 24, 4, 19, 0, 0],
        ERROR_CORRECTION_LEVEL_H: [60, 28, 4, 15, 0, 0]
    },
    7: {
        ERROR_CORRECTION_LEVEL_L: [156, 20, 2, 78, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [124, 18, 4, 31, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [88, 18, 2, 14, 4, 15],
        ERROR_CORRECTION_LEVEL_H: [66, 26, 4, 13, 1, 14]
    },
    8: {
        ERROR_CORRECTION_LEVEL_L: [194, 24, 2, 97, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [154, 22, 2, 38, 2, 39],
        ERROR_CORRECTION_LEVEL_Q: [110, 22, 4, 18, 2, 19],
        ERROR_CORRECTION_LEVEL_H: [86, 26, 4, 14, 2, 15]
    },
    9: {
        ERROR_CORRECTION_LEVEL_L: [232, 30, 2, 116, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [182, 22, 3, 36, 2, 37],
        ERROR_CORRECTION_LEVEL_Q: [132, 20, 4, 16, 4, 17],
        ERROR_CORRECTION_LEVEL_H: [100, 24, 4, 12, 4, 13]
    },
    10: {
        ERROR_CORRECTION_LEVEL_L: [274, 18, 2, 68, 2, 69],
        ERROR_CORRECTION_LEVEL_M: [216, 26, 4, 43, 1, 44],
        ERROR_CORRECTION_LEVEL_Q: [154, 24, 6, 19, 2, 20],
        ERROR_CORRECTION_LEVEL_H: [122, 28, 6, 15, 2, 16]
    },
    11: {
        ERROR_CORRECTION_LEVEL_L: [324, 20, 4, 81, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [254, 30, 1, 50, 4, 51],
        ERROR_CORRECTION_LEVEL_Q: [180, 28, 4, 22, 4, 23],
        ERROR_CORRECTION_LEVEL_H: [140, 24, 3, 12, 8, 13]
    },
    12: {
        ERROR_CORRECTION_LEVEL_L: [370, 24, 2, 92, 2, 93],
        ERROR_CORRECTION_LEVEL_M: [290, 22, 6, 36, 2, 37],
        ERROR_CORRECTION_LEVEL_Q: [206, 26, 4, 20, 6, 21],
        ERROR_CORRECTION_LEVEL_H: [158, 28, 7, 14, 4, 15]
    },
    13: {
        ERROR_CORRECTION_LEVEL_L: [428, 26, 4, 107, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [334, 22, 8, 37, 1, 38],
        ERROR_CORRECTION_LEVEL_Q: [244, 24, 8, 20, 4, 21],
        ERROR_CORRECTION_LEVEL_H: [180, 22, 12, 11, 4, 12]
    },
    14: {
        ERROR_CORRECTION_LEVEL_L: [461, 30, 3, 115, 1, 116],
        ERROR_CORRECTION_LEVEL_M: [365, 24, 4, 40, 5, 41],
        ERROR_CORRECTION_LEVEL_Q: [261, 20, 11, 16, 5, 17],
        ERROR_CORRECTION_LEVEL_H: [197, 24, 11, 12, 5, 13]
    },
    15: {
        ERROR_CORRECTION_LEVEL_L: [523, 22, 5, 87, 1, 88],
        ERROR_CORRECTION_LEVEL_M: [415, 24, 5, 41, 5, 42],
        ERROR_CORRECTION_LEVEL_Q: [295, 30, 5, 24, 7, 25],
        ERROR_CORRECTION_LEVEL_H: [223, 24, 11, 12, 7, 13]
    },
    16: {
        ERROR_CORRECTION_LEVEL_L: [589, 24, 5, 98, 1, 99],
        ERROR_CORRECTION_LEVEL_M: [453, 28, 7, 45, 3, 46],
        ERROR_CORRECTION_LEVEL_Q: [325, 24, 15, 19, 2, 20],
        ERROR_CORRECTION_LEVEL_H: [253, 30, 3, 15, 13, 16]
    },
    17: {
        ERROR_CORRECTION_LEVEL_L: [647, 28, 1, 107, 5, 108],
        ERROR_CORRECTION_LEVEL_M: [507, 28, 10, 46, 1, 47],
        ERROR_CORRECTION_LEVEL_Q: [367, 28, 1, 22, 15, 23],
        ERROR_CORRECTION_LEVEL_H: [283, 28, 2, 14, 17, 15]
    },
    18: {
        ERROR_CORRECTION_LEVEL_L: [721, 30, 5, 120, 1, 121],
        ERROR_CORRECTION_LEVEL_M: [563, 26, 9, 43, 4, 44],
        ERROR_CORRECTION_LEVEL_Q: [397, 28, 17, 22, 1, 23],
        ERROR_CORRECTION_LEVEL_H: [313, 28, 2, 14, 19, 15]
    },
    19: {
        ERROR_CORRECTION_LEVEL_L: [795, 28, 3, 113, 4, 114],
        ERROR_CORRECTION_LEVEL_M: [627, 26, 3, 44, 11, 45],
        ERROR_CORRECTION_LEVEL_Q: [445, 26, 17, 21, 4, 22],
        ERROR_CORRECTION_LEVEL_H: [341, 26, 9, 13, 16, 14]
    },
    20: {
        ERROR_CORRECTION_LEVEL_L: [861, 28, 3, 107, 5, 108],
        ERROR_CORRECTION_LEVEL_M: [669, 26, 3, 41, 13, 42],
        ERROR_CORRECTION_LEVEL_Q: [485, 30, 15, 24, 5, 25],
        ERROR_CORRECTION_LEVEL_H: [385, 28, 15, 15, 10, 16]
    },
    21: {
        ERROR_CORRECTION_LEVEL_L: [932, 28, 4, 116, 4, 117],
        ERROR_CORRECTION_LEVEL_M: [714, 26, 17, 42, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [512, 28, 17, 22, 6, 23],
        ERROR_CORRECTION_LEVEL_H: [406, 30, 19, 16, 6, 17]
    },
    22: {
        ERROR_CORRECTION_LEVEL_L: [1006, 28, 2, 111, 7, 112],
        ERROR_CORRECTION_LEVEL_M: [782, 28, 17, 46, 0, 0],
        ERROR_CORRECTION_LEVEL_Q: [568, 30, 7, 24, 16, 25],
        ERROR_CORRECTION_LEVEL_H: [442, 30, 34, 13, 0, 0]
    },
    23: {
        ERROR_CORRECTION_LEVEL_L: [1094, 30, 4, 121, 5, 122],
        ERROR_CORRECTION_LEVEL_M: [860, 28, 4, 47, 14, 48],
        ERROR_CORRECTION_LEVEL_Q: [614, 30, 11, 24, 14, 25],
        ERROR_CORRECTION_LEVEL_H: [464, 30, 16, 15, 14, 16]
    },
    24: {
        ERROR_CORRECTION_LEVEL_L: [1174, 30, 6, 117, 4, 118],
        ERROR_CORRECTION_LEVEL_M: [914, 28, 6, 45, 14, 46],
        ERROR_CORRECTION_LEVEL_Q: [664, 30, 11, 24, 16, 25],
        ERROR_CORRECTION_LEVEL_H: [514, 30, 30, 16, 2, 17]
    },
    25: {
        ERROR_CORRECTION_LEVEL_L: [1276, 26, 8, 106, 4, 107],
        ERROR_CORRECTION_LEVEL_M: [1000, 28, 8, 47, 13, 48],
        ERROR_CORRECTION_LEVEL_Q: [718, 30, 7, 22, 22, 23],
        ERROR_CORRECTION_LEVEL_H: [538, 30, 22, 15, 13, 16]
    },
    26: {
        ERROR_CORRECTION_LEVEL_L: [1370, 28, 10, 114, 2, 115],
        ERROR_CORRECTION_LEVEL_M: [1062, 28, 19, 46, 4, 47],
        ERROR_CORRECTION_LEVEL_Q: [754, 28, 28, 23, 6, 24],
        ERROR_CORRECTION_LEVEL_H: [596, 30, 33, 16, 4, 17]
    },
    27: {
        ERROR_CORRECTION_LEVEL_L: [1468, 30, 8, 122, 4, 123],
        ERROR_CORRECTION_LEVEL_M: [1128, 28, 22, 45, 3, 46],
        ERROR_CORRECTION_LEVEL_Q: [808, 30, 8, 23, 26, 24],
        ERROR_CORRECTION_LEVEL_H: [628, 30, 12, 15, 28, 16]
    },
    28: {
        ERROR_CORRECTION_LEVEL_L: [1531, 30, 3, 117, 10, 118],
        ERROR_CORRECTION_LEVEL_M: [1193, 28, 3, 45, 23, 46],
        ERROR_CORRECTION_LEVEL_Q: [871, 30, 4, 24, 31, 25],
        ERROR_CORRECTION_LEVEL_H: [661, 30, 11, 15, 31, 16]
    },
    29: {
        ERROR_CORRECTION_LEVEL_L: [1631, 30, 7, 116, 7, 117],
        ERROR_CORRECTION_LEVEL_M: [1267, 28, 21, 45, 7, 46],
        ERROR_CORRECTION_LEVEL_Q: [911, 30, 1, 23, 37, 24],
        ERROR_CORRECTION_LEVEL_H: [701, 30, 19, 15, 26, 16]
    },
    30: {
        ERROR_CORRECTION_LEVEL_L: [1735, 30, 5, 115, 10, 116],
        ERROR_CORRECTION_LEVEL_M: [1373, 28, 19, 47, 10, 48],
        ERROR_CORRECTION_LEVEL_Q: [985, 30, 15, 24, 25, 25],
        ERROR_CORRECTION_LEVEL_H: [745, 30, 23, 15, 25, 16]
    },
    31: {
        ERROR_CORRECTION_LEVEL_L: [1843, 30, 13, 115, 3, 116],
        ERROR_CORRECTION_LEVEL_M: [1455, 28, 2, 46, 29, 47],
        ERROR_CORRECTION_LEVEL_Q: [1033, 30, 42, 24, 1, 25],
        ERROR_CORRECTION_LEVEL_H: [793, 30, 23, 15, 28, 16]
    },
    32: {
        ERROR_CORRECTION_LEVEL_L: [1955, 30, 17, 115, 0, 0],
        ERROR_CORRECTION_LEVEL_M: [1541, 28, 10, 46, 23, 47],
        ERROR_CORRECTION_LEVEL_Q: [1115, 30, 10, 24, 35, 25],
        ERROR_CORRECTION_LEVEL_H: [845, 30, 19, 15, 35, 16]
    },
    33: {
        ERROR_CORRECTION_LEVEL_L: [2071, 30, 17, 115, 1, 116],
        ERROR_CORRECTION_LEVEL_M: [1631, 28, 14, 46, 21, 47],
        ERROR_CORRECTION_LEVEL_Q: [1171, 30, 29, 24, 19, 25],
        ERROR_CORRECTION_LEVEL_H: [901, 30, 11, 15, 46, 16]
    },
    34: {
        ERROR_CORRECTION_LEVEL_L: [2191, 30, 13, 115, 6, 116],
        ERROR_CORRECTION_LEVEL_M: [1725, 28, 14, 46, 23, 47],
        ERROR_CORRECTION_LEVEL_Q: [1231, 30, 44, 24, 7, 25],
        ERROR_CORRECTION_LEVEL_H: [961, 30, 59, 16, 1, 17]
    },
    35: {
        ERROR_CORRECTION_LEVEL_L: [2306, 30, 12, 121, 7, 122],
        ERROR_CORRECTION_LEVEL_M: [1812, 28, 12, 47, 26, 48],
        ERROR_CORRECTION_LEVEL_Q: [1286, 30, 39, 24, 14, 25],
        ERROR_CORRECTION_LEVEL_H: [986, 30, 22, 15, 41, 16]
    },
    36: {
        ERROR_CORRECTION_LEVEL_L: [2434, 30, 6, 121, 14, 122],
        ERROR_CORRECTION_LEVEL_M: [1914, 28, 6, 47, 34, 48],
        ERROR_CORRECTION_LEVEL_Q: [1354, 30, 46, 24, 10, 25],
        ERROR_CORRECTION_LEVEL_H: [1054, 30, 2, 15, 64, 16]
    },
    37: {
        ERROR_CORRECTION_LEVEL_L: [2566, 30, 17, 122, 4, 123],
        ERROR_CORRECTION_LEVEL_M: [1992, 28, 29, 46, 14, 47],
        ERROR_CORRECTION_LEVEL_Q: [1426, 30, 49, 24, 10, 25],
        ERROR_CORRECTION_LEVEL_H: [1096, 30, 24, 15, 46, 16]
    },
    38: {
        ERROR_CORRECTION_LEVEL_L: [2702, 30, 4, 122, 18, 123],
        ERROR_CORRECTION_LEVEL_M: [2102, 28, 13, 46, 32, 47],
        ERROR_CORRECTION_LEVEL_Q: [1502, 30, 48, 24, 14, 25],
        ERROR_CORRECTION_LEVEL_H: [1142, 30, 42, 15, 32, 16]
    },
    39: {
        ERROR_CORRECTION_LEVEL_L: [2812, 30, 20, 117, 4, 118],
        ERROR_CORRECTION_LEVEL_M: [2216, 28, 40, 47, 7, 48],
        ERROR_CORRECTION_LEVEL_Q: [1582, 30, 43, 24, 22, 25],
        ERROR_CORRECTION_LEVEL_H: [1222, 30, 10, 15, 67, 16]
    },
    40: {
        ERROR_CORRECTION_LEVEL_L: [2956, 30, 19, 118, 6, 119],
        ERROR_CORRECTION_LEVEL_M: [2334, 28, 18, 47, 31, 48],
        ERROR_CORRECTION_LEVEL_Q: [1666, 30, 34, 24, 34, 25],
        ERROR_CORRECTION_LEVEL_H: [1276, 30, 20, 15, 61, 16]
    }
}
