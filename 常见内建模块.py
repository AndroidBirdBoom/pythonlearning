from datetime import datetime

if __name__ == "__main__":
    now = datetime.now()
    print(now, "时间戳：", t := now.timestamp(), "转换为：", datetime.fromtimestamp(t))
    dt = datetime(2019, 5, 4, 10, 58, 9)
    print(dt, "时间戳：", t := dt.timestamp(), "转换为：", datetime.fromtimestamp(t))
