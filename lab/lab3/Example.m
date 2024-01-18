%% Live Motion Detection Using Optical Flow
%
% This example shows how to create a video algorithm to detect motion using 
% optical flow technique.This example uses the Image Acquisition Toolbox(TM) System Object 
% along with Computer Vision Toolbox(TM) System objects. 
%
% Copyright 2010-2018 The MathWorks, Inc.

%% Introduction
% This example streams images from an image acquisition device to detect motion 
% in the live video. It uses the optical flow estimation technique to
% estimate the motion vectors in each frame of the live video sequence.
% Once the motion vectors are determined, we draw it over the moving
% objects in the video sequence.

%% Initialization
% Create the Video Device System object.
clc;clear;close all;
vidDevice = imaq.VideoDevice('winvideo', 2, 'MJPG_1280x720', ...
                             'ReturnedColorSpace', 'rgb', ...
                             'DeviceProperties.Brightness', 90, ...
                             'DeviceProperties.Sharpness', 40);

%% 
% Create a System object to estimate direction and speed of object motion
% from one video frame to another using optical flow.
opticFlow = opticalFlowHS;

%% Stream Acquisition and Processing Loop
% Create a processing loop to perform motion detection in the input
% video. This loop uses the System objects you instantiated above.

% Set up for stream
nFrames = 0;
while (nFrames<100)     % Process for the first 100 frames.
    % Acquire single frame from imaging device.
    frameRGB = vidDevice();
    
    % Compute the optical flow for that particular frame.    
    flow = estimateFlow(opticFlow,rgb2gray(frameRGB));
    Vx = flow.Vx;
    Vxo = flow.Vx.*0;
    Vy = flow.Vy;
    Vyo = flow.Vy.*0;
    Vtx = (flow.Vx>=flow.Vx.*0.1).*flow.Vx;
    Vty = (flow.Vy>=flow.Vy.*0.1).*flow.Vy;
    flowx = opticalFlow(Vx,Vyo);
    flowy = opticalFlow(Vxo,Vy);
    flowt = opticalFlow(Vtx,Vty);
    
    figure(1);
%     imshow(frameRGB);
    imshow(flow.Magnitude);
%     hold on
%     plot(flow,'DecimationFactor',[5 5],'ScaleFactor',200);
%     hold on
%     plot(flowx,'DecimationFactor',[5 5],'ScaleFactor',200);
    hold on 
    plot(flowt,'DecimationFactor',[5 5],'ScaleFactor',200);
%     hold on
%     plot(flowy,'DecimationFactor',[5 5],'ScaleFactor',200);
    hold off

    % Increment frame count
    nFrames = nFrames + 1;
end

%% Summary
% In the figure window, you can see that the example detected the 
% motion of the black file. The moving objects are represented using the
% vector field lines as seen in the image. 

%% Release
% Here you call the release method on the System objects to close any open 
% files and devices.
release(vidDevice);
