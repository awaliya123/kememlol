import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT =700 int(g
STRING_SESSION =BQB4SYJQjoSDz8CNnqdIbadbSiFJaDuXQQ8D_ooEOE6O7gmChUCTWKSKV-vmX83TwVRsZRUj7Q7Ea9K0PmBuVoElTwGDBuqUh87DwmeSF76KrggqKV_7h2pkrjlDYbxqAID8HAcrbGzyBiV1GXJW6gJaKejB9YDhFzT-0f7btbweY6PSk410_YjBMjCOj8TQXQf-YgVJqO7dO-AZh6QzVfmaiNOVstiXvSIK9fRD-vPgTj9Glw84A7ZEMfXP9_Z4Ym1HyH5ft7NXcRHzlwmlg9vrwUrlvlvenm-LfqTFhzu9QkirnASrWdzUxlF7asnLdktLqsJoOewKk0AVLAZRKeQ_AAAAAVTZ1jYA getenv("BQB4SYJQjoSDz8CNnqdIbadbSiFJaDuXQQ8D_ooEOE6O7gmChUCTWKSKV-vmX83TwVRsZRUj7Q7Ea9K0PmBuVoElTwGDBuqUh87DwmeSF76KrggqKV_7h2pkrjlDYbxqAID8HAcrbGzyBiV1GXJW6gJaKejB9YDhFzT-0f7btbweY6PSk410_YjBMjCOj8TQXQf-YgVJqO7dO-AZh6QzVfmaiNOVstiXvSIK9fRD-vPgTj9Glw84A7ZEMfXP9_Z4Ym1HyH5ft7NXcRHzlwmlg9vrwUrlvlvenm-LfqTFhzu9QkirnASrWdzUxlF7asnLdktLqsJoOewKk0AVLAZRKeQ_AAAAAVTZ1jYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS =2027429081 list(map(int, getenv("SUDO_USERS", "2027429081").split()))
aiohttpsession = aiohttp.ClientSession()
