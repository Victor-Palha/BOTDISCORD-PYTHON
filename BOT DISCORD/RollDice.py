import discord
from random import randint
from discord.ext import commands
from random import choice
from idBot import idBOT

client = commands.Bot(intents=discord.Intents.all(), command_prefix='>', case_insensitive=True)

@client.event
async def on_read():
    print('Estamos online')


@client.event
async def on_message(message):
    if message.content == "mamaco".lower():
        await message.channel.send("GO RI LA")
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.reply(f"Pong! {round(client.latency * 1000)}ms")

@client.command(
    help='Tabela de itens magicos A',
    brief="Tabela A de itens magicos"
)
async def TitensA(ctx):
    tabelaA = randint(1, 100)
    if tabelaA >= 1 and tabelaA <= 50:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de cura')
    elif tabelaA >= 51 and tabelaA <= 60:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('Pergaminho de magia (Truque)')
    elif tabelaA >= 61 and tabelaA <= 70:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de escalar')
    elif tabelaA >= 71 and tabelaA <= 90:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('Pergaminho de magia (1° nível)')
    elif tabelaA >= 91 and tabelaA <= 94:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('Pergaminho de magia (2° nível)')
    elif tabelaA >= 95 and tabelaA <= 98:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de cura maior')
    elif tabelaA == 99:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('Mochila de carga ')
    else:
        await ctx.send(tabelaA)
        await ctx.send('Você encontrou...')
        await ctx.send('[PARABÉNS PELO CRÍTICO]')
        await ctx.send('Globo de fluxo')


@client.command(
    help='Tabela de itens magicos B',
    brief="Tabela B de itens magicos"
)
async def TitensB(ctx):
    tabelaB = randint(1, 100)
    if tabelaB >= 1 and tabelaB <= 15:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de cura maior')
    elif tabelaB <= 22:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de sopro de fogo')
    elif tabelaB <= 29:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de resistência')
    elif tabelaB <= 34:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Munição +1')
    elif tabelaB <= 39:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de amizade animal')
    elif tabelaB <= 44:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de força do gigante da colina')
    elif tabelaB <= 49:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de aumentar')
    elif tabelaB <= 54:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de respirar na água')
    elif tabelaB <= 59:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Pergaminho de magia (2° nível)')
    elif tabelaB <= 64:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Pergaminho de magia (3° nível)')
    elif tabelaB <= 69:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Mochila de carga')
    elif tabelaB <= 70:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Unguento de Keoghtom')
    elif tabelaB <= 73:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Óleo escorregadio')
    elif tabelaB <= 75:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Pó do desaparecimento')
    elif tabelaB <= 77:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Pó da seca')
    elif tabelaB <= 79:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Pó de espirrar e tossir')
    elif tabelaB <= 81:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Gema elemental')
    elif tabelaB <= 83:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Filtro do amor')
    elif tabelaB == 84:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Jarro de alquimia')
    elif tabelaB == 85:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Capa de respirar na água')
    elif tabelaB == 86:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Manto da arraia')
    elif tabelaB == 87:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Globo de fluxo')
    elif tabelaB == 88:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Óculos noturnos')
    elif tabelaB == 89:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Elmo de compreensão de idiomas')
    elif tabelaB == 90:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Bastão imóvel')
    elif tabelaB == 91:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Lanterna de revelação')
    elif tabelaB == 92:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Armadura do marinheiro')
    elif tabelaB == 93:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Armadura de mitral')
    elif tabelaB == 94:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Poção de envenenamento')
    elif tabelaB == 95:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Anel de natação')
    elif tabelaB == 96:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Robe dos itens úteis')
    elif tabelaB == 97:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Corda de escalada')
    elif tabelaB == 98:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Sela do cavaleiro')
    elif tabelaB == 99:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('Varinha de detectar magia')
    elif tabelaB == 100:
        await ctx.send(tabelaB)
        await ctx.send('Você encontrou...')
        await ctx.send('[PARABÉNS PELO CRÍTICO]')
        await ctx.send('Varinha de segredos')


