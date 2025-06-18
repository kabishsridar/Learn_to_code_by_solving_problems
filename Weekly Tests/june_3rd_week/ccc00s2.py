n = int(input())
streams = []

for i in range(n):
    streams.append(input())
while True:
    op = int(input())
    if op == 77:
        break
    
    elif op == 99:
        stream_num = int(input())
        percent_left = int(input())
        
        idx = stream_num - 1
        
        flow = streams[idx]
        
        left_flow = flow * percent_left / 100
        right_flow = flow - left_flow
        
        streams = streams[:idx] + [left_flow, right_flow] + streams[idx+1:]
    
    elif op == 88:
        stream_num = int(input())
        
        idx = stream_num - 1
        
        new_flow = streams[idx] + streams[idx + 1]
        
        streams = streams[:idx] + [new_flow] + streams[idx + 2:]

rounded_flows = [round(flow) for flow in streams]

print(len(rounded_flows), *rounded_flows)