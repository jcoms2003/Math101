def timeClock(x):
    hour = x // 3600
    mint = (x % 3600) // 60
    sec = x % 60
    return (f"{hour:.0f}:{mint:.0f}:{sec}")
print(timeClock(3665))