@client.command(
    help='A tabela do caos é uma tabela ligada aos feiticeiros, onde é jogado um dado de 100 lados e dependendo do número que foi invocado, vai acontecer um efeito diferente.',
    brief='SURTO DE MAGIA SELVAGEM OU TABELA DO CAOS'
)
async def caos(ctx):
    Tcaos = randint(1, 100)
    if Tcaos <= 2:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Role nessa tabela, no começo de cada um dos seus turnos pelo próximo minuto, ignorando esse resultado em rolagens subsequentes.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 4:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Pelo próximo minuto, você pode ver qualquer criatura invisível, se você tiver linha de visão', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 8:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você conjura bola de fogo, como uma magia de 3° nível, centrada em você', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 10:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você conjura misseis mágicos como uma magia de 5° nível.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 12:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Role um d10. Sua altura muda em um valor igual a 3 cm x o resultado da rolagem. Se o valor for ímpar, você reduz. Se for par, você cresce.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 14:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você conjura confusão, centrada em você', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 16:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Pelo próximo minuto, você recupera 5 pontos de vida no começo de cada um dos seus turnos.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 18:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Uma longa barba feita de penas cresce em você, ela dura até você espirrar, no momento que as penas explodirão para fora do seu rosto.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 20:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você conjura área escorregadia, centrada em você.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 22:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Criaturas tem desvantagem em testes de resistência contra a próxima magia que você conjurar no próximo minuto, que possua um teste de resistência.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 24:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Sua pele adquire um tom vibrante de azul. A magia remover maldição pode acabar com esse efeito.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 26:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Um olho aparece na sua nuca no próximo minuto. Durante esse tempo, você tem vantagem em testes de Sabedoria (Percepção) relacionados à visão.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 28:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Pelo próximo minuto, todas as suas magias com tempo de conjuração de 1 ação podem ser conjuradas com 1 ação bônus', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 30:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você se teletransporte a até 18 metros para um local desocupado, à sua escolha, que você possa ver.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 32:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você é transportado para o Plano Astral até o fim do seu próximo turno, após esse tempo, você volta para o espaço que estava anteriormente ou para o espaço desocupado mais próximo, se o espaço estiver ocupado.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 34:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Maximize o dano da próxima magia que causar dano que você conjurar no próximo minuto.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 36:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Role um d10. Sua idade muda em um valor igual ao resultado da rolagem. Se o valor for ímpar, você fica mais jovem (mínimo 1 ano). Se for par, você fica mais velho.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 38:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='1d6 flumphs, controlados pelo Mestre, aparecem em espaços desocupados a até 18 metros de você e estarão com medo de você. Eles desaparecem após 1 minuto', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 40:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você recupera 2d10 pontos de vida.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 42:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você se transforma numa planta num vaso até o início do seu próximo turno. Enquanto for uma planta, você estará incapacitado e terá vulnerabilidade a todos os danos. Se você cair a 0 pontos e vida, seu vaso quebra e sua forma é revertida.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 44:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Pelo próximo minuto, você pode se teletransportar até 6 metros, com uma ação bônus, em cada um dos seus turnos.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 46:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você conjura levitação em si mesmo.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 48:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Um unicórnio, controlado pelo Mestre, aparece em um espaço a 1,5 metro de você e desaparece 1 minuto depois.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 50:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você não consegue falar pelo próximo minuto. Sempre que você tentar, bolhas rosas sairão da sua boca.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 52:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Um escudo espectral flutua próximo a você pelo próximo minuto, concedendo +2 de bônus na sua CA e imunidade a misseis mágicos.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 54:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você é imune a intoxicação por álcool pelos próximos 5d6 dias.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 56:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Seu cabelo cai, mas volta a crescer dentro de 24 horas.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 58:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value= 'Pelo próximo minuto, qualquer objeto inflamável que você tocar, que não esteja sendo segurado ou carregado por outra criatura, entra em combustão.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 60:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você recupera o seu espaço de magia de menor nível.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 62:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Pelo próximo minuto, você deve gritar quando for falar', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 64:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você conjura névoa obscurecente, centrada em você.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 66:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Até três criaturas, à sua escolha, a até 9 metros de você, sofrem 4d10 de dano elétrico.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 68:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você fica com medo da criatura mais próxima até o fim do seu próximo turno.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 70:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Cada criatura a 9 metros de você, fica invisível pelo próximo minuto. A invisibilidade termina em uma criatura quando ela ataca ou conjura uma magia.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 72:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você ganha resistência a todos os danos pelo próximo minuto.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 74:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Uma criatura aleatória, a até 9 metros de você, fica envenenada por 1d4 horas.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 76:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',
                         icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito',value='Você brilha com luz plena num raio de 9 metros pelo próximo minuto. Qualquer criatura que terminar seu turno a 1,5 metro de você, ficará cega até o fim do próximo turno.', inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 78:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você conjura metamorfose em você. Se você falhar no teste de resistência, você se torna uma ovelha pela duração da magia.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 80:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Borboletas e pétalas de flores ilusórias flutuam no ar a até de 3 metros de você pelo próximo minuto. ',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 82:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você pode realizar uma ação adicional imediatamente.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 84:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Cada criatura a até 9 metros de você, sofre 1d10 de dano necrótico. Você recupera uma quantidade de pontos de vida igual a soma do dano necrótico causado.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 86:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você conjura reflexos.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 88:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você conjura voo numa criatura aleatória a até 18 metros.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 90:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você fica invisível pelo próximo minuto. Durante esse período, outras criaturas não podem ouvi-lo. A invisibilidade termina quando você atacar ou conjurar uma magia.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 92:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Se você morrer no próximo minuto, você volta imediatamente a vida através da magia reencarnação.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 94:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Seu tamanho aumenta em uma categoria pelo próximo minuto.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 96:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100', value=f'{Tcaos}', inline=False)
        ambed.add_field(name='Efeito', value='Você e todas as criaturas a até 9 metros, ganham vulnerabilidade a dano perfurante pelo próximo minuto.',inline=False)
        await ctx.send(embed=ambed)
    elif Tcaos <= 98:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100',value=f'{Tcaos}' ,inline=False)
        ambed.add_field(name='Efeito',value='Você é envolto por uma suave, música etérea pelo próximo minuto.' ,inline=False)
        await ctx.send(embed=ambed)

    elif Tcaos <= 100:
        ambed = discord.Embed(
            title='Boa Sorte.',
            color=11807743
        )
        ambed.set_author(name='Tabela do Caos',icon_url='https://www.tibiawiki.com.br/images/thumb/f/fc/Magias_Home.gif/96px-Magias_Home.gif')
        ambed.add_field(name='Seu d100',value=f'[[{Tcaos}]]' ,inline=False)
        ambed.add_field(name='Efeito',value='Você recupera todos os pontos de feitiçaria gastos.' ,inline=False)
        await ctx.send(embed=ambed)



