bpm=76.9;
T=60/bpm;
ecg = [];
t=1:50;                                             %for 0.050 seq
ecg=[ecg linspace(0,6,length(t))];
t=51:90;                                            %for 0.040 seq
ecg=[ecg linspace(6,0,length(t))];
t=91:90+90;                                         %for 0.090 seq
ecg=[ecg linspace(0,0,length(t))];
plot(ecg)