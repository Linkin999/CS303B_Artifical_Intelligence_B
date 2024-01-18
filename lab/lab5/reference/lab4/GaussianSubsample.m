function img = GaussianSubsample(image, samplerate)
w=7;
sigma = w/6;
smoothed = imgaussfilt(image, sigma);
img = subsample(smoothed, samplerate);
end

