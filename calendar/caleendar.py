from calendar import TextCalendar

year = int(input('Enter year : '))
cal = TextCalendar()
calendar_text = cal.formatyear(year, 2, 1, 8, 3)

print(cal.formatyear(year, 2 ,1 ,8, 3))

with open(f"calendrier_{year}.txt", "w") as f:
    f.write(calendar_text)
print(f"Le calendrier de {year} a ete enregistre dans calendrier_{year}.txt")