import phonenumbers
x = phonenumbers.parse("+442083661177", None)
print(x)

from phonenumbers import carrier
ro_number = phonenumbers.parse("+40721234567", "RO")
print(carrier.name_for_number(ro_number, "en"))

from phonenumbers import timezone
gb_number = phonenumbers.parse("+447986123456", "GB")
print(timezone.time_zones_for_number(gb_number))
