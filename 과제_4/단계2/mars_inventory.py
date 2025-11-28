import csv

INPUT_CSV = "Mars_Base_Inventory_List.csv"
OUTPUT_CSV = "Mars_Base_Inventory_danger.csv"
THRESHOLD = 0.7  # 인화성 지수 기준

def main():
    # 1) CSV 읽어서 화면에 출력
    with open(INPUT_CSV, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = reader.fieldnames or []

    print("=== 원본 CSV ===")
    if headers:
        print(",".join(headers))
    for r in rows:
        print(",".join(r.get(h, "") for h in headers))

    # 2) Python 리스트 객체로 유지(rows 이미 리스트)
    # 3) 인화성 지수(Flammability) 기준 내림차순 정렬
    rows_sorted = sorted(rows, key=lambda r: float(r["Flammability"]), reverse=True)

    # 4) 인화성 지수 >= 0.7 필터링 후 화면 출력
    danger_rows = [r for r in rows_sorted if float(r["Flammability"]) >= THRESHOLD]

    print(f"\n=== 인화성 지수 >= {THRESHOLD} ===")
    if headers:
        print(",".join(headers))
    for r in danger_rows:
        print(",".join(r.get(h, "") for h in headers))

    # 5) 필터링 결과를 CSV로 저장
    with open(OUTPUT_CSV, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(danger_rows)

if __name__ == "__main__":
    main()