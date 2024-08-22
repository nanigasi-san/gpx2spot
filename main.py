import csv
import xml.etree.ElementTree as ET


def extract_waypoints(gpx_file):
    tree = ET.parse(gpx_file)
    root = tree.getroot()

    ns = {'default': 'http://www.topografix.com/GPX/1/1'}
    waypoints = []

    for wpt in root.findall('default:wpt', ns):
        lat = wpt.get('lat')
        lon = wpt.get('lon')
        name = wpt.find('default:name', ns).text if wpt.find('default:name', ns) is not None else 'No name'
        waypoints.append((name, '', lat, lon))  # descは空欄

    return waypoints


def save_to_csv(waypoints, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'desc', 'lat', 'lon'])  # ヘッダー行
        writer.writerows(waypoints)


# 使用例
gpx_file = './spots.gpx'
csv_file = 'output.csv'

waypoints = extract_waypoints(gpx_file)
save_to_csv(waypoints, csv_file)

print(f'ウェイポイントが {csv_file} に保存されました')