@client.command(
    help='Cria um NPC entregando em questôes de segundos as informações: Level, Raça, Classe, Sexo, Traços, Aparencia, Maneirismo, Alinhamento, Vínculos, Dons e Defeitos ou Segredos',
    brief='O comando (npc) cria um npc com todos os detalhes mais importantes'
)
async def npc(ctx):
    aparencia = choice(['Joia chamativa: brincos, colar, pulseira, braceletes',
                        'Piercings', 'Roupas extravagantes ou estrangeiras',
                        'Roupas formais e limpas', 'Roupas rasgadas e sujas',
                        'Cicatriz notória', 'Dente faltando', 'Dedos faltando',
                        'Cor de olho incomum (ou duas cores diferentes)',
                        'Tatuagens', 'Marca de nascença', 'Cor de pele incomum',
                        'Careca', 'Barba ou cabelo trançado', 'Cor de cabelo incomum',
                        'Movimento de olhos nervoso', 'Nariz distinto', 'Postura distinta (torta ou rígida)',
                        'Excepcionalmente belo', 'Excepcionalmente feio'])
    raca = choice(['Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato', 'Gnomo',
                   'Meio-Elfo', 'Meio-Orc', 'Tiefling'])
    classe = choice(['Bárbaro', 'Bardo', 'Bruxo', 'Clérigo', 'Druida', 'Feiticeiro',
                     'Guerreiro', 'Ladino', 'Mago', 'Monge', 'Paladino', 'Patrulheiro'])
    sexo = choice(['Masculino', 'Feminino'])
    level = randint(1, 20)
    dons = choice(['Toca um instrumento musical', 'Fala diversos idiomas fluentemente',
                   'Inacreditavelmente sortudo', 'Memória perfeita', 'Bom com animais',
                   'Bom com crianças', 'Bom em resolver enigmas', 'Bom em um jogo',
                   'Bom em imitação', 'Desenha lindamente', 'Pinta lindamente',
                   'Canta lindamente', 'Bebe tudo sobre a mesa', 'Carpinteiro especialista',
                   'Cozinheiro especialista', 'Especialista em arremessar dardos e fazer pedras saltarem',
                   'Malabarista especialista', 'Ator e mestre dos disfarces perito',
                   'Dançarino experiente', 'Conhece gírias de ladrão'])
    maneirismo = choice(['Inclinado a cantar, assobiar ou resmungar rapidamente',
                         'Fala em rimas ou de alguma outra forma peculiar',
                         'Voz particularmente baixa ou alta',
                         'Palavra incompreensíveis, balbucia ou gagueja', 'Fala excessivamente clara',
                         'Fala gritando', 'Sussurros', 'Fala de forma rebuscada ou com palavras longas',
                         'Usa palavras erradas com frequência', 'Usa injúrias e exclamações',
                         'Faz piadas e trocadilhos constantemente', 'Inclinado à previsões dramáticas',
                         'Impaciente', 'Vesgo', 'Olhar distante', 'Masca alguma coisa', 'Paciente',
                         'Estrala os dedos', 'Rói as unhas', 'Enrola os cabelos ou puxa a barba'])
    traco = choice(['Argumentativo', 'Arrogante', 'Barulhento', 'Rude', 'Curioso', 'Amigável',
                    'Honesto', 'Esquentado', 'Irritadiço', 'Ponderado', 'Quieto', 'Desconfiado'])
    alinhamento = choice(['Leal e Bom', 'Leal e Neutro', 'Leal e Mau'
                                                         'Neutro e Bom', 'Neutro', 'Neutro e Mau',
                          'Caótico e Bom', 'Caótico e Neutro', 'Caótico e Mau'])
    vinculo = choice(['Dedicado a completar um objetivo de vida pessoal', 'Protege membros próximos da família',
                      'Protege colegas ou compatriotas', 'Leal a um benfeitor, patrono ou empregador',
                      'Cativado por um interesse romântico', 'Atraído por um local especial',
                      'Protege uma lembrança especial', 'Protege um bem valioso', 'Em busca de vingança'])
    defseg = choice(['Amor perdido ou suscetível a se apaixonar', 'Gosta de prazeres escusos',
                     'Arrogante', 'Inveja as posses ou posto de outra criatura', 'Ganância desenfreada',
                     'Inclinado a se enfurecer', 'Tem um inimigo poderoso', 'Fobia específica',
                     'História vergonhosa ou escandalosa', 'Crime ou delito secreto', 'Possui conhecimento proibido',
                     'Bravura imprudente'])

    embednpc = discord.Embed(
        color=11807743
    )
    embednpc.set_author(name="Gerador de NPC's!",
     icon_url='https://www.tibiawiki.com.br/images/d/dd/Loremaster_Doll.gif')
    embednpc.set_thumbnail(url='https://www.tibiawiki.com.br/images/2/21/Sorcerer_Home.gif')
    embednpc.add_field(name='Sexo, Raça, Classe e Nível:', value=f'Sexo biológico: {sexo}. Raça: {raca}. Classe: {classe}. Nível: {level}', inline=False)
    embednpc.add_field(name='Alinhamento', value=f'{alinhamento}',inline=False)
    embednpc.add_field(name='Detalhe marcante na aparencia:', value=f'{aparencia}',inline=False)
    embednpc.add_field(name='Maneirismo: ',value=f'{maneirismo}',inline=False)
    embednpc.add_field(name='Dom:', value=f'{dons}', inline=False)
    embednpc.add_field(name='Traço de personalidade:', value=f'{traco}', inline=False)
    embednpc.add_field(name='Vínculo: ', value=f'{vinculo}', inline=False)
    embednpc.add_field(name='Defeitos ou segredo:', value=f'{defseg}', inline=False)
    await ctx.send(embed=embednpc)

