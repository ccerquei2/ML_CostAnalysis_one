
#
# from crewai import Task
#
#
# class AnalyzeVariationTask():
#     def analyze_variation(self, agent, order_details):
#         return Task(
#             description=f"""
#                 Analyze the provided justification in relation to the variation and decide on the approval.
#
#                 Order Details and Percentage Variations:
#                 - 'Material Used': {order_details['Material_Used']}%
#                 - 'Setup Hours': {order_details['Setup_Hours']}%
#                 - 'Labor Hours': {order_details['Labor_Hours']}%
#                 - 'Machine Hours': {order_details['Machine_Hours']}%
#                 - 'External Operation': {order_details['External_Operation']}%
#                 - 'Standard x Real': {order_details['Standard_x_Real']}%
#                 - 'IM x IC Variation': {order_details['Variation_IMxIC']}%
#                 - 'Material Variation': {order_details['Variation_Material']}%
#                 - 'Machine Rate': {order_details['Rate_Machine']}%
#                 - 'Labor Rate': {order_details['Rate_Labor']}%
#                 - 'Labor Variation Rate': {order_details['Rate_Var_Labor']}%
#                 - Predicted Action by the Agent: {order_details['Predicted_OUTCOME']}
#
#                 - Factory Justification: '{order_details['Factory_Justify']}'
#
#                 Guidelines:
#                 - 'IM x IC Variation' greater than 0.02 then Do Not approve, but if 'IM x IC Variation' is less than
#                 0.02 evaluate other cost parameters to decide on the approval.
#                 - Predicted Action as 'REQUIRES FACTORY JUSTIFICATION': Requires detailed justification.
#                 - Predicted Action as 'APPROVED WITH COST SECTOR JUSTIFICATION': Approve the order with comments on
#                 the values.
#             """,
#             agent=agent,
#             expected_output="Provide an approval or rejection decision with clear justifications for each variation analyzed. ",
#             async_execution = False,
#         )
#
# class ReviewVariationTask():
#     def review_variation(self, agent, approval_decision, order_details):
#         return Task(
#             description=f"""
#                 Review the approval decision and the provided justification to ensure accuracy and relevance.
#
#                 Approval Decision:
#                 {approval_decision}
#                 Order Percentage Variations:
#                 -  Negative Values equal better profitability
#                 -  Positive Values equal higher than expected cost
#                 {order_details}
#
#                 Guidelines:
#                 - Verify if the justification is relevant and appropriate for the observed variation.
#                 - Issue a validation decision based on the analyst's decision review.
#                 - 'IM x IC Variation' greater than 0.02 then order Not Validated, but if 'IM x IC Variation' is less than
#                 0.02 evaluate other cost parameters to decide on the approval.
#                 Expected response format:
#                 - Validation Decision: [Validated/Not Validated]
#                 - Reason for Decision: [Briefly explain the basis of your decision, focusing on the relevance and
#                 adequacy of the provided justification].
#                 """,
#             agent=agent,
#             expected_output="Provide a validation decision with clear justifications for the approval or rejection of the initial decision.",
#             async_execution = False,
#         )
#
# class Cost_AnalyzeVariationTask():
#     def costanalyze_variation(self, agent, order_details):
#         return Task(
#             description=f"""
#                 Analyze the order variation data and provide your justification for approval.
#
#                 Order Details and Percentage Variations:
#                 - 'Material Used': {order_details['Material_Used']}%
#                 - 'Setup Hours': {order_details['Setup_Hours']}%
#                 - 'Labor Hours': {order_details['Labor_Hours']}%
#                 - 'Machine Hours': {order_details['Machine_Hours']}%
#                 - 'External Operation': {order_details['External_Operation']}%
#                 - 'Standard x Real': {order_details['Standard_x_Real']}%
#                 - 'IM x IC Variation': {order_details['Variation_IMxIC']}%
#                 - 'Material Variation': {order_details['Variation_Material']}%
#                 - 'Machine Rate': {order_details['Rate_Machine']}%
#                 - 'Labor Rate': {order_details['Rate_Labor']}%
#                 - 'Labor Variation Rate': {order_details['Rate_Var_Labor']}%
#                 - Predicted Action by the Agent: {order_details['Predicted_OUTCOME']}
#
#                 Guidelines:
#                 - 'IM x IC Variation' greater than 0.02 then Do Not approve, but if 'IM x IC Variation' is less than
#                 0.02 evaluate other cost parameters to decide on the approval.
#                 - Predicted Action as 'REQUIRES FACTORY JUSTIFICATION': Requires detailed justification.
#                 - Predicted Action as 'APPROVED WITH COST SECTOR JUSTIFICATION': Approve the order with comments on
#                 the values.
#                 """,
#             agent=agent,
#             expected_output="Provide an approval or rejection decision with clear justifications for each variation analyzed.",
#             async_execution = False,
# )
#
# class CostReviewVariationTask():
#     def cost_review_variation(self, agent, approval_decision, order_details):
#         return Task(
#             description=f"""
#                 Use the previous agent's justification to refine and provide a more professional justification.
#
#                 Approval Decision:
#                 {approval_decision}
#                 Order Percentage Variations:
#                 -  Negative Values equal better profitability
#                 -  Positive Values equal higher than expected cost
#                 {order_details}
#
#                 Guidelines:
#                 - Verify if the justification is relevant and appropriate for the observed variation.
#                 - Issue a validation decision based on the analyst's decision review.
#                 - 'IM x IC Variation' greater than 0.02 then Do Not approve, but if 'IM x IC Variation' is less than
#                 0.02 evaluate other cost parameters to decide on the approval.
#
#                 Expected response format:
#                 - Validation Decision: [Validated/Not Validated]
#                 - Reason for Decision: [Briefly explain the basis of your decision, focusing on the relevance and
#                 adequacy of the provided justification].
#                 """,
#             agent=agent,
#             expected_output="Provide a validation decision with clear justifications for the approval or rejection.",
#             async_execution=False,
#     )


