function edgeImage = edgedetection(img)
w = 7;
sigma = w/6;
times = 3;
threshold = 50;

for i = 1:times
    smoothedImage = imfilter(img, fspecial('gaussian', w, sigma), 'replicate');
end

sobelX = [-1, 0, 1; -2, 0, 2; -1, 0, 1];
sobelY = [-1, -2, -1; 0, 0, 0; 1, 2, 1];
gradientX = conv2(double(smoothedImage), sobelX, 'same');
gradientY = conv2(double(smoothedImage), sobelY, 'same');
gradientMagnitude = sqrt(gradientX.^2 + gradientY.^2);
edgeImage = gradientMagnitude > threshold;
end

