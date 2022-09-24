import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID =10349797 int(getenv("10349797"))
API_HASH =79554098746a63dadd45d7176bed5ede getenv("79554098746a63dadd45d7176bed5ede")
BOT_USERNAME =ASTRONOT getenv("ASTRONOT")
BOT_TOKEN =5776724856:AAEwhUjnkC8gavhUB9i7Wp14R4CHUJ1rw5g getenv("5776724856:AAEwhUjnkC8gavhUB9i7Wp14R4CHUJ1rw5g")
DURATION_LIMIT =700 int(getenv("DURATION_LIMIT", "700"))
STRING_SESSION =BQB4SYJQjoSDz8CNnqdIbadbSiFJaDuXQQ8D_ooEOE6O7gmChUCTWKSKV-vmX83TwVRsZRUj7Q7Ea9K0PmBuVoElTwGDBuqUh87DwmeSF76KrggqKV_7h2pkrjlDYbxqAID8HAcrbGzyBiV1GXJW6gJaKejB9YDhFzT-0f7btbweY6PSk410_YjBMjCOj8TQXQf-YgVJqO7dO-AZh6QzVfmaiNOVstiXvSIK9fRD-vPgTj9Glw84A7ZEMfXP9_Z4Ym1HyH5ft7NXcRHzlwmlg9vrwUrlvlvenm-LfqTFhzu9QkirnASrWdzUxlF7asnLdktLqsJoOewKk0AVLAZRKeQ_AAAAAVTZ1jYA getenv("BQB4SYJQjoSDz8CNnqdIbadbSiFJaDuXQQ8D_ooEOE6O7gmChUCTWKSKV-vmX83TwVRsZRUj7Q7Ea9K0PmBuVoElTwGDBuqUh87DwmeSF76KrggqKV_7h2pkrjlDYbxqAID8HAcrbGzyBiV1GXJW6gJaKejB9YDhFzT-0f7btbweY6PSk410_YjBMjCOj8TQXQf-YgVJqO7dO-AZh6QzVfmaiNOVstiXvSIK9fRD-vPgTj9Glw84A7ZEMfXP9_Z4Ym1HyH5ft7NXcRHzlwmlg9vrwUrlvlvenm-LfqTFhzu9QkirnASrWdzUxlF7asnLdktLqsJoOewKk0AVLAZRKeQ_AAAAAVTZ1jYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS =2027429081 list(map(int, getenv("SUDO_USERS", "2027429081").split()))
aiohttpsession = aiohttp.ClientSession()
