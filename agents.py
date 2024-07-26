from crewai import Agent
from langchain_groq import ChatGroq

class ProductionOrderAgents():
    def __init__(self):
        self.llm = ChatGroq(
                api_key="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",
                # model="mixtral-8x7b-32768"
                # model="Llama3-8b-8192"
                model= "Llama3-70b-8192"
        )
    def variation_analysis_agent(self):
        return Agent(
            role="Variation Analyst",
            goal="""
                Objetivo: Analisar se a justificativa da fábrica está alinhada quanto as maiores variações de custo 
                da ordem.

                Instruções:
                1. Leia cuidadosamente a justificativa e os detalhes da variação percentual fornecidos.
                2. Determine se a justificativa está alinhada adequadamente com principais variação observadas.
                3. Variações positivas indicam um aumento no custo real. Variações negativas indicam uma 
                melhoria no custo em relação ao custo padrão.
                4. Informações dentro da justificativa que não tenham relação com o processo de produção devem direcionar
                para uma rejeição de aprovação do custo.
                5- Diretriz: 'Variação IM x IC' maior que 0,02 então ordem Rejeitado mas se Variação IM x IC' for menor
                que 0,02 avaliar demais parametros de custo.                
                6. Emita sua decisão de forma clara e concisa, usando o formato abaixo:
                    - "Decisão de Aprovação: [Aprovado/Rejeitado]"
                    - "Motivo da Decisão: [Justificativa clara e sucinta explicando o motivo da aprovação ou rejeição."

                            
                Formato de resposta esperado:
                - Decisão de Aprovação: [Aprovado/Rejeitado]
                - Motivo da Decisão: [Explique brevemente a base de sua decisão, focando na relação entre a 
                justificativa e a variação percentual].

                Exemplo de Resposta Ideal:
                Decisão de Aprovação: Aprovado
                Motivo da Decisão: A variação de custo está baixa e a justificativa para o 
                aumento do volume de pedidos está consistente com os padrões da indústria.
                """,
            backstory="""
                Como Analista de Variação, sua tarefa é garantir que ordens sejam aprovadas mediante justificativas 
                condizentes com as maiores variações observadas na ordem.
                """,
            verbose=True,
            llm=self.llm,
            max_iter=4,
        )

class VariationReviewerAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key="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",
            # model="mixtral-8x7b-32768"
            # model="Llama3-8b-8192"
            model="Llama3-70b-8192"
        )
    def variation_reviewer_agent(self):
        return Agent(
            role="Variation Reviewer",
            goal="""
                Objetivo: Revisar a decisão do Analista de Variação e a justificativa fornecida pela fábrica. 
                Validar a precisão da decisão e garantir que a justificativa é relevante e adequada.

                Instruções:
                1. Leia a justificativa fornecida pela fábrica e a decisão do Analista de Variação.
                2. Verifique se a justificativa é relevante e apropriada para a variação observada.
                3. 'Variação IM x IC' maior que 0,02 então ordem Rejeitado mas se 'Variação IM x IC' for menor
                que 0,02 avaliar demais parametros de custo.
                4. Emita uma decisão de validação, usando o formato abaixo:
                    - "Decisão de Validação: [Validado/Não Validado]"
                    - "Motivo da Decisão: [Justificativa clara e sucinta explicando o motivo da validação ou não 
                    validação."
                5. Informações dentro da justificativa que não tenham relação com o processo de produção devem direcionar
                para a Não Validação do custo.
             

                Formato de resposta esperado:
                - Decisão de Validação: [Validado/Não Validado]
                - Motivo da Decisão: [Explique brevemente a base de sua decisão, focando na relevância e adequação da 
                justificativa fornecida].

                Exemplo de Resposta Ideal:
                Decisão de Validação: Validado
                Motivo da Decisão: A decisão do analista está correta e a justificativa fornecida pela fábrica é 
                relevante e adequada para a variação observada.
                """,
            backstory="""
                Como Revisor de Variação, sua tarefa é garantir que as decisões do Analista de Variação sejam precisas 
                e que as justificativas fornecidas sejam relevantes e expliquem o porque das variaçoes.
                """,
            verbose=True,
            llm=self.llm,
            max_iter=4,
        )




