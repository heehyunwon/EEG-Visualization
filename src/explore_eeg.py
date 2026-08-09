import mne

#EEG  파일 읽기
raw = mne.io.read_raw_edf(
    "data/S001R01.edf",
    preload=True
)

# 채널 이름
print("채널 이름: ")
print(raw.ch_names)

# 채널 개수
print("채널 개수: ")
print(len(raw.ch_names))

# Sampling rate
print("\nSampling Rate:")
print(raw.info["sfreq"])

# 데이터 크기
print("\n데이터 크기: ")
print(raw.get_data().shape)

data = raw.get_data()
print("\n첫 번째 채널 데이터: ")
print(data[0][:10])