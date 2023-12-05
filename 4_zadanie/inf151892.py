import glob
import sys
from scipy.io import wavfile
from scipy.fft import fft

male = [85,160]
female = [165,255]

def HPS(channel, rate):
    parts = []
    i=0
    while i < len(channel):
        sub = channel[i:i+rate]
        parts.append(sub)
        i+=rate

    fft_results = [fft(sub) for sub in parts]

    print(fft_results)
    # for i in range(0,len(left_channel),rate):


    # print(len(channel))

if __name__ == "__main__":

        file = sys.argv[1]
        rate, data =wavfile.read(file)
        left_channel = data[:, 0]
        right_channel = data[:, 1]
        HPS(left_channel,rate)