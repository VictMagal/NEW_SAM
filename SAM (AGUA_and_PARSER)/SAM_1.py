import sys
from PyQt5 import uic, QtWidgets
from SAM_2 import verificação
from SAM_4_docparser import Parseamento_docparser
import openpyxl
import os


class load_arquivos:
        def __init__(self):
            self.arquivo_fornecedor = []
            self.palavra_chave = []
            self.list_fornecedor = []
            self.nome_fornecedor = []
            
            self.lista_parser = ['Telecom_SimInternet', 'Agua_Aegea', 'Agua_Aegea_Seta_Vermelha', 'Agua_Aegea_Seta_Vermelha_testes', 'Agua_Aguas_Arenapolis', 'Agua_AguasDoBrasil', 'Agua_BRK', 'Agua_CAERR', 'Agua_CAESA', 'Agua_Caesb', 'Agua_Cagece', 'Agua_Casan', 'Agua_CEDAE', 'Agua_Cesama', 'Agua_Cesama_teste', 'Agua_Cesan', 'Agua_CIS', 'Agua_Codau', 'Agua_COGERH', 'Agua_Cohasb', 'Agua_Compesa', 'Agua_Comusa', 'Agua_Copasa', 'Agua_Corsan', 'Agua_Cosanpa', 'Agua_DAAE_Araraquara', 'Agua_DAAE_Rio_Claro', 'Agua_DAE_Americana', 'Agua_DAE_Bauru', 'Agua_DAE_Jundiai', 'Agua_DAE_Santa_Barbara', 'Agua_DAE_Santana_do_Livramento', 'Agua_DAEM', 'Agua_DAEP', 'Agua_DAES_Juina', 'Agua_DAEV', 'Agua_Damae_SaoJoaoDelRei', 'Agua_DEMAE_Campo_Belo', 'Agua_Departamento_Divisao_Servico', 'Agua_Depasa', 'Agua_DMAE_Poços_de_Caldas', 'Agua_DMAE_Poços_de_Caldas_copy1', 'Agua_DMAE_Porto_Alegre', 'Agua_DMAE_Uberlandia', 'Agua_Elipse', 'Agua_Emasa', 'Agua_Embasa', 'Agua_Embasa_testes', 'Agua_EMDAEP', 'Agua_Iguasa', 'Agua_Linhas', 'Agua_Prefeitura_Itirapina', 'Agua_Prefeituras', 'Agua_Prolagos', 'Agua_SAAE_Amparo', 'Agua_SAAE_Atibaia', 'Agua_SAAE_Bacabal', 'Agua_SAAE_Balsas', 'Agua_SAAE_Barra_Mansa', 'Agua_SAAE_Bebedouro', 'Agua_SAAE_Campo_Maior', 'Agua_SAAE_Canaa_Dos_Acarajas', 'Agua_SAAE_Capivari', 'Agua_SAAE_Catu', 'Agua_SAAE_Caxias', 'Agua_SAAE_Ceara_Mirim', 'Agua_SAAE_Codo', 'Agua_SAAE_Estancia', 'Agua_SAAE_Garca', 'Agua_SAAE_Governador_Valadares', 'Agua_SAAE_Grajau', 'Agua_SAAE_Ibitinga', 'Agua_SAAE_Iguatu', 'Agua_SAAE_Indaiatuba', 'Agua_SAAE_Itapetinga', 'Agua_SAAE_Itapira', 'Agua_SAAE_Jacareí', 'Agua_SAAE_Juazeiro', 'Agua_SAAE_LençoisPaulistas', 'Agua_SAAE_Limoeiro', 'Agua_SAAE_Linhares', 'Agua_SAAE_Mogi_Mirim', 'Agua_SAAE_Morada_Nova', 'Agua_SAAE_Parauapebas', 'Agua_SAAE_Parintins', 'Agua_SAAE_PDFSimples', 'Agua_SAAE_Penedo', 'Agua_SAAE_Quadrado', 'Agua_SAAE_Quadradoteste', 'Agua_SAAE_Quixeramobim', 'Agua_SAAE_Sao_Carlos', 'Agua_SAAE_Sobral', 'Agua_SAAE_Volta_Redonda', 'Agua_SAAEJ_Jaboticabal', 'Agua_SAAEP', 'Agua_SAAETRI', 'Agua_Sabesp', 'Agua_SAE_Araguari', 'Agua_SAE_Ituiutaba', 'Agua_Saec', 'Agua_Saecil', 'Agua_SaemaAraras', 'Agua_SAEP', 'Agua_SAESA', 'Agua_SAEV', 'Agua_SAMAE_Blumenau', 'Agua_SAMAE_Brusque', 'Agua_SAMAE_Caxias', 'Agua_SAMAE_Jaragua_do_Sul', 'Agua_Samae_Mogi_Guaçu', 'Agua_Sanasa', 'Agua_Saneago', 'Agua_Saneamento', 'Agua_Sanebavi', 'Agua_SANEP', 'Agua_Sanepar', 'Agua_Saneparteste', 'Agua_Sanesalto', 'Agua_SANESUL', 'Agua_SEMAE_Ararangua', 'Agua_Semae_Mogi_das_Cruzes', 'Agua_SEMAE_Piracicaba', 'Agua_SEMAE_São_José_do_Rio_Preto', 'Agua_SEMAE_Sao_Leopoldo', 'Agua_Semasa_Itajaí', 'Agua_Semasa_Santo_Andre', 'Agua_SESAN', 'Agua_Setae', 'Algar_Mapeamento_Bahia', 'Aluguel_2008_Empreendimentos', 'Aluguel_ABS_Administracao', 'Aluguel_Acir_Administracao', 'Aluguel_ACRC_Imoveis', 'Aluguel_ACTA', 'Aluguel_Adala&Adala', 'Aluguel_Adiplantec', 'Aluguel_ADM_Opala', 'Aluguel_ADM_Quatro_Marias', 'Aluguel_AE_Patrimonio', 'Aluguel_AenaBrasil', 'Aluguel_Aeroporto_de_Florianopolis', 'Aluguel_Aguiar_Vasconcelos_Imoveis', 'Aluguel_ALA_Empreendimentos', 'Aluguel_Alianca_Imoveis', 'Aluguel_Americas_Shopping', 'Aluguel_AMPLA', 'Aluguel_Anage_Imoveis', 'Aluguel_Ancora_Imoveis', 'Aluguel_APSA', 'Aluguel_Aracaju_Parque_Shopping', 'Aluguel_ASA_Imoveis', 'Aluguel_Bahia_Outlet_Center', 'Aluguel_Barbara_Scarano', 'Aluguel_Bassanesi', 'Aluguel_Belluomini_Campo_ADM', 'Aluguel_Blumenau_Shopping', 'Aluguel_BNT_Administracao', 'Aluguel_Boulevard_Belem', 'Aluguel_Boulevard_Rio_Shopping', 'Aluguel_Boulevard_Vila_Velha', 'Aluguel_Bourbon_Shopping_SP', 'Aluguel_BPS_Shopping', 'Aluguel_BR_ADM', 'Aluguel_BR_Condominios', 'Aluguel_Brasilia_Shopping', 'Aluguel_Braz_Gondim', 'Aluguel_Castanheira_Shopping', 'Aluguel_CBREAluguel', 'Aluguel_Celeste_Imoveis', 'Aluguel_CenterLeste_Empreendimentos', 'Aluguel_Centro_da_Praia_Shopping', 'Aluguel_Centro_Empresarial_Paseo', 'Aluguel_Champagnat_Center', 'Aluguel_Chindler_ADM', 'Aluguel_Cityspace', 'Aluguel_Civil_Center_Lapa', 'Aluguel_Cohab', 'Aluguel_Cond_CNB_Salistas', 'Aluguel_Condominio_Belo_Horizonte', 'Aluguel_Condominio_Brasilia', 'Aluguel_Condominio_Cidade_Nova', 'Aluguel_Consorcio_Riguat', 'Aluguel_DCL_ADM', 'Aluguel_DF_Service_ADM', 'Aluguel_Ed_Nathalia_Ferreira', 'Aluguel_Edificio_Novitta', 'Aluguel_Edificio_SantoAfonso', 'Aluguel_Emanuel_Elesbao_Marcal', 'Aluguel_Essencial_Imoveis', 'Aluguel_Estila_Administracao', 'Aluguel_Executive_Trade_Center', 'Aluguel_Extra_Center', 'Aluguel_Ferreira_Costa', 'Aluguel_Fili_Empreendimentos', 'Aluguel_Formosa_Supermercados', 'Aluguel_Fraport', 'Aluguel_Frias_Neto', 'Aluguel_Fz_Imoveis', 'Aluguel_Galeria_Minerva', 'Aluguel_Galicia_Imoveis', 'Aluguel_Garantia_Imoveis', 'Aluguel_Gestao3E', 'Aluguel_GM_Administradora', 'Aluguel_Gois_Imobiliaria', 'Aluguel_Golden_Square_Shopping', 'Aluguel_Grand_Shopping_Messejana', 'Aluguel_GRU_Airport', 'Aluguel_Grupo_Big', 'Aluguel_Grupo_Lider', 'Aluguel_Grupo_Pao_De_Acucar', 'Aluguel_Ibiacu', 'Aluguel_Icatu_Holding', 'Aluguel_Iguacu_Participacoes', 'Aluguel_Imobiliaria_Betha', 'Aluguel_Imobiliaria_Forte', 'Aluguel_ImobiliariaRony', 'Aluguel_Infraero', 'Aluguel_INFRAMERICA', 'Aluguel_Interlagos_Shopping', 'Aluguel_Irmaos_Rodopoulos', 'Aluguel_Irmaos_Teixeira', 'Aluguel_J3_ADM', 'Aluguel_Jair_Amintas', 'Aluguel_JCM_ADM', 'Aluguel_Joel_Imoveis', 'Aluguel_Lab_ADM_Imoveis', 'Aluguel_Lago_Imobiliaria', 'Aluguel_Laredo_ADM_Shopping', 'Aluguel_LGN_Empreendimentos', 'Aluguel_Locatual_Participacoes', 'Aluguel_Lojas_Visao_Cruzeiro', 'Aluguel_LuizClaudio_Empreendimentos', 'Aluguel_M4_Condominios', 'Aluguel_Macro_Engenharia_ltda', 'Aluguel_MAG_Shopping', 'Aluguel_Mais_Shopping', 'Aluguel_Mangabeira_Shopping', 'Aluguel_Maranguape_Mall', 'Aluguel_Marca_Imoveis', 'Aluguel_Marilia_Imoveis', 'Aluguel_Marinho_Imoveis', 'Aluguel_Mavira', 'Aluguel_Maxi_Shopping_Jundiai', 'Aluguel_Meira_Imoveis', 'Aluguel_Metha', 'Aluguel_MG_Imobiliaria', 'Aluguel_Minas_Shopping', 'Aluguel_MKA_Locacoes', 'Aluguel_ML_ADM', 'Aluguel_MMS_Empreedimentos', 'Aluguel_Moradia_Empreendimentos', 'Aluguel_Morumbi_Town_Shopping', 'Aluguel_Multicentros_Participacoes', 'Aluguel_Multiplan', 'Aluguel_Naciguat', 'Aluguel_Nazare_Comercial', 'Aluguel_Nilopolis_Shopping', 'Aluguel_North_Shopping_Maracanau', 'Aluguel_Novo_Mundo_ADM', 'Aluguel_Palladium_Shopping', 'Aluguel_Parque_Shopping_Bahia', 'Aluguel_Parque_Shopping_Belem', 'Aluguel_Passeio_Shopping', 'Aluguel_Patio_Batel', 'Aluguel_Patio_Belem', 'Aluguel_Patio_Brasil_Shopping', 'Aluguel_Patio_Dom_Luis', 'Aluguel_Place_Imoveis', 'Aluguel_Planalto_Central_Imoveis', 'Aluguel_Plaza_Shopping', 'Aluguel_Pontual_Imobiliaria', 'Aluguel_Portal_ADM_Bens', 'Aluguel_Power_ADM', 'Aluguel_RC_Nunes_Imoveis', 'Aluguel_Regional_Imoveis', 'Aluguel_Riomar_Fortaleza', 'Aluguel_Riomar_Presidente_Kennedy', 'Aluguel_Riomar_Recife', 'Aluguel_Riomar_Shopping_Aracaju', 'Aluguel_Robotton', 'Aluguel_Rodoviaria_Rio_de_Janeiro', 'Aluguel_Salvador_Shopping', 'Aluguel_Sampaio_Imoveis', 'Aluguel_Santa_Cruz_Shopping', 'Aluguel_Sao_Goncalo_Shopping', 'Aluguel_SaoBernardo_Plaza_Shopping', 'Aluguel_Sendas_Assai', 'Aluguel_Shopping_ABC', 'Aluguel_Shopping_Aldeota', 'Aluguel_Shopping_Barra', 'Aluguel_Shopping_Barra_Bonita', 'Aluguel_Shopping_Bela_Vista', 'Aluguel_Shopping_Boa_Vista', 'Aluguel_Shopping_Center_AguaVerde', 'Aluguel_Shopping_Center_Altiplano', 'Aluguel_Shopping_Center_Piedade', 'Aluguel_Shopping_Center_Sul', 'Aluguel_Shopping_Cidade', 'Aluguel_Shopping_Del_Rey', 'Aluguel_Shopping_Estrada_do_Coco', 'Aluguel_Shopping_Guararapes', 'Aluguel_Shopping_Ibirapuera', 'Aluguel_Shopping_Iguatemi', 'Aluguel_Shopping_Itaigara', 'Aluguel_Shopping_Jardim_das_Americas', 'Aluguel_Shopping_Leblon', 'Aluguel_Shopping_Light', 'Aluguel_Shopping_Metropole_Ananindeua', 'Aluguel_Shopping_Mueller', 'Aluguel_Shopping_Neumarket_Blumenau', 'Aluguel_Shopping_Nova_America', 'Aluguel_Shopping_Park_Europeu', 'Aluguel_Shopping_Praca_da_Moca', 'Aluguel_Shopping_Recife', 'Aluguel_Shopping_RIOSUL', 'Aluguel_Shopping_Tacaruna', 'Aluguel_Shopping_Tambia', 'Aluguel_Shopping_Tijuca', 'Aluguel_Shopping_Uniao_Osasco', 'Aluguel_Shopping_Vale_do_Aco', 'Aluguel_Shopping_Vitoria', 'Aluguel_SMC_Empreendimentos', 'Aluguel_Soul_Malls', 'Aluguel_Termini', 'Aluguel_Terraco_Shopping', 'Aluguel_Terrena_ADM', 'Aluguel_Tiburcio_Rodrigues', 'Aluguel_Today_Imoveis', 'Aluguel_Top_Center', 'Aluguel_Topmig_Imoveis', 'Aluguel_Unimoveis', 'Aluguel_Vasconcelos_Teixeira', 'Aluguel_Via_Illuminata_Mall', 'Aluguel_Via_Park_Shopping', 'Aluguel_Via_Shopping', 'Aluguel_Vivant_Imobiliaria', 'Aluguel_Viviane_Mesquita', 'Aluguel_VRV_Administracao', 'Aluguel_West_Shopping', 'Aluguel_Winner', 'Arkadin_Arcelor', 'Boleto_Itau', 'Boleto_Santander', 'Boleto_Sicredi', 'Combustivel_Ipiranga', 'Combustivel_Petrobras', 'Combustivel_Raizen', 'Condominio_ABG', 'Condominio_Acta', 'Condominio_ADALA&ADALA', 'Condominio_AdfapAdministradora', 'Condominio_Adm_2C', 'Condominio_AdmAngelica', 'Condominio_Agrupador_Condominio', 'Condominio_Alberstein', 'Condominio_Alice_Helena', 'Condominio_Allegro', 'Condominio_AngeloContabilidade', 'Condominio_Apoio', 'Condominio_Apsa', 'Condominio_ArBellentani', 'Condominio_BCF', 'Condominio_Benin', 'Condominio_Birmann', 'Condominio_Bona', 'Condominio_CBRE', 'Condominio_CCP', 'Condominio_CGCExcelent', 'Condominio_Cidade_Nova', 'Condominio_CONAD', 'Condominio_Conservadora_Tropical', 'Condominio_ControlPred', 'Condominio_Crase_Sigma', 'Condominio_Cushman_Wakefield', 'Condominio_DLegend', 'Condominio_Dottus', 'Condominio_Dukman', 'Condominio_Elite', 'Condominio_Exata', 'Condominio_Facel', 'Condominio_Ferrari_ADM', 'Condominio_FLEX', 'Condominio_G2Imoveis', 'Condominio_GestaoAdm', 'Condominio_Gestart', 'Condominio_GialmarCondominios', 'Condominio_Gregorini', 'Condominio_Grupo_Mercurio', 'Condominio_Guarida', 'Condominio_GV', 'Condominio_Habitacional', 'Condominio_Holder', 'Condominio_Hsa', 'Condominio_Hubert', 'Condominio_Itabr', 'Condominio_J2M', 'Condominio_JHI', 'Condominio_JLL', 'Condominio_JoseJoaquim', 'Condominio_JSallum_Wimar_Alliz', 'Condominio_Lar', 'Condominio_Lello', 'Condominio_Lideranca_ADM', 'Condominio_Link_Contabilidade', 'Condominio_Liv_Imobiliaria', 'Condominio_LOGO', 'Condominio_Maranata', 'Condominio_Masset', 'Condominio_Maximize', 'Condominio_Mix', 'Condominio_Moviva', 'Condominio_MS2_Condominios', 'Condominio_Norvic', 'Condominio_NunezAldin', 'Condominio_OfficeCenter', 'Condominio_OfficeOne', 'Condominio_OliconAdministracoes', 'Condominio_OMA', 'Condominio_Operativa', 'Condominio_PactoAdministradora', 'Condominio_PanelliArruda', 'Condominio_ParisCondominios', 'Condominio_PJBank', 'Condominio_Ponto_Futuro', 'Condominio_Predial', 'Condominio_Prefeitura_Brasilia', 'Condominio_Promenade', 'Condominio_Prosind', 'Condominio_Protel', 'Condominio_Quality_House', 'Condominio_RRMarques', 'Condominio_Ruggiero', 'Condominio_Solucao', 'Condominio_SolucoesADM', 'Condominio_Stylo', 'Condominio_SucessoADM', 'Condominio_Target', 'Condominio_TerraBrasilis', 'Condominio_Tocantins', 'Condominio_Torquato', 'Consultoria_Tidsoft', 'Consultoria_XCelis', 'DepartamentoPessoal_Bradesco_Saude', 'DepartamentoPessoal_Prudential', 'DepartamentoPessoal_Sul_America', 'Energia_2W', 'Energia_Aliança', 'Energia_AmazonasEnergia', 'Energia_Banco_BTG', 'Energia_CEA', 'Energia_CEB', 'Energia_CEEE', 'Energia_CELESC', 'Energia_CELESC_copy', 'Energia_Cemig', 'Energia_CemigSim', 'Energia_Cerbanorte', 'Energia_Cercar', 'Energia_CERCI', 'Energia_Cergal', 'Energia_CERMOFUL', 'Energia_CERRP', 'Energia_CHESP', 'Energia_COCEL', 'Energia_Copel', 'Energia_Coprel', 'Energia_CPFL', 'Energia_Demei', 'Energia_DME', 'Energia_Ecom', 'Energia_EDP', 'Energia_Elektro', 'Energia_EMGD', 'Energia_Enel', 'Energia_Energisa', 'Energia_Energisa_testes', 'Energia_Engie', 'Energia_EquatorialEnergia', 'Energia_EquatorialEnergia_testes', 'Energia_Lemon', 'Energia_Light', 'Energia_Merito', 'Energia_NeoEnergia', 'Energia_Nova', 'Energia_Roraima', 'Energia_Safira', 'Energia_SantaMaria', 'Energia_SULGIPE', 'Energia_Tereos', 'Energia_Test', 'Equipamentos_Atm', 'Facilities_Boletos', 'Facilities_Notas_Fiscais', 'GAS_Algas', 'Gas_BahiaGas', 'GAS_Brasiliano', 'GAS_ComGas', 'GAS_Compagas', 'GAS_EXEMPLO', 'GAS_Liquigas', 'GAS_Naturgy', 'GAS_NF_CEGAS', 'GAS_PBGAS', 'GAS_Supergasbras', 'Impressao_RICOH', 'Impressao_Simpress', 'IPTU_Prefeitura_Aracaju', 'IPTU_Prefeitura_Belo_Horizonte', 'IPTU_Prefeitura_Bom_Despacho', 'IPTU_Prefeitura_Caxias_do_Sul', 'IPTU_Prefeitura_Contagem', 'IPTU_Prefeitura_de_Ananindeua', 'IPTU_Prefeitura_de_Anapolis', 'IPTU_Prefeitura_de_Aracatuba', 'IPTU_Prefeitura_de_Balneario_Camboriu', 'IPTU_Prefeitura_de_Bauru', 'IPTU_Prefeitura_de_Bertioga', 'IPTU_Prefeitura_de_Betim', 'IPTU_Prefeitura_de_Blumenau', 'IPTU_Prefeitura_de_Cabo_Frio', 'IPTU_Prefeitura_de_Cajamar', 'IPTU_Prefeitura_de_Camacari', 'IPTU_Prefeitura_de_Campinas', 'IPTU_Prefeitura_de_Campo_grande', 'IPTU_Prefeitura_de_Canoas', 'IPTU_Prefeitura_de_Carapicuiba', 'IPTU_Prefeitura_de_Cariacica', 'IPTU_Prefeitura_de_Catalão', 'IPTU_Prefeitura_de_Conselheiro_Lafaiete', 'IPTU_Prefeitura_de_Cubatao', 'IPTU_Prefeitura_de_Cuiaba', 'IPTU_Prefeitura_de_Curitiba', 'IPTU_Prefeitura_de_Diadema', 'IPTU_Prefeitura_de_Divinopolis', 'IPTU_Prefeitura_de_Duque_de_Caxias', 'IPTU_Prefeitura_de_Florianopolis', 'IPTU_Prefeitura_de_Fortaleza', 'IPTU_Prefeitura_de_Goiania', 'IPTU_Prefeitura_de_Guanambi', 'IPTU_Prefeitura_de_Guaratingueta', 'IPTU_Prefeitura_de_Guarulhos', 'IPTU_Prefeitura_de_Indaiatuba', 'IPTU_Prefeitura_de_Itabira', 'IPTU_Prefeitura_de_Itajai', 'IPTU_Prefeitura_de_Itapevi', 'IPTU_Prefeitura_de_Itu', 'IPTU_Prefeitura_de_Itumbiara', 'IPTU_Prefeitura_de_Jaboatao_dos_Guararapes', 'IPTU_Prefeitura_de_Jandira', 'IPTU_Prefeitura_de_Jatai', 'IPTU_Prefeitura_de_Joao_Pessoa', 'IPTU_Prefeitura_de_Juazeiro_do_Norte', 'IPTU_Prefeitura_de_Juiz_de_Fora', 'IPTU_Prefeitura_de_Jundiai', 'IPTU_Prefeitura_de_Lagarto', 'IPTU_Prefeitura_de_Lagoa_Santa', 'IPTU_Prefeitura_de_Lauro_Freitas', 'IPTU_Prefeitura_de_Londrina', 'IPTU_Prefeitura_de_Macae', 'IPTU_Prefeitura_de_Maceio', 'IPTU_Prefeitura_de_Manaus', 'IPTU_Prefeitura_de_Mogi_das_Cruzes', 'IPTU_Prefeitura_de_Natal', 'IPTU_Prefeitura_de_Navegantes', 'IPTU_Prefeitura_de_Niteroi', 'IPTU_Prefeitura_de_Nova_Iguacu', 'IPTU_Prefeitura_de_Novo_Hamburgo', 'IPTU_Prefeitura_de_Osasco', 'IPTU_Prefeitura_de_Pelotas', 'IPTU_Prefeitura_de_Pouso_Alegre', 'IPTU_Prefeitura_de_Praia_Grande', 'IPTU_Prefeitura_de_Presidente_Prudente', 'IPTU_Prefeitura_de_Presidente_Prudente', 'IPTU_Prefeitura_de_Recife', 'IPTU_Prefeitura_de_Resende', 'IPTU_Prefeitura_de_Ribeirao_Preto', 'IPTU_Prefeitura_de_Rio_Claro', 'IPTU_Prefeitura_de_Rio_Largo', 'IPTU_Prefeitura_de_Santa_Cruz_do_Sul', 'IPTU_Prefeitura_de_Santana_de_Paranaiba', 'IPTU_Prefeitura_de_Santo_Andre', 'IPTU_Prefeitura_de_Sao_Caetano_do_Sul', 'IPTU_Prefeitura_de_Sao_Jose_dos_Campos', 'IPTU_Prefeitura_de_Sao_Jose-SC', 'IPTU_Prefeitura_de_São_Paulo', 'IPTU_Prefeitura_de_Sete_Lagoas', 'IPTU_Prefeitura_de_Teresina', 'IPTU_Prefeitura_de_Uberaba', 'IPTU_Prefeitura_de_Uberlandia', 'IPTU_Prefeitura_de_Uruguaiana', 'IPTU_Prefeitura_de_Varzea_Grande', 'IPTU_Prefeitura_de_Vitoria', 'IPTU_Prefeitura_de_Xangrila', 'IPTU_Prefeitura_Franca', 'IPTU_Prefeitura_Mossoró', 'IPTU_Prefeitura_Porto_Seguro', 'IPTU_Prefeitura_Santos', 'IPTU_Prefeitura_São_Bernardo_Do_Campo', 'IPTU_Prefeitura_Sao_Jose_do_Rio_Preto', 'IPTU_Rio_De_Janeiro', 'IPTU_Salvador', 'IPTU_Sertaozinho', 'iVeloz', 'LicencaSoftware_WASolutions', 'LicencaSoftware_WEVO', 'Limpeza_MGServicos', 'Limpeza_TEJOFRAN', 'Locacao_A4', 'Locacao_AboveNet', 'Locacao_AlertSecurity', 'Locacao_CHGMeridian', 'Locacao_Hitachi', 'Locacao_HPFinancial', 'Locacao_Intelsat', 'Locacao_LocalizaRentACar', 'Locacao_Meso', 'Locacao_MetodoMobile', 'Locacao_Simpress', 'Manutencao_Bestflow', 'Manutencao_Helfen', 'Meio_Ambiente_IBAMA', 'My Document Parser', 'My Invoice Parser', 'SAAE_Sao_Lourenco', 'Servico_Orcali', 'Servicos_Alctel', 'Servicos_AQUIGAS', 'Servicos_Araujo_Abreu', 'Servicos_Aymores', 'Servicos_BNO_Transportes', 'Servicos_Brasvac', 'Servicos_Brinks', 'Servicos_CDL_Belo_Horizonte', 'Servicos_Crowe', 'Servicos_DISAGUA', 'Servicos_DRESSALL', 'Servicos_DROID', 'Servicos_Emplasmyl', 'Servicos_Green_Solutions', 'Servicos_Grupo_Amazonas', 'Servicos_HashtagTV', 'Servicos_HashtagTVTeste', 'Servicos_Icone_One', 'Servicos_INTERGARD', 'Servicos_Klimatos', 'Servicos_Linx', 'Servicos_Metest', 'Servicos_Movenet', 'Servicos_NF_JuizDeFora', 'Servicos_NF_Mandarine', 'Servicos_NF_SSB', 'Servicos_NFEPrefeituraBarueri', 'Servicos_NFEPrefeituraCamposdosGoytacazes', 'Servicos_NFEPrefeituraCarpina', 'Servicos_NFEPrefeituraPoçosDeCaldas', 'Servicos_NFEPrefeituraSaoPaulo', 'Servicos_NFEPrefeituraUberladia', 'Servicos_NFEPrefeituraValinhos', 'Servicos_NFEPrefeituraXanxerê', 'Servicos_NFS-ePrefeituraBH', 'Servicos_Onixlimp', 'Servicos_Owe', 'Servicos_PLANALTO_MS', 'Servicos_Play_Services', 'Servicos_Prefeitura_Belo_Horizonte', 'Servicos_Prefeitura_Municipal_de_Aracaju', 'Servicos_Prefeitura_Municipal_de_Pelotas', 'Servicos_Prefeitura_Municipal_de_Salvador', 'Servicos_Roda_de_Ouro', 'Servicos_Secretaria_Municipal_de_Cascavel', 'Servicos_Secretaria_Municipal_de_Catanduva', 'Servicos_Secretaria_Municipal_de_Dourados', 'Servicos_Selbetti', 'Servicos_Solucx', 'Servicos_Sonda_Ativas', 'Servicos_Studio_OficinaArte', 'Servicos_Supricorp', 'Servicos_TecnoSystem', 'Servicos_TruckWEB', 'Servicos_Unimed', 'Tabelas Schittini TEMP', 'Taxa_FGTS', 'Taxa_FUNESBOM', 'Taxa_INSS', 'Taxa_IRRF', 'Taxa_Taxa_Assistencial', 'Telecom_2ATelecom', 'Telecom_4bTelecom', 'Telecom_4INet', 'Telecom_67Telecom', 'Telecom_AbaseTelecom', 'Telecom_AccessTelecom', 'Telecom_AcemTelecom', 'Telecom_AcerTelecom', 'Telecom_Acesso10', 'Telecom_AcessoTelecomunicações', 'Telecom_Advantage', 'Telecom_Advnet', 'Telecom_Adwave', 'Telecom_AdylNet', 'Telecom_AgilityTelecom', 'Telecom_AgoraNet', 'Telecom_AKTO', 'Telecom_AlgarDados', 'Telecom_Alonet', 'Telecom_AlooTelecom', 'Telecom_Alternativa', 'Telecom_Alternex', 'Telecom_AmazonWifi', 'Telecom_Americanet', 'Telecom_AmericanetTeste', 'Telecom_AmericanTower', 'Telecom_AMilTelecom', 'Telecom_AMNET', 'Telecom_Amplanet', 'Telecom_Apoiocom', 'Telecom_ArenaTelecom', 'Telecom_Arganet', 'Telecom_Arion', 'Telecom_ARKADIN', 'Telecom_Assim', 'Telecom_AssimTelecom', 'Telecom_AT&T', 'Telecom_Atel_do_Brasil', 'Telecom_Avanzi', 'Telecom_Axes', 'Telecom_AzzaTelecom', 'Telecom_BBGTelecom', 'Telecom_Bit_Wave', 'Telecom_Boingo', 'Telecom_BRDigital', 'Telecom_Brisanet', 'Telecom_BrShield', 'Telecom_BRSULNET', 'Telecom_BTCommunications', 'Telecom_Byteweb', 'Telecom_Cabonnet', 'Telecom_CaboTelecom', 'Telecom_CarajasNetwork', 'Telecom_CBNTelecom', 'Telecom_CDL', 'Telecom_CensaNet', 'Telecom_CenturyLink', 'Telecom_CenturyTelecom', 'Telecom_ChapaNet', 'Telecom_Claro', 'Telecom_Claro_testes', 'Telecom_ClaroArgentina', 'Telecom_Click', 'Telecom_CLIG', 'Telecom_CMA', 'Telecom_Comexport ', 'Telecom_CommCORP', 'Telecom_Conectar', 'Telecom_ConectaTelecom', 'Telecom_ConecteTelecom', 'Telecom_ConectivaTelecom', 'Telecom_Conectlan', 'Telecom_ConexaoBA', 'Telecom_Connect_Virtua', 'Telecom_Connectronic', 'Telecom_Connew', 'Telecom_Copel', 'Telecom_CPDQ', 'Telecom_CWMC', 'Telecom_CYLKTechnologing', 'Telecom_DanielTelecom', 'Telecom_DataNetwork', 'Telecom_DCSTelecom', 'Telecom_DesktopSigmanet', 'Telecom_DI2S', 'Telecom_Diatel', 'Telecom_Digitro', 'Telecom_DinamicaServicos', 'Telecom_DirectCall', 'Telecom_DirectNet', 'Telecom_Direta', 'Telecom_Dominet', 'Telecom_DTC', 'Telecom_Duarte_e_Dias', 'Telecom_EBRNet', 'Telecom_EGTech', 'Telecom_Elo', 'Telecom_Embratel', 'Telecom_Embratel_Arbor', 'Telecom_Embratel_PDF', 'Telecom_Emex', 'Telecom_Ensite', 'Telecom_ENW', 'Telecom_Equinix', 'Telecom_Etecc', 'Telecom_EvoInternet', 'Telecom_Evolnet', 'Telecom_Evolunet', 'Telecom_FacilNET', 'Telecom_FaleNET', 'Telecom_Fenix', 'Telecom_Fibralink', 'Telecom_Fibranet', 'Telecom_FIT', 'Telecom_Fixtell', 'Telecom_FlashNet', 'Telecom_Flynet', 'Telecom_Fonelight', 'Telecom_FonteTelecom', 'Telecom_Forte_Telecom', 'Telecom_Frente', 'Telecom_FSF_Tecnologia', 'Telecom_FSOnline', 'Telecom_FullNet', 'Telecom_FuturoNet', 'Telecom_GalizaNET', 'Telecom_GarraTelecom', 'Telecom_GenteTelecom', 'Telecom_GHNET', 'Telecom_GigaLink', 'Telecom_GigaMS', 'Telecom_GlobalLig', 'Telecom_GlobalLines', 'Telecom_GlobalOSI', 'Telecom_Globenet', 'Telecom_GoWIFI', 'Telecom_GrupoA', 'Telecom_GrupoHost', 'Telecom_GrupoPrint', 'Telecom_GTCTelecom', 'Telecom_Guiando', 'Telecom_GuiandoSP', 'Telecom_HILINK', 'Telecom_HIT', 'Telecom_Hitss', 'Telecom_HotLink', 'Telecom_Hotwave', 'Telecom_Housenet', 'Telecom_HT', 'Telecom_Hubtel', 'Telecom_HughesNet', 'Telecom_ICOM', 'Telecom_IFNet', 'Telecom_IFTNET', 'Telecom_IGNET', 'Telecom_IMAX', 'Telecom_Infolink', 'Telecom_Informac', 'Telecom_Infornet', 'Telecom_Infortel', 'Telecom_Infovale', 'Telecom_InoveMidia', 'Telecom_Insidesign', 'Telecom_InsideTelecom', 'Telecom_Intelig', 'Telecom_Interatell', 'Telecom_InterHome', 'Telecom_Interpira', 'Telecom_Intexnet', 'Telecom_IP7', 'Telecom_IPNET', 'Telecom_IT_Net', 'Telecom_ITSBrasil', 'Telecom_ITSTelecom', 'Telecom_ITSTelecom_copy', 'Telecom_Jetz', 'Telecom_JiveTelecom', 'Telecom_Khomp', 'Telecom_L5', 'Telecom_Lanteca', 'Telecom_Lettel', 'Telecom_Life', 'Telecom_LigaFibra', 'Telecom_Link_Cariri', 'Telecom_LinkFire', 'Telecom_Linktel', 'Telecom_Linkweb', 'Telecom_Liv', 'Telecom_LiveTim', 'Telecom_LMTelecom', 'Telecom_Locaweb', 'Telecom_LPNET', 'Telecom_LS_Internet', 'Telecom_M2Telecomunicacoes', 'Telecom_MadeInBrasil', 'Telecom_Mafredine', 'Telecom_MaisLink', 'Telecom_MaisNET', 'Telecom_MaisTelecom', 'Telecom_MARLINK', 'Telecom_MaxiSpeed', 'Telecom_MaxTelecom', 'Telecom_MDNET', 'Telecom_MegafibraTV', 'Telecom_Megafox', 'Telecom_Meganet', 'Telecom_MegaTelecom', 'Telecom_MILTELECOM', 'Telecom_MinasTelecom', 'Telecom_Minutes4All', 'Telecom_MLSWireless', 'Telecom_Movistar', 'Telecom_MTNET', 'Telecom_Multilink', 'Telecom_Multiplay', 'Telecom_Mundivox', 'Telecom_MundoTelecom', 'Telecom_N4Telecomunicacoes', 'Telecom_N8Tecnologia', 'Telecom_Naja', 'Telecom_Navetech', 'Telecom_NBTelecom', 'Telecom_Neogrid', 'Telecom_Net', 'Telecom_NET_&_Telecom', 'Telecom_Net_Telecom', 'Telecom_Net_World', 'Telecom_Netcar', 'Telecom_NetJacarei', 'Telecom_Netonline', 'Telecom_Netsun', 'Telecom_Netway', 'Telecom_NetworkTelecomunicacoes', 'Telecom_Nevoli', 'Telecom_NewConnect', 'Telecom_Nextall', 'Telecom_Nextel', 'Telecom_Nexus', 'Telecom_NexusInformatica', 'Telecom_NIPBR', 'Telecom_Nordeste', 'Telecom_NorteLine', 'Telecom_Nova', 'Telecom_NovaFibra', 'Telecom_Novanet', 'Telecom_NovvaCore', 'Telecom_Oi_B2B', 'Telecom_Oncabo', 'Telecom_OneTech', 'Telecom_OneTelecom', 'Telecom_OnllineTelecom', 'Telecom_Orion', 'Telecom_ORM', 'Telecom_OXI_Brasil_Telecom', 'Telecom_Oxman', 'Telecom_Pamnet', 'Telecom_Paranhananet', 'Telecom_Pilter', 'Telecom_PlanetFone', 'Telecom_Plis', 'Telecom_PointTelecom', 'Telecom_PontoNet', 'Telecom_PontoTelecom', 'Telecom_PortalConexao', 'Telecom_Portalsat', 'Telecom_PowerLine', 'Telecom_PowerNet', 'Telecom_PredialNet', 'Telecom_Primesys', 'Telecom_Prinse', 'Telecom_ProcessTelecom', 'Telecom_ProntoFibra', 'Telecom_ProntoNet', 'Telecom_Provecom', 'Telecom_Quality', 'Telecom_RadioBras', 'Telecom_RCSNet', 'Telecom_RedeCasanet', 'Telecom_RedeIDL', 'Telecom_ReiDasTecnologias', 'Telecom_RGTECH', 'Telecom_RioGaleao', 'Telecom_RiosNetwork', 'Telecom_RomaCabo', 'Telecom_RTM', 'Telecom_RVA', 'Telecom_SeegFibras', 'Telecom_Selbetti', 'Telecom_Sercomtel', 'Telecom_ServNet', 'Telecom_Sigmafone', 'Telecom_Sitecnet', 'Telecom_Sky', 'Telecom_Smart_Sigma', 'Telecom_SMATelecom', 'Telecom_SoftBahia', 'Telecom_SolutionMaster', 'Telecom_SP2TELECOM', 'Telecom_SpeedConnect', 'Telecom_SpeedWeb', 'Telecom_Speedzone_Telecomunicacoes', 'Telecom_SPIN18', 'Telecom_SPNET', 'Telecom_SpnTelecom', 'Telecom_Stetnet', 'Telecom_StreetNet', 'Telecom_STTelecom', 'Telecom_Sudoeste', 'Telecom_Sumicity', 'Telecom_SuperOnda', 'Telecom_SuportWeb', 'Telecom_SupraTelecomunicacoes', 'Telecom_Sustenta', 'Telecom_TCMTelecom', 'Telecom_TekTurbo', 'Telecom_Telecall', 'Telecom_Telecom_Argentina', 'Telecom_TELEFONARNET', 'Telecom_Telefonica_Agentina', 'Telecom_Teletalk', 'Telecom_Teletrend', 'Telecom_Telium', 'Telecom_Telnet', 'Telecom_Tely', 'Telecom_TenInternet', 'Telecom_Terra', 'Telecom_TesaTelecom', 'Telecom_Tim', 'Telecom_Titania', 'Telecom_Tracecom', 'Telecom_Transit', 'Telecom_Transtelco', 'Telecom_TREMNET', 'Telecom_TriTelecom', 'Telecom_TSIBrasil', 'Telecom_TSystems', 'Telecom_TurkeyTelecom', 'Telecom_TVC', 'Telecom_TVN', 'Telecom_UCTelecom', 'Telecom_UltraIP', 'Telecom_UltranetSCM', 'Telecom_Ultrawave', 'Telecom_Um_Telecom', 'Telecom_Unifique', 'Telecom_Unitelco', 'Telecom_Univox', 'Telecom_UpSolucoes', 'Telecom_Valenet', 'Telecom_VarzeaNet', 'Telecom_VellozNet', 'Telecom_Velosat', 'Telecom_Vero', 'Telecom_Vetorial', 'Telecom_VGS', 'Telecom_Vianet', 'Telecom_ViaReal', 'Telecom_ViaTelecom', 'Telecom_ViaVetorial', 'Telecom_Virtex', 'Telecom_Vivo', 'Telecom_Vivo_cop', 'Telecom_VivoRedeInteligente', 'Telecom_VOANET', 'Telecom_VoceTelecom', 'Telecom_Vogel', 'Telecom_Vonex', 'Telecom_VoxConexao', 'Telecom_VsistemTelecom', 'Telecom_W3MEGA', 'Telecom_WCS', 'Telecom_Webby', 'Telecom_WebNet', 'Telecom_WebRoute', 'Telecom_Wgo', 'Telecom_WikiTelecom', 'Telecom_WireLink', 'Telecom_WKVE_Telecom', 'Telecom_WLENET', 'Telecom_Womp', 'Telecom_WSPTelecom', 'Telecom_XTurbo', 'Telecom_YIPI', 'teste_confg_doc_parser', 'Teste_Webhook', 'testeDocParser', 'TesteSaulo', 'Transportadora_Correios', 'Transporte_Boleto', 'Várzea Net', 'Vigilancia_GPS_Tec', 'Vigilancia_ORSEGUPS', 'W2I TELECOM']
            self.lista_parser_agua = ['Agua_Aegea', 'Agua_Aegea_Seta_Vermelha', 'Agua_Aegea_Seta_Vermelha_testes', 'Agua_Aguas_Arenapolis', 'Agua_AguasDoBrasil', 'Agua_BRK', 'Agua_CAERR', 'Agua_CAESA', 'Agua_Caesb', 'Agua_Cagece', 'Agua_Casan', 'Agua_CEDAE', 'Agua_Cesama', 'Agua_Cesama_teste', 'Agua_Cesan', 'Agua_CIS', 'Agua_Codau', 'Agua_COGERH', 'Agua_Cohasb', 'Agua_Compesa', 'Agua_Comusa', 'Agua_Copasa', 'Agua_Corsan', 'Agua_Cosanpa', 'Agua_DAAE_Araraquara', 'Agua_DAAE_Rio_Claro', 'Agua_DAE_Americana', 'Agua_DAE_Bauru', 'Agua_DAE_Jundiai', 'Agua_DAE_Santa_Barbara', 'Agua_DAE_Santana_do_Livramento', 'Agua_DAEM', 'Agua_DAEP', 'Agua_DAES_Juina', 'Agua_DAEV', 'Agua_Damae_SaoJoaoDelRei', 'Agua_DEMAE_Campo_Belo', 'Agua_Departamento_Divisao_Servico', 'Agua_Depasa', 'Agua_DMAE_Poços_de_Caldas', 'Agua_DMAE_Poços_de_Caldas_copy1', 'Agua_DMAE_Porto_Alegre', 'Agua_DMAE_Uberlandia', 'Agua_Elipse', 'Agua_Emasa', 'Agua_Embasa', 'Agua_Embasa_testes', 'Agua_EMDAEP', 'Agua_Iguasa', 'Agua_Linhas', 'Agua_Prefeitura_Itirapina', 'Agua_Prefeituras', 'Agua_Prolagos', 'Agua_SAAE_Amparo', 'Agua_SAAE_Atibaia', 'Agua_SAAE_Bacabal', 'Agua_SAAE_Balsas', 'Agua_SAAE_Barra_Mansa', 'Agua_SAAE_Bebedouro', 'Agua_SAAE_Campo_Maior', 'Agua_SAAE_Canaa_Dos_Acarajas', 'Agua_SAAE_Capivari', 'Agua_SAAE_Catu', 'Agua_SAAE_Caxias', 'Agua_SAAE_Ceara_Mirim', 'Agua_SAAE_Codo', 'Agua_SAAE_Estancia', 'Agua_SAAE_Garca', 'Agua_SAAE_Governador_Valadares', 'Agua_SAAE_Grajau', 'Agua_SAAE_Ibitinga', 'Agua_SAAE_Iguatu', 'Agua_SAAE_Indaiatuba', 'Agua_SAAE_Itapetinga', 'Agua_SAAE_Itapira', 'Agua_SAAE_Jacareí', 'Agua_SAAE_Juazeiro', 'Agua_SAAE_LençoisPaulistas', 'Agua_SAAE_Limoeiro', 'Agua_SAAE_Linhares', 'Agua_SAAE_Mogi_Mirim', 'Agua_SAAE_Morada_Nova', 'Agua_SAAE_Parauapebas', 'Agua_SAAE_Parintins', 'Agua_SAAE_PDFSimples', 'Agua_SAAE_Penedo', 'Agua_SAAE_Quadrado', 'Agua_SAAE_Quadradoteste', 'Agua_SAAE_Quixeramobim', 'Agua_SAAE_Sao_Carlos', 'Agua_SAAE_Sobral', 'Agua_SAAE_Volta_Redonda', 'Agua_SAAEJ_Jaboticabal', 'Agua_SAAEP', 'Agua_SAAETRI', 'Agua_Sabesp', 'Agua_SAE_Araguari', 'Agua_SAE_Ituiutaba', 'Agua_Saec', 'Agua_Saecil', 'Agua_SaemaAraras', 'Agua_SAEP', 'Agua_SAESA', 'Agua_SAEV', 'Agua_SAMAE_Blumenau', 'Agua_SAMAE_Brusque', 'Agua_SAMAE_Caxias', 'Agua_SAMAE_Jaragua_do_Sul', 'Agua_Samae_Mogi_Guaçu', 'Agua_Sanasa', 'Agua_Saneago', 'Agua_Saneamento', 'Agua_Sanebavi', 'Agua_SANEP', 'Agua_Sanepar', 'Agua_Saneparteste', 'Agua_Sanesalto', 'Agua_SANESUL', 'Agua_SEMAE_Ararangua', 'Agua_Semae_Mogi_das_Cruzes', 'Agua_SEMAE_Piracicaba', 'Agua_SEMAE_São_José_do_Rio_Preto', 'Agua_SEMAE_Sao_Leopoldo', 'Agua_Semasa_Itajaí', 'Agua_Semasa_Santo_Andre', 'Agua_SESAN', 'Agua_Setae', 'Aluguel_Shopping_Center_AguaVerde']
            self.lista_parser_energia = ['Energia_2W', 'Energia_Aliança', 'Energia_AmazonasEnergia', 'Energia_Banco_BTG', 'Energia_CEA', 'Energia_CEB', 'Energia_CEEE', 'Energia_CELESC', 'Energia_CELESC_copy', 'Energia_Cemig', 'Energia_CemigSim', 'Energia_Cerbanorte', 'Energia_Cercar', 'Energia_CERCI', 'Energia_Cergal', 'Energia_CERMOFUL', 'Energia_CERRP', 'Energia_CHESP', 'Energia_COCEL', 'Energia_Copel', 'Energia_Coprel', 'Energia_CPFL', 'Energia_Demei', 'Energia_DME', 'Energia_Ecom', 'Energia_EDP', 'Energia_Elektro', 'Energia_EMGD', 'Energia_Enel', 'Energia_Energisa', 'Energia_Energisa_testes', 'Energia_Engie', 'Energia_EquatorialEnergia', 'Energia_EquatorialEnergia_testes', 'Energia_Lemon', 'Energia_Light', 'Energia_Merito', 'Energia_NeoEnergia', 'Energia_Nova', 'Energia_Roraima', 'Energia_Safira', 'Energia_SantaMaria', 'Energia_SULGIPE', 'Energia_Tereos', 'Energia_Test']

        def ler_arquivo_fornecedor(self):
            fornecedor = QtWidgets.QFileDialog.getOpenFileNames()[0]
            
            print(fornecedor)
            print('Arquivos importados:', len(fornecedor))
            
            # with open (fornecedor, 'r') as a:
            #     self.arquivo_fornecedor = a.name
            for arquivo in fornecedor:
                self.list_fornecedor.append(arquivo)

            print('Load file fornecedor complete!')
            print('list_fornecedor:', self.list_fornecedor)
            

        def Identificar_Cliente(self):
            if self.palavra_chave[:3] == 'PUC':
                 self.Cliente = 'PUC'
                 print('Cliente = ',self.Cliente)
                
            elif self.palavra_chave[:3] == 'LOC':
                self.Cliente = 'LOCALIZA'
                print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'RIA':
                self.Cliente = 'RIACHUELO'
                print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'FLE':
                self.Cliente = 'FLEURY'
                print('Cliente = ',self.Cliente)
                
            elif self.palavra_chave[:3] == 'DAK':
                 self.Cliente = 'DAKI'
                 print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'PAG':
                 self.Cliente = 'PAGUE_MENOS'
                 print('Cliente = ',self.Cliente)
            
            elif self.palavra_chave[:3] == 'MRV':
                 self.Cliente = 'MRV'
                 print('Cliente = ',self.Cliente)
                 
            elif self.palavra_chave[:3] == 'DPS':
                 self.Cliente = 'DPSP'
                 print('Cliente = ',self.Cliente)
        
            else: 
                print('Cliente não identificado!!')
      
        def executar_SAM4(self):
            self.nova_list_fornecedor = []
            for nome_arquivo in self.list_fornecedor:
                file_oldname = os.path.join(nome_arquivo)
                
                novo_nome = nome_arquivo[:-4] + self.palavra_chave + '.pdf'
                self.nova_list_fornecedor.append(novo_nome)
                
                file_newname_newfile = os.path.join(novo_nome)
                os.rename(file_oldname, file_newname_newfile)
                
                
            self.list_fornecedor = self.nova_list_fornecedor
            
            
            nome_fornecedor = self.nome_fornecedor
            arquivo_pdf = self.list_fornecedor
            
            chama_SAM4 = Parseamento_docparser(nome_fornecedor, arquivo_pdf)
            self.list_json_parseado = chama_SAM4.importar_pdf()
         
            load_active.json_for_excel()
            
            
        def json_for_excel(self):
            print(self.nome_fornecedor.upper())
            
            if 'AGUA' in self.nome_fornecedor.upper():
                vertical = 'AGUA'
            elif 'ENERGIA' in self.nome_fornecedor.upper():
                vertical = 'ENERGIA'
            
            if vertical == 'AGUA':  
                self.wb_vertical = openpyxl.load_workbook('vertical_agua.xlsx')
                self.ws_vertical = self.wb_vertical['Worksheet']
                
                coluna_faturados = 'valores_faturados'
                
            elif vertical == 'ENERGIA': 
                self.wb_vertical = openpyxl.load_workbook('vertical_energia.xlsx')
                self.ws_vertical = self.wb_vertical['Worksheet']
                
                coluna_faturados = 'valores_faturados_auditoria'
            
            is_data = True
            count_col_vertical = 0
            while is_data:
                count_col_vertical += 1
                data =  self.ws_vertical.cell (row = 1, column = count_col_vertical).value
                if data == None:
                    is_data = False
            
            row_vertical = 2
            print(self.list_json_parseado)
            
            for json_parseado in self.list_json_parseado:
                json_parseado = json_parseado[0]
                print(json_parseado)
                print()
               
                
                if type(json_parseado[coluna_faturados]) == list:
                    quant_pdf = len(json_parseado[coluna_faturados])
                else:
                    quant_pdf = 1
                
                for num_descricao in range(quant_pdf):
                    json_valores_faturados = json_parseado[coluna_faturados]
        
                    if type(json_parseado[coluna_faturados]) == list:
                        json_valores_faturados = json_valores_faturados[num_descricao]
                    
                    print(json_valores_faturados)
                    for j in range(count_col_vertical-1):
                        j+=1
                        column_vertical = self.ws_vertical.cell (row = 1, column = j).value
                        
                        if column_vertical.lower() == 'valores_faturados valor':
                           column_vertical = 'valor'
                        
                        if column_vertical.lower() == 'valores_faturados descricao':
                           column_vertical = 'descricao'
                         
                        if column_vertical.lower() == 'valores_faturados_auditoria descricao':
                           column_vertical = 'descricao'
                        
                        if column_vertical.lower() == 'valores_faturados_auditoria quantidade':
                           column_vertical = 'quantidade'
                           
                        if column_vertical.lower() == 'valores_faturados_auditoria tarifa preco':
                           column_vertical = 'tarifa_preco'
                        
                        if column_vertical.lower() == 'valores_faturados_auditoria valor':
                           column_vertical = 'valor'
                          
                        if json_parseado == None:
                            json_parseado == {}
                        
                        if json_valores_faturados == None:
                            json_valores_faturados == {}
                        
                        if type(json_parseado) != dict:
                            json_parseado == {}
                            print('aviso: json com problema')
                            
                        if type(json_valores_faturados) != dict:  
                            json_valores_faturados == {}
                            print('aviso: json com problema valores faturados')
                        
                        if column_vertical.lower() in json_parseado.keys():
                                valor_parseado = json_parseado[column_vertical.lower()]
                    
                                if vertical == 'AGUA':
                                    if column_vertical.lower() == 'valores_consumo':
                                       json_valor = json_parseado[column_vertical.lower()]
                                       print('json_valor=', json_valor)
                                       print('tipo json_valor=', type(json_valor))
                                       
                                       if type(json_valor) == list:
                                           json_valor = json_valor[0]
                                      
                                       if json_valor == None:
                                           valor_parseado = 0
                                       
                                       elif type(json_valor) == int or type(json_valor) == float or type(json_valor) == str:
                                           valor_parseado = json_valor
                                       
                                       else:
                                           valor_parseado = json_valor['valor']
                                
                                if type(valor_parseado) == list:
                                    valor_parseado = valor_parseado[0]
                                
                                self.ws_vertical.cell (row = row_vertical, column = j).value = valor_parseado

                        elif column_vertical.lower() in json_valores_faturados.keys():
                                print('sim:', column_vertical.lower())
                                
                                valor_faturado = json_valores_faturados[column_vertical.lower()]
                                
                                self.ws_vertical.cell (row = row_vertical, column = j).value = valor_faturado
                    
                    row_vertical += 1
                        
    
            self.wb_vertical.save('______vertical' + self.Cliente + '__' + self.nome_fornecedor+'.xlsx')
            print('Save file >>>>>', '______vertical' + self.Cliente + '__' + self.nome_fornecedor+'.xlsx')
            
            self.list_fornecedor = [('______vertical' + self.Cliente + '__' + self.nome_fornecedor+'.xlsx')]

        
        def executar_SAM2(self):
            print('Executando SAM_2...')
            palavra_chave = tela.lineEdit.text()
            self.palavra_chave = palavra_chave
            
            nome_fornecedor = tela.lineEdit_2.text()
            self.nome_fornecedor = nome_fornecedor
            
            load_active.Identificar_Cliente()
            load_active.executar_SAM4()
            
            fornecedor_x = 0 
            while fornecedor_x < len(self.list_fornecedor):
                print("Fazendo....>> ", self.list_fornecedor[fornecedor_x])
            
                chama_SAM2 = verificação(self.list_fornecedor[fornecedor_x], self.palavra_chave, self.Cliente)
                chama_SAM2.criar_new_sheet()
                chama_SAM2.count_ws()
                chama_SAM2.File_name()      
                chama_SAM2.count_new_ws()
                chama_SAM2.tabela_dinâmica_new_sheet()
                chama_SAM2.comparar_valores()
            
                fornecedor_x+=1
            

app = QtWidgets.QApplication([])
tela = uic.loadUi("Interface_SAM.ui")

tela.show()

load_active = load_arquivos()
tela.pushButton.clicked.connect(load_active.ler_arquivo_fornecedor)
tela.pushButton_4.clicked.connect(load_active.executar_SAM2)

sys.exit(app.exec_())