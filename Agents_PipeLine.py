import time
from crewai import Crew
from agents import ProductionOrderAgents, VariationReviewerAgents, CostDecisionAgents, CostVariationReviewerAgents
from tasks import AnalyzeVariationTask, ReviewVariationTask, Cost_AnalyzeVariationTask, CostReviewVariationTask
from datetime import datetime
import pyodbc
import re
from dotenv import load_dotenv
load_dotenv()

import os
import sys
import joblib
import json



def load_prompts():
    if hasattr(sys, '_MEIPASS'):
        # Estamos em um executável PyInstaller
        base_path = sys._MEIPASS
    else:
        # Estamos em um ambiente de desenvolvimento
        base_path = os.path.abspath(os.path.dirname(__file__))

    translation_path = os.path.join(base_path, 'crewai', 'translations', 'en.json')

    with open(translation_path, 'r') as file:
        prompts = json.load(file)
    return prompts

def load_model():
    if hasattr(sys, '_MEIPASS'):
        # Estamos em um executável PyInstaller
        model_path = os.path.join(sys._MEIPASS, 'best_random_forest_model.joblib')
    else:
        # Estamos em um ambiente de desenvolvimento
        model_path = 'C:/Users/ccerq/OneDrive/Documentos/Python Scripts/ML_CostAnalysis/best_random_forest_model.joblib'

    model = joblib.load(model_path)
    return model

# Exemplo de como usar as funções
prompts1 = load_prompts()
model1 = load_model()



