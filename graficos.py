
import mplfinance as mpf
import matplotlib.pyplot as plt
import seaborn as sns 


def grafico_fundamental(diccionario, dato, xlabel='Fecha', ylabel='Valor'):
    df_out = None
    column_names = []
    for clave, valor in diccionario.items():
        column_names.append(clave)
        if df_out is None:
            df_out = valor[[dato]]
        else:
            df_out = df_out.merge(valor[[dato]], left_index=True, right_index=True, how='outer', suffixes=('', '_{}'.format(clave)))
    df_out.columns = column_names
    
    # Utilizar Seaborn para graficar
    sns.lineplot(data=df_out, markers=True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    plt.title(dato)
    plt.legend()
    plt.legend(loc = "upper left")
    plt.show()
    return(df_out)

def grafigrafico_fundamentals(ticket, datos, xlabel='Fecha', ylabel='Valor'):
    # Utilizar Seaborn para graficar
    sns.lineplot(ticket[datos], markers=True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    #plt.title(dato)
    plt.legend()
    plt.legend(loc = "upper left")
    plt.show()

    

def grafico_vela(ticket, volume=True, style='mike', yscale = 'log'):
    mpf.plot(ticket, type='candle', volume=volume, 
            style=style, 
            yscale = yscale, 
            ylabel='Precio', 
            xlabel='Tiempo',
        figscale=0.7 )
    #plt.plot(ticket)
    #plt.grid()
    #plt.show()

def grafico_comparacion(tickets):
    s = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 6})
    fig = mpf.figure(figsize=(10, 7), style=s) # pass in the self defined style to the whole canvas
    ax = fig.add_subplot(2,1,1) # main candle stick chart subplot, you can also pass in the self defined style here only for this subplot
    av = fig.add_subplot(2,1,2, sharex=ax)  # volume chart subplot
    mpf.plot(tickets, type='candle', ax=ax, volume=av)



#No esta funcionando
def grafico_cierre(ticket):
    fig = plt.figure(figsize=(16,8))
    plt.subplot(2,1,1)
    plt.plot( ticket[['Close']] )
    #plt.axhline(y=0, color='r')
    plt.title("Precio de cierre")
    plt.subplot(2,1,2)
    plt.plot( ticket[['MA_50']] )
    plt.title("MA_50")
    plt.show()

# def graficos(tickets, period = '5y'):
#     for ticket in tickets:
#         data = tickets[ticket].history(period=period) 
#         plt.plot(data['Close'], label = ticket)
    
#     plt.legend(loc = "upper left")
#     plt.title("COMPARACION DE VARIABLES")
#     plt.xlabel("TIEMPO")
#     plt.ylabel("PRECIO")
#     plt.show()

def graficos( diccionario , dato='close', grid = True, title='COMPARACION DE VARIABLES',xlabel='TIEMPO', ylabel='PRECIO'):
    for clave, valor in diccionario.items(): 
        plt.plot(valor[dato], label = clave)
    
    plt.legend(loc = "upper left")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if( grid == True):
        plt.grid()
    plt.show()

def grafico_volumen(diccionario):
    fig, (ax1, ax2) = plt.subplots(2)
    for clave, valor in diccionario.items(): 
        ax1.plot(valor['Close'], label = clave)
        ax2.plot(valor['Volume'], label = clave)   

    ax1.set_title('COMPARACION PRECIO')
    ax2.set_title('COMPARACION VOLUMEN')
    plt.legend(loc = "upper left")
    #plt.title("COMPARACION DE VARIABLES")
    #plt.xlabel("TIEMPO")
    #plt.ylabel("PRECIO")
    plt.show()

