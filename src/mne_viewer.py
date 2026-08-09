import mne
import matplotlib.pyplot as plt

raw = mne.io.read_raw_edf(
    "data/S001R01.edf",
    preload=True
)

print(raw)

raw.plot(
    duration=5,
    n_channels=10,
    scalings="auto",
    show=False
)

plt.show()