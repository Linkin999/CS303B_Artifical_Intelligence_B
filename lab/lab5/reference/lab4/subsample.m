function subsampledImage = subsample(image, samplerate)

[height, width] = size(image);

subsampledheight = ceil(height/samplerate);
subsampledwidth = ceil(width/samplerate);
subsampledImage = zeros(subsampledheight,subsampledwidth);

heightindex = 1:samplerate:height;
widthindex = 1:samplerate:width;

for i = 1:subsampledheight
    subsampledImage(i,:) = image(heightindex(i),widthindex);
end

end