@client.command(
help='Cria um Vilão entregando em questôes de segundos as informações: Level, Raça, Classe, Sexo, Aparencia, Objetivos, Métodos e fraquezas',
    brief='O comando (villain) cria um vilão aleatório'
)
async def villain(ctx):

    global objetivo, tipo
    aparencia = choice(['Joia chamativa: brincos, colar, pulseira, braceletes',
                        'Piercings', 'Roupas extravagantes ou estrangeiras',
                        'Roupas formais e limpas', 'Roupas rasgadas e sujas',
                        'Cicatriz notória', 'Dente faltando', 'Dedos faltando',
                        'Cor de olho incomum (ou duas cores diferentes)',
                        'Tatuagens', 'Marca de nascença', 'Cor de pele incomum',
                        'Careca', 'Barba ou cabelo trançado', 'Cor de cabelo incomum',
                        'Movimento de olhos nervoso', 'Nariz distinto', 'Postura distinta (torta ou rígida)',
                        'Excepcionalmente belo', 'Excepcionalmente feio'])
    classe = choice(['Bárbaro', 'Bardo', 'Bruxo', 'Clérigo', 'Druida', 'Feiticeiro',
                     'Guerreiro', 'Ladino', 'Mago', 'Monge', 'Paladino', 'Patrulheiro'])
    sexo = choice(['Masculino', 'Feminino'])
    level = randint(8, 20)
    raca = choice(['Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato', 'Gnomo', 'Meio-Elfo', 'Meio-Orc', 'Tiefling'])


    trama = randint(1, 8)
    if trama == 1:
        objetivo = 'Imortalidade'
        tipo = choice(['Adquirir um item lendário para prologar a vida', 'Ascender à divindade','Tornar-se um morto-vivo ou obter um corpo mais jovem', 'Roubar a essência de uma criatura planar'])

    elif trama == 2:
        objetivo = 'Influência'
        tipo = choice(['Adquirir uma posição de poder ou título', 'Vencer uma disputa ou torneio', 'Ganhar o favor de um indivíduo poderoso', 'Colocar um peão em uma posição de poder'])

    elif trama == 3:
        objetivo = 'Magia'
        tipo = choice(['Obter um artefato antigo', 'Construir um edifício ou dispositivo mágico', 'Executar os desejos de uma divindade', 'Oferecer sacrifícios para uma divindade', 'Contatar uma divindade ou poder perdido', 'Abrir um portal para outro mundo'])

    elif trama == 4:
        objetivo = 'Desordem'
        tipo = choice(['Cumprir uma profecia apocalíptica', 'Decretar a vontade vingativa de um deus ou patrono', 'Espalhar uma praga maligna', 'Destronar um governante', 'Desencadear um desastre natural', 'Destruir totalmente uma linhagem ou clã'])

    elif trama == 5:
        objetivo = 'Paixão'
        tipo = choice(['Prolongar a vida de um ente querido', 'Mostrar-se merecedor do amor de outra pessoa', 'Reanimar ou reviver um ente querido', 'Destruir rivais pela afeição de outra pessoa'])

    elif trama == 6:
        objetivo = 'Poder'
        tipo = choice(['Conquistar uma região ou incitar uma rebelião', 'Adquirir controle de um exército', 'Tornar-se o poder por trás do trono', 'Ganhar o favor de um governante'])

    elif trama == 7:
        objetivo = 'Vingança'
        tipo = choice(['Vingar uma humilhação ou insulto passado', 'Vingar um aprisionamento ou injúria passada', 'Vingar a morte de um ente querido', 'Recuperar propriedade roubada e punir o ladrão'])

    elif trama == 8:
        objetivo = 'Riqueza'
        tipo = choice(['Controlar recursos naturais ou comércio', 'Casar-se por riqueza', 'Saquear ruínas antigas', 'Roubar terras, bens ou dinheiro'])


    metodo = randint(1, 20)
    if metodo == 1:
        princ = 'Devastação agrícola'
        acao = choice(['Praga', 'Colheita fracassada', 'Seca', 'Fome'])

    elif metodo == 2:
        princ = '-'
        acao = 'Assalto ou ataques'

    elif metodo == 3:
        princ = '-'
        acao = 'Caça de recompensa ou assassinato'

    elif metodo == 4:
        princ = 'Cativeiro ou coerção'
        acao = choice(['Suborno', 'Sedução','Despejo','Aprisionamento','Sequestro','Intimação legal','Quadrilha de imprensa','Acorrentamento','Escravidão', 'Ameaças ou perseguição'])

    elif metodo ==5:
        princ = 'Golpes confiantes'
        acao = choice(['Quebra de contrato','Trapaça', 'Persuasão', 'Letras miúdas', 'Fralde ou estelionato', 'Charlatanismo ou enganação'])

    elif metodo == 6:
        princ = 'Difamação'
        acao = choice(['Enquadramento', 'Fofoca ou calúnia', 'Humilhação','Difamação ou insultos'])

    elif metodo == 7:
        princ = '-'
        acao = 'Duelos'

    elif metodo == 8:
        princ = 'Execução'
        acao = choice(['Decapitação', 'Queimado na fogueira', 'Enterrado vivo', 'Crucificação','Estripado e esquartejado', 'Enforcado','Empalado','Sacrificado (vivo)'])

    elif metodo == 9:
        princ = '-'
        acao = 'Personificação ou disfarce'

    elif metodo == 10:
        princ = '-'
        acao = 'Mentira ou perjúrio'

    elif metodo == 11:
        princ = 'Caos mágico'
        acao = choice(['Assombrações', 'Ilusões', 'Barganhas infernais', 'Controle mental', 'Petrificação', 'Erguendo ou reanimando os mortos', 'Invocando monstros', 'Controle do clima'])

    elif metodo == 12:
        princ = 'Homicídio'
        acao = choice(['Assassinato', 'Canibalismo', 'Desmembramento', 'Afogamento Eletrocussão', 'Eutanásia (involuntária)', 'Doença', 'Envenenamento', 'Esfaqueamento', 'Estrangulamento ou sufocamento'])

    elif metodo == 13:
        princ = '-'
        acao = 'Negligência'

    elif metodo == 14:
        princ = 'Política'
        acao = choice(['Traição ou infidelidade' 'Conspiração', 'Espionagem ou perscrutação', 'Genocídio', 'Opressão', 'Aumentar impostos'])

    elif metodo == 15:
        princ = 'Religião'
        acao = choice(['Maldições', 'Profanação', 'Deuses falsos', 'Heresia ou cultos'])

    elif metodo == 16:
        princ = '-'
        acao = 'Perseguição'

    elif metodo == 17:
        princ = 'Roubo ou crime contra a propriedade'
        acao = choice(['Incêndio criminoso', 'Chantagem ou extorsão', 'Assalto', 'Falsificação', 'Roubo em estradas', 'Pilhagem', 'Roubo', 'Caça ilegal', 'Apropriação de propriedade', 'Contrabando'])

    elif metodo == 18:
        princ = 'Tortura'
        acao = choice(['Ácido', 'Cegueira', 'Marcar a ferro', 'Dilaceração', 'Perfurações', 'Açoitamento'])

    elif metodo == 19:
        princ = 'Vício'
        acao = choice(['Adultério', 'Drogas ou álcool', 'Jogos de azar', 'Sedução'])

    else:
        princ = 'Guerra'
        acao = choice(['Emboscada', 'Invasão', 'Massacre', 'Mercenários', 'Rebelião', 'Terrorismo'])


    fraqueza = choice(['Um objeto escondido contém a alma do vilão.',
    'O poder do vilão acaba se a morte do seu verdadeiro amor for vingada.',
    'vilão fica enfraquecido na presença de um artefato em particular.',
    'Uma arma especial causa dano extra quando usada contra o vilão.',
    'O vilão é destruído se falarem seu nome verdadeiro.',
    'Uma profecia ou enigma antigo revela como o vilão pode ser derrotado.' ,
    'O vilão perece quando um inimigo antigo perdoa-lo por suas ações passadas.',
    'O vilão perde seu poder se uma barganha mística que ele fez há muito tempo for concluída.'])

    ambed = discord.Embed(
        color=11807743
    )
    ambed.set_author(name='Gerador de vilão', icon_url='https://www.tibiawiki.com.br/images/1/18/Braindeath.gif')
    ambed.set_thumbnail(url='https://www.tibiawiki.com.br/images/9/94/Barbarian_Brutetamer.gif')
    ambed.add_field(name='Sexo, Raça, Classe e Nível:', value=f'Sexo biológico: {sexo}. Raça: {raca}. Classe: {classe}. Nível: {level}', inline=False)
    ambed.add_field(name='Detalhe marcante na aparencia:', value=f'{aparencia}',inline=False)
    ambed.add_field(name='Fraqueza do vilão', value=f'{fraqueza}', inline=False)
    ambed.add_field(name=f'Metodo do vilão: {princ}', value=f'meio de {acao}', inline=False)
    ambed.add_field(name=f'Objetivo do vilão: {objetivo}', value=f'Trama do vilão: {tipo}', inline=False)
    await ctx.send(embed = ambed)


