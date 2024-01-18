function img = GaussianSupersample(image, samplerate)
w=7;
sigma = w/6;
smoothed = imgaussfilt(image, sigma);
img = supersample(smoothed, samplerate);
end

