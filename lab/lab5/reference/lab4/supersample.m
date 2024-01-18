function supersampled = supersample(image, samplerate)
[height, width] = size(image);
supersampledx = zeros(height * samplerate, width * samplerate);
supersampled = zeros(height * samplerate, width * samplerate);

for a = 1:samplerate
    for i = 1+a-1:samplerate:width*samplerate
        supersampledx(1:height,i) = image(:,(i+(samplerate-a))/samplerate);
    end
end

for a = 1:samplerate
    for j = 1+a-1:samplerate:width*samplerate
        supersampled(j,:) = supersampledx((j+(samplerate-a))/samplerate,:);
    end
end
end

