n = int(input()) # Get the number of initial streams
streams = []

for flow in range(n): # loop through the flows
    flows = int(input())
    streams.append(flows)  

while True: # loop until the input is 77 (exit)
    operation = int(input())  # get the input
    if operation == 77: # break for 77
        break  
    
    stream_index = int(input()) - 1  # this will be the actual index values

    if operation == 99:  # split
        split_percentage = int(input()) # get split %
        flow_left = streams[stream_index] * split_percentage // 100 # flow_left and flow_right formulae took from chatgpt
        # calculating amount of stream flows left

        flow_right = streams[stream_index] - flow_left # in 100 units, if 40 goes to left, the remaining 60 goes to right
        streams.insert(stream_index + 1, flow_right)
        streams[stream_index] = flow_left

    elif operation == 88:  # Merge
        merged_flow = streams[stream_index] + streams.pop(stream_index + 1) # streams's last element and the flows are added
        streams[stream_index] = merged_flow

new_streams = []
for flow in streams:  # loop through each stream and round values
    new_streams.append(round(flow)) 

stream_count = len(new_streams)  
print(stream_count)

for flow in new_streams:
    print(flow)