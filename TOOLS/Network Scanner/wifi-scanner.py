import pywifi
from pywifi import const
import time

def wifi_scan():
  wifi = pywifi.PyWiFi()
  iface = wifi.interfaces()[0]
  
  iface.scan()
  time.sleep(5)
  
  scan_results = iface.scan_results()
  
  networks = []
  for network in scan_results:
    network_info = {
      'SSID': network.ssid,
      'BSSID': network.bssid,
      'Signal': network.signal,
      'Channel': getattr(network, 'freq', 'Unknown'),  
      'Encrypted': getattr(network, 'akm', ['Unknown'])[0] if network.akm else 'Unknown',  
    }
    networks.append(network_info)
  return networks


if __name__ == "__main__":
  networks = wifi_scan()
  for net in networks:
    print(f"SSID: {net['SSID']}, BSSID: {net['BSSID']}, Signal: {net['Signal']}, Channel: {net['Channel']}, Encrypted: {net['Encrypted']}")