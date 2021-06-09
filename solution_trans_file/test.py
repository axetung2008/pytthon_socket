import os
file_name = "D:/ball.png"
file_size = os.path.getsize(file_name)
with open(file_name, 'rb') as f:
    remaining = file_size
    while remaining:
        chunk_size = 4096 if remaining >= 4096 else remaining
        print(chunk_size)
        # chunk = connbuf.get_bytes(chunk_size)
        # if not chunk: break
        # f.write(chunk)
        # remaining -= len(chunk)
    # if remaining:
    #     print('File incomplete.  Missing',remaining,'bytes.')
    # else:
    #     print('File received successfully.')
