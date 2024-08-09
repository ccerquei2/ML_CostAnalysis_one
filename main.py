
# seq_key = 412931
# # 469085  400965 # Aporva com justificativa de Custos
# #412931    # Aprova com Justificativa da Fabrica
# #469085  #405019 #469085  # Substitua pelo número da ordem real 405019
# 443254 variaçao IM X IC

# Reinstala todas as dependencias
# pip install -r requirements.txt

# Limpa Diretórios com algum lixo de instalação
# pyinstaller --clean --onefile --name AI_WO_Approval --collect-all embedchain main.py

# pip freeze > requirements.txt
# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --additional-hooks-dir=. main.py
# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" main.py
# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" --add-data "translations;translations" main.py


# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" --add-data "crewai/translations;crewai/translations" main.py

# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" --add-data "crewai/translations\en.json;translations/en.json" main.py

# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\en.json;crewai/translations/en.json" --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" main.py


# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\en.json;crewai/translations" --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" main.py

# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --hidden-import=sklearn.ensemble._forest --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\en.json;crewai/translations" --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\best_random_forest_model.joblib;." main.py

# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --hidden-import=sklearn.ensemble._forest --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\en.json;crewai/translations" --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\best_random_forest_model.joblib;." main.py

# pyinstaller --onefile --name AI_WO_Approval --hidden-import=embedchain --hidden-import=importlib_metadata --hidden-import=sklearn.ensemble._forest --add-data "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\en.json;crewai/translations" --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\slices.json;crewai/translations" --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\role_playing.json;crewai/translations" --add-data "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\best_random_forest_model.joblib;." main.py

# PS C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\dist> .\AI_WO_Approval.exe 412931  "Tivemos um aumento do custo real devido a uma maior utilização das horas de execução de máquina. Tivemos que utilizar a máquina por mais tempo que o previsto."
# C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\crewai\utilities

# .\AI_WO_Approval.exe 412931  "Tivemos um aumento do custo real devido a uma maior utilização das horas de execução de máquina. Tivemos que utilizar a máquina por mais tempo que o previsto."

# pyinstaller - -onefile - -name
# AI_WO_Approval - -hidden -
# import=embedchain - -hidden -
# import=importlib_metadata - -hidden -
# import=sklearn.ensemble._forest - -add - data
# "C:\Users\ccerq\Envs\pythonProject1\ML_CostAnalysis\Lib\site-packages\embedchain-0.1.110.dist-info;embedchain-0.1.110.dist-info" - -add - data
# "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\crewai\translations\en.json;crewai/translations" - -add - data
# "C:\Users\ccerq\OneDrive\Documentos\Python Scripts\ML_CostAnalysis\best_random_forest_model.joblib;."
# main.py

# atualizar o requirements
# pip freeze > requirements.txt
# Visualizar a arvore de diretorios das dependencia
# # pipdeptree

# 412931 "Tivemos um aumento do custo real devido a uma maior utilizaçao das horas de execuçao de maquina. Tivemos que utilizar a maquina por mais tempo que o previsto"

# PS C:\Users\ccerq\OneDrive\Documentos\Python Scripts\WebApprovalWo\WebApprovalWo> python app.py
# PS C:\Users\ccerq\OneDrive\Documentos\Python Scripts\WebApprovalWo\web-frontend> npm start

# git init
# git add *
# git commit -m "commit inicial2"
# git remote add origin https://github.com/ccerquei2/ML_CostAnalysis_one.git
# git branch -M main
# git push -u origin main
#


# ############################################################################################
# # Avalia se Ordem Segue para aprovação
# # Ação	Descriçao_Ação
# # 0	Aprova com Justificativa Plausivel
# # 1	Não Aprovava: Limites fora da Faixa de Aceitação
# # 2	Aprovado Considerando que o Analista de Custo Aprovaria Ordem com tais Limites
# # 3	Não Aprovava: Limites fora da Faixa de Aceitação
# ############################################################################################

import argparse
import Agents_PipeLine
import pandas as pd
import Classify_WorkOrder
from dotenv import load_dotenv
load_dotenv()
import json

class Analise_WO:
    def buscar_justificativa_fabrica(self, SEQ_KEY):
        justificativas = pd.read_csv('C:/Users/ccerq/OneDrive/Documentos/Python Scripts/ML_CostAnalysis/Justificativa_Fabrica.csv', sep=';')
        print("Columns in the CSV file:", justificativas.columns)
        justificativa = justificativas[justificativas['SEQ_KEY'] == SEQ_KEY]
        if not justificativa.empty:
            return justificativa.iloc[0]['JUSTIFICATIVA']
        else:
            return None

def main(seq_key, justificativa):
    classificaWo = Classify_WorkOrder.Analise()
    df = classificaWo.extrair_dados(seq_key)

    predicao = ''
    resultado = ''
    if df is not None:
        resultado = classificaWo.classificar_ordem(df)
        predicao = resultado['Predicted_OUTCOME'].iloc[0]
        if predicao == 'APROVADO AUTOMATICAMENTE':
            predicao = 'APROVADO COM JUSTIFICATIVA SETOR CUSTOS'
        print(predicao)

    json_avalia_limites = []
    json_avalia_limites_str = ''

    json_avalia_limites_str = classificaWo.json_avalia_faixas_aprovacao(seq_key, predicao)
    json_avalia_limites = json.loads(json_avalia_limites_str)

    decisao_aprovar = (json_avalia_limites[0]["Acao"])
    print(decisao_aprovar)


    if decisao_aprovar == 1 or decisao_aprovar == 3:
        print('Um ou mais valores extrapolaram os limites de aprovação via ''Agentes AI'', Segue detalhamento:\n', json_avalia_limites_str)
        try_approve = Agents_PipeLine.PipeLineCoastJustify()
        try_approve.insert_approval_result(seq_key,
                                           float(json_avalia_limites[0]['ORDEM']),
                                           decisao_aprovar,
                                           'Um ou mais valores extrapolaram os limites de aprovação via Agentes AI Analistas de Custos',
                                           json_avalia_limites_str,
                                           'Decisão de Validação: Não Validado')

    else:
        if predicao == 'APROVADO COM JUSTIFICATIVA SETOR CUSTOS':
            try_approve = Agents_PipeLine.PipeLineCoastJustify()
            try_approve.cost_approval_decision(df, decisao_aprovar, json_avalia_limites_str)
        else:
            if justificativa == None or justificativa == '':
                try_approve = Agents_PipeLine.PipeLineCoastJustify()
                try_approve.insert_approval_result(seq_key,
                                                   float(json_avalia_limites[0]['ORDEM']),
                                                   decisao_aprovar,
                                                   'A analise da ordem requer uma Justificativa Plausivel da Fabrica para as Variações Observadas',
                                                   json_avalia_limites_str,
                                                   'Decisão de Validação: Não Validado')
                print('A analise da ordem requer uma Justificativa Plausivel da Fabrica para as Variações Observadas')
            else:
                fab_justificativa = justificativa if justificativa else Analise_WO().buscar_justificativa_fabrica(seq_key)
                print(fab_justificativa)
                print(resultado)

                try_approve = Agents_PipeLine.PipeLineCoastJustify()
                try_approve.approval_decision(df, fab_justificativa, decisao_aprovar, json_avalia_limites_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processar uma ordem de produção.')
    parser.add_argument('SEQ_KEY', type=int, help='O identificador da ordem de produção.')
    parser.add_argument('JUSTIFICATIVA', type=str, nargs='?', help='Justificativa para a diferença de custo da ordem.', default=None)

    args = parser.parse_args()
    main(args.SEQ_KEY, args.JUSTIFICATIVA)