class PipeLineCoastJustify:


    def julian_date(self, date):
        """ Converte uma data em formato padrão para o formato Julian Date."""
        year = date.year % 100  # Obtém os dois últimos dígitos do ano
        day_of_year = (date - datetime(date.year, 1, 1)).days + 1
        return f"1{year:02d}{day_of_year:03d}"

    def insert_approval_result(self, seq_key, ordem, decisao_aprovar, agent_return, json_avalia_limites_str,
                               approval_decision):
        # Conexão com o SQL Server
        conn_str = (
            "DRIVER={SQL Server};"
            "SERVER=DBDEV;"
            "DATABASE=JDE_CRP;"
            "UID=usercisp;"
            "PWD=Dcfsds!245"

        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Obter o próximo valor para GFN002
        cursor.execute("""
            SELECT ISNULL(MAX(GFN002), 0) + 1
            FROM CRPDTA.FN31112Z
            WHERE GFDOCO = ?
        """, ordem)
        gfn002 = cursor.fetchone()[0]

        # Obter a data e hora atuais
        now = datetime.now()
        julian_now = self.julian_date(now)
        gftday = now.strftime("%H%M%S")

        # Inserir os dados na tabela
        cursor.execute("""
            INSERT INTO CRPDTA.FN31112Z (
                GFN001, GFDOCO, GFN002, GFN003, GFDES1, GFNOTTE, GFANSR,
                GFURCD, GFURDT, GFURRF, GFURAT, GFURAB, GFCFGD, GFUSER,
                GFPID, GFUPMJ, GFTDAY
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, seq_key, ordem, gfn002, decisao_aprovar, approval_decision, agent_return, json_avalia_limites_str,
                       '', 0, '', 0, 0, julian_now, 'AIAGENT1', 'PYTHONAI1', julian_now, gftday)

        # Confirmar a transação
        conn.commit()

        # Fechar a conexão
        cursor.close()
        conn.close()




    def execute_with_retries(self, crew, max_retries=3):
        attempts = 0
        while attempts < max_retries:
            try:
                result = crew.kickoff()
                return result
            except Exception as e:
                if "iteration limit" in str(e) or "time limit" in str(e):
                    print(f"Erro encontrado: {e}. Tentando novamente... ({attempts + 1}/{max_retries})")
                    attempts += 1
                else:
                    raise e
        raise Exception("Número máximo de tentativas atingido.")

    def approval_decision(self, df, justify, acao, limits_return):
        # Criação dos agentes
        agents = ProductionOrderAgents()
        reviewer_agents = VariationReviewerAgents()

        variation_analyzer = agents.variation_analysis_agent()
        variation_reviewer = reviewer_agents.variation_reviewer_agent()

        tasks = AnalyzeVariationTask()
        review_tasks = ReviewVariationTask()

        analyze_variation_tasks = []
        review_variation_tasks = []

        order_details = {
            'Material_Used': float(df['MAT_DIF_PERCENTUAL'].iloc[0]),
            'Setup_Hours': float(df['HR_CONFIG_VLR'].iloc[0]),
            'Labor_Hours': float(df['MO_VALOR'].iloc[0]),
            'Machine_Hours': float(df['HR_MAQ_VALOR'].iloc[0]),
            'External_Operation': float(df['EXTERNA_OPERACAO'].iloc[0]),
            'Standard_x_Real': float(df['DIF_CUSTO_P_x_R'].iloc[0]),
            'Variation_IMxIC': float(df['VARIACAO_IMXIC'].iloc[0]),
            'Variation_Material': float(df['MAT_DIF_PERCENTUAL'].iloc[0]),
            'Rate_Machine': float(df['TAXA_MAQUINA_FIXA'].iloc[0]),
            'Rate_Labor': float(df['TAXA_MO_FIXA'].iloc[0]),
            'Rate_Var_Labor': float(df['TAXA_FIXA_VAR_MO'].iloc[0]),
            'Predicted_OUTCOME': df['Predicted_OUTCOME'].iloc[0],
            'Factory_Justify': justify
        }

        # Criação da tarefa de análise de variação
        analyze_task = tasks.analyze_variation(
            agent=variation_analyzer,
            order_details=order_details
        )

        # Adiciona a tarefa de análise ao crew
        analyze_variation_tasks.append(analyze_task)

        # Executa a análise de variação e obtém a decisão
        crew = Crew(
            agents=[variation_analyzer],
            tasks=analyze_variation_tasks,
            max_rpm=29
        )

        start_time = time.time()
        results = self.execute_with_retries(crew)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Crew kickoff took {elapsed_time} seconds.")
        print("Crew usage", crew.usage_metrics)

        print("Resultado da Analise do Primeiro Agente:", results)

        # Criação da tarefa de análise de variação
        analyze_task = review_tasks.review_variation(
            agent=variation_reviewer,
            approval_decision=results,
            order_details=order_details
        )

        # Adiciona a tarefa de análise ao crew
        review_variation_tasks.append(analyze_task)

        # Adiciona a tarefa de revisão ao crew
        crew = Crew(
            agents=[variation_reviewer],
            tasks=review_variation_tasks,
            max_rpm=29
        )

        time.sleep(5)
        start_time = time.time()
        review_results = self.execute_with_retries(crew)
        end_time = time.time()
        elapsed_time = end_time - start_time



        # Usando expressão regular para extrair a decisão de validação
        match = re.search(r"Decisão de Validação: (Validado|Não Validado)", review_results)
        if match:
            decisao_aprovar = match.group(0)
            # print("Decisão de Aprovação:", decisao_aprovar)
        else:
            decisao_aprovar = "Decisão de Validação: Não Validado"

        self.insert_approval_result(float(df['SEQ_KEY'].iloc[0]),
                                    float(df['ORDEM'].iloc[0]),
                                    acao,
                                    review_results,
                                    limits_return,
                                    decisao_aprovar)

        # Exemplo de uso
        print("Resultado da Analise do Segundo Agente:", review_results)
        print("Decisão de Aprovação:", decisao_aprovar)

        print("Resultado da Analise do Segundo Agente:", review_results)

        print(f"Review crew kickoff took {elapsed_time} seconds.")
        print("Review crew usage", crew.usage_metrics)

    def cost_approval_decision(self, df, acao, limits_return):
        # Criação dos agentes
        agents = CostDecisionAgents()
        reviewer_agents = CostVariationReviewerAgents()

        variation_analyzer = agents.cost_variation_analysis_agent()
        variation_reviewer = reviewer_agents.cost_variation_reviewer_agent()

        tasks = Cost_AnalyzeVariationTask()
        review_tasks = CostReviewVariationTask()

        analyze_variation_tasks = []
        review_variation_tasks = []

        order_details = {
            'Material_Used': float(df['MAT_DIF_PERCENTUAL'].iloc[0]),
            'Setup_Hours': float(df['HR_CONFIG_VLR'].iloc[0]),
            'Labor_Hours': float(df['MO_VALOR'].iloc[0]),
            'Machine_Hours': float(df['HR_MAQ_VALOR'].iloc[0]),
            'External_Operation': float(df['EXTERNA_OPERACAO'].iloc[0]),
            'Standard_x_Real': float(df['DIF_CUSTO_P_x_R'].iloc[0]),
            'Variation_IMxIC': float(df['VARIACAO_IMXIC'].iloc[0]),
            'Variation_Material': float(df['MAT_DIF_PERCENTUAL'].iloc[0]),
            'Rate_Machine': float(df['TAXA_MAQUINA_FIXA'].iloc[0]),
            'Rate_Labor': float(df['TAXA_MO_FIXA'].iloc[0]),
            'Rate_Var_Labor': float(df['TAXA_FIXA_VAR_MO'].iloc[0]),
            'Predicted_OUTCOME': df['Predicted_OUTCOME'].iloc[0]
        }

        # Criação da tarefa de análise de variação
        analyze_task = tasks.costanalyze_variation(
            agent=variation_analyzer,
            order_details=order_details
        )

        # Adiciona a tarefa de análise ao crew
        analyze_variation_tasks.append(analyze_task)

        # Executa a análise de variação e obtém a decisão
        crew = Crew(
            agents=[variation_analyzer],
            tasks=analyze_variation_tasks,
            max_rpm=29
        )

        start_time = time.time()
        results = self.execute_with_retries(crew)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Crew kickoff took {elapsed_time} seconds.")
        print("Crew usage", crew.usage_metrics)

        print("Resultado da Analise do Primeiro Agente:", results)

        # Criação da tarefa de análise de variação
        analyze_task = review_tasks.cost_review_variation(
            agent=variation_reviewer,
            approval_decision=results,
            order_details=order_details
        )

        # Adiciona a tarefa de análise ao crew
        review_variation_tasks.append(analyze_task)

        # Adiciona a tarefa de revisão ao crew
        crew = Crew(
            agents=[variation_reviewer],
            tasks=review_variation_tasks,
            max_rpm=29
        )

        time.sleep(5)
        start_time = time.time()
        review_results = self.execute_with_retries(crew)
        end_time = time.time()
        elapsed_time = end_time - start_time


        # Usando expressão regular para extrair a decisão de validação
        match = re.search(r"Decisão de Validação: (Validado|Não Validado)", review_results)
        if match:
            decisao_aprovar = match.group(0)
            # print("Decisão de Aprovação:", decisao_aprovar)
        else:
            decisao_aprovar = "Decisão de Validação: Não Validado"

        self.insert_approval_result(float(df['SEQ_KEY'].iloc[0]),
                                    float(df['ORDEM'].iloc[0]),
                                    acao,
                                    review_results,
                                    limits_return,
                                    decisao_aprovar)

        print("Resultado da Analise do Segundo Agente:", review_results)

        print(f"Review crew kickoff took {elapsed_time} seconds.")
        print("Review crew usage", crew.usage_metrics)
