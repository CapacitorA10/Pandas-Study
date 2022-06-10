import numpy as np
import pandas as pd
import easygui
import csv
##
def xy2dut(x,y):
    index = [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 432, 454, 476, 498, 520, 542, 564, 586, 608, 630, 652, 674, 696, 718, 740, 762, 784, 806, 828, 850, 872, 894, 916, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 270, 290, 310, 330, 350, 370, 390, 410, 431, 453, 475, 497, 519, 541, 563, 585, 607, 629, 651, 673, 695, 717, 739, 761, 783, 805, 827, 849, 871, 893, 915, 936, 956, 976, 996, 1016, 1036, 1056, 1076, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 178, 196, 214, 232, 250, 269, 289, 309, 329, 349, 369, 389, 409, 430, 452, 474, 496, 518, 540, 562, 584, 606, 628, 650, 672, 694, 716, 738, 760, 782, 804, 826, 848, 870, 892, 914, 935, 955, 975, 995, 1015, 1035, 1055, 1075, 1094, 1112, 1130, 1148, 1166, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 128, 144, 160, 177, 195, 213, 231, 249, 268, 288, 308, 328, 348, 368, 388, 408, 429, 451, 473, 495, 517, 539, 561, 583, 605, 627, 649, 671, 693, 715, 737, 759, 781, 803, 825, 847, 869, 891, 913, 934, 954, 974, 994, 1014, 1034, 1054, 1074, 1093, 1111, 1129, 1147, 1165, 1182, 1198, 1214, 1230, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 84, 98, 112, 127, 143, 159, 176, 194, 212, 230, 248, 267, 287, 307, 327, 347, 367, 387, 407, 428, 450, 472, 494, 516, 538, 560, 582, 604, 626, 648, 670, 692, 714, 736, 758, 780, 802, 824, 846, 868, 890, 912, 933, 953, 973, 993, 1013, 1033, 1053, 1073, 1092, 1110, 1128, 1146, 1164, 1181, 1197, 1213, 1229, 1244, 1258, 1272, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 58, 70, 83, 97, 111, 126, 142, 158, 175, 193, 211, 229, 247, 266, 286, 306, 326, 346, 366, 386, 406, 427, 449, 471, 493, 515, 537, 559, 581, 603, 625, 647, 669, 691, 713, 735, 757, 779, 801, 823, 845, 867, 889, 911, 932, 952, 972, 992, 1012, 1032, 1052, 1072, 1091, 1109, 1127, 1145, 1163, 1180, 1196, 1212, 1228, 1243, 1257, 1271, 1284, 1296, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 36, 46, 57, 69, 82, 96, 110, 125, 141, 157, 174, 192, 210, 228, 246, 265, 285, 305, 325, 345, 365, 385, 405, 426, 448, 470, 492, 514, 536, 558, 580, 602, 624, 646, 668, 690, 712, 734, 756, 778, 800, 822, 844, 866, 888, 910, 931, 951, 971, 991, 1011, 1031, 1051, 1071, 1090, 1108, 1126, 1144, 1162, 1179, 1195, 1211, 1227, 1242, 1256, 1270, 1283, 1295, 1306, 1316, 9999, 9999, 9999],
    [9999, 9999, 18, 26, 35, 45, 56, 68, 81, 95, 109, 124, 140, 156, 173, 191, 209, 227, 245, 264, 284, 304, 324, 344, 364, 384, 404, 425, 447, 469, 491, 513, 535, 557, 579, 601, 623, 645, 667, 689, 711, 733, 755, 777, 799, 821, 843, 865, 887, 909, 930, 950, 970, 990, 1010, 1030, 1050, 1070, 1089, 1107, 1125, 1143, 1161, 1178, 1194, 1210, 1226, 1241, 1255, 1269, 1282, 1294, 1305, 1315, 1324, 9999, 9999],
    [9999, 10, 17, 25, 34, 44, 55, 67, 80, 94, 108, 123, 139, 155, 172, 190, 208, 226, 244, 263, 283, 303, 323, 343, 363, 383, 403, 424, 446, 468, 490, 512, 534, 556, 578, 600, 622, 644, 666, 688, 710, 732, 754, 776, 798, 820, 842, 864, 886, 908, 929, 949, 969, 989, 1009, 1029, 1049, 1069, 1088, 1106, 1124, 1142, 1160, 1177, 1193, 1209, 1225, 1240, 1254, 1268, 1281, 1293, 1304, 1314, 1323, 1330, 9999],
    [4, 9, 16, 24, 33, 43, 54, 66, 79, 93, 107, 122, 138, 154, 171, 189, 207, 225, 243, 262, 282, 302, 322, 342, 362, 382, 402, 423, 445, 467, 489, 511, 533, 555, 577, 599, 621, 643, 665, 687, 709, 731, 753, 775, 797, 819, 841, 863, 885, 907, 928, 948, 968, 988, 1008, 1028, 1048, 1068, 1087, 1105, 1123, 1141, 1159, 1176, 1192, 1208, 1224, 1239, 1253, 1267, 1280, 1292, 1303, 1313, 1322, 1329, 1334],
    [3, 8, 15, 23, 32, 42, 53, 65, 78, 92, 106, 121, 137, 153, 170, 188, 206, 224, 242, 261, 281, 301, 321, 341, 361, 381, 401, 422, 444, 466, 488, 510, 532, 554, 576, 598, 620, 642, 664, 686, 708, 730, 752, 774, 796, 818, 840, 862, 884, 906, 927, 947, 967, 987, 1007, 1027, 1047, 1067, 1086, 1104, 1122, 1140, 1158, 1175, 1191, 1207, 1223, 1238, 1252, 1266, 1279, 1291, 1302, 1312, 1321, 1328, 1333],
    [2, 7, 14, 22, 31, 41, 52, 64, 77, 91, 105, 120, 136, 152, 169, 187, 205, 223, 241, 260, 280, 300, 320, 340, 360, 380, 400, 421, 443, 465, 487, 509, 531, 553, 575, 597, 619, 641, 663, 685, 707, 729, 751, 773, 795, 817, 839, 861, 883, 905, 926, 946, 966, 986, 1006, 1026, 1046, 1066, 1085, 1103, 1121, 1139, 1157, 1174, 1190, 1206, 1222, 1237, 1251, 1265, 1278, 1290, 1301, 1311, 1320, 1327, 1332],
    [1, 6, 13, 21, 30, 40, 51, 63, 76, 90, 104, 119, 135, 151, 168, 186, 204, 222, 240, 259, 279, 299, 319, 339, 359, 379, 399, 420, 442, 464, 486, 508, 530, 552, 574, 596, 618, 640, 662, 684, 706, 728, 750, 772, 794, 816, 838, 860, 882, 904, 925, 945, 965, 985, 1005, 1025, 1045, 1065, 1084, 1102, 1120, 1138, 1156, 1173, 1189, 1205, 1221, 1236, 1250, 1264, 1277, 1289, 1300, 1310, 1319, 1326, 1331],
    [9999, 5, 12, 20, 29, 39, 50, 62, 75, 89, 103, 118, 134, 150, 167, 185, 203, 221, 239, 258, 278, 298, 318, 338, 358, 378, 398, 419, 441, 463, 485, 507, 529, 551, 573, 595, 617, 639, 661, 683, 705, 727, 749, 771, 793, 815, 837, 859, 881, 903, 924, 944, 964, 984, 1004, 1024, 1044, 1064, 1083, 1101, 1119, 1137, 1155, 1172, 1188, 1204, 1220, 1235, 1249, 1263, 1276, 1288, 1299, 1309, 1318, 1325, 9999],
    [9999, 9999, 11, 19, 28, 38, 49, 61, 74, 88, 102, 117, 133, 149, 166, 184, 202, 220, 238, 257, 277, 297, 317, 337, 357, 377, 397, 418, 440, 462, 484, 506, 528, 550, 572, 594, 616, 638, 660, 682, 704, 726, 748, 770, 792, 814, 836, 858, 880, 902, 923, 943, 963, 983, 1003, 1023, 1043, 1063, 1082, 1100, 1118, 1136, 1154, 1171, 1187, 1203, 1219, 1234, 1248, 1262, 1275, 1287, 1298, 1308, 1317, 9999, 9999],
    [9999, 9999, 9999, 9999, 27, 37, 48, 60, 73, 87, 101, 116, 132, 148, 165, 183, 201, 219, 237, 256, 276, 296, 316, 336, 356, 376, 396, 417, 439, 461, 483, 505, 527, 549, 571, 593, 615, 637, 659, 681, 703, 725, 747, 769, 791, 813, 835, 857, 879, 901, 922, 942, 962, 982, 1002, 1022, 1042, 1062, 1081, 1099, 1117, 1135, 1153, 1170, 1186, 1202, 1218, 1233, 1247, 1261, 1274, 1286, 1297, 1307, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 47, 59, 72, 86, 100, 115, 131, 147, 164, 182, 200, 218, 236, 255, 275, 295, 315, 335, 355, 375, 395, 416, 438, 460, 482, 504, 526, 548, 570, 592, 614, 636, 658, 680, 702, 724, 746, 768, 790, 812, 834, 856, 878, 900, 921, 941, 961, 981, 1001, 1021, 1041, 1061, 1080, 1098, 1116, 1134, 1152, 1169, 1185, 1201, 1217, 1232, 1246, 1260, 1273, 1285, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 71, 85, 99, 114, 130, 146, 163, 181, 199, 217, 235, 254, 274, 294, 314, 334, 354, 374, 394, 415, 437, 459, 481, 503, 525, 547, 569, 591, 613, 635, 657, 679, 701, 723, 745, 767, 789, 811, 833, 855, 877, 899, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1079, 1097, 1115, 1133, 1151, 1168, 1184, 1200, 1216, 1231, 1245, 1259, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 113, 129, 145, 162, 180, 198, 216, 234, 253, 273, 293, 313, 333, 353, 373, 393, 414, 436, 458, 480, 502, 524, 546, 568, 590, 612, 634, 656, 678, 700, 722, 744, 766, 788, 810, 832, 854, 876, 898, 919, 939, 959, 979, 999, 1019, 1039, 1059, 1078, 1096, 1114, 1132, 1150, 1167, 1183, 1199, 1215, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 161, 179, 197, 215, 233, 252, 272, 292, 312, 332, 352, 372, 392, 413, 435, 457, 479, 501, 523, 545, 567, 589, 611, 633, 655, 677, 699, 721, 743, 765, 787, 809, 831, 853, 875, 897, 918, 938, 958, 978, 998, 1018, 1038, 1058, 1077, 1095, 1113, 1131, 1149, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 251, 271, 291, 311, 331, 351, 371, 391, 412, 434, 456, 478, 500, 522, 544, 566, 588, 610, 632, 654, 676, 698, 720, 742, 764, 786, 808, 830, 852, 874, 896, 917, 937, 957, 977, 997, 1017, 1037, 1057, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 411, 433, 455, 477, 499, 521, 543, 565, 587, 609, 631, 653, 675, 697, 719, 741, 763, 785, 807, 829, 851, 873, 895, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]]
    dutNum = index[y-11][x-11]

    return dutNum

