from botbuilder.dialogs import ComponentDialog
from botbuilder.core import UserState, MessageFactory
from botbuilder.dialogs.prompts import ChoicePrompt, PromptOptions
from botbuilder.dialogs import WaterfallDialog, WaterfallStepContext
from botbuilder.dialogs.choices import Choice

class MainDialog(ComponentDialog):

    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__("MainDialog")

        #grava na memoria aonde o usuario esta no fluxo de conversa
        self.user_state = user_state
        
        #resgistro do prompt de escolha
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))

        #registro de funções de conversação sequencial
        self.add_dialog(
            WaterfallDialog(
                "MainDialog",
                [
                    self.prompt_option_step
                ]
            )
        )


        self.initial_dialog_id = "MainDialog"

    async def prompt_option_step(self, step_context: WaterfallStepContext):
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Escolha a Opção desejada: "),
                choices=[
                    Choice("Cadastrar Evento"),
                    Choice("Consultar Evento"),
                    Choice("Ajuda"),
                ]
            )
        )