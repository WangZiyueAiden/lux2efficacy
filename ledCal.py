import pandas as pd
import lux2eff
# 读取CSV文件

def test(lux= 200):
    df_eff = pd.read_csv("lux-eff.csv")
    df_spec = pd.read_csv("led-spec.csv")

    # 计算总辐照度
    total_irradiance = 0
    total_relative_intensity = df_spec['Relative spectral value'].sum()
    for index, row in df_spec.iterrows():
        wavelength = row['Wavelength (nm)']
        relative_intensity = row['Relative spectral value'] / total_relative_intensity
        total_irradiance += lux2eff.lux_to_irradiance(lux, wavelength, df_eff) * relative_intensity

    print("Total irradiance for the LED light is {:.2f} W/m^2".format(total_irradiance))