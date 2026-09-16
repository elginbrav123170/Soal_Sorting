import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)


def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    idx = maps[index]
    n = len(data)

    for i in range(n-1):
        for j in range(n - i - 1):
            if rev == False:
                if data[j][idx] > data[j + 1][idx]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j][idx] < data[j + 1][idx]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    # Jangan Dihapus
    show_data(data)

sort_by(data)
sort_by(data, "nim",rev = True)
sort_by(data, "nama")
sort_by(data, "nama", rev = True)
sort_by(data, "presensi")
sort_by(data, "presensi", rev = True)



