import math

DENSITY = {
    "glass": 2.4,
    "aluminum": 2.7,
    "carbon_steel": 7.85,
}
MARS_G_RATIO = 0.38  # 화성 중력 비율

def sphere_area(diameter_m: float, material: str, thickness_cm: float = 1.0):

    if material not in DENSITY:
        raise ValueError("material은 glass, aluminum, carbon_steel 중 하나여야 합니다.")
    if diameter_m <= 0 or thickness_cm <= 0:
        raise ValueError("지름과 두께는 양수여야 합니다.")

    r = diameter_m / 2.0  # m
    area_m2 = 2 * math.pi * (r ** 2)  # 반구체(바닥 제외) 표면적

    thickness_m = thickness_cm / 100.0
    volume_m3 = area_m2 * thickness_m

    # 단위 변환 및 질량 계산
    volume_cm3 = volume_m3 * 1_000_000.0  # 1 m^3 = 1e6 cm^3
    density_g_cm3 = DENSITY[material]
    mass_g = density_g_cm3 * volume_cm3
    mass_kg = mass_g / 1000.0

    # 화성에서의 '무게'(kgf에 해당하는 값으로 요구사항 표현)
    weight_kg_mars = mass_kg * MARS_G_RATIO
    return area_m2, weight_kg_mars


def main():
    while True:
        try:
            raw_d = input("지름(m)을 입력하세요 (종료:q): ").strip()
            if raw_d.lower() == "q":
                print("프로그램을 종료합니다.")
                break
            diameter = float(raw_d)

            material = input("재질을 입력하세요 [glass/aluminum/carbon_steel]: ").strip()
            if material not in DENSITY:
                raise ValueError("재질은 glass, aluminum, carbon_steel 중에서 선택하세요.")

            raw_t = input("두께(cm, 기본 1): ").strip()
            thickness = 1.0 if raw_t == "" else float(raw_t)

            area, weight = sphere_area(diameter, material, thickness)

            # 지정 형식으로 출력
            # 예: 재질 ⇒ 유리, 지름 ⇒ 10, 두께 ⇒ 1, 면적 ⇒ 314.159, 무게 ⇒ 500.987 kg
            print(
                f"재질 ⇒ {material}, 지름 ⇒ {diameter:g}, 두께 ⇒ {thickness:g}, "
                f"면적 ⇒ {area:.3f}, 무게 ⇒ {weight:.3f} kg"
            )

        except ValueError as e:
            print(f"[입력 오류] {e}")
        except Exception as e:
            print(f"[에러] {e}")

if __name__ == "__main__":
    main()
