# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# import joblib
# import json
#
#
# class Analise:
#     def __init__(self):
#         self.server = 'DBDEV'
#         self.database = 'JDE_CRP'
#         self.username = 'consultas_diretas'  # Substitua com seu usuário
#         self.password = 'c_diretas'  # Substitua com sua senha
#
#     def cria_Conn(self):
#         connection_string = (
#             f"DRIVER={{SQL Server}};"
#             f"SERVER={self.server};"
#             f"DATABASE={self.database};"
#             f"UID={self.username};"
#             f"PWD={self.password}"
#         )
#         connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#         engine = create_engine(connection_url)
#         return engine
#
#     def extrair_dados(self, SEQ_KEY):
#         query = f"""
#         SELECT
#             SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL,
#             TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR,
#             HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO
#         FROM  CRPDTA.FNML481
#         WHERE SEQ_KEY = {SEQ_KEY}
#         ORDER BY ORDEM, SEQ_KEY
#         """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(query, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#     def avalia_faixas_aprovacao(self, SEQ_KEY, predict):
#         sql = f"""
#             SELECT
#                     Acao = MAX(FAIXAS.Ação),
#                     ORDEM = VALORES.ORDEM,
#                     FAIXAS.Outcome,
#                     Descriçao_Ação = (SELECT TOP 1 DESCFAIXAS.Descriçao_Ação FROM CRPDTA.FNML481L DESCFAIXAS WHERE MAX(FAIXAS.Ação) = DESCFAIXAS.Ação),
#                     VARIACAO_IMXIC        = MAX(ABS(VALORES.VARIACAO_IMXIC)),
#                     LIMITE_VARIACAO_IMXIC = LIMITE.VARIACAO_IMXIC,
#                     DIF_CUSTO_P_x_R        = MAX(ABS(VALORES.DIF_CUSTO_P_x_R)) ,
#                     LIMITE_DIF_CUSTO_P_x_R = LIMITE.DIF_CUSTO_P_x_R,
#                     MAT_DIF_PERCENTUAL    = MAX(ABS(VALORES.MAT_DIF_PERCENTUAL)),
#                     LIMITE_MAT_DIF_PERCENTUAL = LIMITE.MAT_DIF_PERCENTUAL,
#                     TAXA_MAQUINA_FIXA    = MAX(ABS(VALORES.TAXA_MAQUINA_FIXA)),
#                     LIMITE_TAXA_MAQUINA_FIXA = LIMITE.TAXA_MAQUINA_FIXA,
#                     TAXA_MO_FIXA        = MAX(ABS(VALORES.TAXA_MO_FIXA)),
#                     LIMITE_TAXA_MO_FIXA = LIMITE.TAXA_MO_FIXA,
#                     TAXA_FIXA_VAR_MO    = MAX(ABS(VALORES.TAXA_FIXA_VAR_MO)),
#                     LIMITE_TAXA_FIXA_VAR_MO = LIMITE.TAXA_FIXA_VAR_MO,
#                     MO_VALOR            = MAX(ABS(VALORES.MO_VALOR)),
#                     LIMITE_MO_VALOR = LIMITE.MO_VALOR,
#                     HR_MAQ_VALOR        = MAX(ABS(VALORES.HR_MAQ_VALOR)),
#                     LIMITE_HR_MAQ_VALOR = LIMITE.HR_MAQ_VALOR,
#                     HR_EXC_VLR            = MAX(ABS(VALORES.HR_EXC_VLR)),
#                     LIMITE_HR_EXC_VLR = LIMITE.HR_EXC_VLR,
#                     HR_CONFIG_VLR        = MAX(ABS(VALORES.HR_CONFIG_VLR)),
#                     LIMITE_HR_CONFIG_VLR = LIMITE.HR_CONFIG_VLR,
#                     MO_VARIACAO            = MAX(ABS(VALORES.MO_VARIACAO)),
#                     LIMITE_MO_VARIACAO = LIMITE.MO_VARIACAO,
#                     EXTERNA_OPERACAO    = MAX(ABS(VALORES.EXTERNA_OPERACAO)),
#                     LIMITE_EXTERNA_OPERACAO = LIMITE.EXTERNA_OPERACAO,
#                     VAR_EM_REAIS        = MAX(ABS(VALORES.VAR_EM_REAIS)),
#                     LIMITE_VAR_EM_REAIS = LIMITE.VAR_EM_REAIS
#                 FROM
#                         CRPDTA.FNML481 VALORES,
#                         CRPDTA.FNML481L FAIXAS
#                         LEFT JOIN
#                         CRPDTA.FNML481L LIMITE ON
#                         LIMITE.AÇÃO IN ('1','3') AND
#                         LIMITE.Outcome = FAIXAS.Outcome
#
#                 WHERE
#                     (
#                     ABS(VALORES.VARIACAO_IMXIC)            >    FAIXAS.VARIACAO_IMXIC OR
#                     ABS(VALORES.DIF_CUSTO_P_x_R)        >    FAIXAS.DIF_CUSTO_P_x_R OR
#                     ABS(VALORES.MAT_DIF_PERCENTUAL)      >    FAIXAS.MAT_DIF_PERCENTUAL OR
#                     ABS(VALORES.TAXA_MAQUINA_FIXA)        >    FAIXAS.TAXA_MAQUINA_FIXA OR
#                     ABS(VALORES.TAXA_MO_FIXA)            >    FAIXAS.TAXA_MO_FIXA OR
#                     ABS(VALORES.TAXA_FIXA_VAR_MO)        >    FAIXAS.TAXA_FIXA_VAR_MO OR
#                     ABS(VALORES.MO_VALOR)                >    FAIXAS.MO_VALOR OR
#                     ABS(VALORES.HR_MAQ_VALOR)            >    FAIXAS.HR_MAQ_VALOR OR
#                     ABS(VALORES.HR_EXC_VLR)                >    FAIXAS.HR_EXC_VLR OR
#                     ABS(VALORES.HR_CONFIG_VLR)            >    FAIXAS.HR_CONFIG_VLR OR
#                     ABS(VALORES.MO_VARIACAO)            >    FAIXAS.MO_VARIACAO OR
#                     ABS(VALORES.EXTERNA_OPERACAO)        >    FAIXAS.EXTERNA_OPERACAO OR
#                     ABS(VALORES.VAR_EM_REAIS)            >    FAIXAS.VAR_EM_REAIS
#                     )
#                     AND  VALORES.SEQ_KEY = {SEQ_KEY}
#                     AND  FAIXAS.Outcome = '{predict}'
#                 GROUP BY
#                      FAIXAS.Outcome,
#                      VALORES.ORDEM,
#                      LIMITE.VARIACAO_IMXIC,
#                      LIMITE.DIF_CUSTO_P_x_R,
#                      LIMITE.MAT_DIF_PERCENTUAL,
#                      LIMITE.TAXA_MAQUINA_FIXA,
#                      LIMITE.TAXA_MO_FIXA,
#                      LIMITE.TAXA_FIXA_VAR_MO,
#                      LIMITE.MO_VALOR,
#                      LIMITE.HR_MAQ_VALOR,
#                      LIMITE.HR_EXC_VLR,
#                      LIMITE.HR_CONFIG_VLR,
#                      LIMITE.MO_VARIACAO,
#                      LIMITE.EXTERNA_OPERACAO,
#                      LIMITE.VAR_EM_REAIS
#             """
#         engine = self.cria_Conn()
#         if engine:
#             df = pd.read_sql(sql, engine)
#             engine.dispose()
#             return df
#         else:
#             return None
#
#
#     def json_avalia_faixas_aprovacao(self, SEQ_KEY, predict):
#         df = self.avalia_faixas_aprovacao(SEQ_KEY, predict)
#         if df is not None:
#             # Cria uma lista de dicionários para cada linha, sinalizando valores superiores aos limites
#             results = []
#             for index, row in df.iterrows():
#                 result = {col: row[col] for col in df.columns}
#                 for col in df.columns:
#                     if "LIMITE_" in col and col.replace("LIMITE_", "") in df.columns:
#                         value_col = col.replace("LIMITE_", "")
#                         result[f"{value_col}_EXCEDE_LIMITE"] = row[value_col] > row[col]
#                 results.append(result)
#
#             # Converte a lista de resultados em JSON
#             json_result = json.dumps(results, ensure_ascii=False, indent=4)
#
#             return json_result
#         else:
#             return None
#
#
#     def preprocess_data(self, df):
#         # Remover as colunas identificadoras
#         identifiers = df[['SEQ_KEY', 'ORDEM']]
#         df = df.drop(['SEQ_KEY', 'ORDEM'], axis=1)
#
#         # Aplicar a codificação dummies (se necessário)
#         df = pd.get_dummies(df)
#
#         # Carregar o scaler treinado
#         scaler = joblib.load('C:/Users/ccerq/OneDrive/Documentos/Python Scripts/ML_CostAnalysis/scaler.joblib')
#         df_normalized = scaler.transform(df)
#
#         return df_normalized, identifiers
#
#     def classificar_ordem(self, df):
#         # Carregar o modelo treinado
#         model = joblib.load('C:/Users/ccerq/OneDrive/Documentos/Python Scripts/ML_CostAnalysis/best_random_forest_model.joblib')
#
#         # Pré-processar os dados
#         df_normalized, identifiers = self.preprocess_data(df)
#
#         # Realizar a classificação
#         predictions = model.predict(df_normalized)
#
#         # Adicionar as previsões ao DataFrame original
#         df['Predicted_OUTCOME'] = predictions
#
#         # Restaurar os identificadores
#         result_df = pd.concat([identifiers.reset_index(drop=True), df.reset_index(drop=True)], axis=1)
#
#         return result_df
#
#
#


