from datetime import datetime
PYCON_DATE= datetime(year=2021, month=5, day=12, hour=8)
countdown= PYCON_DATE-datetime.now()
print(f"countdown to pycon us 2021: {countdown}")