from crewai import Task

class AnalyzeVariationTask():
    def analyze_variation(self, agent, order_details):
        return Task(
            description=f"""
                Analise a justificativa fornecida em relação à variação e decida sobre a aprovação.

                Detalhes da Ordem e Variações Percentuais:
                - 'Material Utilizado': {order_details['Material_Used']}%
                - 'Horas de Setup': {order_details['Setup_Hours']}%
                - 'Horas de Trabalho': {order_details['Labor_Hours']}%
                - 'Horas de Máquina': {order_details['Machine_Hours']}%
                - 'Operação Externa': {order_details['External_Operation']}%
                - 'Padrão x Real': {order_details['Standard_x_Real']}%
                - 'Variação IM x IC': {order_details['Variation_IMxIC']}%
                - 'Variação de Material': {order_details['Variation_Material']}%
                - 'Taxa de Máquina': {order_details['Rate_Machine']}%
                - 'Taxa de Trabalho': {order_details['Rate_Labor']}%
                - 'Taxa de Variação do Trabalho': {order_details['Rate_Var_Labor']}%
                - Ação Prevista pelo Agente: {order_details['Predicted_OUTCOME']}

                - Justificativa da Fábrica: '{order_details['Factory_Justify']}'

                Diretrizes:
                - 'Variação IM x IC' maior que 0,02 então Não aprovar, mas se 'Variação IM x IC' for menor que
                0,02 avaliar demais parametros de custo para decidir sobrea a aprovação.
                - Ação Prevista como 'REQUER JUSTIFICATIVA FABRICA': Requer justificativa detalhada.
                - Ação Prevista como 'APROVADO COM JUSTIFICATIVA SETOR CUSTOS': Aprovar a ordem com comentários sobre
                os valores.

            """,
            agent=agent,
            expected_output="Forneça uma decisão de aprovação ou rejeição com justificativas claras para cada variação "
                            "analisada.",
            async_execution=False,
        )


