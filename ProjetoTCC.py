import pandas as pd
import pyodbc
import requests
from io import StringIO

def download_csv(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

url = "https://www.ispdados.rj.gov.br/Arquivos/BaseMunicipioMensal.csv"

csv_data = download_csv(url)

if csv_data:
    data = pd.read_csv(StringIO(csv_data), sep=';')
    df = pd.DataFrame(data)

    dados_conexao = (
        'Driver={SQL Server};'
        r"Server=Phellippi\TCC;"
        'Database=ProjetoTCC;'
    )
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    transposed_df = df.transpose()

    for row in df.itertuples():
        cursor.execute('''
            INSERT INTO TabelaProjeto(fmun_cod, fmun, ano, mes, mes_ano, regiao,hom_doloso,lesao_corp_morte,latrocinio,cvli,hom_por_interv_policial,letalidade_violenta,tentat_hom,lesao_corp_dolosa,estupro,hom_culposo,lesao_corp_culposa,roubo_transeunte,roubo_celular,roubo_em_coletivo,roubo_rua,roubo_veiculo,roubo_carga,roubo_comercio,roubo_residencia,roubo_banco,roubo_cx_eletronico,roubo_conducao_saque,roubo_apos_saque,roubo_bicicleta,outros_roubos,total_roubos,furto_veiculos,furto_transeunte,furto_coletivo,furto_celular,furto_bicicleta,outros_furtos,total_furtos,sequestro,extorsao,sequestro_relampago,estelionato,apreensao_drogas,posse_drogas,trafico_drogas,apreensao_drogas_sem_autor,recuperacao_veiculos,apf,aaapai,cmp,cmba,ameaca,pessoas_desaparecidas,encontro_cadaver,encontro_ossada,pol_militares_mortos_serv,pol_civis_mortos_serv,registro_ocorrencias,fase)
            SELECT 
              *
            FROM (VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)) x (fmun_cod, fmun, ano, mes, mes_ano, regiao,hom_doloso,lesao_corp_morte,latrocinio,cvli,hom_por_interv_policial,letalidade_violenta,tentat_hom,lesao_corp_dolosa,estupro,hom_culposo,lesao_corp_culposa,roubo_transeunte,roubo_celular,roubo_em_coletivo,roubo_rua,roubo_veiculo,roubo_carga,roubo_comercio,roubo_residencia,roubo_banco,roubo_cx_eletronico,roubo_conducao_saque,roubo_apos_saque,roubo_bicicleta,outros_roubos,total_roubos,furto_veiculos,furto_transeunte,furto_coletivo,furto_celular,furto_bicicleta,outros_furtos,total_furtos,sequestro,extorsao,sequestro_relampago,estelionato,apreensao_drogas,posse_drogas,trafico_drogas,apreensao_drogas_sem_autor,recuperacao_veiculos,apf,aaapai,cmp,cmba,ameaca,pessoas_desaparecidas,encontro_cadaver,encontro_ossada,pol_militares_mortos_serv,pol_civis_mortos_serv,registro_ocorrencias,fase)
            WHERE NOT EXISTS (
                SELECT 1 FROM TabelaProjeto y
                WHERE y.fmun_cod = x.fmun_cod
                    and y.ano = x.ano
                    and y.mes = x.mes
            )
        ''', row.fmun_cod, row.fmun, row.ano, row.mes, row.mes_ano, row.regiao, row.hom_doloso, row.lesao_corp_morte,
                       row.latrocinio, row.cvli, row.hom_por_interv_policial, row.letalidade_violenta, row.tentat_hom,
                       row.lesao_corp_dolosa, row.estupro, row.hom_culposo, row.lesao_corp_culposa,
                       row.roubo_transeunte, row.roubo_celular, row.roubo_em_coletivo, row.roubo_rua, row.roubo_veiculo,
                       row.roubo_carga, row.roubo_comercio, row.roubo_residencia, row.roubo_banco,
                       row.roubo_cx_eletronico, row.roubo_conducao_saque, row.roubo_apos_saque, row.roubo_bicicleta,
                       row.outros_roubos, row.total_roubos, row.furto_veiculos, row.furto_transeunte,
                       row.furto_coletivo, row.furto_celular, row.furto_bicicleta, row.outros_furtos, row.total_furtos,
                       row.sequestro, row.extorsao, row.sequestro_relampago, row.estelionato, row.apreensao_drogas,
                       row.posse_drogas, row.trafico_drogas, row.apreensao_drogas_sem_autor, row.recuperacao_veiculos,
                       row.apf, row.aaapai, row.cmp, row.cmba, row.ameaca, row.pessoas_desaparecidas,
                       row.encontro_cadaver, row.encontro_ossada, row.pol_militares_mortos_serv,
                       row.pol_civis_mortos_serv, row.registro_ocorrencias, row.fase
                       )

    # Confirmar as alterações
    conexao.commit()
else:
    print("Falha ao baixar o CSV.")

# Fechar a conexão com o banco de dados
conexao.close()
