# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
import requests
import csv
from pathlib import Path


def fetch_srs_data():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=SRS&year=2024&rformat=csv"
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    out_path = data_dir / "hko_srs_2024.csv"

    # 文件存在就不再下载（作业Fetch once硬性要求）
    if out_path.exists():
        print(f"File {out_path} already exists, skip fetch.")
        return out_path

    resp = requests.get(url)
    resp.raise_for_status()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(resp.text)
    print(f"Raw data saved to {out_path}")
    return out_path


if __name__ == "__main__":
    file_path = fetch_srs_data()

    # 读取并打印原始数据，满足作业Print要求
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print("First row of raw data:", rows[0])
    print("One value from data:", rows[0]["RISE"])
    print("Type of that value:", type(rows[0]["RISE"]))