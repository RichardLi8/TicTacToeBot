import discord
import random
from config import TOKEN
import TicTacToe


class myClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
            print("Synced")


def createButtonCallback(x:int, y:int, view:discord.ui.View, game:TicTacToe.game, buttons, user:int):
    async def button_callback(interaction: discord.Interaction):
        if user != interaction.user.id:
            await interaction.response.send_message("You are not in this game!", ephemeral=True)
            return
        output:str = "Game Board"
        if game.board [x][y] == 0:
            if game.cnt != 9 and not game.over():
                game.user(x, y)
                buttons[x][y].label = "X"
                buttons[x][y].disabled = True
            if game.cnt != 9 and not game.over():
                r,c = game.comp()
                buttons[r][c].label = "O"
                buttons[r][c].disabled = True
        if game.over():
            if game.check(game.board) == -10:
                output = "You Win"
            elif game.check(game.board) == 10:
                output = "You Lose"
            else:
                output = "Tie"
            for i in range(3):
                for j in range(3):
                    buttons[i][j].disabled = True
        await interaction.response.edit_message(content=output, view=view)
    return button_callback

bot = myClient()

tree = discord.app_commands.CommandTree(bot)

@tree.command(name = "play")
async def play(interaction: discord.Interaction):
    buttons = [[] for i in range(3)]
    view = discord.ui.View()
    game = TicTacToe.game()

    for i in range(3):
        for j in range(3):
            buttons [i].append(discord.ui.Button(label = " ", style=discord.ButtonStyle.green, row=i))
            buttons[i][j].callback = createButtonCallback(i, j, view, game, buttons, interaction.user.id)
            view.add_item(buttons[i][j])
    
    first:int = random.randint(1,2)
    
    if first == 1:
        await interaction.response.send_message("Game Board", view=view)
    else:
        r,c = game.comp()
        buttons[r][c].label = "O"
        buttons[r][c].disabled = True
        await interaction.response.send_message("Game Board", view=view)


bot.run(TOKEN)

