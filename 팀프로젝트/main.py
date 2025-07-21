import map_direct_save  # 여기에 main()이 정의되어 있다고 가정
import map_draw         # 예: 시각화만 하는 파일
import caffee_map       # 예: 데이터를 전처리하거나 만드는 파일

def main():
    print("✅ Step 1: 카페 위치 데이터 생성")
    caffee_map.main()

    print("✅ Step 2: 지도 시각화")
    map_draw.main()

    print("✅ Step 3: 최단 경로 계산 및 저장")
    map_direct_save.main()

if __name__ == "__main__":
    main()
