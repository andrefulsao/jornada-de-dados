import pandas as pd
import os
import glob
from utils_log import log_decorator

@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    """
    Uma função de extract que le e consolida os jsons
    """
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Uma função que transforma
    """
    df["Total"] = df["Quantidade"] * df["Venda"]

    return df

@log_decorator
def carregar_dados(formato_saida: list, df: pd.DataFrame):
    """
    Uma função que da load em csv ou parquet
    """
    if "csv" in formato_saida:
        df.to_csv("dados.csv", index=False)
    if "parquet" in formato_saida:
        df.to_parquet("dados.parquet", index=False)

@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_saida: list):    
    data_frame = extrair_dados_e_consolidar(pasta=pasta)
    date_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)    
    carregar_dados(formato_saida, date_frame_calculado)