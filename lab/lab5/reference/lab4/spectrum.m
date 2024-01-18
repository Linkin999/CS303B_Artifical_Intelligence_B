function spectrum = spectrum(img)

F = fft2(double(img));
IF = fftshift(F);

spectrum = abs(IF).^2;
end

