import mne
import matplotlib.pyplot as plt

# EEG 데이터 
raw = mne.io.read_raw_edf(
    "data/S001R01.edf",
    preload=True
)

# 첫번째 채널 선택
channel_name = raw.ch_names[:6]

plt.figure(figsize=(10, 6))

for channel_name in channel_name:
    raw_channel = raw.copy().pick_channels([channel_name])
    
# PSD 계산
    spectrum = raw_channel.compute_psd(
        method="welch",
        fmin=1,
        fmax=40
    )

# PSD 데이터
    psd = spectrum.get_data()
    frequencies = spectrum.freqs

# 그래프

    plt.plot(
        frequencies,
        psd[0]
    )
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power Spectral Density")

    plt.title("EEG Power Spectrum")

    plt.legend()
    
    plt.tight_layout()

    plt.savefig("results/psd_multiple_channel.png", dpi=300)

    plt.show()

bands = {
    "Delta": (1, 4),
    "Theta": (4, 8),
    "Alpha": (8, 13),
    "Beta": (13, 30),
    "Gamma": (30, 40)
}

for band_name, (low, high) in bands.items():
    band_mask = (
        (frequencies >= low) & (frequencies <= high)
    )
    band_power = psd[0][band_mask].mean()
    print(f"{band_name}: {band_power:.6e}")