## file open

totalFile = easygui.fileopenbox(filetypes="*.MR1", multiple=True)

out = [['LOT', 'WAF', 'X', 'Y', 'DUT', 'BLOCK', 'FAIL', 'TEST_CATEGORY'],
       ['String', 'Integer', 'Integer', 'Integer', 'Integer', 'Integer', 'String', 'String']]

for fileName in totalFile:
    data = pd.read_table(fileName, header=None)
    # fileName = 'C:\\Users\\2076523\\PycharmProjects\\Pandas연습\\MR1Files\\4QQ1002P04.CL2.MR1'
    # data = pd.read_table(fileName, header=None)

    # 데이터 내 각 행별로 순회
    lot = fileName[-18:-11]
    wafer = fileName[-10:-8]
    category = fileName[-7:-4]

    for i in range(len(data)):
        item = data.iloc[i][0]  # 각 행별로 비교

        if item[0:3] == 'die':
            xdie, ydie = item.split()[1:3]
            xdie = int(xdie)
            ydie = int(ydie)
            dut = xy2dut(xdie, ydie)
        elif item == 'END':
            pass
        elif item[0:3] == 'RDG':
            plane = int(item[3:6])
            semiBlock = int(item[7:11], base=16)
            block = (semiBlock * 4) + plane

            row = [lot, wafer, xdie, ydie, dut, block, 'F', category]

            out.append(row)
    ##
outDF = pd.DataFrame(out)
outDF.to_csv('MR1_merged.csv', index=False, header=False)
