
# w, b, b 입력
w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)

volume_bit = w * h * b      # 전체 비트 용량
volume_mb = volume_bit / (8 * 1024 * 1024)  # mb 단위로 변환
volume_mb = round(volume_mb, 2)     # 소수 2의 자리까지 반올림

print('%.2f MB' % volume_mb)
