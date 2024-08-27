import pywifi
from pywifi import const
import time

AKM_MAP = {
    0: 'Open',
    1: 'WEP',
    2: 'WPA',
    3: 'WPA2',
    4: 'WPA2'
}

def wifi_scan():
  wifi = pywifi.PyWiFi()
  iface = wifi.interfaces()[0]
  
  iface.scan()
  time.sleep(5)
  
  scan_results = iface.scan_results()
  
  networks = []
  for network in scan_results:
    
    akm_value = network.akm[0] if network.akm else 'Unknown'
    encrypted = AKM_MAP.get(akm_value, 'Unknown')
    
    network_info = {
      'SSID': network.ssid,
      'BSSID': network.bssid,
      'Signal': network.signal,
      'Channel': getattr(network, 'freq', 'Unknown'),  
      'Encrypted': encrypted,  
    }
    networks.append(network_info)
  return networks


if __name__ == "__main__":
  networks = wifi_scan()
  for net in networks:
    print(f"SSID: {net['SSID']}, BSSID: {net['BSSID']}, Signal: {net['Signal']}, Channel: {net['Channel']}, Encrypted: {net['Encrypted']}")