@client.command(
    help='O comando gera uma história completa, com o começo, local de aventura, criador do local, vilão, climax e NPC que ajuda o grupo, tudo que uma aventura épica precisa, com um simples comando de texto!',
    brief='O comando cria uma base para uma aventura de D&D 5e')
async def quest(ctx):
    inicio = choice(['Enquanto estiverem viajando pela natureza, os personagens percebem a entrada de um local de aventura.','Enquanto estiverem viajando por uma estrada, os personagens são atacados por monstros que fogem para o local de aventura mais próximo.','Os aventureiros encontram um mapa em um cadáver. Além do mapa encontrado levar a aventura, o vilão da aventura deseja o mapa.','Um item mágico misterioso ou um vilão cruel teletransporte os personagens para o local de aventura.','Um estranho se aproxima dos personagens em uma taverna e os instiga a ir para o local de aventura.','Uma cidade ou vila precisa de voluntários para ir ao local de aventura.','Um PdM com quem os personagens se importam precisa deles para ir ao local de aventura.','Um PdM que os personagens devem obedecer ordena-os a ir ao local de aventura.','Um PdM que os personagens respeitam pede que eles vão ao local de aventura.','Uma noite, todos os personagens sonham com a entrada do local de aventura.','Um fantasma aparece e aterroriza uma vila. Pesquisas revelam que ele só pode ter o descanso eterno entrando no local de aventura.'])
    dg = choice(['Uma construção em uma cidade','Catacumbas ou esgotos abaixo de uma cidade','Abaixo de uma casa depi fazenda','Abaixo de um cemitério','Abaixo de um castelo em ruínas','Abaixo de uma cidade em ruínas','Abaixo de um templo','um abismo','Frente a face de um penhasco','um deserto','uma floresta','uma geleira','um desfiladeiro','uma floresta','uma passagem de uma montanha','um pântano','Abaixo ou no topo de um platô','grutas marinhas','diversas mesas interligadas','um pico de uma montanha','um promontório','uma ilha Submersa'])
    criador = choice(['Observador', 'Culto ou grupo religioso','Anões','Elfos (incluindo drow)','Gigantes','Hobgoblins','Humanos','Kuo-toa','Lich','Devoradores de mentes','Yuan-ti','Sem criador'])
    elmalvado = choice(['Besta ou monstruosidade sem motivações específicas','Aberração propensa a corrupção ou dominação','Corruptor propenso a corrupção ou destruição','Dragão propenso a dominação ou saque','Gigante propenso a saquear','Morto-vivo com qualquer motivação','Fada com um objetivo misterioso','Humanoide cultista','Humanoide conquistador','Humanoide buscando vingança','Humanoide conspirador buscando governar','Humanoide mestre do crime','Humanoide incursor ou devastador','Humanoide sob uma maldição','Humanoide fanático desorientado'])
    climax = choice([
        'Os aventureiros enfrentam o vilão principal e um grupo de lacaios em uma batalha sangrenta para a conclusão.',
        'Os aventureiros perseguem o vilão enquanto desviam de obstáculos colocados para impedi-los, levando ao confronto final dentro ou fora do refúgio do vilão.',
        'As ações dos aventureiros ou do vilão resultam em um evento cataclísmico o qual os aventureiros devem escapar.',
        'Os aventureiros correm até o local onde o vilão está concluindo seu plano mestre, chegando exatamente no momento que o plano está prestes a se concluir.',
        'O vilão e dois ou três tenentes realizam rituais separados em um imenso salão. Os aventureiros devem impedir todos os rituais ao mesmo tempo.',
        'Um aliado trai os aventureiros quando eles estão prestes a concluir seu objetivo. (Use esse clímax com cuidado e não abuse dele.)',
        'Um portal se abre para outro plano de existência. As criaturas do outro lado saem, forçando os aventureiros a fechar o portal e lidarem com o vilão ao mesmo tempo.',
        'Armadilhas, perigos ou objetos animados se vltam contra os aventureiros enquanto o vilão principal ataca.',
        'A masmorra começa a desmoronar enquanto os aventureiros enfrentam o vilão principal, que tenta escapar em meio ao caos.',
        'Uma ameaça mais poderosa que os aventureiros aparece, destrói o vilão principal e então volta suas atenções para os personagens.',
        'Os aventureiros devem escolher se perseguem o vilão principal em fuga ou salvam um PdM com quem se importam ou um grupo de inocentes.',
        'Os aventureiros devem descobrir a fraqueza secreta do vilão principal antes de terem esperança de derrota-lo.'
    ])
    ambed = discord.Embed(
        title='A sua aventura épica!',
        color=11807743
    )
    ambed.set_author(name='Gerador de aventura!', icon_url='https://www.tibiawiki.com.br/images/4/47/Tome_of_Knowledge.gif')
    ambed.set_thumbnail(url='https://www.tibiawiki.com.br/images/c/ce/The_Epic_Wisdom.gif')
    ambed.add_field(name='O começo da aventura:', value=f'A aventura se inicia quando: {inicio}', inline=False)
    ambed.add_field(name='Local da missão:', value=f'Os aventureiros se deparam com uma construção antiga em: [{dg}]', inline=False)
    ambed.add_field(name='Criador do local:', value=f'Que mais tarde se revela tendo sido construido por: {criador}', inline=False)
    ambed.add_field(name='Vilão da aventura:', value=f'O grande vilão que se abriga e trama seus planos neste lugar, acaba sendo revelado como um: {elmalvado}', inline=False)
    ambed.add_field(name='Climax:', value=f'No momento decisivo acaba que acontece [{climax}]', inline=False)
    ambed.add_field(name='Aliado:', value=f'Toda aventura tendo um aliado leal ao lado, sendo ele:', inline=False)
    await ctx.send(embed = ambed)
    await npc.__call__(ctx)


client.run(idBOT)
