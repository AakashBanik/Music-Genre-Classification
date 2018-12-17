import librosa
import matplotlib.pyplot as plt
import librosa.display as display

music, sr = librosa.load('./1.mp3', sr=44100) #returns an audio time series as a numpy array with a sampling rate(sr) of 44.1KHZ mono

print(type(music))
print(music.shape)

plt.figure(figsize=(14, 5))
display.waveplot(music, sr=sr)
