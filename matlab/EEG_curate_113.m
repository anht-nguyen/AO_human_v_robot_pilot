Emotiv_data = EEG.data(5:36, :);

% % Select intervalMarker.csv file corresponding to the dataset
% [filename, pathname] = uigetfile('*.*', 'Select a file');
% 
% % Import data from intervalMarker.csv
% intervalMarker_table = readtable(fullfile(pathname,filename), 'NumHeaderLines',1);
% 
% event_col = table2array(intervalMarker_table(:,4));
% event_ur_col = table2array(intervalMarker_table(:,7));
% latency_col = table2array(intervalMarker_table(:,1));
% % ts_col = table2array(intervalMarker_table(:,6));
% 
% event_type = [];
% event_latency = [];
% event_ur = [];
% for i =1:height(intervalMarker_table)
%     event_type = [event_type; event_col(i)];
%     latency = find(EEG.times == latency_col(i));
%     event_latency = [event_latency; latency];
%     event_ur = [event_ur; event_ur_col(i)];
% end
% 


event_line = round(EEG.data(44, :)); % why using round() here?

event_type = [];
event_latency = [];
event_ur = [];
n = 0;

for i =1:length(event_line)
    if event_line(i) ~= 0 
        if isempty(event_type) | event_line(i) ~= event_type(end) 
            event_type = [event_type; event_line(i)];
            event_latency = [event_latency; i];
            n = n+1;
            event_ur = [event_ur; n];
        end
    end
end

for j = 1:length(event_type)
    EEG.event(j).type = event_type(j);
    EEG.event(j).latency = event_latency(j);
    EEG.event(j).urevent = event_ur(j);

    EEG.urevent(j).type = event_type(j);
    EEG.urevent(j).latency = event_latency(j);
end

data_length = size(Emotiv_data, 2);

EEG.data = single(Emotiv_data);

EEG.nbchan = 32;

EEG.pnts = data_length;

EEG.srate = 128;



