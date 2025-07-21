import pandas as pd

def generate_map_data():
    # CSV 파일 경로
    path_category = "dataFile/area_category.csv"
    path_map = "dataFile/area_map.csv"
    path_struct = "dataFile/area_struct.csv"

    # 1. CSV 파일 불러오기
    category_df = pd.read_csv(path_category)
    map_df = pd.read_csv(path_map)
    struct_df = pd.read_csv(path_struct)

    # 2. 데이터 병합 (x, y 기준)
    merged_df = pd.merge(struct_df, map_df, on=["x", "y"], how="inner")

    # 3. area == 1인 데이터만 필터링
    area1_df = merged_df[merged_df["area"] == 1]

    # 4. MyHome(category == 3) 데이터만 필터링 (area 상관없이)
    myhome_df = merged_df[merged_df["category"] == 3]

    # 5. area1_df에 없는 MyHome만 남기기 (중복 제거)
    myhome_unique = myhome_df[~myhome_df[["x", "y"]].apply(tuple, axis=1).isin(area1_df[["x", "y"]].apply(tuple, axis=1))]

    # 6. area1 데이터 + MyHome 데이터 합치기
    filtered_df = pd.concat([area1_df, myhome_unique], ignore_index=True)

    # 7. category 숫자를 이름(struct)으로 매핑
    category_df["category"] = category_df["category"].astype(int)
    filtered_df = pd.merge(filtered_df, category_df, on="category", how="left")

    # 8. 결과 저장
    filtered_df.to_csv("map_data.csv", index=False)
    print("   area1 데이터 필터링 완료 : map_data.csv")

def main():
    generate_map_data()

if __name__ == "__main__":
    main()