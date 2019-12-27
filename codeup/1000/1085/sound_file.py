
# h, b, c, s 입력
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

volume_byte = h * b * c * s     # 전체 바이트 용량
volume_mb = volume_byte / (8 * 1024 * 1024)   # mb 단위로 변환
volume_mb = round(volume_mb, 1)     # 소수 일의자리 까지 반올림

print('%.1f MB' % volume_mb)
