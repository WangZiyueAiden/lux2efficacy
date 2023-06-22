import pandas as pd

# 读取CSV文件


# 定义一个函数来根据波长找到对应的光通量效率
def get_efficacy(wavelength, df=None):
    # 用波长找到对应的行
    if df is None:
        df = pd.read_csv("lux-eff.csv")
    row = df[df['wavelength'] == wavelength]
    if len(row) == 0:
        raise ValueError("No efficacy data for wavelength {} nm".format(wavelength))
    return row['efficacy'].values[0]

# 定义一个函数来将lux转换为辐照度
def lux_to_irradiance(lux, wavelength, df=None):
    efficacy = get_efficacy(wavelength, df) * 683  # Multiply by maximum efficacy
    return lux / efficacy

# 测试函数
def test():
    wavelength = 555  # nm
    lux = 1000        # lm/m^2
    print("Irradiance for {} nm light with intensity {} lux is {} W/m^2".format(wavelength, lux, lux_to_irradiance(lux, wavelength)))
