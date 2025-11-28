# mars_parts_analysis.py
import numpy as np
import pandas as pd

# 파일 이름
F1 = "mars_base_main_parts-001.csv"
F2 = "mars_base_main_parts-002.csv"
F3 = "mars_base_main_parts-003.csv"
OUT = "parts_to_work_on.csv"

def main():
    # 1) CSV 파일을 NumPy로 읽어 각각 배열 생성
    df1 = pd.read_csv(F1)
    df2 = pd.read_csv(F2)
    df3 = pd.read_csv(F3)

    arr1 = df1["strength"].to_numpy()
    arr2 = df2["strength"].to_numpy()
    arr3 = df3["strength"].to_numpy()

    # 2) 공통 parts 기준 병합
    merged = (
        df1.rename(columns={"strength": "s1"})
        .merge(df2.rename(columns={"strength": "s2"}), on="parts", how="inner")
        .merge(df3.rename(columns={"strength": "s3"}), on="parts", how="inner")
    )

    # 3) 세 배열을 병합하여 parts라는 ndarray 생성
    parts = np.column_stack([merged["s1"], merged["s2"], merged["s3"]])

    # 4) 항목별 평균값 계산
    avg = np.mean(parts, axis=1)

    # 5) 평균값이 50보다 작은 항목만 필터링
    mask = avg < 50
    filtered = merged.loc[mask, ["parts", "s1", "s2", "s3"]].copy()
    filtered["avg"] = avg[mask]

    # 6) CSV로 저장 (예외 처리 포함)
    try:
        filtered.to_csv(OUT, index=False)
        print(f"저장 완료: {OUT}")
    except Exception as e:
        print(f"[저장 오류] {e}")

if __name__ == "__main__":
    main()
