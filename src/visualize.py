import mne
import matplotlib.pyplot as plt

# EEG 데이터 불러오기
raw = mne.io.read_raw_edf(
    "data/S001R01.edf",
    preload=True
)

data = raw.get_data()
first_channel = data[0]

sampling_rate = raw.info["sfreq"] # Hz
time = range(len(first_channel))
time = [t / sampling_rate for t in time]

plt.figure(figsize=(12, 4))
plt.plot(time, first_channel)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (V)")
channel_name = raw.ch_names[0]
plt.title(f"EEG Signal - {channel_name}")

plt.tight_layout()

plt.savefig("results/single_channel.png", dpi=300)

plt.show()

print("첫 번째 채널: ", raw.ch_names[0])

channel_indices = [0, 1, 2, 3, 4, 5]

selected_data = data[channel_indices]

plt.figure(figsize=(12, 8))

for i in range(len(channel_indices)):
    plt.subplot(6, 1, i + 1)
    plt.plot(time, selected_data[i])
    channel_name = raw.ch_names[channel_indices[i]]
    plt.ylabel(channel_name)
plt.xlabel("Time (seconds)")
plt.tight_layout()
plt.savefig("results/multi_channel.png", dpi=300)
plt.show()