class ReviewVariationTask():
    def review_variation(self, agent, approval_decision, order_details):
        return Task(
            description=f"""
                Revise a decisão de aprovação e a justificativa fornecida para garantir precisão e relevância.

                Decisão de Aprovação:
                {approval_decision}
                Variações Percentuais da Ordem:
                -  Valores Negativos igual a melhor rentabilidade
                -  Valores Positivos igual a custo acima do esperado
                {order_details}

                Diretrizes:
                - Verifique se a justificativa é relevante e apropriada para a variação observada.
                - Emita uma decisão de validação com base na revisão da decisão do analista.
                - 'Variação IM x IC' maior que 0,02 então ordem  Não Validado, mas se 'Variação IM x IC' for menor que
                0,02 avaliar demais parametros de custo para decidir sobrea a aprovação.
                Formato de resposta esperado:
                - Decisão de Validação: [Validado/Não Validado]
                - Motivo da Decisão: [Explique brevemente a base de sua decisão, focando na relevância e adequação da
                justificativa fornecida].
            """,
            agent=agent,
            expected_output="Forneça uma decisão de validação com justificativas claras para a aprovação ou rejeição da "
                            "decisão inicial.",
            async_execution=False,
        )


class Cost_AnalyzeVariationTask():

    def costanalyze_variation(self, agent, order_details):
        return Task(
            description=f"""
                Analise os dados de variação da ordem e fornceça a sua justificativa sobre a aprovação.

                Detalhes da Ordem e Variações Percentuais:
                - 'Material Utilizado': {order_details['Material_Used']}%
                - 'Horas de Setup': {order_details['Setup_Hours']}%
                - 'Horas de Trabalho': {order_details['Labor_Hours']}%
                - 'Horas de Máquina': {order_details['Machine_Hours']}%
                - 'Operação Externa': {order_details['External_Operation']}%
                - 'Padrão x Real': {order_details['Standard_x_Real']}%
                - 'Variação IM x IC': {order_details['Variation_IMxIC']}%
                - 'Variação de Material': {order_details['Variation_Material']}%
                - 'Taxa de Máquina': {order_details['Rate_Machine']}%
                - 'Taxa de Trabalho': {order_details['Rate_Labor']}%
                - 'Taxa de Variação do Trabalho': {order_details['Rate_Var_Labor']}%
                - Ação Prevista pelo Agente: {order_details['Predicted_OUTCOME']}



                Diretrizes:
                - 'Variação IM x IC' maior que 0,02 então Não aprovar, mas se 'Variação IM x IC' for menor que
                0,02 avaliar demais parametros de custo para decidir sobre a aprovação.
                - Ação Prevista como 'REQUER JUSTIFICATIVA FABRICA': Requer justificativa detalhada.
                - Ação Prevista como 'APROVADO COM JUSTIFICATIVA SETOR CUSTOS': Aprovar a ordem com comentários sobre
                os valores.

            """,
            agent=agent,
            expected_output="Forneça uma decisão de aprovação ou rejeição com justificativas claras para cada variação "
                            "analisada.",
            async_execution=False,
        )


class CostReviewVariationTask():
    def cost_review_variation(self, agent, approval_decision, order_details):
        return Task(
            description=f"""
                Utilize a justificativa do agente anterior para elaborar a sua justificativa mais refinada e profissional

                Decisão de Aprovação:
                {approval_decision}
                Variações Percentuais da Ordem:
                -  Valores Negativos igual a melhor rentabilidade
                -  Valores Positivos igual a custo acima do esperado
                {order_details}

                Diretrizes:
                - Verifique se a justificativa é relevante e apropriada para a variação observada.
                - Emita uma decisão de validação com base na revisão da decisão do analista.
                -  'Variação IM x IC' maior que 0,02 então Não aprovar, mas se 'Variação IM x IC' for menor que
                0,02 avaliar demais parametros de custo para decidir sobre a aprovação.

                Formato de resposta esperado:
                - Decisão de Validação: [Validado/Não Validado]
                - Motivo da Decisão: [Explique brevemente a base de sua decisão, focando na relevância e adequação da
                justificativa fornecida].
            """,
            agent=agent,
            expected_output="Forneça uma decisão de validação com as suas justificativas claras para a aprovação ou rejeição",
            async_execution=False,
        )




