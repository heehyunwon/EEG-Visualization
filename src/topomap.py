import mne
import matplotlib.pyplot as plt

# EEG 데이터 불러오기
raw = mne.io.read_raw_edf(
    "data/S001R01.edf",
    preload=True
)

raw.rename_channels(
    lambda name: name.rstrip(".")
)

montage = mne.channels.make_standard_montage("standard_1020") # EEG에서 잘 사용되는 전극배치체계

montage_names = {
    name.upper(): name
    for name in montage.ch_names
}

rename_dict = {}
for name in raw.ch_names:
    if name.upper() in montage_names:
        rename_dict[name] = montage_names[name.upper()]

raw.rename_channels(rename_dict)

# 표준 전극 위치 설정
raw.set_montage(
    montage
)

print("정리된 채널 이름: ")
print(raw.ch_names)

# EEG 데이터 가져오기
data = raw.get_data()

# 데이터 선택
sample_index = 1000
values = data[:, sample_index]

# Topomap
mne.viz.plot_topomap(
    values,
    raw.info,
    show=True
)