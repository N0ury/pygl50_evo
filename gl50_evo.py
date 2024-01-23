import asyncio
import sys
import bleak
import platform

global context_follows

def Record_Access_Control_Point_indic_func(handle: int, data: bytearray):
  if data[0] == 6:
      # This is a response code
      if data[2] == 1 and data[3] == 1:
        # request was "Report stored values" and Response is success
        print ("Measurements got successfully")
        sys.exit()
      else:
        print("*** Error during processing ***")
        sys.exit()

def Glucose_Measurement_Context_notif_func(handle: int, data: bytearray):
  # 4 (Casual), and 5 (Bedtime) => Changed to no context (in bgstar act_events)
  if data[3] in [4, 5]:
    print("")
  else:
    print(f" {data[3] :d}")

def Glucose_Measurement_notif_func(handle: int, data: bytearray):
  year = (data[4] << 8 | data[3])
  month = data[5]
  day = data[6]
  hour = data[7]
  minute = data[8]
  measurement = (data[9] << 8 | data[10])
  print(f"{year :4d}-{month :02d}-{day :02d} {hour :02d}:{minute :02d} {measurement :d}"
    , end='')
  if (data[0] >> 4 != 1):
    context_follows = False
    print("")
  else:
    context_follows = True

async def main(address):
  try:
    async with bleak.BleakClient(address) as client:
      print(f"Connected to {address}")

      await client.start_notify(
        bleak.uuids.normalize_uuid_16(0x2a52), Record_Access_Control_Point_indic_func
      )
      await client.start_notify(
        bleak.uuids.normalize_uuid_16(0x2a34), Glucose_Measurement_Context_notif_func
      )
      await client.start_notify(
        bleak.uuids.normalize_uuid_16(0x2a18), Glucose_Measurement_notif_func
      )
      serial_num = await client.read_gatt_char(bleak.uuids.normalize_uuid_16(0x2a25))
      print(f"Serial Number: {serial_num.decode()}")
#      device_name = await client.read_gatt_char( bleak.uuids.normalize_uuid_16(0x2a00) )
#      print(f"Device Name: {device_name.decode()}")
#      DEVICE_NAME_UUID = "00002a00-0000-1000-8000-00805f9b34fb"
#      device_name = (await client.read_gatt_char(DEVICE_NAME_UUID)).decode()
#      print(f"Connected to {device_name}")
      GET_ALL_RECORDS_COMMAND = bytes([0x1, 0x1])
      await client.write_gatt_char(
        bleak.uuids.normalize_uuid_16(0x2a52), GET_ALL_RECORDS_COMMAND
      )
      print("Waiting for measurements...")
      while True:
        await asyncio.sleep(1)

  except asyncio.exceptions.TimeoutError:
    print(f"Can't connect to device {address}.")


if __name__ == "__main__":
  address = ( # GL50 address
    "ED:AC:3E:EA:54:FF"
    if platform.system() != "Darwin"
    else "2ACAC34E-A163-F72E-30B7-963F16F6E7E1"
  )
  is_success = False
  asyncio.run(main(address))