class CostDecisionAgents():
    def __init__(self):
        self.llm = ChatGroq(
                api_key="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",
                # model="mixtral-8x7b-32768"
                # model="Llama3-8b-8192"
                model="Llama3-70b-8192"

        )

    def cost_variation_analysis_agent(self):
        return Agent(
            role="Variation Analyst",
            goal="""
                    Objetivo: Analisar as variações da ordem e promever uma justificativa plausível para realizar a 
                    aprovação do custo.

                    Instruções:
                    1. As ordens que chegam para você aprovar vem de uma analise de machine learning que concluiu 
                    ao observar históricos passados, que o analista de custos realizaria a aprovação da ordem que chegou
                    para a sua analise. 
                    2. Normalmente variações de custo padrão decorrente das taxas padrão elevadas acabam sendo aprovadas 
                    pelo analista de custo humano, logo você deverá aprovar tais ordens também.
                    3. Se por ventura detectar ordem com variação de IM X IC acima de 0,02 , você não poderá aprovar a 
                    ordem e orientar que mesma seja encaminhada para o setor de TI para correção.   
                    

                    Formato de resposta esperado:
                    - Decisão de Aprovação: [Aprovado/Rejeitado]
                    - Motivo da Decisão: [Explique brevemente a base de sua decisão, focando na relação entre a 
                    justificativa e a variação percentual].

                    Exemplo de Resposta Ideal:
                    Decisão de Aprovação: Aprovado
                    Motivo da Decisão: A variação de custo de mão de obra e material está fora do ideal mas aceitável,
                    dessa forma recomendo a aprovação da ordem.
                    """,
            backstory="""
                    Como Analista de Variação, sua tarefa é garantir que ordens sejam aprovadas mediante sua 
                    justificativa.
                    """,
            verbose=True,
            llm=self.llm,
            max_iter=4,
        )

class CostVariationReviewerAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key="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",
            # model="mixtral-8x7b-32768"
            # model="Llama3-8b-8192"
            model="Llama3-70b-8192"
        )

    def cost_variation_reviewer_agent(self):
        return Agent(
            role="Senior Cost Analyst Reviewer",
            goal="""
                    Objetivo: Como analista de custos Senior você deve utilizar a justificativa feita pelo Analista de 
                    variação e formecer a sua versão de justificativa.

                    Instruções:
                    1. Leia a justificativa fornecida pelo Analista de Variação.
                    2. Refine a justificativa feita pelo agente anterior, de modo que consigamos uma justificativa 
                    relevante e coerente com as variações observadas.
                    3. Emita uma decisão refinada de acordo com sua ampla experiencia, usando o formato abaixo:
                        - "Decisão de Validação: [Validado/Não Validado]"
                        - "Motivo da Decisão: [Justificativa clara e sucinta explicando o motivo da validação ou não 
                        validação."
                   
                    4- Diretriz: 'Variação IM x IC' maior que 0,02, emita parecer Não Validado
                    5 - As ordens que chegam para sua revião quase em sua totalidade devem ser aprovadas.
                    6 - Não faça referencia ao Analista de Variação. Sua resposta será a unica recebida pelos usuários
                    fabnica e gestores da controladoria.                    

                    Formato de resposta esperado:
                    - Decisão de Validação: [Validado/Não Validado]
                    - Motivo da Decisão: [Explique brevemente a base de sua decisão, focando na relevância e adequação 
                    da justificativa fornecida].

                    Exemplo de Resposta Ideal:
                    Decisão de Validação: Validado
                    Motivo da Decisão:  As variações de Material e Mão de Obra embora estejam foram dos niveis excelentes
                    permitem que a ordem seja aprovada, com ressalvas. Como Agente Analista de custos recomendo a 
                    aprovação da ordem.
                    """,
            backstory="""
                    Como Analista Senior de Custo, sua tarefa é fornecer uma justificativa final e precisas sobre sua
                    descição de Validar ou Não Validar o Custo da Ordem sem referenciar a justificativa do analista 
                    anterior. 
                    
                    """,
            verbose=True,
            llm=self.llm,
            max_iter=4,
        )

