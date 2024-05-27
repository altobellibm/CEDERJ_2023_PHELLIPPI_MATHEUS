--Scripts de Criação da base de dados no SQL SERVER, utilizando o Management Studio
CREATE DATABASE ProjetoTCC
GO

--Utilização a base de dados
USE ProjetoTCC
GO

--Criação da tabela
CREATE TABLE [dbo].[TabelaProjeto](
	[fmun_cod] [int] NOT NULL,
	[fmun] [nvarchar](50) NULL,
	[ano] [smallint] NOT NULL,
	[mes] [tinyint] NOT NULL,
	[mes_ano] [nvarchar](50) NULL,
	[regiao] [nvarchar](50) NULL,
	[hom_doloso] [int] NULL,
	[lesao_corp_morte] [int] NULL,
	[latrocinio] [int] NULL,
	[cvli] [int] NULL,
	[hom_por_interv_policial] [int] NULL,
	[letalidade_violenta] [int] NULL,
	[tentat_hom] [int] NULL,
	[lesao_corp_dolosa] [int] NULL,
	[estupro] [int] NULL,
	[hom_culposo] [int] NULL,
	[lesao_corp_culposa] [int] NULL,
	[roubo_transeunte] [int] NULL,
	[roubo_celular] [int] NULL,
	[roubo_em_coletivo] [int] NULL,
	[roubo_rua] [int] NULL,
	[roubo_veiculo] [int] NULL,
	[roubo_carga] [int] NULL,
	[roubo_comercio] [int] NULL,
	[roubo_residencia] [int] NULL,
	[roubo_banco] [int] NULL,
	[roubo_cx_eletronico] [int] NULL,
	[roubo_conducao_saque] [int] NULL,
	[roubo_apos_saque] [int] NULL,
	[roubo_bicicleta] [int] NULL,
	[outros_roubos] [int] NULL,
	[total_roubos] [int] NULL,
	[furto_veiculos] [int] NULL,
	[furto_transeunte] [int] NULL,
	[furto_coletivo] [int] NULL,
	[furto_celular] [int] NULL,
	[furto_bicicleta] [int] NULL,
	[outros_furtos] [int] NULL,
	[total_furtos] [int] NULL,
	[sequestro] [int] NULL,
	[extorsao] [int] NULL,
	[sequestro_relampago] [int] NULL,
	[estelionato] [int] NULL,
	[apreensao_drogas] [int] NULL,
	[posse_drogas] [int] NULL,
	[trafico_drogas] [int] NULL,
	[apreensao_drogas_sem_autor] [int] NULL,
	[recuperacao_veiculos] [int] NULL,
	[apf] [int] NULL,
	[aaapai] [int] NULL,
	[cmp] [int] NULL,
	[cmba] [int] NULL,
	[ameaca] [int] NULL,
	[pessoas_desaparecidas] [int] NULL,
	[encontro_cadaver] [int] NULL,
	[encontro_ossada] [int] NULL,
	[pol_militares_mortos_serv] [int] NULL,
	[pol_civis_mortos_serv] [int] NULL,
	[registro_ocorrencias] [int] NULL,
	[fase] [tinyint] NULL,
 CONSTRAINT [PK_TabelaProjeto] PRIMARY KEY ([fmun_cod] ,[ano],[mes]))
 GO


