import mne
import matplotlib.pyplot as plt

# EEG 데이터 불러오기
raw = mne.io.read_raw_edf(
    "data/S001R01.edf",
    preload=True
)

data = raw.get_data()

sampling_rate = raw.info["sfreq"] # Hz

start_time = 10
end_time = 15

start_sample = int(start_time  * sampling_rate)
end_sample = int(end_time * sampling_rate)

channel_index = 0
channel_data = data[channel_index]
selected_data = channel_data[start_sample:end_sample]

time = (range(start_sample, end_sample))
time = [t / sampling_rate for t in time]

plt.figure(figsize=(12, 4))
plt.plot(time, selected_data)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (V)")
channel_name = raw.ch_names[channel_index]
plt.title(
    f"EEG Signal - {channel_name}"
    f"({start_time}-{end_time} sec)"
)
plt.tight_layout()

plt.savefig("results/eeg_5sec.png", dpi=300)

plt.show()
