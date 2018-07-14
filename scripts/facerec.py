import face_recognition
import cv2
import numpy as np

nameEncMap = {}
nameEncMap["downey"] = np.array([-0.10914367,  0.03330677,  0.10364366, -0.02746783,  0.01561657,
       -0.14334421, -0.02367203, -0.08613437,  0.0998663 , -0.09768367,
        0.27009335,  0.02139437, -0.20274001, -0.02888612,  0.03036231,
        0.08648898, -0.18612897, -0.07569585, -0.09155796, -0.04054004,
        0.04652566,  0.03506777,  0.10634197,  0.04215866, -0.15927297,
       -0.30595696, -0.16349937, -0.02015364,  0.09547165, -0.11248672,
        0.03506772, -0.04606473, -0.1757843 , -0.04512041, -0.02263235,
        0.0733306 , -0.08285597, -0.11554074,  0.18560058,  0.06166399,
       -0.15575649,  0.02577422, -0.00777424,  0.32345742,  0.16284133,
        0.04385211,  0.03632348, -0.0524075 ,  0.01664636, -0.28342283,
        0.09247139,  0.07379508,  0.09397196,  0.02017271,  0.18066019,
       -0.15141222,  0.06027877,  0.17641282, -0.15459697,  0.09106795,
        0.00652699,  0.05316038,  0.13758573,  0.03235835,  0.20541622,
        0.07802792, -0.13839325, -0.07638975,  0.05876798, -0.13264346,
       -0.05461299,  0.09311932, -0.04316366, -0.19911177, -0.32258135,
        0.00148334,  0.35807866,  0.10125239, -0.20033041,  0.0298272 ,
       -0.07734743, -0.08444025,  0.10968289,  0.05902911, -0.12482904,
        0.02429382, -0.22425272,  0.01258478,  0.17863481,  0.03601426,
       -0.06584571,  0.24403434,  0.00310373,  0.0016928 ,  0.06879634,
        0.05445546, -0.21357328,  0.00463627, -0.12188579, -0.07592547,
        0.08587924, -0.03166508, -0.06188898,  0.15615168, -0.15528767,
        0.19205144,  0.00823193, -0.06022593, -0.010275  ,  0.03200605,
       -0.15629478, -0.0224096 ,  0.07722262, -0.29334736,  0.12921129,
        0.21880595,  0.00145719,  0.10161664,  0.09808771, -0.0291272 ,
       -0.03357828,  0.05980432, -0.13856782, -0.02735936, -0.01682665,
       -0.05144803,  0.09364341,  0.03287503])
nameEncMap["deng"] = np.array([-9.02924240e-02,  6.38809875e-02,  5.55930622e-02, -2.23218482e-02,
       -2.77444944e-02, -4.40028980e-02, -7.98203275e-02, -6.18093908e-02,
        1.42005265e-01, -1.31031156e-01,  2.57122487e-01, -8.86216387e-03,
       -1.99026883e-01, -7.95401633e-02,  3.16724461e-03,  1.25977337e-01,
       -1.68371230e-01, -1.04316168e-01, -7.45512620e-02, -1.23955309e-02,
        2.97160372e-02,  8.08428600e-03,  2.46725362e-02, -4.10753675e-03,
       -1.07676618e-01, -3.79998595e-01, -1.43646866e-01, -4.30025067e-03,
       -1.96256675e-02, -1.16594078e-03, -4.32435237e-02,  1.13297351e-01,
       -1.05817571e-01, -3.84484604e-02,  4.55721691e-02,  1.73014089e-01,
       -1.30711138e-01, -5.47920205e-02,  2.17912018e-01,  5.13075851e-04,
       -1.49230883e-01, -1.08032823e-02,  3.28558460e-02,  2.67986476e-01,
        1.84415191e-01,  4.45653945e-02,  2.12455951e-02, -4.41163778e-02,
        4.32407185e-02, -2.48526156e-01,  4.47237492e-02,  2.07219556e-01,
        7.27140605e-02,  1.20136738e-01,  9.96197239e-02, -1.06207572e-01,
        3.89541127e-02,  1.47958592e-01, -1.50171876e-01,  9.54626314e-03,
       -1.20618185e-02, -1.55133948e-01, -1.59045607e-02, -7.46380836e-02,
        1.98509067e-01,  1.68183923e-01, -1.12990119e-01, -1.60569429e-01,
        1.51426286e-01, -1.51645929e-01, -1.01185642e-01,  7.51766786e-02,
       -1.19183294e-01, -2.42980465e-01, -2.82751203e-01,  2.25256644e-02,
        3.67301673e-01,  1.73617899e-01, -1.48599625e-01,  5.53373769e-02,
        2.00182758e-02, -1.03048146e-01,  1.19849861e-01,  1.07356884e-01,
       -7.94338211e-02,  1.75630767e-02, -1.19585894e-01,  8.04263726e-03,
        2.06356689e-01, -1.33263972e-03, -8.99093226e-02,  1.92347825e-01,
       -2.06666067e-04,  8.50928202e-02,  9.55954343e-02,  1.90339168e-04,
        6.17000647e-03,  3.14369332e-03, -1.94912508e-01, -1.19971177e-02,
        7.85339475e-02, -1.33404210e-01, -5.02028354e-02,  5.61290607e-02,
       -8.31144452e-02,  1.25890225e-01,  1.28224865e-02,  2.11995877e-02,
        3.87239270e-03, -8.57827999e-03, -1.69450566e-01, -1.86321083e-02,
        1.79698944e-01, -2.77009428e-01,  1.78815499e-01,  1.81649193e-01,
        3.43222953e-02,  1.72449633e-01,  1.54616371e-01,  9.31961089e-02,
       -2.07867213e-02, -7.16042593e-02, -1.78224221e-01, -6.72780126e-02,
        2.78016105e-02,  6.34550750e-02,  9.36240256e-02,  4.29442711e-02])

def facereco(unknown_encoding):
    message = 'unKnown'
    for k, v in nameEncMap.items():
        results = face_recognition.compare_faces([v],unknown_encoding)
        if results == [True]:
            print(k)
            return k
    print(message)
    return message

if __name__ == '__main__':
    #res = facereco('upload_img.jpg')
    res = facereco('unlabel.jpg')
    print(res)
