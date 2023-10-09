def convert(time):
    h, m = time.split(':')
    time = float(h) + (float(m)/60)
    return time

def main():
    x=input('What time is it? ')
    x=convert(x)
    if 7 <= x <= 8:
        print('Breakfast Time')
    elif 12 <= x <= 13:
        print('Lunch Time')
    elif 18 <= x <= 19:
        print('Dinner Time')

if __name__ == "__main__":
    main()