import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import joblib
import json


class Analise:
    def __init__(self):
        self.server = 'DBDEV'
        self.database = 'JDE_CRP'
        self.username = 'consultas_diretas'  # Substitua com seu usuário
        self.password = 'c_diretas'  # Substitua com sua senha
        self.root_path = os.path.dirname(os.path.abspath(__file__))  # Caminho da pasta raiz do executável

    def cria_Conn(self):
        connection_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password}"
        )
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        engine = create_engine(connection_url)
        return engine

    def extrair_dados(self, SEQ_KEY):
        query = f"""
        SELECT 
            SEQ_KEY, ORDEM, VARIACAO_IMXIC = ABS(VARIACAO_IMXIC), DIF_CUSTO_P_x_R, MAT_DIF_PERCENTUAL, 
            TAXA_MAQUINA_FIXA, TAXA_MO_FIXA, TAXA_FIXA_VAR_MO, MO_VALOR, HR_MAQ_VALOR, 
            HR_EXC_VLR, HR_CONFIG_VLR, MO_VARIACAO, EXTERNA_OPERACAO 
        FROM  CRPDTA.FNML481
        WHERE SEQ_KEY = {SEQ_KEY}
        ORDER BY ORDEM, SEQ_KEY
        """
        engine = self.cria_Conn()
        if engine:
            df = pd.read_sql(query, engine)
            engine.dispose()
            return df
        else:
            return None

    def avalia_faixas_aprovacao(self, SEQ_KEY, predict):
        sql = f"""        
            SELECT     
                    Acao = MAX(FAIXAS.Ação),
                    ORDEM = VALORES.ORDEM,
                    FAIXAS.Outcome,
                    Descriçao_Ação = (SELECT TOP 1 DESCFAIXAS.Descriçao_Ação FROM CRPDTA.FNML481L DESCFAIXAS WHERE MAX(FAIXAS.Ação) = DESCFAIXAS.Ação),
                    VARIACAO_IMXIC        = MAX(ABS(VALORES.VARIACAO_IMXIC)),    
                    LIMITE_VARIACAO_IMXIC = LIMITE.VARIACAO_IMXIC,
                    DIF_CUSTO_P_x_R        = MAX(ABS(VALORES.DIF_CUSTO_P_x_R)) ,
                    LIMITE_DIF_CUSTO_P_x_R = LIMITE.DIF_CUSTO_P_x_R,
                    MAT_DIF_PERCENTUAL    = MAX(ABS(VALORES.MAT_DIF_PERCENTUAL)), 
                    LIMITE_MAT_DIF_PERCENTUAL = LIMITE.MAT_DIF_PERCENTUAL,
                    TAXA_MAQUINA_FIXA    = MAX(ABS(VALORES.TAXA_MAQUINA_FIXA)),
                    LIMITE_TAXA_MAQUINA_FIXA = LIMITE.TAXA_MAQUINA_FIXA,
                    TAXA_MO_FIXA        = MAX(ABS(VALORES.TAXA_MO_FIXA)),
                    LIMITE_TAXA_MO_FIXA = LIMITE.TAXA_MO_FIXA,
                    TAXA_FIXA_VAR_MO    = MAX(ABS(VALORES.TAXA_FIXA_VAR_MO)),
                    LIMITE_TAXA_FIXA_VAR_MO = LIMITE.TAXA_FIXA_VAR_MO,
                    MO_VALOR            = MAX(ABS(VALORES.MO_VALOR)),
                    LIMITE_MO_VALOR = LIMITE.MO_VALOR,
                    HR_MAQ_VALOR        = MAX(ABS(VALORES.HR_MAQ_VALOR)),
                    LIMITE_HR_MAQ_VALOR = LIMITE.HR_MAQ_VALOR,
                    HR_EXC_VLR            = MAX(ABS(VALORES.HR_EXC_VLR)),    
                    LIMITE_HR_EXC_VLR = LIMITE.HR_EXC_VLR,
                    HR_CONFIG_VLR        = MAX(ABS(VALORES.HR_CONFIG_VLR)),    
                    LIMITE_HR_CONFIG_VLR = LIMITE.HR_CONFIG_VLR,
                    MO_VARIACAO            = MAX(ABS(VALORES.MO_VARIACAO)),
                    LIMITE_MO_VARIACAO = LIMITE.MO_VARIACAO,
                    EXTERNA_OPERACAO    = MAX(ABS(VALORES.EXTERNA_OPERACAO)),
                    LIMITE_EXTERNA_OPERACAO = LIMITE.EXTERNA_OPERACAO,
                    VAR_EM_REAIS        = MAX(ABS(VALORES.VAR_EM_REAIS)),
                    LIMITE_VAR_EM_REAIS = LIMITE.VAR_EM_REAIS 
                FROM  
                        CRPDTA.FNML481 VALORES,
                        CRPDTA.FNML481L FAIXAS
                        LEFT JOIN 
                        CRPDTA.FNML481L LIMITE ON
                        LIMITE.AÇÃO IN ('1','3') AND
                        LIMITE.Outcome = FAIXAS.Outcome

                WHERE
                    (
                    ABS(VALORES.VARIACAO_IMXIC)            >    FAIXAS.VARIACAO_IMXIC OR 
                    ABS(VALORES.DIF_CUSTO_P_x_R)        >    FAIXAS.DIF_CUSTO_P_x_R OR
                    ABS(VALORES.MAT_DIF_PERCENTUAL)      >    FAIXAS.MAT_DIF_PERCENTUAL OR
                    ABS(VALORES.TAXA_MAQUINA_FIXA)        >    FAIXAS.TAXA_MAQUINA_FIXA OR
                    ABS(VALORES.TAXA_MO_FIXA)            >    FAIXAS.TAXA_MO_FIXA OR
                    ABS(VALORES.TAXA_FIXA_VAR_MO)        >    FAIXAS.TAXA_FIXA_VAR_MO OR
                    ABS(VALORES.MO_VALOR)                >    FAIXAS.MO_VALOR OR
                    ABS(VALORES.HR_MAQ_VALOR)            >    FAIXAS.HR_MAQ_VALOR OR
                    ABS(VALORES.HR_EXC_VLR)                >    FAIXAS.HR_EXC_VLR OR
                    ABS(VALORES.HR_CONFIG_VLR)            >    FAIXAS.HR_CONFIG_VLR OR
                    ABS(VALORES.MO_VARIACAO)            >    FAIXAS.MO_VARIACAO OR
                    ABS(VALORES.EXTERNA_OPERACAO)        >    FAIXAS.EXTERNA_OPERACAO OR
                    ABS(VALORES.VAR_EM_REAIS)            >    FAIXAS.VAR_EM_REAIS
                    )
                    AND  VALORES.SEQ_KEY = {SEQ_KEY}
                    AND  FAIXAS.Outcome = '{predict}'       
                GROUP BY 
                     FAIXAS.Outcome,
                     VALORES.ORDEM,
                     LIMITE.VARIACAO_IMXIC,
                     LIMITE.DIF_CUSTO_P_x_R,
                     LIMITE.MAT_DIF_PERCENTUAL,
                     LIMITE.TAXA_MAQUINA_FIXA,
                     LIMITE.TAXA_MO_FIXA,
                     LIMITE.TAXA_FIXA_VAR_MO,
                     LIMITE.MO_VALOR,
                     LIMITE.HR_MAQ_VALOR,
                     LIMITE.HR_EXC_VLR,
                     LIMITE.HR_CONFIG_VLR,
                     LIMITE.MO_VARIACAO,
                     LIMITE.EXTERNA_OPERACAO,
                     LIMITE.VAR_EM_REAIS               
            """
        engine = self.cria_Conn()
        if engine:
            df = pd.read_sql(sql, engine)
            engine.dispose()
            return df
        else:
            return None


    def json_avalia_faixas_aprovacao(self, SEQ_KEY, predict):
        df = self.avalia_faixas_aprovacao(SEQ_KEY, predict)
        if df is not None:
            # Cria uma lista de dicionários para cada linha, sinalizando valores superiores aos limites
            results = []
            for index, row in df.iterrows():
                result = {col: row[col] for col in df.columns}
                for col in df.columns:
                    if "LIMITE_" in col and col.replace("LIMITE_", "") in df.columns:
                        value_col = col.replace("LIMITE_", "")
                        result[f"{value_col}_EXCEDE_LIMITE"] = row[value_col] > row[col]
                results.append(result)

            # Converte a lista de resultados em JSON
            json_result = json.dumps(results, ensure_ascii=False, indent=4)

            return json_result
        else:
            return None


    def preprocess_data(self, df):
        # Remover as colunas identificadoras
        identifiers = df[['SEQ_KEY', 'ORDEM']]
        df = df.drop(['SEQ_KEY', 'ORDEM'], axis=1)

        # Aplicar a codificação dummies (se necessário)
        df = pd.get_dummies(df)

        # Carregar o scaler treinado
        scaler_path = os.path.join(self.root_path, 'scaler.joblib')
        scaler = joblib.load(scaler_path)
        df_normalized = scaler.transform(df)

        return df_normalized, identifiers

    def classificar_ordem(self, df):
        # Carregar o modelo treinado
        model_path = os.path.join(self.root_path, 'best_random_forest_model.joblib')
        model = joblib.load(model_path)

        # Pré-processar os dados
        df_normalized, identifiers = self.preprocess_data(df)

        # Realizar a classificação
        predictions = model.predict(df_normalized)

        # Adicionar as previsões ao DataFrame original
        df['Predicted_OUTCOME'] = predictions

        # Restaurar os identificadores
        result_df = pd.concat([identifiers.reset_index(drop=True), df.reset_index(drop=True)], axis=1)

        return result_df
