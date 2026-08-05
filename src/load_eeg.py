import mne
raw = mne.io.read_raw_edf('data/S001R01.edf', preload=True)
print(raw)
